import pymongo

class Base:
    __client = pymongo.MongoClient()
    __collection = 0

    def __init__(self, db_name):
        # print("Here is Base.")
        self.__client = pymongo.MongoClient()
        self.__collection = db_name
        self.set_collection()

    def set_collection(self):
        # print("Here is set collection.")
        # print(self.__collection)
        self.__collection = self.__client.yssy[self.__collection]
    
    def add_document(post):
        pass

    def update_document(post):
        pass

    def delete_document(post):
        pass

    def get_documents_by_condition(self, con = ''):
        if(con==''):
            result = self.__collection.find()
        else:
            result = "here"
        return result

    def get_document_by_condition(self, con):
        return self.__collection.find_one(con)

    def count_by_condition(self, con = ''):
        if(con==''):
            result = self.__collection.count()
        else:
            result = con
        return result

