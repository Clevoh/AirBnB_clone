#!/usr/bin/python3


import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State

new_classes = {'BaseModel': BaseModel, 'User': User, 'State': State, 'Place': Place, 'City': City, 'Amenity': Amenity}

class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """

    prompt = "(hbnb) "

    def create(self, line):
	"""Create command to create a new User"""
	splitline = line.split()
	if not splitline:
		print("** user name missing **")
	elif splitline[0] not in new_user:
		print("** class doesn't exist **")
	else:
		new_instance = new_user[splitline[0]]()
		print(new_instance.id)
		new_instance.save()

