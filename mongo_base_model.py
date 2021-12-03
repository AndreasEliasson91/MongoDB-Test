from abc import ABC
from collections import UserDict
from pymongo import MongoClient

client = MongoClient('mongodb://root:s3cr37@localhost:27017')
db = client.DynamicModelDB


class Document(UserDict, ABC):
    collection = None


class User(Document):
    collection = db.users
