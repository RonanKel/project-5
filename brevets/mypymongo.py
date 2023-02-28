import os
from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb


def brevet_insert(start_time, brevet_dist, checkpoints):
    races = db["races"]
    races.insert_one({"begin_date": start_time, "distance": brevet_dist, "checkpoints": checkpoints})
    pass


def brevet_find():
    # return start_time, brevet_dist, checkpoints
    result = db["races"].find()
    for data in result:
        returnval = data

    returnval.pop("_id")

    return returnval
