#!/usr/bin/python3
try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    pass
import cmd 

class My_interactive(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_greet(self, line):
        print("hello guys")
    
    def do_EOF(self, line):
        return True
    
    def do_eat(self , food):
        if food:
            print("hi a eat "+ food)
        else:
            print("Oh it looks delisious , What do you eat ?")
    
    def do_run(self, person):
        if person:
            print("Run {:s}".format(person))
        else:
            print("Run forest , Run !!")
            
    def help_eat(self):
        print('\n'.join(['type [food]', 'ask of type of food']))
        
    def help_run(self):
        print('\n'.join(['run [forest]', 'run a named person']))
    
if __name__ == "__main__":
    My_interactive().cmdloop()