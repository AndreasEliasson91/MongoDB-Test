from abc import ABC
from collections import UserDict
from pymongo import MongoClient

client = MongoClient('mongodb://root:s3cr37@localhost:27017')
db = client.DynamicModelDB


class ResultList(list):
    def first_or_none(self):
        return self[0] if len(self) > 0 else None

    def last_or_none(self):
        return self[-1] if len(self) > 0 else None


class Document(dict, ABC):
    collection = None

    def __init__(self, **data):
        super().__init__()

        if '_id' not in data:
            self._id = None
        self.__dict__.update(data)

    def __repr__(self):
        return '\n'.join(f'{key}: {value}' for key, value in self.__dict__.items())

    def save(self):
        if not self._id:
            del self.__dict__['_id']
            self.collection.insert_one(self.__dict__)
        else:
            self.collection.replace_one({'_id': self._id}, self.__dict__)

    @classmethod
    def all(cls):
        return [cls(**item) for item in cls.collection.find()]

    @classmethod
    def find(cls, **kwargs):
        return ResultList(cls(**item) for item in cls.collection.find(kwargs))


class User(Document):
    collection = db.users


class Post(Document):
    collection = db.posts


post = Post(title='Endgame', body='Love You 3000!', likes=3000)
post.save()

for post in Post.all():
    print(post.title)


# user = User(name='Natascha', age=36)
# user.save()
# user.age = 151
# user.save()
# print(user)

# users = User.all()
# for user in users:
#     print(user)

user = User.find(name='Tony').first_or_none()
print(user)
