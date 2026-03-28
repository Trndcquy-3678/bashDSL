from dataclasses import dataclass

@dataclass
class VarDecl:
    name: str
    value: str
    value_type: str # 'INT' or 'STRING'
    is_local: bool = False
    is_ref: bool = False # Is the value a variable reference?

@dataclass
class OutStmt:
    value: str
    value_type: str
    is_ref: bool = False

@dataclass
class RunStmt:
    executable: str
    args: list[str]
    # We'll treat all args as refs for now if they aren't quoted strings
    arg_is_ref: list[bool] = None 

@dataclass
class FuncDef:
    name: str
    args: list[str]
    body: list
