keyword: custom class, class in python

# Cara Membuat Class

```
class User:
    pass


user_1 = User()
user_1.id = "01"
user_1.username = "ibnushevayanto"

print(user_1.username) # Output "ibnushevayanto"
```

# Constructor pada class

```
# Jika ingin mengakses attribute / method dalam class gunakan "self", "self" selalu berada pada parameter pertama dari method yang ada dalam class
class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0


user_1 = User("01", "ibnushevayanto")
print(user_1.username)  # Output "ibnushevayanto"
```