import Util


class Map:
    def __init__(self):
        # self.mobs = []
        pass

    def populate(self):
        n_monsters = 0
        n_items = 0
        for i in range(n_monsters):
            # make and insert monsters on map
            pass
        for i in range(n_items):
            # make and insert items on map
            pass


class Tile:
    # The type of tile (e.g. wall, grass, floor, river)

    # Any other data (e.g. a trap, a hole in the floor, stairs)

    # What other data is needed? I would use another byte to determine any
    # special dungeon features the tile carries, such as traps, stairs,
    # glyphs, chests and so on. Store all of these in an array, and substitute
    # this value into the array to find what, if anything, is at the tile.
    # Alternatively you could just store these things in the tile's linked
    # list too.

    # If your system uses 11 bytes, then to make a dungeon that is 100 by 100
    # tiles, you would need 100*100*11 ~= 100K of memory. This increase is
    # quadratic as width and height increase, so be careful that you don't run
    # out of memory. If you need to squeeze your tile size further, and you're
    # using a programming language that supports them, consider using bit
    # fields. They let you use less than 1 byte of memory for a variable.

    def __init__(self):
        self.explored = False
        self.passable = False
        self.transparent = False
        self.illuminated = False
        self.glyph = ""
        self.items = []
        self.creature = []
        pass

    '''def visible_glyph(self):
        if self.creature:
            # return self.creature.glyph
        elif self.items:
            return self.items.glyph
        else:
            return self.glyph
    '''
    def on_enter(self):
        pass


class WallTile(Tile):
    Tile.passable = False
    Tile.transparent = False
    Tile.glyph = "#"


class FloorTile(Tile):
    Tile.passable = True
    Tile.transparent = True
    Tile.glyph = "."
    pass


class StairsUpTile(Tile):
    Tile.passable = True
    Tile.transparent = True
    Tile.glyph = ">"
    pass


class StairsDownTile(Tile):
    Tile.passable = True
    Tile.transparent = True
    Tile.glyph = "<"
    pass


class DoorTile(Tile):
    Tile.passable = False
    Tile.transparent = False
    Tile.glyph = "+"
    closed = True

    def open(self):
        self.closed = False
        Tile.passable = True
        Tile.transparent = True
        Tile.glyph = "/"

    def close(self):
        self.closed = True
        Tile.passable = False
        Tile.transparent = False
        Tile.glyph = "+"


class WaterTile(Tile):
    Tile.passable = False
    Tile.transparent = True
    Tile.glyph = "~"


class TreeTile(Tile):
    Tile.passable = True
    Tile.Transparent = True
    Tile.glyph = "f"
