from mongoengine import connect, Document, StringField, IntField

connect('FirstDB', username='root', password='s3cr37', authentication_source='admin')


class User(Document):
    name = StringField(required=True)
    age = IntField()
    email = StringField(max_length=50)

    meta = {
        'collection': 'users'
    }

    def __init__(self, name, age, email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.age = age
        self.email = email


def main():
    for user in User.objects:
        print(user.name)
    # user = User('Tony', 47, 'iamironman@avengers.com')
    # user.save()


if __name__ == '__main__':
    main()
