# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xviz/v2/style.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xviz_avs.v2 import options_pb2 as xviz_dot_v2_dot_options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='xviz/v2/style.proto',
  package='xviz.v2',
  syntax='proto3',
  serialized_options=_b('\n\013com.xviz.v2B\nStyleProtoP\001Z\004v2pb\242\002\004XVIZ\252\002\007xviz.V2\312\002\007Xviz\\V2'),
  serialized_pb=_b('\n\x13xviz/v2/style.proto\x12\x07xviz.v2\x1a\x15xviz/v2/options.proto\"U\n\nStyleClass\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x05style\x18\x02 \x01(\x0b\x32\x19.xviz.v2.StyleObjectValue:\x0f\xc2\xbb\x1a\x0bstyle/class\"\x95\x02\n\x10StyleObjectValue\x12\x12\n\nfill_color\x18\x01 \x01(\x0c\x12\x14\n\x0cstroke_color\x18\x02 \x01(\x0c\x12\x14\n\x0cstroke_width\x18\x03 \x01(\x02\x12\x0e\n\x06radius\x18\x04 \x01(\x02\x12\x11\n\ttext_size\x18\x05 \x01(\x02\x12\x15\n\rtext_rotation\x18\x06 \x01(\x02\x12(\n\x0btext_anchor\x18\x07 \x01(\x0e\x32\x13.xviz.v2.TextAnchor\x12\x35\n\rtext_baseline\x18\x08 \x01(\x0e\x32\x1e.xviz.v2.TextAlignmentBaseline\x12\x0e\n\x06height\x18\t \x01(\x02:\x16\xc2\xbb\x1a\x12style/object_value\"\xe1\x04\n\x10StyleStreamValue\x12\x12\n\nfill_color\x18\x01 \x01(\x0c\x12\x14\n\x0cstroke_color\x18\x02 \x01(\x0c\x12\x14\n\x0cstroke_width\x18\x03 \x01(\x02\x12\x0e\n\x06radius\x18\x04 \x01(\x02\x12\x11\n\ttext_size\x18\x05 \x01(\x02\x12\x15\n\rtext_rotation\x18\x06 \x01(\x02\x12(\n\x0btext_anchor\x18\x07 \x01(\x0e\x32\x13.xviz.v2.TextAnchor\x12\x35\n\rtext_baseline\x18\x08 \x01(\x0e\x32\x1e.xviz.v2.TextAlignmentBaseline\x12\x0e\n\x06height\x18\t \x01(\x02\x12\x19\n\x11radius_min_pixels\x18\n \x01(\r\x12\x19\n\x11radius_max_pixels\x18\x0b \x01(\r\x12\x1f\n\x17stroke_width_min_pixels\x18\x0c \x01(\r\x12\x1f\n\x17stroke_width_max_pixels\x18\r \x01(\r\x12\x0f\n\x07opacity\x18\x0e \x01(\x02\x12\x0f\n\x07stroked\x18\x0f \x01(\x08\x12\x0e\n\x06\x66illed\x18\x10 \x01(\x08\x12\x10\n\x08\x65xtruded\x18\x11 \x01(\x08\x12\x15\n\rradius_pixels\x18\x12 \x01(\r\x12\x13\n\x0b\x66ont_weight\x18\x13 \x01(\r\x12\x13\n\x0b\x66ont_family\x18\x14 \x01(\t\x12\x31\n\x10point_color_mode\x18\x15 \x01(\x0e\x32\x17.xviz.v2.PointColorMode\x12\x1a\n\x12point_color_domain\x18\x16 \x03(\x02:\x16\xc2\xbb\x1a\x12style/stream_value\"\x17\n\x05\x43olor\x12\x0e\n\x06values\x18\x01 \x01(\x0c*E\n\nTextAnchor\x12\x17\n\x13TEXT_ANCHOR_INVALID\x10\x00\x12\t\n\x05START\x10\x01\x12\n\n\x06MIDDLE\x10\x02\x12\x07\n\x03\x45ND\x10\x03*]\n\x15TextAlignmentBaseline\x12#\n\x1fTEXT_ALIGNMENT_BASELINE_INVALID\x10\x00\x12\x07\n\x03TOP\x10\x01\x12\n\n\x06\x43\x45NTER\x10\x02\x12\n\n\x06\x42OTTOM\x10\x03*V\n\x0ePointColorMode\x12\x1c\n\x18POINT_COLOR_MODE_INVALID\x10\x00\x12\r\n\tELEVATION\x10\x01\x12\x17\n\x13\x44ISTANCE_TO_VEHICLE\x10\x02\x42<\n\x0b\x63om.xviz.v2B\nStyleProtoP\x01Z\x04v2pb\xa2\x02\x04XVIZ\xaa\x02\x07xviz.V2\xca\x02\x07Xviz\\V2b\x06proto3')
  ,
  dependencies=[xviz_dot_v2_dot_options__pb2.DESCRIPTOR,])

_TEXTANCHOR = _descriptor.EnumDescriptor(
  name='TextAnchor',
  full_name='xviz.v2.TextAnchor',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEXT_ANCHOR_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIDDLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1059,
  serialized_end=1128,
)
_sym_db.RegisterEnumDescriptor(_TEXTANCHOR)

TextAnchor = enum_type_wrapper.EnumTypeWrapper(_TEXTANCHOR)
_TEXTALIGNMENTBASELINE = _descriptor.EnumDescriptor(
  name='TextAlignmentBaseline',
  full_name='xviz.v2.TextAlignmentBaseline',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEXT_ALIGNMENT_BASELINE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CENTER', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOTTOM', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1130,
  serialized_end=1223,
)
_sym_db.RegisterEnumDescriptor(_TEXTALIGNMENTBASELINE)

TextAlignmentBaseline = enum_type_wrapper.EnumTypeWrapper(_TEXTALIGNMENTBASELINE)
_POINTCOLORMODE = _descriptor.EnumDescriptor(
  name='PointColorMode',
  full_name='xviz.v2.PointColorMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POINT_COLOR_MODE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELEVATION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISTANCE_TO_VEHICLE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1225,
  serialized_end=1311,
)
_sym_db.RegisterEnumDescriptor(_POINTCOLORMODE)

PointColorMode = enum_type_wrapper.EnumTypeWrapper(_POINTCOLORMODE)
TEXT_ANCHOR_INVALID = 0
START = 1
MIDDLE = 2
END = 3
TEXT_ALIGNMENT_BASELINE_INVALID = 0
TOP = 1
CENTER = 2
BOTTOM = 3
POINT_COLOR_MODE_INVALID = 0
ELEVATION = 1
DISTANCE_TO_VEHICLE = 2



_STYLECLASS = _descriptor.Descriptor(
  name='StyleClass',
  full_name='xviz.v2.StyleClass',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='xviz.v2.StyleClass.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='style', full_name='xviz.v2.StyleClass.style', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('\302\273\032\013style/class'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=140,
)


_STYLEOBJECTVALUE = _descriptor.Descriptor(
  name='StyleObjectValue',
  full_name='xviz.v2.StyleObjectValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fill_color', full_name='xviz.v2.StyleObjectValue.fill_color', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stroke_color', full_name='xviz.v2.StyleObjectValue.stroke_color', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stroke_width', full_name='xviz.v2.StyleObjectValue.stroke_width', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius', full_name='xviz.v2.StyleObjectValue.radius', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_size', full_name='xviz.v2.StyleObjectValue.text_size', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_rotation', full_name='xviz.v2.StyleObjectValue.text_rotation', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_anchor', full_name='xviz.v2.StyleObjectValue.text_anchor', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_baseline', full_name='xviz.v2.StyleObjectValue.text_baseline', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='xviz.v2.StyleObjectValue.height', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\302\273\032\022style/object_value'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=420,
)


_STYLESTREAMVALUE = _descriptor.Descriptor(
  name='StyleStreamValue',
  full_name='xviz.v2.StyleStreamValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fill_color', full_name='xviz.v2.StyleStreamValue.fill_color', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stroke_color', full_name='xviz.v2.StyleStreamValue.stroke_color', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stroke_width', full_name='xviz.v2.StyleStreamValue.stroke_width', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius', full_name='xviz.v2.StyleStreamValue.radius', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_size', full_name='xviz.v2.StyleStreamValue.text_size', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_rotation', full_name='xviz.v2.StyleStreamValue.text_rotation', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_anchor', full_name='xviz.v2.StyleStreamValue.text_anchor', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_baseline', full_name='xviz.v2.StyleStreamValue.text_baseline', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='xviz.v2.StyleStreamValue.height', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius_min_pixels', full_name='xviz.v2.StyleStreamValue.radius_min_pixels', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius_max_pixels', full_name='xviz.v2.StyleStreamValue.radius_max_pixels', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stroke_width_min_pixels', full_name='xviz.v2.StyleStreamValue.stroke_width_min_pixels', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stroke_width_max_pixels', full_name='xviz.v2.StyleStreamValue.stroke_width_max_pixels', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opacity', full_name='xviz.v2.StyleStreamValue.opacity', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stroked', full_name='xviz.v2.StyleStreamValue.stroked', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filled', full_name='xviz.v2.StyleStreamValue.filled', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extruded', full_name='xviz.v2.StyleStreamValue.extruded', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius_pixels', full_name='xviz.v2.StyleStreamValue.radius_pixels', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='font_weight', full_name='xviz.v2.StyleStreamValue.font_weight', index=18,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='font_family', full_name='xviz.v2.StyleStreamValue.font_family', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point_color_mode', full_name='xviz.v2.StyleStreamValue.point_color_mode', index=20,
      number=21, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point_color_domain', full_name='xviz.v2.StyleStreamValue.point_color_domain', index=21,
      number=22, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\302\273\032\022style/stream_value'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=1032,
)


_COLOR = _descriptor.Descriptor(
  name='Color',
  full_name='xviz.v2.Color',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='xviz.v2.Color.values', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=1034,
  serialized_end=1057,
)

_STYLECLASS.fields_by_name['style'].message_type = _STYLEOBJECTVALUE
_STYLEOBJECTVALUE.fields_by_name['text_anchor'].enum_type = _TEXTANCHOR
_STYLEOBJECTVALUE.fields_by_name['text_baseline'].enum_type = _TEXTALIGNMENTBASELINE
_STYLESTREAMVALUE.fields_by_name['text_anchor'].enum_type = _TEXTANCHOR
_STYLESTREAMVALUE.fields_by_name['text_baseline'].enum_type = _TEXTALIGNMENTBASELINE
_STYLESTREAMVALUE.fields_by_name['point_color_mode'].enum_type = _POINTCOLORMODE
DESCRIPTOR.message_types_by_name['StyleClass'] = _STYLECLASS
DESCRIPTOR.message_types_by_name['StyleObjectValue'] = _STYLEOBJECTVALUE
DESCRIPTOR.message_types_by_name['StyleStreamValue'] = _STYLESTREAMVALUE
DESCRIPTOR.message_types_by_name['Color'] = _COLOR
DESCRIPTOR.enum_types_by_name['TextAnchor'] = _TEXTANCHOR
DESCRIPTOR.enum_types_by_name['TextAlignmentBaseline'] = _TEXTALIGNMENTBASELINE
DESCRIPTOR.enum_types_by_name['PointColorMode'] = _POINTCOLORMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StyleClass = _reflection.GeneratedProtocolMessageType('StyleClass', (_message.Message,), dict(
  DESCRIPTOR = _STYLECLASS,
  __module__ = 'xviz.v2.style_pb2'
  # @@protoc_insertion_point(class_scope:xviz.v2.StyleClass)
  ))
_sym_db.RegisterMessage(StyleClass)

StyleObjectValue = _reflection.GeneratedProtocolMessageType('StyleObjectValue', (_message.Message,), dict(
  DESCRIPTOR = _STYLEOBJECTVALUE,
  __module__ = 'xviz.v2.style_pb2'
  # @@protoc_insertion_point(class_scope:xviz.v2.StyleObjectValue)
  ))
_sym_db.RegisterMessage(StyleObjectValue)

StyleStreamValue = _reflection.GeneratedProtocolMessageType('StyleStreamValue', (_message.Message,), dict(
  DESCRIPTOR = _STYLESTREAMVALUE,
  __module__ = 'xviz.v2.style_pb2'
  # @@protoc_insertion_point(class_scope:xviz.v2.StyleStreamValue)
  ))
_sym_db.RegisterMessage(StyleStreamValue)

Color = _reflection.GeneratedProtocolMessageType('Color', (_message.Message,), dict(
  DESCRIPTOR = _COLOR,
  __module__ = 'xviz.v2.style_pb2'
  # @@protoc_insertion_point(class_scope:xviz.v2.Color)
  ))
_sym_db.RegisterMessage(Color)


DESCRIPTOR._options = None
_STYLECLASS._options = None
_STYLEOBJECTVALUE._options = None
_STYLESTREAMVALUE._options = None
# @@protoc_insertion_point(module_scope)
