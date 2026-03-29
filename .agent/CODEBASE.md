# Codebase DNA: bashDSL

This document provides a comprehensive overview of the bashDSL architecture, security model, and implementation details for context preservation.

## Project Overview
- **Purpose**: A strict, typed DSL for generating POSIX-compliant Bash scripts.
- **Stack**: Python 3 Standard Library (no external dependencies).
- **Design Goals**: Safety, modularity, and robust error reporting.

## Modular Architecture
The codebase is organized into three primary modules:

### 1. modules/core/
- **lexer.py**: Implements regex-based tokenization with line and column tracking.
- **nodes.py**: Defines the Abstract Syntax Tree (AST) nodes (e.g., VarDecl, FuncDef, ClassDef).
- **parser.py**: A recursive descent parser that handles language constructs, including 'run' for system commands and dot-access for class methods.

### 2. modules/engine/
- **checker.py**: The Type Checker. Validates types (INT/STRING), scope isolation, and prevents duplicate definitions. Implements precise error reporting with visual pointers.
- **generator.py**: The Transpiler. Converts AST nodes into Bash script lines, handling 'local' variables, automatic unsetting, and namespacing.

### 3. modules/cli/
- **main.py**: The primary entry point for file-based transpilation.
- **repl.py**: An interactive Read-Eval-Print Loop with a persistent background shell process.

## Security Model
To prevent arbitrary shell injection (Bash XSS):
- **Undefined Token Check**: Identifiers must be declared before use.
- **Explicit Execution**: External system commands require the 'run' keyword.
- **Scope Isolation**: Prevents internal variables from leaking into parent scopes.

## Language Specification
- **Variables**: Declared with 'var'. Supports basic type inference (INT/STRING).
- **Functions**: Declared with 'func'. Support local scoping.
- **Classes**: Simulated OOP via namespacing. Methods use 'ClassName:MethodName' format.
- **Output**: 'out' statement with support for 'stdout' and 'stderr' destinations.
- **Comments**: Supports single-line (#) and multi-line (/* */) comments.

## Testing and Verification
- **Test Runner**: 'run_tests.py' executes the test suite.
- **Naming Convention**:
  - pass_*.shtm: Expected to succeed.
  - fail_*.shtm: Expected to fail with a validation error.

---
**Status**: Stable and Modular.
