import sys
import subprocess
from modules.core.lexer import tokenize
from modules.core.parser import Parser
from modules.engine.generator import generate_bash
from modules.engine.checker import TypeChecker, DSLVibeError

def start_repl():
    print("💅 bashDSL Interactive REPL 🚀")
    print("Type 'exit' to yeet, or 'help' for vibes. ✌️")
    print("-" * 30)

    checker = TypeChecker("<repl>", "")
    
    shell = subprocess.Popen(
        ['/bin/sh'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
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

            tokens = tokenize(code)
            parser = Parser(tokens)
            nodes = parser.parse_all()

            checker.code = code
            checker.check(nodes)

            # Important: generator.generate_bash needs to use 'modules.engine.generator'
            bash_code = generate_bash(nodes)
            
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
