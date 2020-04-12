import logging
from copy import deepcopy
from gym_wrapper import gym_envs
from common.unity_wrapper import UnityWrapper
from common.unity_wrapper import InfoWrapper, UnityReturnWrapper, SamplerWrapper, ActionWrapper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("common.make_env")

def make_env(env_args):
    if env_args['type'] == 'gym':
        env = make_gym_env(env_args)
    elif env_args['type'] == 'unity':
        env = make_unity_env(env_args)
    else:
        raise Exception('Unknown environment type.')
    return env


def make_gym_env(env_args):
    env_kargs = deepcopy(env_args)
    env = gym_envs(env_kargs)
    return env


def make_unity_env(env_args):
    env_kargs = deepcopy(env_args)
    env = UnityWrapper(env_kargs)
    logger.debug('Unity UnityWrapper success.')

    env = InfoWrapper(env, env_args)
    logger.debug('Unity InfoWrapper success.')

    env = UnityReturnWrapper(env)
    logger.debug('Unity UnityReturnWrapper success.')

    env = SamplerWrapper(env, env_args)
    logger.debug('Unity SamplerWrapper success.')

    env = ActionWrapper(env)
    logger.debug('Unity ActionWrapper success.')
    
    return env
