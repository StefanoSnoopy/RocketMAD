# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/get_player_day_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/get_player_day_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nDpogoprotos/networking/requests/messages/get_player_day_message.proto\x12\'pogoprotos.networking.requests.messages\"\x15\n\x13GetPlayerDayMessageb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETPLAYERDAYMESSAGE = _descriptor.Descriptor(
  name='GetPlayerDayMessage',
  full_name='pogoprotos.networking.requests.messages.GetPlayerDayMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['GetPlayerDayMessage'] = _GETPLAYERDAYMESSAGE

GetPlayerDayMessage = _reflection.GeneratedProtocolMessageType('GetPlayerDayMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETPLAYERDAYMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.get_player_day_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GetPlayerDayMessage)
  ))
_sym_db.RegisterMessage(GetPlayerDayMessage)


# @@protoc_insertion_point(module_scope)