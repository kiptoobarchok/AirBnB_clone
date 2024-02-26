#!/usr/bin/python3
"""
Custom command line interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Contains entry point of command interpreter
    """
    def do_EOF(self, line):
        "Exit the command line interpreter"
        print("")
        return True
    
    def do_quit(self, line):
        "Quit command to exit the program"
        return True
    
    def do_create(self, line):
        "create new instance of BaseModel"


if __name__ == "__main__":
    HBNBCommand().cmdloop()
