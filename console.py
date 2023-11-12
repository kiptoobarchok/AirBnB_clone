#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    "command line interpreter"
    prompt = '(hbnb) '

    def do_EOF(self, line):
        "Exit"
        print("")
        return True

    def do_quit(self, line):
        "exit command interpreter"
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
