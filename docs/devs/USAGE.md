# 🎮 Usage: Running & Testing bashDSL 🏃‍♂️💨

Yo! Here's how to actually get this transpiler working. 🏎️💨

## 🏗️ Transpiling Code
Use `main.py` via the module path. 🏢🐍
```bash
python3 -m modules.cli.main <file.shtm>
```

### Example:
```bash
python3 -m modules.cli.main tests/pass_example.shtm
```

## 🧪 Running the Test Suite
The `run_tests.py` script is modular. 🧩✨ It discovers all files in the `tests/` directory and checks them based on their prefix:
- `pass_*.shtm`: Expected to succeed. ✅
- `fail_*.shtm`: Expected to fail. 🛑

### Run it like this:
```bash
python3 run_tests.py
```

## 🛡️ Adding a Test
Just drop a new `.shtm` file into the `tests/` folder!
- Name it `pass_my_test.shtm` if you want it to succeed.
- Name it `fail_my_test.shtm` if you're testing the Bouncer 🚪 and want it to block something.

Happy coding! 🚀✨
