from lexer import Token, tokenize
from nodes import VarDecl, OutStmt, RunStmt, FuncDef, ClassDef, Comment

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
            raise SyntaxError(f"Line {token.line}: Expected {expected_type}, but got {token.type} ('{token.value}')")
        self.pos += 1
        return token

    def parse_statement(self):
        token = self.peek()
        if not token: return None

        if token.type == 'COMMENT_SINGLE':
            return Comment(self.consume().value[1:].strip(), False)
        elif token.type == 'COMMENT_MULTI':
            return Comment(self.consume().value[2:-2].strip(), True)

        is_pub = False
        if token.type == 'IDENT' and token.value == 'pub':
            self.consume('IDENT')
            is_pub = True
            token = self.peek()

        if token.type == 'IDENT':
            if token.value == 'var':
                node = self.parse_var_decl()
                if isinstance(node, VarDecl): node.is_pub = is_pub
                return node
            elif token.value == 'out':
                return self.parse_out()
            elif token.value == 'func':
                node = self.parse_func_def()
                if isinstance(node, FuncDef): node.is_pub = is_pub
                return node
            else:
                return self.parse_run()
        
        raise SyntaxError(f"Line {token.line}: Wait, I don't know what to do with {token.value}")

    def parse_var_decl(self):
        self.consume('IDENT') # 'var'
        name = self.consume('IDENT').value
        self.consume('ASSIGN')
        val_token = self.peek()
        val = self.consume().value
        is_ref = val_token.type == 'IDENT'
        vtype = 'INT' if val_token.type == 'NUMBER' else 'STRING'
        
        # Semicolon is optional if at the end of a line or before a CBRACE
        if self.peek() and self.peek().type == 'SEMICOLON':
            self.consume('SEMICOLON')
        return VarDecl(name, val, vtype, is_local=self.in_func, is_ref=is_ref)

    def parse_out(self):
        self.consume('IDENT') # 'out'
        values, types, refs = [], [], []
        while self.peek() and self.peek().type not in ['SEMICOLON', 'CBRACE', 'NEWLINE']:
            val_token = self.peek()
            values.append(self.consume().value)
            types.append('INT' if val_token.type == 'NUMBER' else 'STRING')
            refs.append(val_token.type == 'IDENT')
        
        if self.peek() and self.peek().type == 'SEMICOLON':
            self.consume('SEMICOLON')
        return OutStmt(values, types, refs)

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
            stmt = self.parse_statement()
            if stmt: body.append(stmt)
        self.consume('CBRACE')
        self.in_func = old_in_func
        return FuncDef(name, args, body)

    def parse_run(self):
        exec_name = self.consume('IDENT').value
        args, arg_is_ref = [], []
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
            while self.peek() and self.peek().type not in ['SEMICOLON', 'CBRACE']:
                token = self.peek()
                args.append(self.consume().value)
                arg_is_ref.append(token.type == 'IDENT')
        
        if self.peek() and self.peek().type == 'SEMICOLON':
            self.consume('SEMICOLON')
        return RunStmt(exec_name, args, arg_is_ref=arg_is_ref)

    def parse_all(self):
        nodes = []
        while self.peek():
            stmt = self.parse_statement()
            if stmt: nodes.append(stmt)
        return nodes
