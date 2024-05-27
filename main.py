# pylint: disable=R0913

""" The entry point for the test suite. """


import sys
import pickle
from typing import List, Dict


class Person:
  """ A class representing a person. """

  def __init__(
      self,
      name: str,
      age: int,
      city: str,
      has_apartment: bool,
      hobbies: List[str],
      grades: Dict[str, float]
  ) -> None:
    self.name = name.capitalize()
    self.age = age
    self.city = city
    self.has_apartment = has_apartment
    self.hobbies = hobbies
    self.grades = grades

  def __str__(self) -> str:
    return f"{self.name} is {self.age} years old and lives in {self.city}"

  def __repr__(self) -> str:
    return f"Person(name={self.name}, age={self.age}, city={self.city})"

  def hello(self) -> str:
    """ Returns a greeting. """
    return f"Hello, my name is {self.name} and I live in {self.city}."


# People
alice = {
    "name": "Alice",
    "age": 24,  # Changed to int for consistency
    "city": "Karlskrona",
    "has_apartment": True,
    "hobbies": ["reading", "swimming"],
    "grades": {
        "math": 4.56,
        "english": 3.78
    }
}

bob = [
    "Bob",
    25,
    "Stockholm",
    False,
    ["running", "biking"],
    {
        "math": 3.45,
        "english": 4.78
    }
]

sarah = (
    "Sarah",
    29,
    "Göteborg",
    True,
    ["drawing", "painting"],
    {
        "math": 5.00,
        "english": 4.16
    }
)

kevin = Person(
    "Kevin",
    26,
    "Kalmar",
    False,
    ["coding", "gaming"],
    {
        "math": 4.78,
        "english": 3.45
    }
)

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


def main() -> int:
  """ Entrypoint for the main module of the test suite. """

  # Serialize the objects to a file
  with open("objects.pickle", "wb") as file:
    pickle.dump(objects, file)

  # Deserialize the objects from the file
  with open("objects.pickle", "rb") as file:
    pickled_objects = pickle.load(file)

  # Save the results
  with open("results.txt", "w", encoding="utf-8") as file:
    file.write(str(pickled_objects))

  return 0


if __name__ == "__main__":
  sys.exit(main())
