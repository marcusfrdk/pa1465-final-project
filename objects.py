""" A module of various objects for testing. """


class Person():
  """ A class representing a person. """

  def __init__(self, name: str, age: str, city: str) -> None:
    self.name = name.capitalize()
    self.age = age
    self.city = city

  def __str__(self) -> str:
    return f"{self.name} is {self.age} years old and lives in {self.city}"

  def __repr__(self) -> str:
    return f"Person(name={self.name}, age={self.age}, city={self.city})"

  def hello(self) -> str:
    """ Returns a greeting. """
    return f"Hello, my name is {self.name}"


# People
alice = {"name": "Alice", "age": 24, "city": "Karlskrona"}
bob = ["Bob", 25, "Stockholm"]
sarah = ("Sarah", 29, "Göteborg")
kevin = Person("Kevin", 26, "Kalmar")

# Data
people = [alice, bob, sarah, kevin]
ages = {alice["age"], bob[1], sarah[1], kevin.age}
objects = {
    "dict": alice,
    "list": bob,
    "tuple": sarah,
    "object": kevin,
    "set": ages
}


if __name__ == "__main__":
  mk = max(len(k) for k in objects) + 1  # max key length
  for k, v in objects.items():
    print(f"{f'{k}:'.ljust(mk)} {repr(v)}")
