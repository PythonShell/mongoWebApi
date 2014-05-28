import dbsetup, datetime

dbsetup.user_table.drop()

PythonShell = {
    "userName": "PythonShell",
    "nickName": "提问机",
    "lastOnline": datetime.datetime(2014, 5, 19, 13, 29, 14),
    "lastIP": "211.99.222.55",
    "life": 364,
    "sex": True, # True for male, False for female
    "totalArticles": 232,
    "totalLogin": 531,
    "privateInfo": {
        "realName": "陈凯祥",
        "address": "上海市东川路800号D18-216",
        "birthday": datetime.datetime(1992, 10, 15),
        "mail": "deatheart@yeah.net",
        "valid": True, # True if user passed the authentication, False if not.
        "registDate": datetime.datetime(2011, 7, 13, 10, 43, 45),
    }
}
Deatheart = {
    "userName": "Deatheart",
    "nickName": "...",
}
dbsetup.user_table.insert(PythonShell)
dbsetup.user_table.insert(Deatheart)

