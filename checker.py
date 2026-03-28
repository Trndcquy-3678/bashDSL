from nodes import VarDecl, OutStmt, RunStmt, FuncDef

class TypeChecker:
    def __init__(self):
        # Stack of scopes (symbol tables)
        self.scopes = [{}] # Global scope is at the bottom

    def current_scope(self):
        return self.scopes[-1]

    def check(self, nodes):
        for node in nodes:
            if isinstance(node, VarDecl):
                # Check for duplicate in the CURRENT scope
                if node.name in self.current_scope():
                    raise NameError(f"Hold up! '{node.name}' is already defined in this scope. You can't just 'var' it again. 🙅‍♂️")
                
                self.current_scope()[node.name] = node.value_type
            
            elif isinstance(node, OutStmt):
                pass
            
            elif isinstance(node, RunStmt):
                pass
            
            elif isinstance(node, FuncDef):
                # Push a new scope for the function body! 🏢🛡️
                new_scope = {arg: 'STRING' for arg in node.args} # Args are strings in bash
                self.scopes.append(new_scope)
                
                self.check(node.body) # Recursive check! 🧠🔄
                
                self.scopes.pop() # Bye bye scope! 🚪✨
