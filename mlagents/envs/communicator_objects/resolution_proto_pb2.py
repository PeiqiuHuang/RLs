# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mlagents/envs/communicator_objects/resolution_proto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mlagents/envs/communicator_objects/resolution_proto.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_options=_b('\252\002\034MLAgents.CommunicatorObjects'),
  serialized_pb=_b('\n9mlagents/envs/communicator_objects/resolution_proto.proto\x12\x14\x63ommunicator_objects\"D\n\x0fResolutionProto\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x12\n\ngray_scale\x18\x03 \x01(\x08\x42\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
)




_RESOLUTIONPROTO = _descriptor.Descriptor(
  name='ResolutionProto',
  full_name='communicator_objects.ResolutionProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='communicator_objects.ResolutionProto.width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='communicator_objects.ResolutionProto.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gray_scale', full_name='communicator_objects.ResolutionProto.gray_scale', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=83,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['ResolutionProto'] = _RESOLUTIONPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResolutionProto = _reflection.GeneratedProtocolMessageType('ResolutionProto', (_message.Message,), dict(
  DESCRIPTOR = _RESOLUTIONPROTO,
  __module__ = 'mlagents.envs.communicator_objects.resolution_proto_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.ResolutionProto)
  ))
_sym_db.RegisterMessage(ResolutionProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
