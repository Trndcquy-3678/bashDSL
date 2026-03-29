# Functions and Scoping

Functions in bashDSL provide isolated execution environments and clean namespacing.

## Definition
Functions are defined using the `func` keyword.
```javascript
func calculate(a, b) {
    var result = a;
    out result;
}
```

## Scoping Rules
Variables declared inside a function are local to that function. The transpiler automatically generates the `local` keyword for these variables in the output Bash script.

## Argument Handling
Function arguments are automatically mapped to local variables from the Bash positional parameters ($1, $2, etc.).

## Security
The compiler ensures that identifiers used as function calls are actually defined functions. If you need to call an external system command, you must use the `run` keyword.
```javascript
func my_helper() {
    run clear;
    out "Helper active";
}
```
