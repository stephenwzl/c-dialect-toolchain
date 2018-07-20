
class GlobalPool(object):
    instance = None
    pool = []

    def __init__(self):
        raise SyntaxError('can not be called')

    @staticmethod
    def shared_instance():
        if GlobalPool.instance is None:
            GlobalPool.instance = object.__new__(GlobalPool)
        return GlobalPool.instance

    def add_variable(self, symbol, type_specifier, value):
        """
        when doing global variable codegen, will not return bytecode op directly
        they will be add into global pool, then generate global pool create/initialize op together
        global pool variables can be changed dynamically

        DEVELOPER IMPORTANT: take care of constant global variable

        :param symbol: symbol is an identifier literal, at runtime, code access global variable by symbol
        :param type_specifier: global variable type
        :param value: variable value
        :return: None
        """
        self.pool.append((symbol, type_specifier, value))

