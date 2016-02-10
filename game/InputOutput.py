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
                    "d": lambda: print("drop"),
                    "e": lambda: print("eat / drink"),
                    "f": lambda: print("fire"),
                    "i": lambda: print("inventory"),
                    "l": lambda: print("look around"),
                    "p": lambda: print("pick up"),
                    "r": lambda: print("remove from container / unequip"),
                    "S": lambda: print("sleep"),
                    "t": lambda: print("throw"),
                    "w": lambda: print("wear"),
                    "0": lambda: print("wait / defend"),
                    "5": lambda: print("select"),
                    " ": lambda: print("interact")}

        while True:
            prompt_as_int = stdscr.getch()
            prompt_as_char = chr(prompt_as_int).encode\
                ("cp1252", "replace").decode("cp1252", "replace")
            print("prompt: {:}".format(prompt_as_char))
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
