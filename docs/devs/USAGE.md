# Usage Guide

Instructions for running and testing the bashDSL transpiler.

## Transpilation
Use the Python module execution flag to run the main entry point.

```bash
python3 -m modules.cli.main <file.shtm>
```

### Example
```bash
python3 -m modules.cli.main tests/pass_example.shtm
```

## Interactive REPL
Running the main module without arguments launches the interactive REPL.

```bash
python3 -m modules.cli.main
```

## Testing
The test runner automatically discovers and executes tests located in the `tests/` directory.

```bash
python3 run_tests.py
```

### Test Naming Conventions
- **pass_*.shtm**: Tests that are expected to transpile successfully.
- **fail_*.shtm**: Tests designed to trigger specific compiler errors.

## Adding New Tests
To add a test case, create a new `.shtm` file in the `tests/` directory following the naming conventions above.
