keyword: read file, close file, buka file, tutup file, menulis file, write file

# Contoh 1, code membuka dan membaca file

```
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close() # Saat membuka file jangan lupa untuk menutup file
```

# Contoh 2, code untuk membuka dan membaca file
```
with open("my_file.txt") as file:
    contents = file.read()
    print(contents) # Keuntungan menggunakan kode seperti ini tidak perlu menutup file
```

# Contoh, code untuk menulis file
```
with open("new_file.txt", mode="w") as file:
    file.write("New text.")
```