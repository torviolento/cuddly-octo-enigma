import BodyParts
import random


Slime = BodyParts.SlimeBody("Slime")
Hero = BodyParts.HumanoidBody("Hero")

def damageCheck(mobA,partD): #TODO: refine the formula for dmg, add luck as positive random factor
    dmgRoll = random.randint(1,20)
    endrRoll = random.randint(1,20)
    dmg = ((dmgRoll/10)*mobA.strength)/endrRoll
    partD.setHP(partD.hp-dmg)
    print(mobA.name+" deals "+str(dmg)+" damage!")
pass

def attackCheck(mobA,mobD): #TODO: refine the formula to take into account aiming to a certain body part or making certain body parts non-targetable
    return mobD.parts[random.randint(0,len(mobD.parts)-1)] #Chooses a random part from the list of all parts to target

pass


def fight(mobA,mobB): #Temporary proof-of-concept function
    helper = [mobA, mobB]
    attacker = helper[0]
    defender = helper[1]
    turn = 0
    while(mobA.alive and mobB.alive):
        damageCheck(attacker,attackCheck(attacker, defender))
        defender.isAlive() #quite necessary call after damagecheck
        helper[0] = defender
        helper[1] = attacker
        attacker = helper[0]
        defender = helper[1]
        pass
    if(mobA.alive):
        print(mobA.name +" won!")
    else:
        print("mobB won!")
pass

def initialAttacker(mobA,mobB):
    if(mobA.dexterity > mobB.dexterity):
        return mobA
    elif(mobA.dexterity < mobB.dexterity):
        return mobB
    else:
        helper = random.randint(0,1)
        if helper == 0:
            return mobA
        else:
            return mobB
        pass
    pass
pass

fight(Hero,Slime) #demonstrates a fight between a Humanoid and a Slime
