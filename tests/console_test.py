#!/usr/bin/python3

"""
Unittests for `console.py`, covering various functionalities of the HBNBCommand class.

**Classes:**
    - `TestHBNBCommandPrompt`: Tests functionality related to user prompts and inputs.
    - `TestHBNBCommand_help`: Tests the `help` command and its output.
    - `TestHBNBCommand_exit`: Tests the `quit` command and its behavior.
    - `TestHBNBCommand_create`: Tests the `create` command for different model types.
    - `TestHBNBCommand_show`: Tests the `show` command for retrieving and displaying objects.
    - `TestHBNBCommand_all`: Tests the `all` command for retrieving all objects of a model type.
    - `TestHBNBCommand_destroy`: Tests the `destroy` command for deleting objects.
    - `TestHBNBCommand_update`: Tests the `update` command for modifying object attributes.

**Additional Resources:**
    - Models storage: [link to models.storage documentation]
    - File storage engine: [link to models.engine.file_storage documentation]
    - HBNBCommand class: [link to console.HBNBCommand documentation]
"""

import os
import sys
import unittest
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

storage = FileStorage()

class TestHBNBCommandPrompt(unittest.TestCase):
    """
    Tests user interaction through prompts and input handling in HBNBCommand.

    Methods:
        - test_prompt_and_get_input: Verifies prompts display and proper input retrieval.
        - test_validate_input: Checks input validation based on expected formats.
        - ... (add more test methods as needed)
    """
    def test_promptString(self):
        self.assertEqual("(AirBnB-clone)/> ", HBNBCommand.prompt)

    def test_emptyLine(self):
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", file.getvalue().strip())


class TestHBNBCommandHelp(unittest.TestCase):
    """Unittests that test help of the CMD intepretor."""

    def test_helpExit(self):
        var_0 = "Command to quit the program"
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help do_exit"))
            self.assertEqual(var_0, file.getvalue().strip())

    def test_helpCreate(self):
        var_0 = ("Creates a new instance of class and print its id")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help do_create"))
            self.assertEqual(var_0, file.getvalue().strip())

    def test_helpEOF(self):
        var_0 = "EOF signal => a signal to end the program"
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help do_EOF"))
            self.assertEqual(var_0, file.getvalue().strip())

    def test_helpShow(self):
        var_0 = ("Displays the string representation of a class instance, but with a unique identifier")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help do_show"))
            self.assertEqual(var_0, file.getvalue().strip())

    def test_helpDestroy(self):
        var_0 = ("Deletes a class instance of a particular id.")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help do_destroy"))
            self.assertEqual(var_0, file.getvalue().strip())

    def test_helpAll(self):
        var_0 = ("Displays the string representations of all instances of a given class")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help do_all"))
            self.assertEqual(var_0, file.getvalue().strip())

    def test_helpCount(self):
        var_0 = ("Retrieves the number of instances of a certain class")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help do_count"))
            self.assertEqual(var_0, file.getvalue().strip())

    def test_helpUpdate(self):
        var_0 = ("Updates a class instance of a particular id by adding or updating an attribute")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help do_update"))
            self.assertEqual(var_0, file.getvalue().strip())

    def test_helpCmd(self):
        var_0 = ("Display all commands: EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help help"))
            self.assertEqual(var_0, file.getvalue().strip())

class TestHBNBCommandCreate(unittest.TestCase):
    """Unittests for testing the do_create command"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_createMissingClass(self):
        correct = "*** the class name is missing ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_createInvalidClass(self):
        correct = "*** the class doesn't exist ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create My_Model"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_createInvalidSyntax(self):
        correct = "*** Unknown syntax: My_Model.do_create() ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("My_Model.do_create()"))
            self.assertEqual(correct, file_0.getvalue().strip())
        correct = "*** Unknown syntax: Base_Model.do_create()"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Base_Model.do_create()"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_createObject(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Base_Model"))
            self.assertLess(0, len(file_0.getvalue().strip()))
            test_Key = "Base_Model: {}".format(file_0.getvalue().strip())
            self.assertIn(test_Key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create User"))
            self.assertLess(0, len(file_0.getvalue().strip()))
            test_Key = "User: {}".format(file_0.getvalue().strip())
            self.assertIn(test_Key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create State"))
            self.assertLess(0, len(file_0.getvalue().strip()))
            test_Key = "State: {}".format(file_0.getvalue().strip())
            self.assertIn(test_Key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create City"))
            self.assertLess(0, len(file_0.getvalue().strip()))
            test_Key = "City: {}".format(file_0.getvalue().strip())
            self.assertIn(test_Key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Amenity"))
            self.assertLess(0, len(file_0.getvalue().strip()))
            test_Key = "Amenity: {}".format(file_0.getvalue().strip())
            self.assertIn(test_Key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Place"))
            self.assertLess(0, len(file_0.getvalue().strip()))
            test_Key = "Place: {}".format(file_0.getvalue().strip())
            self.assertIn(test_Key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Review"))
            self.assertLess(0, len(file_0.getvalue().strip()))
            test_Key = "Review: {}".format(file_0.getvalue().strip())
            self.assertIn(test_Key, storage.all().keys())

class TestHBNBCommandShow(unittest.TestCase):
    """ Unittests for testing show from test_command """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage.__test_objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_showMissingClass(self):
        correct = "** the class name is missing **"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show"))
            self.assertEqual(correct, file_0.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(".do_show()"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_showInvalidClass(self):
        correct = "*** the class doesn't exist ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show My_Model"))
            self.assertEqual(correct, file_0.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("My_Model.do_show()"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_showMissingID_space(self):
        correct = "*** the instance id missing ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show BaseModel"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show User"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show State"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show City"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show Amenity"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show Place"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show Review"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_do_showMissingId_dot(self):
        correct = "*** instance id missing ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.do_show()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("User.do_show()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("State.do_show()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("City.do_show()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Amenity.do_show()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Place.do_show()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Review.do_show()"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_do_showNoInstance_found(self):
        correct = "*** no instance found ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show BaseModel 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show User 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show State 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show City 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show Amenity 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show Place 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_show Review 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_do_showNoInstance_dot(self):
        correct = "*** no instance found ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.do_show(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("User.do_show(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("State.do_show(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("City.do_show(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Amenity.do_show(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Place.do_show(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Review.do_show(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_do_showObjects_space(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create BaseModel"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["BaseModel:{}".format(id_test)]
            test_command = "do_show BaseModel {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create User"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["User:{}".format(id_test)]
            test_command = "do_show User {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create State"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["State:{}".format(id_test)]
            test_command = "do_show State {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Place"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["Place:{}".format(id_test)]
            test_command = "do_show Place {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create City"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["City:{}".format(id_test)]
            test_command = "do_show City {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Amenity"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["Amenity:{}".format(id_test)]
            test_command = "do_show Amenity {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Review"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["Review:{}".format(id_test)]
            test_command = "do_show Review {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

    def test_do_showTestObjects_space(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create BaseModel"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["BaseModel:{}".format(id_test)]
            test_command = "BaseModel.do_show({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create User"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["User:{}".format(id_test)]
            test_command = "User.do_show({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create State"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["State:{}".format(id_test)]
            test_command = "State.do_show({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Place"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["Place:{}".format(id_test)]
            test_command = "Place.do_show({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create City"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["City:{}".format(id_test)]
            test_command = "City.do_show({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Amenity"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["Amenity:{}".format(id_test)]
            test_command = "Amenity.do_show({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Review"))
            id_test = file_0.getvalue().strip()
            
        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["Review:{}".format(id_test)]
            test_command = "Review.do_show({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(test_obj.__str__(), file_0.getvalue().strip())

class TestHBNBCommandDestroy(unittest.TestCase):
    """ Unittests for testing do_destroy """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass
        storage.reload()

    def test_destroyMissingClass(self):
        correct = "*** the class name missing ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(".do_destroy()"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_destroyInvalidClass(self):
        correct = "*** the class doesn't exist ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy My_Model"))
            self.assertEqual(correct, file_0.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("My_Model.do_destroy()"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_destroyIdMissing_space(self):
        correct = "*** instance id missing ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy BaseModel"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy User"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy State"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy City"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy Amenity"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy Place"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy Review"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_destroyIdMissing_dot(self):
        correct = "*** instance id missing ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.do_destroy()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("User.do_destroy()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("State.do_destroy()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("City.do_destroy()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Amenity.do_destroy()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Place.do_destroy()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Review.do_destroy()"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_destroyInvalidId_space(self):
        correct = "*** no instance found ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy BaseModel 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy User 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy State 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy City 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy Amenity 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy Place 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_destroy Review 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_destroyInvalidId_dot(self):
        correct = "*** no instance found ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.do_destroy(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("User.do_destroy(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("State.do_destroy(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("City.do_destroy(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Amenity.do_destroy(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Place.do_destroy(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Review.do_destroy(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_destroyObjects_space(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create BaseModel"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["BaseModel.{}".format(id_test)]
            test_cmd = "do_destroy BaseModel {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create User"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["User.{}".format(id_test)]
            test_cmd = "show User {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create State"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["State.{}".format(id_test)]
            test_cmd = "show State {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Place"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["Place.{}".format(id_test)]
            test_cmd = "show Place {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create City"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["City.{}".format(id_test)]
            test_cmd = "show City {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Amenity"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["Amenity.{}".format(id_test)]
            test_cmd = "show Amenity {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Review"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["Review.{}".format(id_test)]
            test_cmd = "show Review {}".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

    def test_destroyObjects_dot(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create BaseModel"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["BaseModel.{}".format(id_test)]
            test_cmd = "BaseModel.do_destroy({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create User"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["User.{}".format(id_test)]
            test_cmd = "User.do_destroy({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create State"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["State.{}".format(id_test)]
            test_cmd = "State.do_destroy({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Place"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["Place.{}".format(id_test)]
            test_cmd = "Place.do_destroy({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create City"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["City.{}".format(id_test)]
            test_cmd = "City.do_destroy({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Amenity"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["Amenity.{}".format(id_test)]
            test_cmd = "Amenity.do_destroy({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Review"))
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_obj = storage.all()["Review.{}".format(id_test)]
            test_cmd = "Review.do_destory({})".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertNotIn(test_obj, storage.all())

class TestHBNBCommandAll(unittest.TestCase):
    """Unittests for testing do_all """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_allInvalidClass(self):
        correct = "*** class doesn't exist ***"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_all MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.do_all()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_allObjects_space(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("do_create User"))
            self.assertFalse(HBNBCommand().onecmd("do_create State"))
            self.assertFalse(HBNBCommand().onecmd("do_create Place"))
            self.assertFalse(HBNBCommand().onecmd("do_create City"))
            self.assertFalse(HBNBCommand().onecmd("do_create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("do_create Review"))

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_allObjects_dot(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("do_create User"))
            self.assertFalse(HBNBCommand().onecmd("do_create State"))
            self.assertFalse(HBNBCommand().onecmd("do_create Place"))
            self.assertFalse(HBNBCommand().onecmd("do_create City"))
            self.assertFalse(HBNBCommand().onecmd("do_create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("do_create Review"))

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".do_all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_allSingle_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("do_create User"))
            self.assertFalse(HBNBCommand().onecmd("do_create State"))
            self.assertFalse(HBNBCommand().onecmd("do_create Place"))
            self.assertFalse(HBNBCommand().onecmd("do_create City"))
            self.assertFalse(HBNBCommand().onecmd("do_create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("do_create Review"))

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_all BaseModel"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_all User"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_all State"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_all City"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_all Amenity"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_all Place"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_all Review"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_allSingleObject_dot(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("do_create User"))
            self.assertFalse(HBNBCommand().onecmd("do_create State"))
            self.assertFalse(HBNBCommand().onecmd("do_create Place"))
            self.assertFalse(HBNBCommand().onecmd("do_create City"))
            self.assertFalse(HBNBCommand().onecmd("do_create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("do_create Review"))

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.do_all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.do_all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.do_all()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.do_all()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.do_all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.do_all()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
            
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.do_all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

class TestHBNBCommandUpdate(unittest.TestCase):
    """Unittests for testing do_update """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_updateMissing_class(self):
        correct = "*** the class name missing ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(".do_update()"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_updateInvalidClass(self):
        correct = "*** class doesn't exist ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update My_Model"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("My_Model.do_update()"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_updateMissingId_space(self):
        correct = "*** instance id missing ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update BaseModel"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update User"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update State"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update City"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update Amenity"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update Place"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update Review"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_updateMissingId_dot(self):
        correct = "*** instance id missing ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.do_update()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("User.do_update()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("State.do_update()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("City.do_update()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Amenity.do_update()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Place.do_update()"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Review.do_update()"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_updateInvalidId_space(self):
        correct = "*** no instance found ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update BaseModel 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update User 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update State 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update City 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update Amenity 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update Place 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_update Review 1"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_updateInvalidId_dot(self):
        correct = "*** no instance found ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.do_update(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("User.do_update(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("State.do_update(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("City.do_update(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Amenity.do_update(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Place.do_update(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("Review.do_update(1)"))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_updateMissingAttr_name(self):
        correct = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create BaseModel"))
            id_test = file_0.getvalue().strip()
            test_cmd = "do_update BaseModel {}".format(id_test)

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create User"))
            id_test = file_0.getvalue().strip()
            test_cmd = "do_update User {}".format(id_test)

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create State"))
            id_test = file_0.getvalue().strip()
            test_cmd = "do_update State {}".format(id_test)

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create City"))
            id_test = file_0.getvalue().strip()
            test_cmd = "do_update City {}".format(id_test)

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Amenity"))
            id_test = file_0.getvalue().strip()
            test_cmd = "do_update Amenity {}".format(id_test)

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Place"))
            id_test = file_0.getvalue().strip()
            test_cmd = "do_update Place {}".format(id_test)

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_updateMissingAttr_name(self):
        correct = "*** attribute name missing ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create BaseModel"))
            id_test = file_0.getvalue().strip()
            test_cmd = "BaseModel.do_update({})".format(id_test)

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create User"))
            id_test = file_0.getvalue().strip()
            test_cmd = "User.do_update({})".format(id_test)

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create State"))
            id_test = file_0.getvalue().strip()
            test_cmd = "State.do_update({})".format(id_test)

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create City"))
            id_test = file_0.getvalue().strip()
            test_cmd = "City.do_update({})".format(id_test)

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Amenity"))
            id_test = file_0.getvalue().strip()
            test_cmd = "Amenity.do_update({})".format(id_test)

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd("do_create Place"))
            id_test = file_0.getvalue().strip()
            test_cmd = "Place.do_update({})".format(id_test)

        with patch("sys.stdout", new=StringIO()) as file_0:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_updateMissingAttr_value(self):
        correct = "*** value missing ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create BaseModel")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "do_update BaseModel {} attribute_name".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create User")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "do_update User {} attribute_name".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create State")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "do_update State {} attribute_name".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create City")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "do_update City {} attribute_name".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Amenity")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "do_update Amenity {} attribute_name".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "do_update Place {} attribute_name".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Review")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "do_update Review {} attribute_name".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_updateMissingAttr_value_(self):
        correct = "*** value missing ***"
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create BaseModel")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "BaseModel.do_update({}, attribute_name)".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create User")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "User.do_update({}, attribute_name)".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create State")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "State.do_update({}, attribute_name)".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create City")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "City.do_update({}, attribute_name)".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Amenity")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "Amenity.do_update({}, attribute_name)".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "Place.do_update({}, attribute_name)".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Review")
            id_test = file_0.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as file_0:
            test_cmd = "Review.do_update({}, attribute_name)".format(id_test)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, file_0.getvalue().strip())

    def test_updateValidString_(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create BaseModel")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update BaseModel {} attribute_name 'attribute_value'".format(id_test)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["BaseModel:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create User")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update User {} attribute_name 'attribute_value'".format(id_test)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["User:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create State")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update State {} attribute_name 'attribute_value'".format(id_test)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["State:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create City")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update City {} attribute_name 'attribute_value'".format(id_test)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["City:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update Place {} attribute_name 'attribute_value'".format(id_test)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["Place:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Amenity")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update Amenity {} attribute_name 'attribute_value'".format(id_test)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["Amenity:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Review")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update Review {} attribute_name 'attribute_value'".format(id_test)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["Review:{}".format(id_test)].__dict__
        self.assertTrue("attribute_value", test_dictionary["attribute_name"])

    def test_updateValidString_attr_dot_(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create BaseModel")
            tId = file_0.getvalue().strip()
        test_cmd = "BaseModel.do_update({}, attribute_name, 'attribute_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["BaseModel:{}".format(tId)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create User")
            tId = file_0.getvalue().strip()
        test_cmd = "User.do_update({}, attribute_name, 'attribute_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["User:{}".format(tId)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create State")
            tId = file_0.getvalue().strip()
        test_cmd = "State.do_update({}, attribute_name, 'attribute_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["State:{}".format(tId)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create City")
            tId = file_0.getvalue().strip()
        test_cmd = "City.do_update({}, attribute_name, 'attribute_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["City:{}".format(tId)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            tId = file_0.getvalue().strip()
        test_cmd = "Place.do_update({}, attribute_name, 'attribute_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["Place:{}".format(tId)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Amenity")
            tId = file_0.getvalue().strip()
        test_cmd = "Amenity.do_update({}, attribute_name, 'attribute_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["Amenity:{}".format(tId)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Review")
            tId = file_0.getvalue().strip()
        test_cmd = "Review.do_update({}, attribute_name, 'attribute_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["Review:{}".format(tId)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

    def test_updateValidInt_attr_space(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update Place {} most_guest 99".format(id_test)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["Place:{}".format(id_test)].__dict__
        self.assertEqual(99, test_dictionary["most_guest"])

    def test_updateValidIntAttr_dot(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            tId = file_0.getvalue().strip()
        test_cmd = "Place.do_update({}, most_guest, 99)".format(tId)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["Place:{}".format(tId)].__dict__
        self.assertEqual(99, test_dictionary["most_guest"])

    def test_updateValidFloatAttr_space(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update Place {} latitude 7.2".format(id_test)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["Place:{}".format(id_test)].__dict__
        self.assertEqual(7.2, test_dictionary["latitude"])

    def test_updateValidFloatAttr_dot(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            tId = file_0.getvalue().strip()
        test_cmd = "Place.do_update({}, latitude, 7.2)".format(tId)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dictionary = storage.all()["Place:{}".format(tId)].__dict__
        self.assertEqual(7.2, test_dictionary["latitude"])

    def test_updateValidDictionary_space(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create BaseModel")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update BaseModel {} ".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'}"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["BaseModel:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create User")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update User {} ".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'}"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["User:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create State")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update State {} ".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'}"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["State:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create City")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update City {} ".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'}"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["City:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update Place {} ".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'}"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["Place:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Amenity")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update Amenity {} ".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'}"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["Amenity:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Review")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update Review {} ".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'}"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["Review:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

    def test_updateValidDictionary_dot(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create BaseModel")
            id_test = file_0.getvalue().strip()
        test_cmd = "BaseModel.do_update({}".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'})"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["BaseModel:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create User")
            id_test = file_0.getvalue().strip()
        test_cmd = "User.do_update({}, ".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'})"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["User:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create State")
            id_test = file_0.getvalue().strip()
        test_cmd = "State.do_update({}, ".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'})"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["State:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create City")
            id_test = file_0.getvalue().strip()
        test_cmd = "City.do_update({}, ".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'})"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["City:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            id_test = file_0.getvalue().strip()
        test_cmd = "Place.do_update({}, ".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'})"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["Place:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Amenity")
            id_test = file_0.getvalue().strip()
        test_cmd = "Amenity.do_update({}, ".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'})"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["Amenity:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Review")
            id_test = file_0.getvalue().strip()
        test_cmd = "Review.do_update({}, ".format(id_test)
        test_cmd += "{'attribute_name': 'attribute_value'})"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["Review:{}".format(id_test)].__dict__
        self.assertEqual("attribute_value", test_dictionary["attribute_name"])

    def test_updateValidDictionary_with_space(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update Place {} ".format(id_test)
        test_cmd += "{'most_guest': 99})"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["Place:{}".format(id_test)].__dict__
        self.assertEqual(99, test_dictionary["most_guest"])

    def test_updateValidDictionaryWithInt_dot(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            id_test = file_0.getvalue().strip()
        test_cmd = "Place.do_update({}, ".format(id_test)
        test_cmd += "{'most_guest': 99})"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["Place:{}".format(id_test)].__dict__
        self.assertEqual(99, test_dictionary["most_guest"])

    def test_updateValidDictionaryWithFloat_space(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            id_test = file_0.getvalue().strip()
        test_cmd = "do_update Place {} ".format(id_test)
        test_cmd += "{'latitude': 10.8})"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["Place:{}".format(id_test)].__dict__
        self.assertEqual (10.8, test_dictionary["latitude"])

    def test_updateValidDictionaryWithFloat_dot(self):
        with patch("sys.stdout", new=StringIO()) as file_0:
            HBNBCommand().onecmd("do_create Place")
            id_test = file_0.getvalue().strip()
        test_cmd = "Place.do_update({}, ".format(id_test)
        test_cmd += "{'latitude':  10.8})"
        HBNBCommand().onecmd(test_cmd)
        test_dictionary = storage.all()["Place:{}".format(id_test)].__dict__
        self.assertEqual (10.8, test_dictionary["latitude"])

class TestHBNBCommandCount(unittest.TestCase):
    """Unittests for testing do_count """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_countInvalidClass(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("My_Model.do_count()"))
            self.assertEqual("0", output.getvalue().strip())

    def test_countObject(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_create BaseModel"))

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.do_count()"))
            self.assertEqual("3", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_create User"))

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.do_count()"))
            self.assertEqual("3", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_create State"))

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.do_count()"))
            self.assertEqual("3", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_create Place"))

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.do_count()"))
            self.assertEqual("3", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_create City"))

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.do_count()"))
            self.assertEqual("3", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_create Amenity"))

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.do_count()"))
            self.assertEqual("3", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("do_create Review"))

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.do_count()"))
            self.assertEqual("3", output.getvalue().strip())

if __name__ == "__main__":
    unittest.main()

