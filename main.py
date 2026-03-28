import sys
from lexer import tokenize
from parser import Parser
from generator import generate_bash
from checker import TypeChecker

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <file.shtemplate>")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        code = f.read()

    try:
        tokens = tokenize(code)
        parser = Parser(tokens)
        nodes = parser.parse_all()
        
        # 🛡️ THE BOUNCER ENTERS THE CHAT
        checker = TypeChecker()
        checker.check(nodes)
        
        bash_output = generate_bash(nodes)
        print(bash_output)
    except Exception as e:
        print(f"Bummer! Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
