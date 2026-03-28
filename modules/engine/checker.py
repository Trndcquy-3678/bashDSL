from modules.core.nodes import VarDecl, OutStmt, RunStmt, FuncDef, ClassDef, MethodDef, Comment

class DSLVibeError(Exception):
    def __init__(self, message, line, col, file_path, code):
        self.message = message
        self.line = line
        self.col = col
        self.file_path = file_path
        self.code = code

    def __str__(self):
        lines = self.code.split('\n')
        line_idx = self.line - 1
        col_idx = self.col - 1
        error_msg = [
            f"⛔ Error: {self.message} on line {self.line}",
            f"Last call stopped at {self.file_path}:{self.line}:{self.col}",
            "\nStack trace:"
        ]
        if line_idx > 0: error_msg.append(f"| {self.line - 1} {lines[line_idx - 1]}")
        actual_line = lines[line_idx]
        error_msg.append(f"| {self.line} {actual_line}")
        prefix = f"| {self.line} "
        pointer = " " * (len(prefix) + col_idx - 1) + "^~~~~~"
        error_msg.append(pointer)
        if line_idx < len(lines) - 1: error_msg.append(f"| {self.line + 1} {lines[line_idx + 1]}")
        return "\n".join(error_msg)

class TypeChecker:
    def __init__(self, file_path, code):
        # 🎭 Track both variables and functions!
        self.scopes = [{}] 
        self.file_path = file_path
        self.code = code

    def current_scope(self):
        return self.scopes[-1]

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def check(self, nodes):
        for node in nodes:
            if isinstance(node, Comment): continue

            if isinstance(node, VarDecl):
                if self.lookup(node.name):
                    raise DSLVibeError(f"duplicate definition of '{node.name}'", node.line, node.name_col, self.file_path, self.code)
                if node.is_ref:
                    if not self.lookup(node.value):
                        raise DSLVibeError(f"undefined token '{node.value}'", node.line, node.value_col, self.file_path, self.code)
                self.current_scope()[node.name] = 'VAR'
            
            elif isinstance(node, OutStmt):
                for val, col, is_ref in zip(node.values, node.val_cols, node.refs):
                    if is_ref and not self.lookup(val):
                        raise DSLVibeError(f"undefined token '{val}'", node.line, col, self.file_path, self.code)
            
            elif isinstance(node, RunStmt):
                # 🛡️ THE BASH XSS PROTECTOR:
                # If it's a namespaced call (e.g. Human:sayHi), we assume it's a class method for now.
                # If it's a plain identifier, it MUST be a defined function or a known command.
                if ":" not in node.executable:
                    if not self.lookup(node.executable):
                        # If it's not a function, we check if it was intended as a system command
                        raise DSLVibeError(f"undefined token '{node.executable}' (If this is a system command, you gotta use 'run') 🛡️🛑", node.line, node.col, self.file_path, self.code)
                
                if node.arg_is_ref:
                    for arg, col, is_ref in zip(node.args, node.arg_cols, node.arg_is_ref):
                        if is_ref and not self.lookup(arg):
                            raise DSLVibeError(f"undefined token '{arg}'", node.line, col, self.file_path, self.code)
            
            elif isinstance(node, FuncDef):
                # Define function in current scope BEFORE checking body
                if self.lookup(node.name):
                     raise DSLVibeError(f"duplicate definition of function '{node.name}'", node.line, node.col, self.file_path, self.code)
                self.current_scope()[node.name] = 'FUNC'
                
                new_scope = {arg: 'VAR' for arg in node.args}
                self.scopes.append(new_scope)
                self.check(node.body)
                self.scopes.pop()

            elif isinstance(node, ClassDef):
                if self.lookup(node.name):
                     raise DSLVibeError(f"duplicate definition of class '{node.name}'", node.line, node.col, self.file_path, self.code)
                self.current_scope()[node.name] = 'CLASS'
                
                class_scope = {f.name: 'VAR' for f in node.fields}
                self.scopes.append(class_scope)
                for method in node.methods:
                    method_scope = {arg: 'VAR' for arg in method.args}
                    self.scopes.append({**self.current_scope(), **method_scope})
                    self.check(method.body)
                    self.scopes.pop()
                self.scopes.pop()
