from pymongo import MongoClient, InsertOne
import json

client = MongoClient('mongodb://root:s3cr37@localhost:27017')
db = client.FirstDB


def main():
    in_files = []

    with open('customers.json', 'r', encoding='utf-8') as j_file:
        for obj in j_file:
            my_dict = json.loads(obj)
            in_files.append(InsertOne(my_dict))

    result = db.customers.bulk_write(in_files)
    client.close()


if __name__ == '__main__':
    main()
