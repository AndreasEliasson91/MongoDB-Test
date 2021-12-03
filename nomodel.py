from pymongo import MongoClient

client = MongoClient('mongodb://root:s3cr37@localhost:27017')
db = client.FirstDB


def find_all_users():
    for i in db.users.find():
        print(i)


def main():
    # ADD DOCUMENT
    # person = {
    #     'name': 'Sven',
    #     'age': 67,
    #     'email': 'svensvensson@doublename.com'
    # }
    # db.users.insert_one(person)

    result = db.users.find({"age": {"$lt": 40}})
    for i in result:
        print(i)

    # find_all_users()


if __name__ == '__main__':
    main()
