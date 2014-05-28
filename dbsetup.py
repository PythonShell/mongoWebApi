import pymongo

connection = pymongo.Connection('localhost', 27017)
db = connection['yssy']

user_table = db.user
board_table = db.board
topic_table = db.topic
article_table = db.article

