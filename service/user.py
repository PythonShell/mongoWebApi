import pymongo
from service_base import Base

class UserService (Base) :

    def __init__(self):
        # print("Here is UserService.")
        super(UserService, self).__init__("user")

    def find_by_username(self, username):
        return super(UserService, self).get_document_by_condition({"userName": username})

    def find_all_users(self):
        return super(UserService, self).get_documents_by_condition()

