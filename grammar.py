import ply.yacc as yacc
from lexer import tokens


# grammar start
def p_translation_unit(p):
    """translation_unit : top_level_declaration
                        | translation_unit top_level_declaration
    """
    pass


# FIXME: currently, top level 'function_definition', 'declaration', 'class_declaration_list' is not supported
# in code generation, 'class_declaration_list' is ignored
# 'top_level_declaration' implementation
def p_top_level_declaration(p):
    """top_level_declaration: class_interface
                            | class_implementation
                            | category_interface
                            | category_implementation
                            | protocol_declaration
    """
    pass


# FIXME: currently, class_interface do not support instance_variables, only support properties
# properties are contained in interface_delcaration_list
# 'class_interface' implementation
def p_class_interface(p):
    """class_interface: INTERFACE class_name interface_declaration_list END
                      | INTERFACE class_name COLON superclass_name interface_declaration_list END
                      | INTERFACE class_name protocol_reference_list interface_declaration_list END
                      | INTERFACE class_name COLON superclass_name protocol_reference_list interface_declaration_list END
    """
    pass


# 'class_name' implementation
def p_class_name(p):
    """class_name: IDENTIFIER
    """
    pass