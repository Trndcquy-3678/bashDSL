# Architecture: The bashDSL Pipeline

This document outlines the internal stages of the bashDSL transpiler.

## 1. Lexer (modules/core/lexer.py)
- **Role**: Performs lexical analysis, converting raw text into Token objects.
- **Implementation**: Uses a regular expression specification (TOKEN_SPEC) to identify symbols, keywords, and literals.
- **Tracking**: Captures both line and column information for every token to support precise error reporting.

## 2. Parser (modules/core/parser.py)
- **Role**: Performs syntactic analysis, converting tokens into an Abstract Syntax Tree (AST).
- **Implementation**: A recursive descent parser that validates the language grammar and builds node objects defined in `modules/core/nodes.py`.
- **Key Constructs**: Handles variable declarations, function definitions, class structures, and explicit command execution via the 'run' keyword.

## 3. Type Checker (modules/engine/checker.py)
- **Role**: Performs semantic analysis and validation before code generation.
- **Features**:
  - **Type Validation**: Ensures consistent usage of INT and STRING types.
  - **Scope Management**: Uses a stack of symbol tables to manage function and class scopes, preventing variable leakage and unauthorized shadowing.
  - **Error Reporting**: Implements the DSLVibeError class to provide visual caret pointers and source code context for errors.

## 4. Generator (modules/engine/generator.py)
- **Role**: Transpilation stage that generates POSIX-compliant Bash scripts.
- **Features**:
  - **Namespacing**: Implements class methods using 'ClassName:MethodName' formatting.
  - **Scoping**: Maps internal variables to Bash 'local' variables where appropriate.
  - **Cleanup**: Appends 'unset' commands for script-level variables to ensure environment integrity.

## 5. CLI (modules/cli/)
- **main.py**: Standard entry point for file transpilation.
- **repl.py**: Interactive execution environment using a persistent shell process.
