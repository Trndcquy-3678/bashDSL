# Features

bashDSL provides several high-level features designed to improve the shell scripting experience.

## 1. Variables
Variables are declared using the 'var' keyword. The transpiler performs basic type checking and prevents duplicate definitions.
```javascript
var x = 10;
var message = "Hello";
```

## 2. Functions
Functions support local scoping. Variables declared inside a function are generated as 'local' variables in the resulting Bash script.
```javascript
func greet(name) {
    var prefix = "Hi ";
    out prefix name;
}
```

## 3. Classes
OOP is simulated through namespacing. Methods are accessible via dot-notation and are transpiled to prefixed Bash functions.
```javascript
class User {
    var role = "guest";
    func setRole(r) {
        role = r;
    }
}
User.setRole("admin");
```

## 4. Output and Redirection
The 'out' statement supports multiple arguments and built-in redirection to stdout or stderr.
```javascript
out "Operation successful" "stdout";
out "Error occurred" "stderr";
```

## 5. Explicit Command Execution
To prevent accidental execution of shell commands, external executables must be prefixed with the 'run' keyword.
```javascript
run ls "-la";
run mkdir "build";
```

## 6. Automatic Cleanup
Variables declared at the script level are automatically unset at the end of the generated script, preventing environment pollution.
