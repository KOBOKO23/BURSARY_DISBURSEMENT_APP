import cmd
import re
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.bursary_application import BursaryApplication

current_classes = {'BaseModel': BaseModel, 'User': User, 'BursaryApplication': BursaryApplication}

class BUDACommand(cmd.Cmd):
    prompt = '(BUDA) '
    intro = "Welcome to the BUDA command interpreter.\n"

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of File (EOF) command to exit the program"""
        return self.do_quit(line)

    def help_quit(self):
        """Help message for the quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for the EOF command"""
        print("End of File (EOF) command to exit the program")

    def emptyline(self):
        """Override empty line behavior to do nothing"""
        pass

    def do_create(self, arg):
        """Creates a new instance."""
        args = arg.split()
        if not self.validate_classname(args):
            return

        new_obj = current_classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not self.validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        print(req_instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not self.validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return

        del instance_objs[key]
        storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances."""
        args = arg.split()
        all_objs = storage.all()

        if len(args) < 1:
            print([str(v) for v in all_objs.values()])
            return
        if args[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return
        else:
            print([str(v) for k, v in all_objs.items() if type(v).__name__ == args[0]])
            return

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split(maxsplit=3)
        if not self.validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return

        match_json = re.findall(r"{.*}", arg)
        if match_json:
            try:
                payload = json.loads(match_json[0])
            except Exception:
                print("** invalid syntax")
                return
            for k, v in payload.items():
                setattr(req_instance, k, v)
            storage.save()
            return
        if not self.validate_attrs(args):
            return
        first_attr = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        if first_attr:
            setattr(req_instance, args[2], first_attr[0])
        else:
            value_list = args[3].split()
            setattr(req_instance, args[2], self.parse_str(value_list[0]))
        storage.save()

    def validate_classname(self, args, check_id=False):
        """Runs checks on args to validate classname entry."""
        if len(args) < 1:
            print("** class name missing **")
            return False
        if args[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return False
        if len(args) < 2 and check_id:
            print("** instance id missing **")
            return False
        return True

    def validate_attrs(self, args):
        """Runs checks on args to validate classname attributes and values."""
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        return True

    def parse_str(self, arg):
        """Parse `arg` to an `int`, `float` or `string`."""
        parsed = re.sub("\"", "", arg)
        try:
            a = float(parsed)
            if a.is_integer():
                return int(a)
            return a
        except ValueError:
            return parsed

if __name__ == '__main__':
    BUDACommand().cmdloop()
