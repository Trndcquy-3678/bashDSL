# 🗣️ Output & Redirection

The `out` statement is smart.
```javascript
out "Success!" "stdout"; // Normal echo
out "Error!" "stderr";   // echo >&2
```
- **Variable Referencing**: `out x;` automatically becomes `echo $x`. 💸
