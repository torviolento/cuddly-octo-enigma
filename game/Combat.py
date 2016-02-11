import Creature
import random


Slime = Creature.SlimeBody("Slime")
Hero = Creature.HumanoidBody("Hero")

# TODO: refine the formula for dmg, add luck as positive random factor


def damage_check(mob_a, part_d):
    damage_roll = random.randint(1, 20)
    endurance_roll = random.randint(1, 20)
    dmg = ((damage_roll/10)*mob_a.strength)/endurance_roll
    part_d.set_hp(part_d.hp-dmg)
    print(mob_a.name+" deals "+str(dmg)+" damage!")

# TODO: refine the formula to take into account aiming to a certain body part
# TODO: or making certain body parts non-targetable


def attack_check(mob_a, mob_d):
    # Chooses a random part from the list of all parts to target
    return mob_d.parts[random.randint(0, len(mob_d.parts)-1)]


def fight(mob_a, mob_b):  # Temporary proof-of-concept function
    helper = [mob_a, mob_b]
    attacker = helper[0]
    defender = helper[1]
    while mob_a.alive and mob_b.alive:
        damage_check(attacker, attack_check(attacker, defender))
        defender.is_alive()  # quite necessary call after damagecheck
        helper[0] = defender
        helper[1] = attacker
        attacker = helper[0]
        defender = helper[1]
        pass
    if mob_a.alive:
        print(mob_a.name + " won!")
    else:
        print("mob_b won!")


def initial_attacker(mob_a, mob_b):
    if mob_a.dexterity > mob_b.dexterity:
        return mob_a
    elif mob_a.dexterity < mob_b.dexterity:
        return mob_b
    else:
        helper = random.randint(0, 1)
        if helper == 0:
            return mob_a
        else:
            return mob_b
        pass
    pass
pass

# fight(Hero, Slime)  # demonstrates a fight between a Humanoid and a Slime
