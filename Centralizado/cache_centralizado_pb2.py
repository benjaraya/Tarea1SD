# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cache_centralizado.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63\x61\x63he_centralizado.proto\x12\x05\x63\x61\x63he\"\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x1c\n\x0bGetResponse\x12\r\n\x05value\x18\x01 \x01(\t\"(\n\nPutRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x1e\n\x0bPutResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2n\n\x0c\x43\x61\x63heService\x12.\n\x03Get\x12\x11.cache.GetRequest\x1a\x12.cache.GetResponse\"\x00\x12.\n\x03Put\x12\x11.cache.PutRequest\x1a\x12.cache.PutResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cache_centralizado_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETREQUEST']._serialized_start=35
  _globals['_GETREQUEST']._serialized_end=60
  _globals['_GETRESPONSE']._serialized_start=62
  _globals['_GETRESPONSE']._serialized_end=90
  _globals['_PUTREQUEST']._serialized_start=92
  _globals['_PUTREQUEST']._serialized_end=132
  _globals['_PUTRESPONSE']._serialized_start=134
  _globals['_PUTRESPONSE']._serialized_end=164
  _globals['_CACHESERVICE']._serialized_start=166
  _globals['_CACHESERVICE']._serialized_end=276
# @@protoc_insertion_point(module_scope)
