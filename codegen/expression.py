"""
when generating expression bytecode, always do:
gen left node first, then gen right node
"""

from grammar.ObjectiveCParser import ObjectiveCParser

TYPENAME_void = 0
TYPENAME_char = 1
TYPENAME_short = 2
TYPENAME_int = 3
TYPENAME_long = 4
TYPENAME_float = 5
TYPENAME_double = 6
TYPENAME_signed = 7
TYPENAME_unsigned = 8
TYPENAME_POINTER = 9  # this includes: genericType, identifier pointer
TYPENAME_STRUCT = 10
TYPENAME_UNION = 11
TYPENAME_ENUM = 12


# TODO: enumDeclaration
def gen_enum_declaration(ctx):
    pass


# varDeclaration is always the format: declarationSpecifiers initDeclaratorList
def gen_var_declaration(ctx):
    code = []
    declaration_specifiers_ctx = ctx.declarationSpecifiers()
    init_declarator_list_ctx = ctx.initDeclaratorList()
    (is_static, is_const, type_names) = gen_declaration_specifiers(declaration_specifiers_ctx)

    return code


# TODO: complete
def gen_declaration_specifiers(ctx):
    count = ctx.getChildCount()
    is_static = False
    is_const = False
    type_names = []
    for index in range(0, count):
        child_ctx = ctx.getChild(index)
        if child_ctx.getRuleIndex() == ObjectiveCParser.RULE_storageClassSpecifier:
            is_static = gen_storagge_class_specifier(child_ctx)
        if child_ctx.getRuleIndex() == ObjectiveCParser.RULE_typeQualifier:
            is_const = gen_type_qualifier(child_ctx)
        if child_ctx.getRuleIndex() == ObjectiveCParser.RULE_typeSpecifier:
            type_names.append(gen_type_specifier(child_ctx))
    # here indicates that: if is value type specifier, default to signed
    if TYPENAME_POINTER not in type_names and TYPENAME_ENUM not in type_names and TYPENAME_STRUCT not in type_names and TYPENAME_UNION not in type_names:
        if TYPENAME_unsigned not in type_names and TYPENAME_signed not in type_names:
            type_names.append(TYPENAME_signed)

    return is_static, is_const, type_names


# TODO: complete
def gen_init_declarator_list(ctx):
    return []


# this only indicates if is static
def gen_storagge_class_specifier(ctx):
    count = ctx.getChildCount()
    for index in range(0, count):
        child_ctx = ctx.getChild(index)
        if child_ctx.getRuleIndex() == ObjectiveCParser.STATIC:
            return True
    return False


# this only indicates if is const
def gen_type_qualifier(ctx):
    return ctx.getChild().getRuleIndex() == ObjectiveCParser.CONST


# TODO: support typeof(expression) to get type specifiers
def gen_type_specifier(ctx):
    rule = ctx.getChild().getRuleIndex()
    if rule == ObjectiveCParser.VOID:
        return TYPENAME_void
    if rule == ObjectiveCParser.CHAR:
        return TYPENAME_char
    if rule == ObjectiveCParser.SHORT:
        return TYPENAME_short
    if rule == ObjectiveCParser.INT:
        return TYPENAME_int
    if rule == ObjectiveCParser.LONG:
        return TYPENAME_long
    if rule == ObjectiveCParser.FLOAT:
        return TYPENAME_float
    if rule == ObjectiveCParser.DOUBLE:
        return TYPENAME_double
    if rule == ObjectiveCParser.SIGNED:
        return TYPENAME_signed
    if rule == ObjectiveCParser.UNSIGNED:
        return TYPENAME_unsigned
    if rule == ObjectiveCParser.RULE_genericTypeSpecifier:
        return TYPENAME_POINTER
    if rule == ObjectiveCParser.RULE_identifier:
        return TYPENAME_POINTER



