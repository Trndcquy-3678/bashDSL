# Classes and OOP Simulation

bashDSL simulates Object-Oriented Programming constructs through namespacing and prefixed generation.

## Class Definition
Use the `class` keyword to group related fields and methods.
```javascript
class Logger {
    var prefix = "[LOG]";
    
    func info(msg) {
        out prefix msg;
    }
}
```

## Method Calls
Methods are called using dot-notation.
```javascript
Logger.info("System started");
```

## Internal Transpilation
The generator converts class constructs into prefixed Bash elements:
- **Fields**: Transpiled to `ClassName_FieldName`.
- **Methods**: Transpiled to `ClassName:MethodName()` functions.

This approach allows for structured code without requiring complex Bash object frameworks.
