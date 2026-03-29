# 🧠 Ultimate Brain Dump: bashDSL DNA 🧬

This document preserves the entire context, architecture, and "vibes" of **bashDSL** for seamless machine switching. 🚀✨

## 🏗️ Project Overview
- **Vibe**: A Gen Z-friendly DSL that makes Bash/POSIX "cosplay" as a real programming language. 🎭
- **Tech Stack**: Strictly **Python 3 Standard Library**. No external dependencies. 🐍
- **Goal**: Safety, strictness, and a modern DX for the shell. 🛡️

## 🗄️ Modular Architecture
The codebase is organized into three distinct "scopes":

1.  **`modules/core/`**: The Foundation 🧬
    -   `lexer.py`: Regex-based tokenization with `line` and `col` tracking. 📍
    -   `nodes.py`: AST definitions (`VarDecl`, `FuncDef`, `ClassDef`, `ShellStmt`, etc.).
    -   `parser.py`: Recursive descent parser. Handles the `run` keyword and `DOT` member access. 🧠🔍

2.  **`modules/engine/`**: The Brains 🧠
    -   `checker.py`: The **Type Checker (Bouncer 🚪)**. Enforces strict types (INT/STRING), scope isolation, and anti-shadowing. Implements **Sniper Error Reporting** with visual caret pointers (`^~~~~~`). 🎯🔭🛡️
    -   `generator.py`: The **Transpiler 🎭**. Generates POSIX-compliant Bash. Handles `local` variables, variable unsetting (cleanup), and colon namespacing for classes (`Human:sayHi`).

3.  **`modules/cli/`**: The Interface 👔
    -   `main.py`: Entry point for transpiling files.
    -   `repl.py`: Interactive, stateful REPL with a persistent `/bin/sh` background process. 🎮

## 🛡️ Security Model (Anti-XSS)
To prevent "Bash XSS" (arbitrary shell injection), we implemented strict rules:
-   **Undefined Tokens**: Using an identifier that isn't a defined variable, function, or class results in a compile error. 🛑
-   **`run` Keyword**: System commands (like `ls`) **must** be prefixed with `run`. This ensures every shell call is intentional. 🏃‍♂️💨
-   **Scope Guarding**: Local variables cannot leak out of their functions. 🏢

## 💅 Language Specification Highlights
-   **Variables**: `var x = 5;` (INT) or `var s = "hi";` (STRING).
-   **Functions**: `func name(args) { body }`.
-   **Classes**: `class Human { var field = 1; func method() { ... } }`.
-   **Output**: `out "msg" "stdout";` or `out "err" "stderr";`. Redirection is built-in. 🗣️
-   **Cleanup**: Script-level variables are automatically `unset` at the end of generated scripts (unless `skip_cleanup` is used in REPL). 🧹

## 🧪 Verification & Testing
-   **Runner**: `run_tests.py` automatically discovers `.shtm` files in `tests/`.
-   **Convention**: `pass_*.shtm` must succeed; `fail_*.shtm` must fail with specific bouncer errors. ✅🛑

## 🛣️ Recent History & Context
-   Migrated from `.shtemplate` to `.shtm`. 🏷️
-   Restructured from flat files to `modules/` structure. 🏗️
-   Implemented strict parent-scope checking to prevent variable shadowing. 🏢
-   Co-authored by **gemini-cli** and **quy** (The brains 🧠). 🤝

---
**Status**: Elite. 💅 Ready for launch. 🚀🌕
