# Variables and Types

Variables in bashDSL are designed to be safer and more predictable than standard Bash variables.

## Declaration
Use the `var` keyword to declare a new variable.
```javascript
var count = 1;
var label = "items";
```

## Type Checking
The compiler tracks the type of each variable. While type inference is basic (INT vs STRING), it prevents common errors such as re-declaring a variable with a different type in the same scope.

## Duplicate Prevention
The compiler prevents duplicate variable declarations within the same scope or any parent scope. This enforces a cleaner coding style and prevents accidental variable shadowing.

## Automatic Cleanup
To maintain a clean shell environment, bashDSL automatically appends `unset` commands for every script-level variable at the end of the generated Bash script. This is especially useful when the generated script is sourced.
