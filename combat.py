from main import _print, menu, display_menu, player, attacks, enemies
import random
import time
import character as _character

def enemy_turn():
    for enemy in list(player['enemies'].keys()):
        enemy_object = player['enemies'][enemy]
        _print(f"\n{enemy_object.name.title()} took a turn!")
        use_attack(attacks[enemy_object.moves[random.randint(0, len(enemy_object.moves) - 1)]], enemy_object, player['character'])
        time.sleep(0.5)


def combat(encounter_enemies):
    for enemy in encounter_enemies:
        enemy_object = _character.Character(enemies[enemy][0], enemies[enemy][1], enemies[enemy][2], enemies[enemy][3], enemies[enemy][4])
        enemy_count = 1
        while enemy_object.name in list(player['enemies'].keys()):
            enemy_count += 1
            if enemy_count > 2:  # This names the enemies if there are multiple of the same type
                enemy_object.name = f"{enemy_object.name[:-2]} {str(enemy_count)}"
            else:
                enemy_object.name = f"{enemy_object.name} {str(enemy_count)}"
        player['enemies'][enemy_object.name] = enemy_object
        print(f"You encountered a {enemy.title()}!")

    fighting = True
    while fighting:
        print(f"\nHP: {player['character'].hp}/{player['character'].max_hp}")
        display_menu('combat_menu')
        if len(list(player['enemies'].keys())) <= 0:
            print("You won!")
            fighting = False
            break
        enemy_turn()
        if player['character'].hp <= 0:
            print("You lost!")
            fighting = False
            #game_over()
            break
    player['enemies'].clear()


def attack_menu():
    print("Attacks:")
    for attack in player['character'].moves:
        print(f" - {attack.title()}")
    while True:
        use_move = input("Choose a move: ").lower()
        if use_move in player['character'].moves and use_move in list(attacks.keys()):
            while True:
                #if len(list(player['enemies'].keys())) <= 1:
                    #target = player['enemies'][0]
                #else:
                for target_enemy in list(player['enemies'].keys()):
                    print(f" - {target_enemy.title()}")
                target = input("Choose a target: ").lower()
                if target in list(player['enemies'].keys()):
                    use_attack(attacks[use_move], player['character'], player['enemies'][target])
                    break
            break


def flee_battle():
    print("You cannot flee yet!")
    pass


def use_item():
    print("You cannot use items yet!")
    pass


def use_attack(attack, attacker, target):
    attack_accuracy = attack.acc * attacker.acc/100
    if random.randint(0, 100) <= attack_accuracy:
        attack_damage = attack.damage * attacker.atk
        target.hp -= attack_damage
        if target.name == player['character'].name:
            player['character'].hp = target.hp
        _print(f"{attacker.name.title()} {attack.use_text.replace('{target}', target.name.title())}")
        _print(f"Dealt {attack_damage} damage!")
        _print(f"{target.name.title()} has {target.hp} health remaining!")
        if target.hp <= 0:
            print(f"Defeated {target.name.title()}!")
            if target.name != player['character'].name:
                player['enemies'].pop(target.name)
    else:
        print(f"{attacker.name.title()} missed! What an idiot!")

menu['combat_menu'] = {"attack": attack_menu, "item": use_item, "run": flee_battle}