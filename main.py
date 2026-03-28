import sys
from lexer import tokenize
from parser import Parser
from generator import generate_bash
from checker import TypeChecker, DSLVibeError

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <file.shtemplate>")
        sys.exit(1)

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
