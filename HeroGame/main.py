import math

from hero import Hero
from monster import Monster


def print_current_game_status(hero: Hero, monster: Monster) -> None:
    print("_" * 10)
    print("Hero and Monster stats:")
    print(f"Hero level: {hero.level}, Hero Health: {hero.hp}, Hero Damage: {hero.damage}, Hero Coins: {hero.coins}"
          f"\nMonster level: {monster.level}, Monster health: {monster.hp}, Monster Damage: {monster.damage}")

    print(f"You need a total of {Hero.level_up_threshold * (hero.level+1)} coins to level up")
    if hero.coins >= Hero.level_up_threshold * (hero.level+1):
        print("You have enough coins to level up!")
    print("_" * 10)

def handle_user_choice(user_choice: str, hero: Hero, monster: Monster):
    if user_choice == "1":
        hero.defending = True
        print("You are now defending")
    elif user_choice == "2":
        hero.attack(monster)
        print("You attacked the monster")
    elif user_choice == "3":
        hero.heal()
        print(f"Healed {math.ceil(hero.hp * Hero.heal_percent)} health")
    elif user_choice == "4":
        hero.level_up()
    hero.increase_coins(1)


def choose_action(hero_name: str):
    print(f"Its your turn {hero_name}, what would you like to do now?")
    return input("1 -> Defend\n2 -> Attack\n3 -> Heal\n4 -> Level Up\n")


def handle_monsters_turn(hero, monster):
    monster.attack(hero)
    print("The monster attacked you.")


def monster_is_dead(monster: Monster) -> bool:
    return monster.hp <= 0


def validated_user_choice(user_choice):
    if user_choice not in ["1", "2", "3", "4"]:
        return False
    return True


def start_playing(hero: Hero):
    monster = Monster("FITZ", hero.level)

    while hero.hp > 0:
        print_current_game_status(hero, monster)
        user_choice = choose_action(hero.name)
        if not validated_user_choice(user_choice):
            continue  # return to the while loop and continue
        handle_user_choice(user_choice, hero, monster)

        if monster_is_dead(monster):
            print("You killed the enemy! You gain 10 coins.")
            hero.increase_coins(10)
            monster = Monster("FITZ", hero.level)

        handle_monsters_turn(hero, monster)


def end_dialog(hero: Hero):
    print(f"You died at level {hero.level} with {hero.coins} coins left, good game!")


def main():
    hero_name = input("Enter your name hero! ")
    hero = Hero(hero_name)
    start_playing(hero)
    end_dialog(hero)


if __name__ == '__main__':
    main()
