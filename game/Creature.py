import Util


class Creature:
    x, y = None, None
    name = ""
    glyph = ""
    speed = 0
    max_hp = 0
    hp = 0
    max_mp = 0
    mp = 0
    regen = 0
    armor = 0
    level = 0
    endurance = 0
    strength = 0
    dexterity = 0
    wisdom = 0
    mind = 0
    charisma = 0
    luck = 0
    effects = []
    items = []
    fov_range = 0
    alive = True

    def __init__(self):
        self.parts = []

    # Checks all vital body parts in a creature.
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


class Player(Creature):
    name = "you"
    glyph = "@"

    def __init__(self):
        super(Player, self).__init__()
        self.level = 1
        self.effects = []
        self.max_hp = Util.roll(None, None, None)
        self.speed = 0
        self.hp = self.max_hp
        self.fov_range = 10
        self.armor = 0
        self.exp = 0
        self.parts = []

    def add_exp(self):
        pass

    def level_up(self):
        self.level += 1

    def drop(self, item):
        pass

    def pick_up(self, item):
        pass


class Monster(Creature):
    ALL = []

    def __init__(self):
        super(Monster, self).__init__()
        self.hp = self.max_hp

    def die(self):
        pass


class BodyPart:  # The Emperor of all body parts
    def __init__(self):
        self.hp = 1  # Initializes an object variable
        pass

    def set_hp(part, hp):
        part.hp = hp


class VitalBodyPart(BodyPart):  # The King of all body parts
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


class Head(VitalBodyPart):  # A Duke of all body parts
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

# MONSTERS


class Slime(Creature):
    endurance = 2
    strength = 2
    dexterity = 2
    luck = 2
    alive = True

    def __init__(self, name):
        super(Slime, self).__init__()
        self.head = Head()
        self.torso = Torso()
        self.parts = [self.head, self.torso]
        self.name = name
    pass


class Humanoid(Creature):
    endurance = 8
    strength = 8
    dexterity = 8
    luck = 8
    alive = True

    def __init__(self, name):
        # Order of supers has effect on self.parts:
        # Body class has parts list but it is empty
        super(Humanoid, self).__init__()
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
