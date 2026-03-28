from nodes import VarDecl, OutStmt, RunStmt, FuncDef, ClassDef, MethodDef, Comment

class DSLVibeError(Exception):
    def __init__(self, message, node, file_path, code):
        self.message = message
        self.node = node
        self.file_path = file_path
        self.code = code

    def __str__(self):
        lines = self.code.split('\n')
        line_idx = self.node.line - 1
        col_idx = self.node.col - 1
        
        error_msg = [
            f"⛔ Error: {self.message} on line {self.node.line}",
            f"Last call stopped at {self.file_path}:{self.node.line}:{self.node.col}",
            "\nStack trace:"
        ]
        
        # Show previous line
        if line_idx > 0:
            error_msg.append(f"| {self.node.line - 1} {lines[line_idx - 1]}")
            
        # Show actual erroring line
        actual_line = lines[line_idx]
        error_msg.append(f"| {self.node.line} {actual_line}")
        
        # Add the caret pointer
        prefix = f"| {self.node.line} "
        pointer = " " * (len(prefix) + col_idx - 3) + "^~~~~~"
        error_msg.append(pointer)
        
        # Show next line
        if line_idx < len(lines) - 1:
            error_msg.append(f"| {self.node.line + 1} {lines[line_idx + 1]}")
            
        return "\n".join(error_msg)

class TypeChecker:
    def __init__(self, file_path, code):
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
                if node.is_ref:
                    if not self.lookup(node.value):
                        raise DSLVibeError(f"undefined token '{node.value}'", node, self.file_path, self.code)
                if node.name in self.current_scope():
                    raise DSLVibeError(f"duplicate definition of '{node.name}'", node, self.file_path, self.code)
                self.current_scope()[node.name] = node.value_type
            
            elif isinstance(node, OutStmt):
                for val, is_ref in zip(node.values, node.refs):
                    if is_ref and not self.lookup(val):
                        raise DSLVibeError(f"undefined token '{val}'", node, self.file_path, self.code)
            
            elif isinstance(node, RunStmt):
                if node.arg_is_ref:
                    for arg, is_ref in zip(node.args, node.arg_is_ref):
                        if is_ref and not self.lookup(arg):
                            raise DSLVibeError(f"undefined token '{arg}'", node, self.file_path, self.code)
            
            elif isinstance(node, FuncDef):
                new_scope = {arg: 'STRING' for arg in node.args}
                self.scopes.append(new_scope)
                self.check(node.body)
                self.scopes.pop()

            elif isinstance(node, ClassDef):
                class_scope = {f.name: f.value_type for f in node.fields}
                self.scopes.append(class_scope)
                for method in node.methods:
                    method_scope = {arg: 'STRING' for arg in method.args}
                    self.scopes.append({**self.current_scope(), **method_scope})
                    self.check(method.body)
                    self.scopes.pop()
                self.scopes.pop()
