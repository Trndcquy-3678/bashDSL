# 🎮 Usage: Running & Testing bashDSL 🏃‍♂️💨

Yo! Here's how to actually get this transpiler working. 🏎️💨

## 🏗️ Transpiling Code
Use `main.py` with the Termux Python path. 🏢🐍
```bash
/data/data/com.termux/files/usr/bin/python3 main.py <file.shtemplate>
```

### Example:
```bash
/data/data/com.termux/files/usr/bin/python3 main.py tests/pass_example.shtemplate
```

## 🧪 Running the Test Suite
The `run_tests.py` script is modular. 🧩✨ It discovers all files in the `tests/` directory and checks them based on their prefix:
- `pass_*.shtemplate`: Expected to succeed. ✅
- `fail_*.shtemplate`: Expected to fail (and the test runner checks for the error message!). 🛑

### Run it like this:
```bash
/data/data/com.termux/files/usr/bin/python3 run_tests.py
```

## 🛡️ Adding a Test
Just drop a new `.shtemplate` file into the `tests/` folder!
- Name it `pass_my_test.shtemplate` if you want it to succeed.
- Name it `fail_my_test.shtemplate` if you're testing the Bouncer 🚪 and want it to block something.

Happy coding! 🚀✨
