# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xviz/v2/uiprimitives.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xviz_avs.v2 import options_pb2 as xviz_dot_v2_dot_options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='xviz/v2/uiprimitives.proto',
  package='xviz.v2',
  syntax='proto3',
  serialized_options=_b('\n\013com.xviz.v2B\021UiprimitivesProtoP\001Z\004v2pb\242\002\004XVIZ\252\002\007xviz.V2\312\002\007Xviz\\V2'),
  serialized_pb=_b('\n\x1axviz/v2/uiprimitives.proto\x12\x07xviz.v2\x1a\x15xviz/v2/options.proto\"z\n\tTreeTable\x12)\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x18.xviz.v2.TreeTableColumn\x12%\n\x05nodes\x18\x02 \x03(\x0b\x32\x16.xviz.v2.TreeTableNode:\x1b\xc2\xbb\x1a\x17ui-primitives/treetable\"\xd1\x01\n\x0fTreeTableColumn\x12\x14\n\x0c\x64isplay_text\x18\x01 \x01(\t\x12\x31\n\x04type\x18\x02 \x01(\x0e\x32#.xviz.v2.TreeTableColumn.ColumnType\x12\x0c\n\x04unit\x18\x03 \x01(\t\"g\n\nColumnType\x12)\n%TREE_TABLE_COLUMN_COLUMN_TYPE_INVALID\x10\x00\x12\t\n\x05INT32\x10\x01\x12\n\n\x06\x44OUBLE\x10\x02\x12\n\n\x06STRING\x10\x03\x12\x0b\n\x07\x42OOLEAN\x10\x04\"B\n\rTreeTableNode\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06parent\x18\x02 \x01(\x05\x12\x15\n\rcolumn_values\x18\x03 \x03(\tBC\n\x0b\x63om.xviz.v2B\x11UiprimitivesProtoP\x01Z\x04v2pb\xa2\x02\x04XVIZ\xaa\x02\x07xviz.V2\xca\x02\x07Xviz\\V2b\x06proto3')
  ,
  dependencies=[xviz_dot_v2_dot_options__pb2.DESCRIPTOR,])



_TREETABLECOLUMN_COLUMNTYPE = _descriptor.EnumDescriptor(
  name='ColumnType',
  full_name='xviz.v2.TreeTableColumn.ColumnType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TREE_TABLE_COLUMN_COLUMN_TYPE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=293,
  serialized_end=396,
)
_sym_db.RegisterEnumDescriptor(_TREETABLECOLUMN_COLUMNTYPE)


_TREETABLE = _descriptor.Descriptor(
  name='TreeTable',
  full_name='xviz.v2.TreeTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='xviz.v2.TreeTable.columns', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='xviz.v2.TreeTable.nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_options=_b('\302\273\032\027ui-primitives/treetable'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=184,
)


_TREETABLECOLUMN = _descriptor.Descriptor(
  name='TreeTableColumn',
  full_name='xviz.v2.TreeTableColumn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_text', full_name='xviz.v2.TreeTableColumn.display_text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='xviz.v2.TreeTableColumn.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='xviz.v2.TreeTableColumn.unit', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TREETABLECOLUMN_COLUMNTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=396,
)


_TREETABLENODE = _descriptor.Descriptor(
  name='TreeTableNode',
  full_name='xviz.v2.TreeTableNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='xviz.v2.TreeTableNode.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='xviz.v2.TreeTableNode.parent', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='column_values', full_name='xviz.v2.TreeTableNode.column_values', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=398,
  serialized_end=464,
)

_TREETABLE.fields_by_name['columns'].message_type = _TREETABLECOLUMN
_TREETABLE.fields_by_name['nodes'].message_type = _TREETABLENODE
_TREETABLECOLUMN.fields_by_name['type'].enum_type = _TREETABLECOLUMN_COLUMNTYPE
_TREETABLECOLUMN_COLUMNTYPE.containing_type = _TREETABLECOLUMN
DESCRIPTOR.message_types_by_name['TreeTable'] = _TREETABLE
DESCRIPTOR.message_types_by_name['TreeTableColumn'] = _TREETABLECOLUMN
DESCRIPTOR.message_types_by_name['TreeTableNode'] = _TREETABLENODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TreeTable = _reflection.GeneratedProtocolMessageType('TreeTable', (_message.Message,), dict(
  DESCRIPTOR = _TREETABLE,
  __module__ = 'xviz.v2.uiprimitives_pb2'
  # @@protoc_insertion_point(class_scope:xviz.v2.TreeTable)
  ))
_sym_db.RegisterMessage(TreeTable)

TreeTableColumn = _reflection.GeneratedProtocolMessageType('TreeTableColumn', (_message.Message,), dict(
  DESCRIPTOR = _TREETABLECOLUMN,
  __module__ = 'xviz.v2.uiprimitives_pb2'
  # @@protoc_insertion_point(class_scope:xviz.v2.TreeTableColumn)
  ))
_sym_db.RegisterMessage(TreeTableColumn)

TreeTableNode = _reflection.GeneratedProtocolMessageType('TreeTableNode', (_message.Message,), dict(
  DESCRIPTOR = _TREETABLENODE,
  __module__ = 'xviz.v2.uiprimitives_pb2'
  # @@protoc_insertion_point(class_scope:xviz.v2.TreeTableNode)
  ))
_sym_db.RegisterMessage(TreeTableNode)


DESCRIPTOR._options = None
_TREETABLE._options = None
# @@protoc_insertion_point(module_scope)
