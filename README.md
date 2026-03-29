# bashDSL: The "TypeScript of Bash"

>[!WARNING]
>this project is in beta stage (and also half AI driven), use it as your own risk

bashDSL is a simple and strict DSL that transpiles to POSIX-compliant Bash. It focuses on safety, strict typing, and modern development experience for shell scripting. Built with Python 3 Standard Library.

## Features
- **Strict Typing**: Supports INT and STRING types with validation.
- **Scoping**: Implements function-level scope and local variable generation.
- **OOP Simulation**: Provides namespaced classes and methods.
- **Precise Error Reporting**: Visual pointers and context for compiler errors.
- **Automatic Cleanup**: Top-level variables are automatically unset at the end of the script.
- **Redirection**: Built-in support for stdout and stderr redirection.

## Quick Start
Transpile a `.shtm` file to Bash:
```bash
python3 -m modules.cli.main <file.shtm>
```

Launch the interactive REPL:
```bash
python3 -m modules.cli.main
```

## Run the Test Suite
```bash
python3 run_tests.py
```

## Documentation
- [Architecture](./docs/devs/ARCHITECTURE.md)
- [Features](./docs/devs/FEATURES.md)
- [Wiki](./docs/wiki/)
## License
MIT License. See [LICENSE](./LICENSE) for details.
