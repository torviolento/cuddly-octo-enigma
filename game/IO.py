import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)


class Input:
    def __init__(self):
        pass

    def input_handler(self):
        commands = {"c": lambda: print("character"),
                    "C": lambda: print("close"),
                    "d": lambda: print("drop"),
                    "e": lambda: print("eat"),
                    "f": lambda: print("fire"),
                    "g": lambda: print("get"),
                    "h": lambda: print("help"),  # huono
                    "i": lambda: print("inventory"),
                    "L": lambda: print("look around"),
                    "o": lambda: print("open"),
                    "q": lambda: print("quaff(drink)"),
                    "r": lambda: print("remove from container / unequip"),
                    "R": lambda: print("read"),
                    "S": lambda: print("sleep"),
                    "t": lambda: print("throw"),
                    "w": lambda: print("wear"),
                    "x": lambda: print("examine"),
                    "0": lambda: print("wait / defend"),
                    "5": lambda: print("select"),
                    "<": lambda: print("descend"),
                    ">": lambda: print("ascend"),
                    " ": lambda: print("interact"),
                    "*": lambda: print("change directional mode")}

        while True:
            prompt_as_int = stdscr.getch()
            print(prompt_as_int)
            prompt_as_char = chr(prompt_as_int)
            try:
                print("prompt: {:}".format(prompt_as_char))
            except:
                print("non-printable character")
            if prompt_as_int in range(49, 53) \
                    or prompt_as_int in range(54, 58):
                self.move(prompt_as_int - 48)
            elif prompt_as_char in commands:
                commands[prompt_as_char]()
            elif prompt_as_int == 27:
                break
            else:
                pass

    def move(self, key):
        print("move", key)
        pass


class Output:
    def __init__(self):
        pass
