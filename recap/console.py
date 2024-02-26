#!/usr/bin/python3

import cmd

class helloWorld(cmd.Cmd):
    "simple command processor"
    def do_greet(self, person):
        """
        Greet [name],
        greets the named person else greet a stranger
        """
        if person:
            print(f"Hello {person}")
        else:
            print("Hello stranger")

    def do_EOF(self, line):
        "Exit the cmd prompt"
        print("")
        return True
    
if __name__ == "__main__":
    helloWorld().cmdloop()
