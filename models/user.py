from datetime import datetime
from models.base_model import BaseModel

class User(BaseModel):
    """A class that represents a user.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        is_admin (bool): Whether the user is an admin.
        is_active (bool): Whether the user's account is active.
        date_of_birth (datetime): The user's date of birth.
        phone_number (str): The user's phone number.
        profile_image (str): URL or path to the user's profile image.
        institution (str): The institution the user is associated with.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    is_admin = False
    is_active = True
    date_of_birth = datetime.now()
    phone_number = ""
    profile_image = ""
    institution = ""

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def check_password(self, password):
        return self.password == password

    def reset_password(self):
        pass

    def activate_user(self):
        self.is_active = True
        self.save()

    def deactivate_user(self):
        self.is_active = False
        self.save()
