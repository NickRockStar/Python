import random


class Unit:

    def __init__(self, name: str):
        self.name = name
        self.score = 100

    def strike(self, enemy: object) -> None:
        enemy.score -= 20
        print(f"Воин {self.name} нанес удар. У врага {enemy.name} осталось {enemy.score} очков")


if __name__ == "__main__":

    units = [
        Unit("Петров"),
        Unit("Иванов"),
    ]

    while not False in [u.score > 0 for u in units]:
        move = random.randint(0, len(units) - 1)

        enemy_selection_list = units.copy()
        enemy_selection_list.pop(move)

        units[move].strike(enemy_selection_list[
                               random.randint(0, len(enemy_selection_list) - 1)
                           ])

    winners = units.copy()
    winners.remove([u for u in units if u.score <= 0][-1])

print(f"Победил воин {winners[0].name}")
