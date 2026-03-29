# Error Reporting

bashDSL features a precise error reporting system designed to speed up debugging.

## Visual Pointers
When a compiler error occurs (such as a type mismatch or undefined token), the system provides a visual caret pointing to the exact location of the error in the source code.

```bash
Error: undefined token 'secret' on line 5
Location: example.shtm:5:1

Context:
| 4 
| 5 out secret;
        ^~~~~~
| 6 
```

## Detailed Metadata
Every error report includes:
- A descriptive error message.
- The file path, line number, and column number.
- A code snippet showing the surrounding lines for context.

## Common Errors
- **Undefined Token**: Attempting to use a variable or function that has not been declared.
- **Duplicate Definition**: Attempting to declare a variable or function name that already exists in the current or a parent scope.
- **Syntax Error**: Using language constructs that do not follow the bashDSL grammar.
