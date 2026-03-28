# 📖 bashDSL Wiki: The Ultimate Guide 🎭✨

Yo! Welcome to the knowledge base for **bashDSL**, the "TypeScript of Bash". 💅

## 📦 Variables & Types
Declare a variable with `var`.
```javascript
var x = 5;       // INT
var name = "Al"; // STRING
```
- **Strictness**: No duplicate declarations, even in parent scopes. 🛡️
- **Cleanup**: Global variables are automatically `unset` at the end of the script to keep the environment clean. 🧹

## 🎭 Functions & Scoping
Functions keep things clean.
```javascript
func greet(name) {
    var msg = "hi";
    out msg name;
}
```
- **Local Variables**: Variables declared with `var` inside a function are generated with the `local` keyword in Bash. 🏢🛡️

## 🏢 Classes & OOP (Mad Scientist Mode 🧪)
Simulated OOP in Bash using namespacing.
```javascript
class Human {
    var greeting = "hello";
    func sayHi(name) {
        out greeting name;
    }
}
Human.sayHi("quy");
```
- **How it works**: Transpiles to `Human_greeting` and `Human_sayHi()`. 🏛️

## 🗣️ Output & Redirection
The `out` statement is smart.
```javascript
out "Success!" "stdout"; // Normal echo
out "Error!" "stderr";   // echo >&2
```
- **Variable Referencing**: `out x;` automatically becomes `echo $x`. 💸

## 🛡️ Sniper Error Reporting 🎯🔭
If your code has "bad vibes," the transpiler will tell you **exactly** where the suspect is.
```bash
⛔ Error: undefined token 'secret' on line 5
Last call stopped at myfile.shtemplate:5:1

Stack trace:
| 4 
| 5 out secret;
        ^~~~~~
| 6 
```

## 📝 Comments
- `#` for single-line vibes.
- `/* ... */` for thick multiline vibes (converted to `#` lines in Bash). 🥥

Happy coding, marksman! 🎯🔭🚀✨
