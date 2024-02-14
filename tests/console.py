#!/usr/bin/python3
"""Defines the HBnB console for interacting with the HolbertonBnB command line application.

This module provides a command-line interface for creating, displaying, updating,
and deleting instances of various classes used in the HolbertonBnB application.

Attributes:
    storage (FileStorage): An instance of the FileStorage class for persisting data.
    __classes_0 (set): A set of available class names for the console.
"""

from shlex import split
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel 
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import cmd
import re


storage = FileStorage()
def do_parse(arg):
    """Parses a given command-line argument string.

    This function parses a command-line argument string, handling curly braces and square brackets
    for defining class names and instance IDs.

    Args:
        arg (str): The command-line argument string to parse.

    Returns:
        list: A list of parsed arguments.
    """
    curly_search = re.search(r"\{(.*?)\}", arg)
    bracket_search = re.search(r"\[(.*?)\]", arg)
    if curly_search is None:
        if bracket_search is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer_var = split(arg[:bracket_search.span()[0]])
            lexer_res = [i.strip(",") for i in lexer_var]
            lexer_res.append(bracket_search.group())
            return lexer_res
    else:
        lexer_var = split(arg[:curly_search.span()[0]])
        lexer_res = [i.strip(",") for i in lexer_var]
        lexer_res.append(curly_search.group())
        return lexer_res


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command-line interpreter.

    This class represents the command-line interpreter for the HolbertonBnB application.
    It inherits from the `cmd` module and provides various command methods for interacting
    with the application.

    Attributes:
        prompt (str): The command-line prompt string.
        __classes_0 (set): A set of available class names for the console.
    """
    prompt = "(AirBnB-clone)/> "
    __classes_0 = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_emptyline(self):
        """Does nothing upon receiving an empty line"""
        pass

    def do_default(self, arg):
        """Default behavior when input is invalid"""
        dict_args = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "track": self.do_count,
            "update": self.do_update
        }

        found = re.search(r"\.", arg)
        if found is not None:
            args_vect = [arg[:found.span()[0]], arg[found.span()[1]:]]
            found = re.search(r"\((.*?)\)", args_vect[1])
            if found is not None:
                cmd_list = [args_vect[1][:found.span()[0]], found.group()[1:-1]]
                if cmd_list[0] in dict_args.keys():
                    call = "{} {}".format(args_vect[0], cmd_list[1])
                    return dict_args[cmd_list[0]](call)
        print("*** Unknown syntax: {} ***".format(arg))
        return False

    def do_exit(self, arg):
        """Quit command to exit program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit program."""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new class instance and prints its ID.

        This method creates a new instance of the specified class and prints its ID.

        Args:
            arg (str): The command-line argument string (e.g., "create User").
        """
        args_vect = do_parse(arg)
        if len(args_vect) == 0:
            print("*** class name missing ***")
        elif args_vect[0] not in HBNBCommand.__classes_0:
            print("*** class does not exist ***")
        else:
            print(eval(args_vect[0])().id)
            storage.save()

    def do_show(self, arg):
        """Displays the string representation of a class instance.

        This method displays the string representation of a class instance of a given ID.

        Args:
            arg (str): The command-line argument string (e.g., "show User 123").
        """
        args_vect = do_parse(arg)
        obj_dict = storage.all()
        if len(args_vect) == 0:
            print("*** class name missing ***")
        elif args_vect[0] not in HBNBCommand.__classes_0:
            print("*** class does not exist ***")
        elif len(args_vect) == 1:
            print("*** instance id missing ***")
        elif "{}.{}".format(args_vect[0], args_vect[1]) not in obj_dict:
            print("*** no instance found ***")
        else:
            print(obj_dict["{}.{}".format(args_vect[0], args_vect[1])])

    def do_destroy(self, arg):
        """Deletes a class instance of a given ID.

        This method deletes a class instance of a given ID.

        Args:
            arg (str): The command-line argument string (e.g., "destroy User 123").
        """
        args_vect = do_parse(arg)
        obj_dict = storage.all()
        if len(args_vect) == 0:
            print("** class name missing **")
        elif args_vect[0] not in HBNBCommand.__classes_0:
            print("** class doesn't exist **")
        elif len(args_vect) == 1:
            print("*** instance id missing ***")
        elif "{}.{}".format(args_vect[0], args_vect[1]) not in obj_dict.keys():
            print("*** no instance found ***")
        else:
            del obj_dict["{}.{}".format(args_vect[0], args_vect[1])]
            storage.save()

    def do_all(self, arg):
        """
        Displays string representations of all instances of a given class or all instantiated objects.

        **Usage:**

        * `all`: Display all instances of all classes.
        * `all <class>`: Display all instances of a specific class.
        * `<class>.all()`: Same as `all <class>`.

        **Example:**

        * `all User`: Print string representations of all User instances.
        * `all`: Print string representations of all instantiated objects.

        **Returns:**

        * None

        **Raises:**

        * ValueError: If an invalid class name is provided.
        """

        args_vect = do_parse(arg)
        if len(args_vect) > 0 and args_vect[0] not in HBNBCommand.__classes_0:
            print("*** class doesn't exist ***")
        else:
            obj_list = []
            for obj_var in storage.all().values():
                if len(args_vect) > 0 and args_vect[0] == obj_var.__class__.__name__:
                    obj_list.append(obj_var.__str__())
                elif len(args_vect) == 0:
                    obj_list.append(obj_var.__str__())
            print(obj_list)

    def do_count(self, arg):
        """
        Retrieves the number of instances of a given class.

        **Usage:**

        * `count <class>`: Count the number of instances of a specific class.
        * `<class>.count()`: Same as `count <class>`.

        **Example:**

        * `count User`: Count the number of User instances.

        **Returns:**

        * The number of instances of the specified class.

        **Raises:**

        * ValueError: If an invalid class name is provided.
        """

        args_vect = do_parse(arg)
        track = 0
        for obj_var in storage.all().values():
            if args_vect[0] == obj_var.__class__.__name__:
                track += 1
        print(track)

    def do_update(self, arg):
        """
        Updates a class instance of a given id by adding or updating attribute(s).

        **Usage:**

        * `update <class> <id> <attribute_name> <attribute_value>`: Update a specific attribute.
        * `<class>.update(<id>, <attribute_name>, <attribute_value>)`: Same as above.
        * `<class>.update(<id>, <dictionary>)`: Update multiple attributes using a dictionary.

        **Example:**

        * `update User 1234 name "New Name"`: Update the name of the User instance with id 1234.
        * `User.update(4567, {"age": 30, "city": "Paris"})`: Update multiple attributes for the User instance with id 4567.

        **Returns:**

        * True if the update was successful, False otherwise.

        **Raises:**

        * ValueError: If an invalid class name, id, or attribute name is provided.
        * TypeError: If an invalid attribute value is provided.
        """

        args_vect = do_parse(arg)
        obj_dict = storage.all()

        if len(args_vect) == 0:
            print("*** class name missing ***")
            return False
        if args_vect[0] not in HBNBCommand.__classes_0:
            print("*** class doesn't exist ***")
            return False
        if len(args_vect) == 1:
            print("*** instance id missing ***")
            return False
        if "{}.{}".format(args_vect[0], args_vect[1]) not in obj_dict.keys():
            print("*** no instance found ***")
            return False
        if len(args_vect) == 2:
            print("*** attribute name missing ***")
            return False
        if len(args_vect) == 3:
            try:
                type(eval(args_vect[2])) != dict
            except NameError:
                print("*** value missing ***")
                return False

        if len(args_vect) == 4:
            obj_var = obj_dict["{}.{}".format(args_vect[0], args_vect[1])]
            if args_vect[2] in obj_var.__class__.__dict__.keys():
                value_type = type(obj_var.__class__.__dict__[args_vect[2]])
                obj_var.__dict__[args_vect[2]] = value_type(args_vect[3])
            else:
                obj_var.__dict__[args_vect[2]] = args_vect[3]
        elif type(eval(args_vect[2])) == dict:
            obj_var = obj_dict["{}.{}".format(args_vect[0], args_vect[1])]
            for key, value in eval(args_vect[2]).items():
                if (key in obj_var.__class__.__dict__.keys() and
                        type(obj_var.__class__.__dict__[key]) in {str, int, float}):
                    value_type = type(obj_var.__class__.__dict__[key])
                    obj_var.__dict__[key] = value_type(value)
                else:
                    obj_var.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
