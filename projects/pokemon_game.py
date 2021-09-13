# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`


class Pokemon:
    # - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
    def __init__(self, name, primary_type, attack_dmg, max_hp, hp) -> None:
        self.name = name
        self.primary_type = primary_type
        self.attack_dmg = attack_dmg
        self.max_hp = max_hp
        self.hp = hp
    
    def __str__(self):
        return f'{self.name} is a {self.primary_type} type, with {self.max_hp} HP. It\'s current HP is {self.hp}.'

    # - Implement a `battle()` method based on rock-paper-scissors that
    #   decides who wins based only on the `primary_type`:
    def battle(self, other):
        if self.primary_type == 'grass' and other.primary_type == 'water':
            other.hp -= self.attack_dmg
            # - Display messages that explain who won or lost a battle
            # - If a Pokemon loses a battle, they lose some of their `hp`
            print(f'{self.name} won the battle, and {other.name} took {self.attack_dmg} damage, leaving {other.name} with {other.hp} HP left.')
            if other.hp <= 0:
                print(f'{other.name} has fainted! Go feed your Pokemon.')
        elif self.primary_type == 'fire' and other.primary_type == 'grass':
            other.hp -= self.attack_dmg
            print(f'{self.name} won the battle, and {other.name} took {self.attack_dmg} damage, leaving {other.name} with {other.hp} HP left.')
            if other.hp <= 0:
                print(f'{other.name} has fainted! Go feed your Pokemon.')
        elif self.primary_type == 'water' and other.primary_type == 'fire':
            other.hp -= self.attack_dmg
            print(f'{self.name} won the battle, and {other.name} took {self.attack_dmg} damage, leaving {other.name} with {other.hp} HP left.')
            if other.hp <= 0:
                print(f'{other.name} has fainted! Go feed your Pokemon.')
        elif self.primary_type == 'fire' and other.primary_type == 'water':
            self.hp -= other.attack_dmg
            print(f'{other.name} won the battle, and {self.name} took {other.attack_dmg} damage, leaving {self.name} with {self.hp} HP left.')
            if self.hp <= 0:
                print(f'{self.name} has fainted! Go feed your Pokemon.')
        elif self.primary_type == 'water' and other.primary_type == 'grass':
            self.hp -= other.attack_dmg
            print(f'{other.name} won the battle, and {self.name} took {other.attack_dmg} damage, leaving {self.name} with {self.hp} HP left.')
            if self.hp <= 0:
                print(f'{self.name} has fainted! Go feed your Pokemon.')
        elif self.primary_type == 'grass' and other.primary_type == 'fire':
            self.hp -= other.attack_dmg
            print(f'{other.name} won the battle, and {self.name} took {other.attack_dmg} damage, leaving {self.name} with {self.hp} HP left.')
            if self.hp <= 0:
                print(f'{self.name} has fainted! Go feed your Pokemon.')


    # If you call the `feed()` method on a Pokemon, they regain some `hp`
    def feed(self):
        self.hp = self.max_hp
        print(f'{self.name}\'s HP restored to {self.hp}')

bulbasaur = Pokemon('Bulbasaur', 'grass', 20, 60, 60)
ivysaur = Pokemon('Ivysaur', 'grass', 40, 90, 90)
venusaur = Pokemon('Venusaur', 'grass', 60, 160, 160)
charmander = Pokemon('Charmander', 'fire', 20, 60, 60)
charmeleon = Pokemon('Charmeleon', 'fire', 40, 90, 90)
charizard = Pokemon('Charizard', 'fire', 60, 160, 160)
squirtle = Pokemon('Squirtle', 'water', 20, 60, 60)
wartortle = Pokemon('Wartortle', 'water', 40, 90, 90)
blastoise = Pokemon('Blastoise', 'water', 60, 160, 160)

charizard.battle(squirtle)
bulbasaur.battle(charizard)
bulbasaur.feed()
print(charmeleon)