from collections import namedtuple
Person = namedtuple("Person", ["name", "age", "gender"])

people = [
    Person("Andy", 30, "m"),
    Person("Ping", 1, "m"),
    Person("Tina", 32, "f"),
    Person("Abby", 14, "f"),
    Person("Adah", 13, "f"),
    Person("Sebastian", 42, "m"),
    Person("Carol" , 68, "f"),
]

# first, let's show how this namedtuple works.

andy = people[0]

print("name:  ", andy.name)
print("age:   ", andy.age)
print("gender:", andy.gender)