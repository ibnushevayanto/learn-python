keyword: inheritance, penurunan class, list slicing, tuples slicing

# Slicing

```
piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(piano_keys[2:5]) # printed ['c', 'd', 'e']
print(piano_keys[:5]) # printed ['a', 'b', 'c', 'd', 'e']
print(piano_keys[2:]) # printed ['c', 'd', 'e', 'f', 'g']
print(piano_keys[2:5:2]) # printed ['c', 'e']
print(piano_keys[::2]) # printed ['a', 'c', 'e', 'g']
print(piano_keys[::-1]) # printed ['g', 'f', 'e', 'd', 'c', 'b', 'a']

```

# Cara Mengextend class di python

contoh:

```
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__() # Mendapatkan atribut dari parent
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
```
