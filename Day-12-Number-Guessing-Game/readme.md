keyword: scope in python

# Cara Membuat Global Scope Variabel

```
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")
```