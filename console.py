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
	elif splitline[0] not in new_classes:
		print("** class doesn't exist **")
	else:
		new_instance = new_classes[splitline[0]]()
		print(new_instance.id)
		new_instance.save()

    def show(self, line):
	"""Show command to show an instance based on User name and id"""
	if not line:
		print("** class name missing **")

	elif line.split()[0] not in new_classes:
		print("** class doesn't exist **")

	elif len(line.split()) < 2:
		print("** instance id missing **")

	else:
		class_name = line.split()[0]
		instance_id = line.split()[1]
		new_instance =  "{}.{}".format(class_name, instance_id)
		objs = models.storage.all()

	if new_instance not in objs:
		print("** no instance found **")
	else:
		print(objs[new_instance])

    def destroy(self, line):
	"""Delete command to delete an instance based on class name and id"""
    	splitline = line.split()

    	if not splitline:
        	print("** class name missing **")
        	return False

    	elif splitline[0] not in new_classes:
        	print("** class doesn't exist **")

    	elif len(splitline) < 2:
        	print("** instance id missing **")

    	else:
        	class_name = splitline[0]
       		instance_id = splitline[1]
        	new_instance = "{}.{}".format(class_name, instance_id)
        	all_objects = models.storage.all()

        if new_instance not in all_objects:
            	print("** no instance found **")
        else:
            	del all_objects[new_instance]
            	models.storage.save()

    def all(self, line):
    	"""All command to print all instances based or not on class name"""
    	str_list = []
    	all_objects = models.storage.all()

    	if not line:
        	for new_instance in all_objects.values():
            	str_list.append(str(new_instance))
    	else:
        	splitline = line.split()
        	if splitline[0] in new_classes:
            		for key, value in all_objects.items():
                	if value.__class__.__name__ == splitline[0]:
                    		str_list.append(str(value))
        	else:
            		print("** class doesn't exist **")
            		return False
    	print(str_list)

    def update(self, line):
        """Update command to update an instance base on class name and id"""
        splitline = split(line)

        if not splitline:
        	print("** class name missing **")

        elif splitline[0] not in new_classes:
            	print("** class doesn't exist **")

        elif len(splitline) < 2:
            	print("** instance id missing **")

        elif len(splitline) < 3:
            	print("** attribute name missing **")

        elif len(splitline) < 4:
            	print("** value missing **")

        else:
            	new_instance = splitline[0] + '.' + splitline[1]
            	if new_instance not in models.storage.all():
                	print("** no instance found **")
            	else:
                	setattr(models.storage.all()[new_instance],
                        	splitline[2], splitline[3])
                	models.storage.save()





if __name__ == '__main__':
    HBNBCommand().cmdloop()
