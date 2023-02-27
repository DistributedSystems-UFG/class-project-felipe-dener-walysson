# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iot_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11iot_service.proto\x12\x0biot_service\"7\n\x12TemperatureRequest\x12\x12\n\nsensorName\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"-\n\x0bUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"3\n\x11UserCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"$\n\x12UserCreateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\"-\n\x0cUserResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\r\n\x05token\x18\x02 \x01(\t\"\'\n\x10TemperatureReply\x12\x13\n\x0btemperature\x18\x01 \x01(\t\";\n\nLedRequest\x12\r\n\x05state\x18\x01 \x01(\r\x12\x0f\n\x07ledname\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\"r\n\x08LedReply\x12\x35\n\x08ledstate\x18\x01 \x03(\x0b\x32#.iot_service.LedReply.LedstateEntry\x1a/\n\rLedstateEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"6\n\x11LightLevelRequest\x12\x12\n\nsensorName\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"%\n\x0fLightLevelReply\x12\x12\n\nlightLevel\x18\x01 \x01(\t\".\n\rActionRequest\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\"\x1d\n\x0b\x41\x63tionReply\x12\x0e\n\x06status\x18\x01 \x01(\t2\xc2\x03\n\nIoTService\x12R\n\x0eSayTemperature\x12\x1f.iot_service.TemperatureRequest\x1a\x1d.iot_service.TemperatureReply\"\x00\x12<\n\x08\x42linkLed\x12\x17.iot_service.LedRequest\x1a\x15.iot_service.LedReply\"\x00\x12O\n\rSayLightLevel\x12\x1e.iot_service.LightLevelRequest\x1a\x1c.iot_service.LightLevelReply\"\x00\x12>\n\x05Login\x12\x18.iot_service.UserRequest\x1a\x19.iot_service.UserResponse\"\x00\x12O\n\nCreateUser\x12\x1e.iot_service.UserCreateRequest\x1a\x1f.iot_service.UserCreateResponse\"\x00\x12@\n\x06\x41\x63tion\x12\x1a.iot_service.ActionRequest\x1a\x18.iot_service.ActionReply\"\x00\x42\x37\n\x1bio.grpc.examples.iotserviceB\x0fIoTServiceProtoP\x01\xa2\x02\x04TEMPb\x06proto3')



_TEMPERATUREREQUEST = DESCRIPTOR.message_types_by_name['TemperatureRequest']
_USERREQUEST = DESCRIPTOR.message_types_by_name['UserRequest']
_USERCREATEREQUEST = DESCRIPTOR.message_types_by_name['UserCreateRequest']
_USERCREATERESPONSE = DESCRIPTOR.message_types_by_name['UserCreateResponse']
_USERRESPONSE = DESCRIPTOR.message_types_by_name['UserResponse']
_TEMPERATUREREPLY = DESCRIPTOR.message_types_by_name['TemperatureReply']
_LEDREQUEST = DESCRIPTOR.message_types_by_name['LedRequest']
_LEDREPLY = DESCRIPTOR.message_types_by_name['LedReply']
_LEDREPLY_LEDSTATEENTRY = _LEDREPLY.nested_types_by_name['LedstateEntry']
_LIGHTLEVELREQUEST = DESCRIPTOR.message_types_by_name['LightLevelRequest']
_LIGHTLEVELREPLY = DESCRIPTOR.message_types_by_name['LightLevelReply']
_ACTIONREQUEST = DESCRIPTOR.message_types_by_name['ActionRequest']
_ACTIONREPLY = DESCRIPTOR.message_types_by_name['ActionReply']
TemperatureRequest = _reflection.GeneratedProtocolMessageType('TemperatureRequest', (_message.Message,), {
  'DESCRIPTOR' : _TEMPERATUREREQUEST,
  '__module__' : 'iot_service_pb2'
  # @@protoc_insertion_point(class_scope:iot_service.TemperatureRequest)
  })
_sym_db.RegisterMessage(TemperatureRequest)

UserRequest = _reflection.GeneratedProtocolMessageType('UserRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERREQUEST,
  '__module__' : 'iot_service_pb2'
  # @@protoc_insertion_point(class_scope:iot_service.UserRequest)
  })
_sym_db.RegisterMessage(UserRequest)

UserCreateRequest = _reflection.GeneratedProtocolMessageType('UserCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERCREATEREQUEST,
  '__module__' : 'iot_service_pb2'
  # @@protoc_insertion_point(class_scope:iot_service.UserCreateRequest)
  })
_sym_db.RegisterMessage(UserCreateRequest)

UserCreateResponse = _reflection.GeneratedProtocolMessageType('UserCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERCREATERESPONSE,
  '__module__' : 'iot_service_pb2'
  # @@protoc_insertion_point(class_scope:iot_service.UserCreateResponse)
  })
_sym_db.RegisterMessage(UserCreateResponse)

UserResponse = _reflection.GeneratedProtocolMessageType('UserResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERRESPONSE,
  '__module__' : 'iot_service_pb2'
  # @@protoc_insertion_point(class_scope:iot_service.UserResponse)
  })
_sym_db.RegisterMessage(UserResponse)

TemperatureReply = _reflection.GeneratedProtocolMessageType('TemperatureReply', (_message.Message,), {
  'DESCRIPTOR' : _TEMPERATUREREPLY,
  '__module__' : 'iot_service_pb2'
  # @@protoc_insertion_point(class_scope:iot_service.TemperatureReply)
  })
_sym_db.RegisterMessage(TemperatureReply)

LedRequest = _reflection.GeneratedProtocolMessageType('LedRequest', (_message.Message,), {
  'DESCRIPTOR' : _LEDREQUEST,
  '__module__' : 'iot_service_pb2'
  # @@protoc_insertion_point(class_scope:iot_service.LedRequest)
  })
_sym_db.RegisterMessage(LedRequest)

LedReply = _reflection.GeneratedProtocolMessageType('LedReply', (_message.Message,), {

  'LedstateEntry' : _reflection.GeneratedProtocolMessageType('LedstateEntry', (_message.Message,), {
    'DESCRIPTOR' : _LEDREPLY_LEDSTATEENTRY,
    '__module__' : 'iot_service_pb2'
    # @@protoc_insertion_point(class_scope:iot_service.LedReply.LedstateEntry)
    })
  ,
  'DESCRIPTOR' : _LEDREPLY,
  '__module__' : 'iot_service_pb2'
  # @@protoc_insertion_point(class_scope:iot_service.LedReply)
  })
_sym_db.RegisterMessage(LedReply)
_sym_db.RegisterMessage(LedReply.LedstateEntry)

LightLevelRequest = _reflection.GeneratedProtocolMessageType('LightLevelRequest', (_message.Message,), {
  'DESCRIPTOR' : _LIGHTLEVELREQUEST,
  '__module__' : 'iot_service_pb2'
  # @@protoc_insertion_point(class_scope:iot_service.LightLevelRequest)
  })
_sym_db.RegisterMessage(LightLevelRequest)

LightLevelReply = _reflection.GeneratedProtocolMessageType('LightLevelReply', (_message.Message,), {
  'DESCRIPTOR' : _LIGHTLEVELREPLY,
  '__module__' : 'iot_service_pb2'
  # @@protoc_insertion_point(class_scope:iot_service.LightLevelReply)
  })
_sym_db.RegisterMessage(LightLevelReply)

ActionRequest = _reflection.GeneratedProtocolMessageType('ActionRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONREQUEST,
  '__module__' : 'iot_service_pb2'
  # @@protoc_insertion_point(class_scope:iot_service.ActionRequest)
  })
_sym_db.RegisterMessage(ActionRequest)

ActionReply = _reflection.GeneratedProtocolMessageType('ActionReply', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONREPLY,
  '__module__' : 'iot_service_pb2'
  # @@protoc_insertion_point(class_scope:iot_service.ActionReply)
  })
_sym_db.RegisterMessage(ActionReply)

_IOTSERVICE = DESCRIPTOR.services_by_name['IoTService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033io.grpc.examples.iotserviceB\017IoTServiceProtoP\001\242\002\004TEMP'
  _LEDREPLY_LEDSTATEENTRY._options = None
  _LEDREPLY_LEDSTATEENTRY._serialized_options = b'8\001'
  _TEMPERATUREREQUEST._serialized_start=34
  _TEMPERATUREREQUEST._serialized_end=89
  _USERREQUEST._serialized_start=91
  _USERREQUEST._serialized_end=136
  _USERCREATEREQUEST._serialized_start=138
  _USERCREATEREQUEST._serialized_end=189
  _USERCREATERESPONSE._serialized_start=191
  _USERCREATERESPONSE._serialized_end=227
  _USERRESPONSE._serialized_start=229
  _USERRESPONSE._serialized_end=274
  _TEMPERATUREREPLY._serialized_start=276
  _TEMPERATUREREPLY._serialized_end=315
  _LEDREQUEST._serialized_start=317
  _LEDREQUEST._serialized_end=376
  _LEDREPLY._serialized_start=378
  _LEDREPLY._serialized_end=492
  _LEDREPLY_LEDSTATEENTRY._serialized_start=445
  _LEDREPLY_LEDSTATEENTRY._serialized_end=492
  _LIGHTLEVELREQUEST._serialized_start=494
  _LIGHTLEVELREQUEST._serialized_end=548
  _LIGHTLEVELREPLY._serialized_start=550
  _LIGHTLEVELREPLY._serialized_end=587
  _ACTIONREQUEST._serialized_start=589
  _ACTIONREQUEST._serialized_end=635
  _ACTIONREPLY._serialized_start=637
  _ACTIONREPLY._serialized_end=666
  _IOTSERVICE._serialized_start=669
  _IOTSERVICE._serialized_end=1119
# @@protoc_insertion_point(module_scope)
