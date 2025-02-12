# test_classes.py

from lib.dog import Dog
from lib.person import Person

def test_dog_initialization():
    # Test with both name and breed provided
    fido = Dog("Fido", "Dalmatian")
    assert fido.name == "Fido"
    assert fido.breed == "Dalmatian"

    # Test with only name provided (breed should default to "Mutt")
    snoopy = Dog("Snoopy")
    assert snoopy.name == "Snoopy"
    assert snoopy.breed == "Mutt"

def test_person_initialization():
    # Test with name provided
    alice = Person("Alice")
    assert alice.name == "Alice"