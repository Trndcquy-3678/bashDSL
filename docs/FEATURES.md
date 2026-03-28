# ✨ bashDSL Features: The "TypeScript of Bash" 💅

## 1. Variables (`var`) 📦
Declare a variable with `var`.
```javascript
var x = 5;       // INT
var name = "Al"; // STRING
```
- **Type Checking**: If you declare `var x = 5;` and then try `var x = "hello";`, the Bouncer 🚪 will stop you. 🛑
- **No Duplicates**: You can't declare `var x` twice in the same scope. 🛡️

## 2. Functions (`func`) 🎭
Functions create their own local scope. 🏢
```javascript
func greet(name) {
    var message = "hello";
    out message;
    out name;
}
```
- **Local Scope**: `message` is local to `greet` and won't leak into the global scope. 🛡️
- **Automatic `local`**: The generator uses `local` for these variables in Bash. ✨

## 3. Output (`out`) 🗣️
- `out "hi";` -> `echo "hi"` (Literal)
- `out x;`    -> `echo $x`  (Reference) 💸

## 4. Variable References 💸✨
The parser automatically spots the difference between a value and a variable reference. If you use a variable without quotes, bashDSL slaps a `$` sign on it during generation. 🤑
```javascript
var x = 5;
var y = x; // y = $x
```

## 5. Command Runs 🏃💨
Any name that isn't `var`, `func`, or `out` is treated as a shell command.
```javascript
ls "-la";
mkdir "new_dir";
```
You can also use function calls:
```javascript
greet(x); // greet $x
```
