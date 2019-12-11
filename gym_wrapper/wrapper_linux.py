import gym
import ray
import numpy as np


@ray.remote
class ENV:
    def __init__(self, gym_env_name):
        self.env = gym.make(gym_env_name)
        self.obs_space = self.env.observation_space
        self.need_one_hot_or_not()

    def need_one_hot_or_not(self):
        if hasattr(self.obs_space, 'n'):
            self.toOneHot = True
            if isinstance(self.obs_space.n, (int, np.int32)):
                obs_dim = [int(self.obs_space.n)]
            else:
                obs_dim = list(self.obs_space.n)    # 在CliffWalking-v0环境其类型为numpy.int32
            self.multiplication_factor = np.asarray(obs_dim[1:] + [1])
            self.one_hot_len = self.multiplication_factor.prod()
        else:
            self.toOneHot = False

    def _maybe_one_hot(self, obs):
        """
        Change discrete observation from list(int) to list(one_hot) format.
        for example:
            action: [1, 0]
            observation space: [3, 4]
            then, output: [0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
        """
        if self.toOneHot:
            obs = np.reshape(obs, (1, -1))
            ints = obs.dot(self.multiplication_factor)
            x = np.zeros([obs.shape[0], self.one_hot_len])
            for i, j in enumerate(ints):
                x[i, j] = 1
            return x
        else:
            return obs

    def seed(self, s):
        self.env.seed(s)

    def reset(self):
        obs = self.env.reset()
        return self._maybe_one_hot(obs)

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        return (self._maybe_one_hot(obs),
                reward,
                done,
                info
                )

    def render(self):
        self.env.render()

    def close(self):
        self.env.close()

    def sample(self):
        return self.env.action_space.sample()


class gym_envs(object):

    def __init__(self, gym_env_name, n, seed=0, render_mode='first'):
        '''
        Input:
            gym_env_name: gym training environment id, i.e. CartPole-v0
            n: environment number
            render_mode: mode of rendering, optional: first, last, all, random_[num] -> i.e. random_2, [list] -> i.e. [0, 2, 4]
        '''
        ray.init()
        self.n = n  # environments number
        self.envs = [ENV.remote(gym_env_name) for i in range(self.n)]
        self.seeds = [seed + i for i in range(self.n)]
        [env.seed.remote(s) for env, s in zip(self.envs, self.seeds)]
        # process observation
        self.e = gym.make(gym_env_name)
        self.obs_space = self.e.observation_space
        if isinstance(self.obs_space, gym.spaces.box.Box):
            self.obs_high = self.obs_space.high
            self.obs_low = self.obs_space.low
        self.obs_type = 'visual' if len(self.obs_space.shape) == 3 else 'vector'

        self.reward_threshold = self.e.env.spec.reward_threshold  # reward threshold refer to solved
        # process action
        self.action_space = self.e.action_space
        if isinstance(self.action_space, gym.spaces.box.Box):
            self.action_type = 'continuous'
            self.action_high = self.action_space.high
            self.action_low = self.action_space.low
        elif isinstance(self.action_space, gym.spaces.tuple.Tuple):
            self.action_type = 'Tuple(Discrete)'
        else:
            self.action_type = 'discrete'
        self.e.close()

        self.action_mu, self.action_sigma = self._get_action_normalize_factor()
        self._get_render_index(render_mode)

    def _get_render_index(self, render_mode):
        '''
        get render windows list, i.e. [0, 1] when there are 4 training enviornment.
        '''
        assert isinstance(render_mode, (list, str)), 'render_mode must have type of str or list.'
        if isinstance(render_mode, list):
            assert all([isinstance(i, int) for i in render_mode]), 'items in render list must have type of int'
            assert min(index) >= 0, 'index must larger than zero'
            assert max(index) <= self.n, 'render index cannot larger than environment number.'
            self.render_index = render_mode
        elif isinstance(render_mode, str):
            if render_mode == 'first':
                self.render_index = [0]
            elif render_mode == 'last':
                self.render_index = [-1]
            elif render_mode == 'all':
                self.render_index = [i for i in range(self.n)]
            else:
                a, b = render_mode.split('_')
                if a == 'random' and 0 < int(b) <= self.n:
                    import random
                    self.render_index = random.sample([i for i in range(self.n)], int(b))
        else:
            raise Exception('render_mode must be first, last, all, [list] or random_[num]')

    def _get_action_normalize_factor(self):
        '''
        get action mu and sigma. mu: action bias. sigma: action scale
        input: 
            self.action_low: [-2, -3],
            self.action_high: [2, 6]
        return: 
            mu: [0, 1.5], 
            sigma: [2, 4.5]
        '''
        if self.action_type == 'continuous':
            return (self.action_high + self.action_low) / 2, (self.action_high - self.action_low) / 2
        else:
            return 0, 1

    def reset(self):
        self.dones_index = []
        obs = np.asarray(ray.get([env.reset.remote() for env in self.envs]))
        return obs

    def partial_reset(self):
        obs = np.asarray(ray.get([self.envs[i].reset.remote() for i in self.dones_index]))
        return obs

    def render(self):
        '''
        render game windows.
        '''
        [self.envs[i].render.remote() for i in self.render_index]

    def sample_action(self):
        '''
        generate ramdom actions for all training environment.
        '''
        return np.asarray(ray.get([env.sample.remote() for env in self.envs]))

    def step(self, actions, scale=True):
        if scale == True:
            actions = self.action_sigma * actions + self.action_mu
        if self.action_type == 'discrete':
            actions = actions.reshape(-1,)
        elif self.action_type == 'Tuple(Discrete)':
            actions = actions.reshape(self.n, -1).tolist()
        obs, reward, done, info = list(zip(*ray.get([env.step.remote(action) for env, action in zip(self.envs, actions)])))
        self.dones_index = np.where(done)[0]
        return (np.asarray(obs),
                np.asarray(reward),
                np.asarray(done),
                info)

    def close(self):
        '''
        close all environments.
        '''
        [env.close.remote() for env in self.envs]
        ray.shutdown()