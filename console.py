#!/usr/bin/python3
"""A command line interpreter"""

import cmd
from models.places import Place
from models.states import State
from models.amenities import Amenity
from models.citys import City
from models.user import User
from models.reviews import Review
from models.basemodel import BaseModel
from models.engine.filestorage import FileStorage
from models import storage

classes = {"BaseModel": BaseModel, "User": User, "Review": Review, "City": City, "Amenity": Amenity,
           "State": State, "Place": Place}
err_msg = ["** class name missing **",
           "** class doesn't exist **",
           "** instance id missing **",
           "** no instance found **",
           "** attribute name missing **",
           "** value missing **"
           "** Attribute name and value must be of same type!**"]

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter
    """
    prompt = "(hbnb) "
    intro = "Welcome Proffessor!                     Type help or ? to list commands.\n"

    def do_EOF(self, line):
        """Exit the program\n"""
        return True

    def help_EOF(self):
        print("CTRL + D (EOF) to exit the program")

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        """Doesn't execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel\n"""
        args = arg.split(' ')
        if args[0]:
            if args[0] in classes:
                new_inst = eval(args[0] + "()")
                print(new_inst.id)
                new_inst.save()
                attr = [s.replace('_',' ') if s.startswith('name=') else s for s in args]
                split_attr = [x.split('=') for x in attr]
                new_attr = [[x.strip('"') for x in new] for new in split_attr]
                attr_keys = [sublist[0] for sublist in new_attr if len(sublist) > 1]
                attr_values = [sublist[1] for sublist in new_attr if len(sublist) > 1]

                for key, val in storage.all().items():
                    obj = val

                for k, v in zip(attr_keys, attr_values):
                    obj_dict = obj.__dict__
                    obj_dict[k] = v
                    storage.save()
            else:
                print(err_msg[1])
        else:
            print(err_msg[0])

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id. 
        Ex: $ show BaseModel 1234-1234-1234.""" 
        args = arg.split(' ')
        if args[0]:
            if args[0] in classes:
                if len(args) == 2:
                    new_key = args[0] + '.' + args[1]
                    if new_key in storage.all():
                        print(storage.all()[new_key])
                    else:
                        print(err_msg[3])
                else:
                    print(err_msg[2])
            else:
                print(err_msg[1])
        else:
            print(err_msg[0])

    def do_destroy(self, arg):
        """Deletes an instance based on the
        class name and id (save the change into
        the JSON file). Ex: $ destroy BaseModel 1234-1234-1234"""
        args = arg.split(' ')
        if args[0]:
            if args[0] in classes:
                if len(args) == 2:
                    new_key = args[0] + '.' + args[1]
                    if new_key in storage.all():
                        del storage.all()[new_key]
                        storage.save()
                        print('instance destroyed!')
                    else:
                        print(err_msg[3])
                else:
                    print(err_msg[2])
            else:
                print(err_msg[1])
        else:
            print(err_msg[0])

    def do_all(self, arg):
        """Prints all string representation
        of all instances based or not on the
        class name. Ex: $ all BaseModel or $ all."""
        args = arg.split(' ')
        new_list  = []
        if len(args) == 1: 
            if args[0] in classes:
                list_item = []
                obj = storage.all()
                for key in obj:
                    if key.split('.')[0] == args[0]:
                        new_list.append(str(obj[key]))
                        print(new_list)
            
            else:
                print(err_msg[1])
        else:
            for key in obj:
                print(obj[key])

    def do_update(self, line):
        """Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file). Ex: $ update
        BaseModel 1234-1234-1234 email "aibnb@mail.com\""""
        line_list = line.split()

        if not line:
            print("** class name missing **")
        elif line_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line_list[0], line_list[1])
            if key not in storage.all().keys():
                print("** no instance found **")

            elif len(line_list) == 2:
                print("** attribute name missing **")
            elif len(line_list) == 3:
                print("** value missing **")
            else:
                attr = line_list[2]
                _type = type(line_list[3])
                value = line_list[3]
                for k, val in storage.all().items():
                    if k == key:
                        obj = val

                obj_dict = obj.__dict__
                obj_dict[attr] = _type(value)
                storage.save()
                print("Instance updated!")

    def do_count(self, line: str) -> int:
        """A function that count all instances based on a particular class"""
        arg = line.split()
        count = 0
        count_list = []
        if arg[0] in classes:
            for key in storage.all().keys():
                newKey = key.split('.')
                keyName = newKey[0]
                count_list.append(keyName)
                for v in count_list:
                    if v == arg[0]:
                        count += 1
            print(count)
        else:
            print("**Class dosen't exist**")
                
            

    def default(self, line: str):
        """A function that output a command when the prefix isn't recognized"""
        arg = line.split('.')
        if len(arg) > 1:
            if arg[0] in classes:
                comArg = arg[1].split('(')
                comd = comArg[0]
                new_arg = comArg[1]
                split_newArg = new_arg.split('"')
                split_newArg = split_newArg[1].strip("'")
                if comd == 'all':
                    HBNBCommand.do_all(self, arg[0])
                elif comd == 'create':
                    HBNBCommand.do_create(self, arg[0])
                elif comd == 'count':
                    HBNBCommand.do_count(self, arg[0])
                elif comd == 'show':
                    line = arg[0] + ' ' + split_newArg
                    HBNBCommand.do_show(self, line)
                else:
                    print("**function dosen't exist**")
            else:
                print("** class name dosen't exist**")
        else:
            print("**Needs extra arguments**")
            



                        
                    
                
            
        
        
                                
                                     





    
if __name__ == '__main__':
    HBNBCommand().cmdloop()