class Item(object):
    ALL = []
    glyph = ""
    slot = None

    def __init__(self):
        pass

    def on_equip(self):
        pass

    def on_unequip(self):
        pass


class Weapon(Item):
    slot = "w"


class Armor(Item):
    pass


class Potion(Item):
    def on_use(self):
        pass


class Scroll(Item):
    def on_use(self):
        pass


class Headgear(Armor):
    slot = "h"


class Torso(Armor):
    slot = "t"


class Gloves(Armor):
    slot = "g"


class Legs(Armor):
    slot = "l"


class Boots(Armor):
    slot = "b"

# WEAPONS


# ARMOR


# POTIONS


# SCROLLS
