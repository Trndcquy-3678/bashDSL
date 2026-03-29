# Output and Redirection

The `out` statement provides a structured way to handle script output and stream redirection.

## Basic Output
The simplest form of `out` prints values to the standard output.
```javascript
out "Hello World";
```

## Variable References
Variable names used in an `out` statement are automatically prefixed with `$` in the generated Bash script.
```javascript
var x = "data";
out x; // Generates: echo $x
```

## Stream Redirection
The `out` statement accepts an optional second argument to specify the output stream.
- **"stdout"**: The default stream.
- **"stderr"**: Redirects the output to the standard error stream (`>&2`).

```javascript
out "Standard message" "stdout";
out "Error message" "stderr";
```
