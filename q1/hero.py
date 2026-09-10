class Hero:
    """Represents an RPG hero with a name and health points (hp)."""

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        """Subtracts the given amount from the hero's hp."""
        self.hp -= amount


arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print(f"{arthur.name}'s HP: {arthur.hp}")
print(f"{morgana.name}'s HP: {morgana.hp}")