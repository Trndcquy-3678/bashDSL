from lexer import Token, tokenize
from nodes import VarDecl, OutStmt, RunStmt, FuncDef

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0
        self.in_func = False

    def peek(self) -> Token | None:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected_type: str = None) -> Token:
        token = self.peek()
        if not token:
            raise EOFError("Yo, we're at the end of the file!")
        if expected_type and token.type != expected_type:
            raise SyntaxError(f"Expected {expected_type}, but got {token.type} ('{token.value}')")
        self.pos += 1
        return token

    def parse_statement(self):
        token = self.peek()
        if not token: return None

        if token.type == 'IDENT':
            if token.value == 'var':
                return self.parse_var_decl()
            elif token.value == 'out':
                return self.parse_out()
            elif token.value == 'func':
                return self.parse_func_def()
            else:
                return self.parse_run()
        
        raise SyntaxError(f"Wait, I don't know what to do with {token.value}")

    def parse_var_decl(self):
        self.consume('IDENT') # 'var'
        name = self.consume('IDENT').value
        self.consume('ASSIGN')
        
        val_token = self.peek()
        val = self.consume().value
        
        # 💸 Check if it's a reference
        is_ref = val_token.type == 'IDENT'
        vtype = 'INT' if val_token.type == 'NUMBER' else 'STRING'
        
        self.consume('SEMICOLON')
        return VarDecl(name, val, vtype, is_local=self.in_func, is_ref=is_ref)

    def parse_out(self):
        self.consume('IDENT') # 'out'
        val_token = self.peek()
        val = self.consume().value
        
        # 💸 Check if it's a reference
        is_ref = val_token.type == 'IDENT'
        vtype = 'INT' if val_token.type == 'NUMBER' else 'STRING'
        
        self.consume('SEMICOLON')
        return OutStmt(val, vtype, is_ref=is_ref)

    def parse_func_def(self):
        self.consume('IDENT') # 'func'
        name = self.consume('IDENT').value
        self.consume('OPAR')
        
        args = []
        while self.peek() and self.peek().type != 'CPAR':
            args.append(self.consume('IDENT').value)
            if self.peek() and self.peek().type == 'COMMA':
                self.consume('COMMA')
        
        self.consume('CPAR')
        self.consume('OBRACE')
        
        old_in_func = self.in_func
        self.in_func = True
        body = []
        while self.peek() and self.peek().type != 'CBRACE':
            body.append(self.parse_statement())
        self.consume('CBRACE')
        self.in_func = old_in_func
        
        return FuncDef(name, args, body)

    def parse_run(self):
        exec_name = self.consume('IDENT').value
        args = []
        arg_is_ref = []
        
        # This is where greet(x) gets weird. Let's make it smarter.
        if self.peek() and self.peek().type == 'OPAR':
            self.consume('OPAR')
            while self.peek() and self.peek().type != 'CPAR':
                token = self.peek()
                args.append(self.consume().value)
                arg_is_ref.append(token.type == 'IDENT')
                if self.peek() and self.peek().type == 'COMMA':
                    self.consume('COMMA')
            self.consume('CPAR')
        else:
            while self.peek() and self.peek().type != 'SEMICOLON':
                token = self.peek()
                args.append(self.consume().value)
                arg_is_ref.append(token.type == 'IDENT')
        
        if self.peek() and self.peek().type == 'SEMICOLON':
            self.consume('SEMICOLON')
            
        return RunStmt(exec_name, args, arg_is_ref=arg_is_ref)

    def parse_all(self):
        nodes = []
        while self.peek():
            nodes.append(self.parse_statement())
        return nodes
