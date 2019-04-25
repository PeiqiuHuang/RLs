# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mlagents/envs/communicator_objects/brain_parameters_proto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mlagents.envs.communicator_objects import resolution_proto_pb2 as mlagents_dot_envs_dot_communicator__objects_dot_resolution__proto__pb2
from mlagents.envs.communicator_objects import space_type_proto_pb2 as mlagents_dot_envs_dot_communicator__objects_dot_space__type__proto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mlagents/envs/communicator_objects/brain_parameters_proto.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_options=_b('\252\002\034MLAgents.CommunicatorObjects'),
  serialized_pb=_b('\n?mlagents/envs/communicator_objects/brain_parameters_proto.proto\x12\x14\x63ommunicator_objects\x1a\x39mlagents/envs/communicator_objects/resolution_proto.proto\x1a\x39mlagents/envs/communicator_objects/space_type_proto.proto\"\xd4\x02\n\x14\x42rainParametersProto\x12\x1f\n\x17vector_observation_size\x18\x01 \x01(\x05\x12\'\n\x1fnum_stacked_vector_observations\x18\x02 \x01(\x05\x12\x1a\n\x12vector_action_size\x18\x03 \x03(\x05\x12\x41\n\x12\x63\x61mera_resolutions\x18\x04 \x03(\x0b\x32%.communicator_objects.ResolutionProto\x12\"\n\x1avector_action_descriptions\x18\x05 \x03(\t\x12\x46\n\x18vector_action_space_type\x18\x06 \x01(\x0e\x32$.communicator_objects.SpaceTypeProto\x12\x12\n\nbrain_name\x18\x07 \x01(\t\x12\x13\n\x0bis_training\x18\x08 \x01(\x08\x42\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
  ,
  dependencies=[mlagents_dot_envs_dot_communicator__objects_dot_resolution__proto__pb2.DESCRIPTOR,mlagents_dot_envs_dot_communicator__objects_dot_space__type__proto__pb2.DESCRIPTOR,])




_BRAINPARAMETERSPROTO = _descriptor.Descriptor(
  name='BrainParametersProto',
  full_name='communicator_objects.BrainParametersProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vector_observation_size', full_name='communicator_objects.BrainParametersProto.vector_observation_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_stacked_vector_observations', full_name='communicator_objects.BrainParametersProto.num_stacked_vector_observations', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vector_action_size', full_name='communicator_objects.BrainParametersProto.vector_action_size', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='camera_resolutions', full_name='communicator_objects.BrainParametersProto.camera_resolutions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vector_action_descriptions', full_name='communicator_objects.BrainParametersProto.vector_action_descriptions', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vector_action_space_type', full_name='communicator_objects.BrainParametersProto.vector_action_space_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brain_name', full_name='communicator_objects.BrainParametersProto.brain_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_training', full_name='communicator_objects.BrainParametersProto.is_training', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=548,
)

_BRAINPARAMETERSPROTO.fields_by_name['camera_resolutions'].message_type = mlagents_dot_envs_dot_communicator__objects_dot_resolution__proto__pb2._RESOLUTIONPROTO
_BRAINPARAMETERSPROTO.fields_by_name['vector_action_space_type'].enum_type = mlagents_dot_envs_dot_communicator__objects_dot_space__type__proto__pb2._SPACETYPEPROTO
DESCRIPTOR.message_types_by_name['BrainParametersProto'] = _BRAINPARAMETERSPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BrainParametersProto = _reflection.GeneratedProtocolMessageType('BrainParametersProto', (_message.Message,), dict(
  DESCRIPTOR = _BRAINPARAMETERSPROTO,
  __module__ = 'mlagents.envs.communicator_objects.brain_parameters_proto_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.BrainParametersProto)
  ))
_sym_db.RegisterMessage(BrainParametersProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
