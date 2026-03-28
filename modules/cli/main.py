import sys
import os

# 🔧 Fix: Ensure the project root is in sys.path so we can find 'modules'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from modules.core.lexer import tokenize
from modules.core.parser import Parser
from modules.engine.generator import generate_bash
from modules.engine.checker import TypeChecker, DSLVibeError

def main():
    if len(sys.argv) < 2:
        # 🚀 No file provided? Launch the REPL! ✨
        from modules.cli.repl import start_repl
        start_repl()
        return

    file_path = sys.argv[1]
    with open(file_path, 'r') as f:
        code = f.read()

    try:
        tokens = tokenize(code)
        parser = Parser(tokens)
        nodes = parser.parse_all()
        
        # 🛡️ THE BOUNCER ENTERS THE CHAT (With elite error training!)
        checker = TypeChecker(file_path, code)
        checker.check(nodes)
        
        bash_output = generate_bash(nodes)
        print(bash_output)
    except DSLVibeError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"Bummer! Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
