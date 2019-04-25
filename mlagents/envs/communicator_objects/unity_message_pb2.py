# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mlagents/envs/communicator_objects/unity_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mlagents.envs.communicator_objects import unity_output_pb2 as mlagents_dot_envs_dot_communicator__objects_dot_unity__output__pb2
from mlagents.envs.communicator_objects import unity_input_pb2 as mlagents_dot_envs_dot_communicator__objects_dot_unity__input__pb2
from mlagents.envs.communicator_objects import header_pb2 as mlagents_dot_envs_dot_communicator__objects_dot_header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mlagents/envs/communicator_objects/unity_message.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_options=_b('\252\002\034MLAgents.CommunicatorObjects'),
  serialized_pb=_b('\n6mlagents/envs/communicator_objects/unity_message.proto\x12\x14\x63ommunicator_objects\x1a\x35mlagents/envs/communicator_objects/unity_output.proto\x1a\x34mlagents/envs/communicator_objects/unity_input.proto\x1a/mlagents/envs/communicator_objects/header.proto\"\xac\x01\n\x0cUnityMessage\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.communicator_objects.Header\x12\x37\n\x0cunity_output\x18\x02 \x01(\x0b\x32!.communicator_objects.UnityOutput\x12\x35\n\x0bunity_input\x18\x03 \x01(\x0b\x32 .communicator_objects.UnityInputB\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
  ,
  dependencies=[mlagents_dot_envs_dot_communicator__objects_dot_unity__output__pb2.DESCRIPTOR,mlagents_dot_envs_dot_communicator__objects_dot_unity__input__pb2.DESCRIPTOR,mlagents_dot_envs_dot_communicator__objects_dot_header__pb2.DESCRIPTOR,])




_UNITYMESSAGE = _descriptor.Descriptor(
  name='UnityMessage',
  full_name='communicator_objects.UnityMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='communicator_objects.UnityMessage.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unity_output', full_name='communicator_objects.UnityMessage.unity_output', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unity_input', full_name='communicator_objects.UnityMessage.unity_input', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=239,
  serialized_end=411,
)

_UNITYMESSAGE.fields_by_name['header'].message_type = mlagents_dot_envs_dot_communicator__objects_dot_header__pb2._HEADER
_UNITYMESSAGE.fields_by_name['unity_output'].message_type = mlagents_dot_envs_dot_communicator__objects_dot_unity__output__pb2._UNITYOUTPUT
_UNITYMESSAGE.fields_by_name['unity_input'].message_type = mlagents_dot_envs_dot_communicator__objects_dot_unity__input__pb2._UNITYINPUT
DESCRIPTOR.message_types_by_name['UnityMessage'] = _UNITYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UnityMessage = _reflection.GeneratedProtocolMessageType('UnityMessage', (_message.Message,), dict(
  DESCRIPTOR = _UNITYMESSAGE,
  __module__ = 'mlagents.envs.communicator_objects.unity_message_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.UnityMessage)
  ))
_sym_db.RegisterMessage(UnityMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
