from service_user import UserService
from bson import Binary, Code, BSON
from bson.json_util import dumps
from bson.json_util import loads
import json

us = UserService()
res = us.find_by_username("PythonShell")
# del res['_id']
line = dumps(res)
res2 = loads(line)
test = dumps(res2)
# print(res)
print(line)
print(type(res2['_id']))
print(test)

