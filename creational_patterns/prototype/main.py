import copy


class CharacterPrototype:
    def __init__(self, name, health, position):
        self.name = name
        self.health = health
        self.position = position

    def __copy__(self):
        """
        Method to create a shallow copy of the character.
        """
        new_character = self.__class__(self.name, self.health, self.position)
        return new_character

    def __deepcopy__(self, memo=None):
        """
        Method to create a deep copy of the character.
        """
        if memo is None:
            memo = {}

        # Here, if the character has complex attributes, deep copies are made.
        name_copy = copy.deepcopy(self.name, memo)
        health_copy = copy.deepcopy(self.health, memo)
        position_copy = copy.deepcopy(self.position, memo)

        new_character = self.__class__(name_copy, health_copy, position_copy)
        return new_character

    def __str__(self):
        return (
            f"Character: {self.name}, Health: {self.health}, Position: {self.position}"
        )


# Base character prototype
base_character = CharacterPrototype("Hero", 100, [0, 0])

# Create a shallow copy
shallow_copy_character = copy.copy(base_character)

# Create a deep copy
deep_copy_character = copy.deepcopy(base_character)

# Modify the copies to see how they behave
shallow_copy_character.name = "Shallow Hero"
deep_copy_character.position = [10, 10]

print("Base Character:", base_character)
print("Shallow Copy Character:", shallow_copy_character)
print("Deep Copy Character:", deep_copy_character)

# Checking if the internal object references have changed
print(f"Base Character Position: {base_character.position}")
print(f"Shallow Copy Position: {shallow_copy_character.position}")
