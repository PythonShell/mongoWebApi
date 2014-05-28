import pymongo
from service_base import Base

class BoardService (Base) :

    def __init__(self):
        # print("Here is UserService.")
        super(BoardService, self).__init__("board")

    def find_by_boardname(self, boardname):
        return super(BoardService, self).get_document_by_condition({"boardName": boardname})

    def find_all_boards(self):
        return super(BoardService, self).get_documents_by_condition()

