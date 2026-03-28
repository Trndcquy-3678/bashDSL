from dataclasses import dataclass, field

@dataclass
class Comment:
    line: int
    col: int
    value: str
    multi_line: bool = False

@dataclass
class VarDecl:
    line: int
    col: int
    name: str
    name_col: int # 🎯 Precise location of the name
    value: str
    value_col: int # 🎯 Precise location of the value
    value_type: str
    is_pub: bool = False
    is_local: bool = False
    is_ref: bool = False

@dataclass
class OutStmt:
    line: int
    col: int
    values: list[str] = field(default_factory=list)
    val_cols: list[int] = field(default_factory=list) # 🎯 Locations of all values
    types: list[str] = field(default_factory=list)
    refs: list[bool] = field(default_factory=list)

@dataclass
class RunStmt:
    line: int
    col: int
    executable: str = ""
    args: list[str] = field(default_factory=list)
    arg_cols: list[int] = field(default_factory=list) # 🎯 Locations of all args
    arg_is_ref: list[bool] = None 

@dataclass
class MethodDef:
    line: int
    col: int
    name: str = ""
    args: list[str] = field(default_factory=list)
    body: list = field(default_factory=list)

@dataclass
class FuncDef:
    line: int
    col: int
    name: str = ""
    args: list[str] = field(default_factory=list)
    body: list = field(default_factory=list)
    is_pub: bool = False

@dataclass
class ClassDef:
    line: int
    col: int
    name: str = ""
    methods: list = field(default_factory=list)
    fields: list = field(default_factory=list)
