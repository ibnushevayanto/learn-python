keyword: turtle library, prettytable library

# Cara menggunakan turtle

```
timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
```

# Cara menggunakan prettytable

Menambahkan dengan cara per-row
```
pokemon_db = PrettyTable(["Name", "Element"])
pokemon_db.add_row(["Chespin", "Grass"])
```

Menambahkan dengan cara per-column
```
pokemon_db = PrettyTable()
pokemon_db.add_column("Name", ["Chespin", "Quilladin"])
pokemon_db.add_column("Element", ["Grass", "Grass"])
```