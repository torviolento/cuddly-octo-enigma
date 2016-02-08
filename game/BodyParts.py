class BodyPart: #The Emperor of all bodyparts
    def __init__(self):
        self.hp = 1 #Initializes an object variable
        pass
    def setHP(part, hp):
        part.hp = hp


class vitalBodyPart(BodyPart): #The King of all bodyparts
    def __init__(self):
        self.hp = 1
        self.alive = True
        super(vitalBodyPart,self).__init__() #Ask Senso wtf is going on
    pass
    def setHP(part, hp):
        part.hp = hp
        if(hp <= 0):
            part.die()
        pass
    pass
    def die(self):
        self.alive = False
    pass
    def isAlive(self):
        return self.alive
    pass




class Head(vitalBodyPart): #A Duke of all bodyparts
    def __init__(self):
        self.hp = 1
        super(Head,self).__init__()
        Head.setHP(self, 30) #Calls BodyPart's setHP and sets Head's HP to be 30
    pass


class Torso(vitalBodyPart):
    def __init__(self):
        self.hp = 1
        super(Torso, self).__init__()
        Torso.setHP(self, 100)
    pass

class Limb(BodyPart):
    def __init__(self):
        self.hp = 1
        super(Limb, self).__init__()
        Limb.setHP(self, 40)
    pass


class Body():
    def __init__(self):
        self.parts = []
        self.name = ""
        pass
    def isAlive(self): #Checks all vital bodyparts in a creature. If one of them is dead, body dies
        for part in self.parts:
            if isinstance(part, vitalBodyPart): #Checks if a part is a vital body part and if so moves into the next block
                if part.isAlive() == False :
                    self.alive = False
                pass
            pass
        pass
    pass



class SlimeBody(Body):
    endurance = 2
    strength = 2
    dexterity = 2
    luck = 2
    alive = True
    def __init__(self, name):
        super(SlimeBody, self).__init__()
        self.head = Head()
        self.torso = Torso()
        self.parts = [self.head, self.torso]
        self.name = name
    pass

class HumanoidBody(Body):
    endurance = 8
    strength = 8
    dexterity = 8
    luck = 8
    alive = True
    def __init__(self, name):
        super(HumanoidBody, self).__init__() #Order of supers has effect on self.parts: Body class has parts list but it is empty
        self.head = Head()
        self.torso = Torso()
        self.rArm = Limb()
        self.lArm = Limb()
        self.rLeg = Limb()
        self.lLeg = Limb()
        self.parts = [self.head, self.torso, self.rArm, self.lArm, self.rLeg, self.lLeg]
        self.name = name
    pass



#x = SlimeBody()
#x.head.setHP(0)
#x.isAlive()
#print(x.alive)
#print(x.head.alive)



