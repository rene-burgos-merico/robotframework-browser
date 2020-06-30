# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: playwright.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='playwright.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10playwright.proto\"\xb6\x02\n\x07Request\x1a\x07\n\x05\x45mpty\x1a\x1a\n\nscreenshot\x12\x0c\n\x04path\x18\x01 \x01(\t\x1a+\n\x0bopenBrowser\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0f\n\x07\x62rowser\x18\x02 \x01(\t\x1a$\n\x04goTo\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0f\n\x07timeout\x18\x02 \x01(\x05\x1a=\n\tinputText\x12\r\n\x05input\x18\x01 \x01(\t\x12\x10\n\x08selector\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x05\x1a\x45\n\x0egetDomProperty\x12\x10\n\x08property\x18\x01 \x01(\t\x12\x10\n\x08selector\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x05\x1a-\n\x08selector\x12\x10\n\x08selector\x18\x01 \x01(\t\x12\x0f\n\x07timeout\x18\x02 \x01(\x05\"h\n\x08Response\x1a\x14\n\x05\x45mpty\x12\x0b\n\x03log\x18\x01 \x01(\t\x1a#\n\x06String\x12\x0b\n\x03log\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x1a!\n\x04\x42ool\x12\x0b\n\x03log\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\x08\x32\xf2\x05\n\nPlaywright\x12\x34\n\nScreenshot\x12\x13.Request.screenshot\x1a\x0f.Response.Empty\"\x00\x12\x36\n\x0bOpenBrowser\x12\x14.Request.openBrowser\x1a\x0f.Response.Empty\"\x00\x12\x31\n\x0c\x43loseBrowser\x12\x0e.Request.Empty\x1a\x0f.Response.Empty\"\x00\x12(\n\x04GoTo\x12\r.Request.goTo\x1a\x0f.Response.Empty\"\x00\x12.\n\x08GetTitle\x12\x0e.Request.Empty\x1a\x10.Response.String\"\x00\x12\x32\n\tInputText\x12\x12.Request.inputText\x1a\x0f.Response.Empty\"\x00\x12=\n\x0eGetDomProperty\x12\x17.Request.getDomProperty\x1a\x10.Response.String\"\x00\x12<\n\x0fGetBoolProperty\x12\x17.Request.getDomProperty\x1a\x0e.Response.Bool\"\x00\x12\x37\n\x0eGetTextContent\x12\x11.Request.selector\x1a\x10.Response.String\"\x00\x12,\n\x06GetUrl\x12\x0e.Request.Empty\x1a\x10.Response.String\"\x00\x12\x33\n\x0b\x43lickButton\x12\x11.Request.selector\x1a\x0f.Response.Empty\"\x00\x12\x35\n\rCheckCheckbox\x12\x11.Request.selector\x1a\x0f.Response.Empty\"\x00\x12\x37\n\x0fUncheckCheckbox\x12\x11.Request.selector\x1a\x0f.Response.Empty\"\x00\x12,\n\x06Health\x12\x0e.Request.Empty\x1a\x10.Response.String\"\x00\x62\x06proto3'
)




_REQUEST_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Request.Empty',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=39,
)

_REQUEST_SCREENSHOT = _descriptor.Descriptor(
  name='screenshot',
  full_name='Request.screenshot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='Request.screenshot.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=41,
  serialized_end=67,
)

_REQUEST_OPENBROWSER = _descriptor.Descriptor(
  name='openBrowser',
  full_name='Request.openBrowser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='Request.openBrowser.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='browser', full_name='Request.openBrowser.browser', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=69,
  serialized_end=112,
)

_REQUEST_GOTO = _descriptor.Descriptor(
  name='goTo',
  full_name='Request.goTo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='Request.goTo.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='Request.goTo.timeout', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=114,
  serialized_end=150,
)

_REQUEST_INPUTTEXT = _descriptor.Descriptor(
  name='inputText',
  full_name='Request.inputText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='Request.inputText.input', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selector', full_name='Request.inputText.selector', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='Request.inputText.timeout', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=152,
  serialized_end=213,
)

_REQUEST_GETDOMPROPERTY = _descriptor.Descriptor(
  name='getDomProperty',
  full_name='Request.getDomProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='property', full_name='Request.getDomProperty.property', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selector', full_name='Request.getDomProperty.selector', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='Request.getDomProperty.timeout', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=215,
  serialized_end=284,
)

_REQUEST_SELECTOR = _descriptor.Descriptor(
  name='selector',
  full_name='Request.selector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='selector', full_name='Request.selector.selector', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='Request.selector.timeout', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=286,
  serialized_end=331,
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_EMPTY, _REQUEST_SCREENSHOT, _REQUEST_OPENBROWSER, _REQUEST_GOTO, _REQUEST_INPUTTEXT, _REQUEST_GETDOMPROPERTY, _REQUEST_SELECTOR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=331,
)


_RESPONSE_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Response.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log', full_name='Response.Empty.log', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=345,
  serialized_end=365,
)

_RESPONSE_STRING = _descriptor.Descriptor(
  name='String',
  full_name='Response.String',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log', full_name='Response.String.log', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='Response.String.body', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=367,
  serialized_end=402,
)

_RESPONSE_BOOL = _descriptor.Descriptor(
  name='Bool',
  full_name='Response.Bool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log', full_name='Response.Bool.log', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='Response.Bool.body', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=404,
  serialized_end=437,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_EMPTY, _RESPONSE_STRING, _RESPONSE_BOOL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=437,
)

_REQUEST_EMPTY.containing_type = _REQUEST
_REQUEST_SCREENSHOT.containing_type = _REQUEST
_REQUEST_OPENBROWSER.containing_type = _REQUEST
_REQUEST_GOTO.containing_type = _REQUEST
_REQUEST_INPUTTEXT.containing_type = _REQUEST
_REQUEST_GETDOMPROPERTY.containing_type = _REQUEST
_REQUEST_SELECTOR.containing_type = _REQUEST
_RESPONSE_EMPTY.containing_type = _RESPONSE
_RESPONSE_STRING.containing_type = _RESPONSE
_RESPONSE_BOOL.containing_type = _RESPONSE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {

  'Empty' : _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_EMPTY,
    '__module__' : 'playwright_pb2'
    # @@protoc_insertion_point(class_scope:Request.Empty)
    })
  ,

  'screenshot' : _reflection.GeneratedProtocolMessageType('screenshot', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_SCREENSHOT,
    '__module__' : 'playwright_pb2'
    # @@protoc_insertion_point(class_scope:Request.screenshot)
    })
  ,

  'openBrowser' : _reflection.GeneratedProtocolMessageType('openBrowser', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_OPENBROWSER,
    '__module__' : 'playwright_pb2'
    # @@protoc_insertion_point(class_scope:Request.openBrowser)
    })
  ,

  'goTo' : _reflection.GeneratedProtocolMessageType('goTo', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_GOTO,
    '__module__' : 'playwright_pb2'
    # @@protoc_insertion_point(class_scope:Request.goTo)
    })
  ,

  'inputText' : _reflection.GeneratedProtocolMessageType('inputText', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_INPUTTEXT,
    '__module__' : 'playwright_pb2'
    # @@protoc_insertion_point(class_scope:Request.inputText)
    })
  ,

  'getDomProperty' : _reflection.GeneratedProtocolMessageType('getDomProperty', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_GETDOMPROPERTY,
    '__module__' : 'playwright_pb2'
    # @@protoc_insertion_point(class_scope:Request.getDomProperty)
    })
  ,

  'selector' : _reflection.GeneratedProtocolMessageType('selector', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_SELECTOR,
    '__module__' : 'playwright_pb2'
    # @@protoc_insertion_point(class_scope:Request.selector)
    })
  ,
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'playwright_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.Empty)
_sym_db.RegisterMessage(Request.screenshot)
_sym_db.RegisterMessage(Request.openBrowser)
_sym_db.RegisterMessage(Request.goTo)
_sym_db.RegisterMessage(Request.inputText)
_sym_db.RegisterMessage(Request.getDomProperty)
_sym_db.RegisterMessage(Request.selector)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {

  'Empty' : _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSE_EMPTY,
    '__module__' : 'playwright_pb2'
    # @@protoc_insertion_point(class_scope:Response.Empty)
    })
  ,

  'String' : _reflection.GeneratedProtocolMessageType('String', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSE_STRING,
    '__module__' : 'playwright_pb2'
    # @@protoc_insertion_point(class_scope:Response.String)
    })
  ,

  'Bool' : _reflection.GeneratedProtocolMessageType('Bool', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSE_BOOL,
    '__module__' : 'playwright_pb2'
    # @@protoc_insertion_point(class_scope:Response.Bool)
    })
  ,
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'playwright_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Empty)
_sym_db.RegisterMessage(Response.String)
_sym_db.RegisterMessage(Response.Bool)



_PLAYWRIGHT = _descriptor.ServiceDescriptor(
  name='Playwright',
  full_name='Playwright',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=440,
  serialized_end=1194,
  methods=[
  _descriptor.MethodDescriptor(
    name='Screenshot',
    full_name='Playwright.Screenshot',
    index=0,
    containing_service=None,
    input_type=_REQUEST_SCREENSHOT,
    output_type=_RESPONSE_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='OpenBrowser',
    full_name='Playwright.OpenBrowser',
    index=1,
    containing_service=None,
    input_type=_REQUEST_OPENBROWSER,
    output_type=_RESPONSE_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CloseBrowser',
    full_name='Playwright.CloseBrowser',
    index=2,
    containing_service=None,
    input_type=_REQUEST_EMPTY,
    output_type=_RESPONSE_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GoTo',
    full_name='Playwright.GoTo',
    index=3,
    containing_service=None,
    input_type=_REQUEST_GOTO,
    output_type=_RESPONSE_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTitle',
    full_name='Playwright.GetTitle',
    index=4,
    containing_service=None,
    input_type=_REQUEST_EMPTY,
    output_type=_RESPONSE_STRING,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InputText',
    full_name='Playwright.InputText',
    index=5,
    containing_service=None,
    input_type=_REQUEST_INPUTTEXT,
    output_type=_RESPONSE_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDomProperty',
    full_name='Playwright.GetDomProperty',
    index=6,
    containing_service=None,
    input_type=_REQUEST_GETDOMPROPERTY,
    output_type=_RESPONSE_STRING,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBoolProperty',
    full_name='Playwright.GetBoolProperty',
    index=7,
    containing_service=None,
    input_type=_REQUEST_GETDOMPROPERTY,
    output_type=_RESPONSE_BOOL,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTextContent',
    full_name='Playwright.GetTextContent',
    index=8,
    containing_service=None,
    input_type=_REQUEST_SELECTOR,
    output_type=_RESPONSE_STRING,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetUrl',
    full_name='Playwright.GetUrl',
    index=9,
    containing_service=None,
    input_type=_REQUEST_EMPTY,
    output_type=_RESPONSE_STRING,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClickButton',
    full_name='Playwright.ClickButton',
    index=10,
    containing_service=None,
    input_type=_REQUEST_SELECTOR,
    output_type=_RESPONSE_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CheckCheckbox',
    full_name='Playwright.CheckCheckbox',
    index=11,
    containing_service=None,
    input_type=_REQUEST_SELECTOR,
    output_type=_RESPONSE_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UncheckCheckbox',
    full_name='Playwright.UncheckCheckbox',
    index=12,
    containing_service=None,
    input_type=_REQUEST_SELECTOR,
    output_type=_RESPONSE_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Health',
    full_name='Playwright.Health',
    index=13,
    containing_service=None,
    input_type=_REQUEST_EMPTY,
    output_type=_RESPONSE_STRING,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PLAYWRIGHT)

DESCRIPTOR.services_by_name['Playwright'] = _PLAYWRIGHT

# @@protoc_insertion_point(module_scope)
