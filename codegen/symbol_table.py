
class SymbolTable(object):
    instance = None
    table = {}

    def __init__(self):
        raise Exception('call shared_instance instead')

    @staticmethod
    def shared_instance():
        if SymbolTable.instance is None:
            SymbolTable.instance = object.__new__(SymbolTable)
        return SymbolTable.instance

    def add_identifier(self, identifier, resolved=False):
        if self.table.get(identifier) is not None:
            return
        self.table[identifier] = {
            'resolved': resolved
        }

