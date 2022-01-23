from app.config import KNIGHTS
from app.players.knight import Knight


def main(knights_config: dict):
    lancelot, arthur, mordred, red_knight = (Knight.from_dict(knight) for knight in knights_config.values())
    lancelot.battle(mordred)
    arthur.battle(red_knight)
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == '__main__':
    print(main(KNIGHTS))
