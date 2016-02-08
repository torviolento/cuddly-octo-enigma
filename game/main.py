#
#
#

# Import required modules
import msvcrt
import BodyParts
import Combat


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
            prompt = ord(msvcrt.getwch())
            print(prompt)
            if prompt in range(49, 53) or prompt in range(54, 58):
                self.move(prompt - 48)
            elif chr(prompt) in commands:
                commands[chr(prompt)]()
            elif prompt == 27:
                break
            else:
                pass

    def move(self, key):
        print("move", key)
        pass


class Output:
    def __init__(self):
        pass


def main():
    print("Start\n")
    input_ = Input()
    input_.input_handler()


if __name__ == '__main__':
    main()
