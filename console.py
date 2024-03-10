#!/usr/bin/python3
"""the starting part of my console"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF than exit the console"""
        return True

    def do_help(self, arg):
        """help to understand funtion"""
        return super().do_help(arg)

    def do_quit(self, line):
        "quit the console"
        return True
    
    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
