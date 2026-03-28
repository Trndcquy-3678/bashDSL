import sys
import os
import subprocess

# 🔧 Fix: Ensure the project root is in sys.path so we can find 'modules'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from modules.core.lexer import tokenize
from modules.core.parser import Parser
from modules.engine.generator import generate_bash
from modules.engine.checker import TypeChecker, DSLVibeError

def start_repl():
    print("💅 bashDSL Interactive REPL 🚀")
    print("Type 'exit' to yeet, or 'help' for vibes. ✌️")
    print("-" * 30)

    # State: The bouncer remembers everything 🛡️
    checker = TypeChecker("<repl>", "")
    
    # 🐚 Fix: Set stdout/stderr to None so the shell prints directly to your terminal!
    shell = subprocess.Popen(
        ['/bin/sh'],
        stdin=subprocess.PIPE,
        stdout=None,
        stderr=None,
        text=True,
        bufsize=1
    )

    while True:
        try:
            code = input("✨ > ")
            if code.strip() == "exit":
                break
            if not code.strip():
                continue

            # 1. Lex & Parse
            tokens = tokenize(code)
            parser = Parser(tokens)
            nodes = parser.parse_all()

            # 2. Type Check (Stateful!)
            checker.code = code
            checker.check(nodes)

            # 3. Generate & Execute
            # We don't want the header every time in REPL
            if not hasattr(generate_bash, 'called'):
                generate_bash.called = True
            
            bash_code = generate_bash(nodes)
            
            # Feed to persistent shell
            shell.stdin.write(bash_code + "\n")
            shell.stdin.flush()
            
        except EOFError:
            print("\nYeeted! ✌️")
            break
        except DSLVibeError as e:
            print(e)
        except Exception as e:
            print(f"⛔ Bummer! {e}")

    shell.terminate()

if __name__ == "__main__":
    start_repl()
