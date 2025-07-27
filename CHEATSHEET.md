# KamalLang Cheat Sheet 🎬

## Basics
| KamalLang         | Python Equivalent | Example                          |
|-------------------|-------------------|----------------------------------|
| `KAMAL.SPEAK "..."` | `print("...")`    | `KAMAL.SPEAK "Hey Ram!"`         |
| `INTELLECT x = y` | `x = y`           | `INTELLECT age = 70`             |
| `IF x THEN y`     | `if x: y`         | `IF age > 60 THEN KAMAL.SPEAK "Legend!"` |

## Thug Life Tips 💡
- Use `+` to join texts:  
  `KAMAL.SPEAK "Age: " + str(age)`
- Math works normally:  
  `INTELLECT films = 230 + 10`

## Error Dictionary
| Error                  | Meaning                          |
|------------------------|----------------------------------|
| `KamalError: Hey Ram!` | Syntax error in your code        |
| `Unrecognized command` | Typo in keyword (e.g., `SPEAK` misspelled) |

## Quick Examples
```python
# Movie counter
INTELLECT movies = 230
IF movies > 200 THEN KAMAL.SPEAK "Ulaga Nayagan!"
```
