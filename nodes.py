from dataclasses import dataclass, field

@dataclass
class Comment:
    value: str
    multi_line: bool = False

@dataclass
class VarDecl:
    name: str
    value: str
    value_type: str
    is_pub: bool = False
    is_local: bool = False
    is_ref: bool = False

@dataclass
class OutStmt:
    values: list[str] = field(default_factory=list)
    types: list[str] = field(default_factory=list)
    refs: list[bool] = field(default_factory=list)

@dataclass
class RunStmt:
    executable: str
    args: list[str]
    arg_is_ref: list[bool] = None 

@dataclass
class FuncDef:
    name: str
    args: list[str]
    body: list
    is_pub: bool = False

@dataclass
class ClassDef:
    name: str
    methods: list = field(default_factory=list)
    fields: list = field(default_factory=list)
