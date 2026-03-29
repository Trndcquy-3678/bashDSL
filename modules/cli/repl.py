import sys
import os
import subprocess

# Ensure the project root is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from modules.core.lexer import tokenize
from modules.core.parser import Parser
from modules.engine.generator import generate_bash
from modules.engine.checker import TypeChecker, DSLVibeError

def start_repl():
    print("bashDSL Interactive REPL")
    print("Type 'exit' to quit.")
    print("-" * 30)

    checker = TypeChecker("<repl>", "")
    
    # Persistent shell process
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
            code = input("> ")
            if code.strip() == "exit":
                break
            if not code.strip():
                continue

            tokens = tokenize(code)
            parser = Parser(tokens)
            nodes = parser.parse_all()

            checker.code = code
            checker.check(nodes)

            if not hasattr(generate_bash, 'called'):
                generate_bash.called = True
            
            bash_code = generate_bash(nodes, skip_cleanup=True)
            
            shell.stdin.write(bash_code + "\n")
            shell.stdin.flush()
            
        except EOFError:
            print("\nExiting.")
            break
        except DSLVibeError as e:
            print(e)
        except Exception as e:
            print(f"Error: {e}")

    shell.terminate()

if __name__ == "__main__":
    start_repl()
