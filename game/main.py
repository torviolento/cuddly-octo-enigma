#
#
#

import msvcrt


class Input:
    def __init__(self):
        pass

    def input_handler(self):
        commands = {"A": lambda: print("aa"), "B": lambda: print("bee")}
        while True:
            prompt = ord(msvcrt.getwch().upper())
            print(prompt)
            if prompt in range(49, 58):
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
    input = Input()
    input.input_handler()


main()
