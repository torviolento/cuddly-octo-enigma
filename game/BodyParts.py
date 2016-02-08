class BodyPart:  # The Emperor of all bodyparts
    def __init__(self):
        self.hp = 1  # Initializes an object variable
        pass

    def set_hp(part, hp):
        part.hp = hp


class VitalBodyPart(BodyPart):  # The King of all bodyparts
    def __init__(self):
        self.hp = 1
        self.alive = True
        super(VitalBodyPart, self).__init__()  # Ask Senso wtf is going on
    pass

    def set_hp(part, hp):
        part.hp = hp
        if hp <= 0:
            part.die()
        pass
    pass

    def die(self):
        self.alive = False
    pass

    def is_alive(self):
        return self.alive
    pass


class Head(VitalBodyPart):  # A Duke of all bodyparts
    def __init__(self):
        self.hp = 1
        super(Head, self).__init__()
        # Calls BodyPart's set_hp and sets Head's HP to be 30
        Head.set_hp(self, 30)
    pass


class Torso(VitalBodyPart):
    def __init__(self):
        self.hp = 1
        super(Torso, self).__init__()
        Torso.set_hp(self, 100)
    pass


class Limb(BodyPart):
    def __init__(self):
        self.hp = 1
        super(Limb, self).__init__()
        Limb.set_hp(self, 40)
    pass


class Body:
    def __init__(self):
        self.parts = []
        self.name = ""
        pass

    # Checks all vital bodyparts in a creature.
    # If one of them is dead, body dies
    def is_alive(self):
        for part in self.parts:
            # Checks if a part is a vital body part and if so moves into the
            # next block
            if isinstance(part, VitalBodyPart):
                if not part.is_alive():
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
        # Order of supers has effect on self.parts:
        # Body class has parts list but it is empty
        super(HumanoidBody, self).__init__()
        self.head = Head()
        self.torso = Torso()
        self.rArm = Limb()
        self.lArm = Limb()
        self.rLeg = Limb()
        self.lLeg = Limb()
        self.parts = [self.head, self.torso, self.rArm, self.lArm,
                      self.rLeg, self.lLeg]
        self.name = name
    pass


# x = SlimeBody()
# x.head.set_hp(0)
# x.isAlive()
# print(x.alive)
# print(x.head.alive)
