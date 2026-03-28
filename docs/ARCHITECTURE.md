# 🏗️ Architecture: The bashDSL Pipeline 🧬

Yo! Here's how the magic happens under the hood. 🪄

## 1. Lexer (`lexer.py`) 🧩
- **Role**: Turns text into `Token` objects.
- **Vibe**: Uses `TOKEN_SPEC` (regexes) to spot symbols like `var`, `=`, `func`, and `(` as separate tokens.
- **Add a feature?**: Add the new symbol's regex to `TOKEN_SPEC` first.

## 2. Parser (`parser.py`) 🧠
- **Role**: Turns tokens into an **AST** (Abstract Syntax Tree) using `nodes.py`.
- **Vibe**: It's a "Recursive Descent" parser. It walks the tokens and builds `VarDecl`, `FuncDef`, `OutStmt`, etc.
- **Add a feature?**: 
  - Add a new `@dataclass` in `nodes.py`.
  - Add a `parse_something()` method in `Parser`.
  - Hook it into `parse_statement()`.

## 3. Type Checker (`checker.py`) 🛡️
- **Role**: The "Bouncer" 🚪. It walks the AST to find errors *before* any Bash is written.
- **Vibe**: 
  - Tracks types (`INT` vs `STRING`).
  - Blocks **Duplicate Definition** (re-declaring with `var`).
  - Handles **Scopes** (a stack of symbol tables) for functions so locals don't leak. 🏢

## 4. Generator (`generator.py`) 🎭
- **Role**: The translator. Turns AST nodes into POSIX-compliant Bash.
- **Vibe**: 
  - Uses `local` for variables inside functions. 🛡️
  - Slaps the `$` sign on **Variable References** so Bash knows you're spending its coins. 💸✨
  - **Add a feature?**: Add a new `elif isinstance(node, YourNewNode):` and return the Bash string.

## 5. Main (`main.py`) 🍬
- **Role**: The glue. It ties all 4 stages together and spits out the final result.
