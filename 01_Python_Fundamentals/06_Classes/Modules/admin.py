from Modules.user import User
from Modules.privileges import Privileges
class Admin(User):
    def __init__(self,first_name, last_name, age, mobile_number,privileges):
        super().__init__(first_name, last_name, age, mobile_number)
        self.privileges=Privileges(privileges)