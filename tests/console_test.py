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
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

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

if __name__ == "__main__":
    unittest.main()

