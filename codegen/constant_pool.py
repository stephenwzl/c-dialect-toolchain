
class ConstantPool(object):
    """
    static value and constant value should be put into constant pool
    this can accelrate value access
    at runtime, constant pool size can be increased dynamically
    but contant pool any value can not be changed dynamically
    """
    instance = None
    pool = []
    poolIndex = {}

    def __init__(self):
        raise SyntaxError('can not be called')

    @staticmethod
    def shared_instance():
        if ConstantPool.instance is None:
            ConstantPool.instance = object.__new__(ConstantPool)
        return ConstantPool.instance

    def push_constant(self, constant_type, constant_value):
        """
        call this to push a constant value into pool
        :param constant_type: type from CONSTANT_TYPE_typename
        :param constant_value: constant actual value
        :return: index in constant pool
        """
        if self.poolIndex.get(constant_value) is not None:
            return self.poolIndex[constant_value]
        ret = len(self.pool)
        self.pool.append((constant_type, constant_value))
        self.poolIndex[constant_value] = ret
        return ret


CONSTANT_TYPE_CHAR = 0
CONSTANT_TYPE_INT = 1  # this also indicates short, long, char, includes signed unsigned
CONSTANT_TYPE_DOUBLE = 2  # this also indicates float
CONSTANT_TYPE_POINTER = 3   # constant pointer should only point to constant
CONSTANT_TYPE_STRUCT = 4
CONSTANT_TYPE_UNION = 5
CONSTANT_TYPE_STRING = 6
