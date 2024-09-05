#!/usr/bin/python3
"""Module console

This Module contains a definition for BUDACommand Class
"""

import cmd
import importlib
from typing import cast
from models import storage

class BUDACommand(cmd.Cmd):
    """Bursary app console"""

    prompt = "(BUDA) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the console using Ctrl + D"""
        print()
        return True

    def emptyline(self):
        """Prevents default behavior of cmd to ignore running command on empty line plus enter"""
        pass

    def do_create(self, line):
        """Creates a new object and saves it"""
        obj_cls = self.get_class_from_input(line)
        if obj_cls is not None:
            try:
                kwargs = self.parse_arguments(line)
                new_obj = obj_cls(**kwargs)
                new_obj.save()
                print(new_obj.id)
            except Exception as e:
                print(f"** error: {e}")

    def do_show(self, line):
        """Prints the string representation of an instance based on class name and id"""
        key = self.get_obj_key_from_input(line)
        if key is None:
            return

        saved_obj = storage.all().get(key, None)
        if saved_obj is None:
            print("** no instance found **")
        else:
            print(saved_obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id and saves the change into the storage file"""
        key = self.get_obj_key_from_input(line)
        if key is None:
            return

        saved_obj = storage.all().pop(key, None)
        if saved_obj is None:
            print("** no instance found **")
        else:
            storage.save()

    def do_all(self, line):
        """Prints all string representations of all instances, or filtered by class name."""
        if not line.strip():
            result = storage.all().values()
        else:
            obj_cls = self.get_class_from_input(line)
            if obj_cls is None:
                return
            result = [item for item in storage.all().values() if isinstance(item, obj_cls)]

        print([str(item) for item in result])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute and saves the change into the storage file"""
        key = self.get_obj_key_from_input(line)
        if key is None:
            return

        saved_obj = storage.all().get(key, None)
        if saved_obj is None:
            print("** no instance found **")
        else:
            attr_name, attr_val = self.get_attribute_name_value_pair(line)
            if attr_name is None or attr_val is None:
                return

            if hasattr(saved_obj, attr_name):
                attr_type = type(getattr(saved_obj, attr_name))
                attr_val = cast(attr_type, attr_val)
            setattr(saved_obj, attr_name, attr_val)
            saved_obj.save()

    def do_count(self, line):
        """Prints the count of all instances based on the class name"""
        obj_cls = self.get_class_from_input(line)
        if obj_cls is None:
            return
        result = [item for item in storage.all().values() if isinstance(item, obj_cls)]

        print(len(result))

    def parse_arguments(self, line):
        """Parses the arguments from the command line"""
        args = line.split()[1:]
        parsed_args = {}
        for arg in args:
            if "=" in arg:
                key, value = arg.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"')
                if value.lower() in ['true', 'false']:
                    value = value.lower() == 'true'
                elif value.replace('.', '', 1).isdigit():
                    value = float(value) if '.' in value else int(value)
                parsed_args[key] = value
        return parsed_args

    def get_obj_key_from_input(self, line):
        """Parses and returns object key from input"""
        obj_cls = self.get_class_from_input(line)
        if obj_cls is None:
            return None
        id = self.get_id_from_input(line)
        if id is None:
            return None
        return f"{obj_cls.__name__}.{id}"

    def get_class_from_input(self, line):
        """Parses and returns class from input"""
        if line is None or len(line.strip()) == 0:
            print("** class name missing **")
            return None

        return self.get_class(line.split()[0])

    def get_id_from_input(self, line):
        """Parses and returns id from input"""
        cmds = line.split()
        if len(cmds) < 2:
            print("** instance id missing **")
            return None
        return cmds[1]

    def get_attribute_name_value_pair(self, line):
        """Parses and returns a tuple of attribute name and value"""
        cmds = line.split()
        if len(cmds) < 4:
            print("** attribute name or value missing **")
            return None, None

        attr_name = cmds[2].strip().strip('"')
        attr_val = cmds[3].strip().strip('"')
        
        return attr_name, attr_val

    def get_class(self, class_name):
        """Dynamically imports and returns a class based on its name"""
        try:
            module_name = f"models.{class_name.lower()}"
            module = importlib.import_module(module_name)
            return getattr(module, class_name)
        except (ImportError, AttributeError) as e:
            print(f"** error: {e}")
            return None

if __name__ == '__main__':
    BUDACommand().cmdloop()
