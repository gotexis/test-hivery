import json
import os

from rest_framework.fields import CharField, IntegerField, BooleanField, ListField
from rest_framework.serializers import Serializer

companies_file = os.environ.get("HIVERY_COMPANIES_JSON",
                                os.path.join(os.path.dirname(__file__), './resources/companies.json'))
people_file = os.environ.get("HIVERY_PEOPLE_JSON", os.path.join(os.path.dirname(__file__), './resources/people.json'))

with open(companies_file, 'r') as f:
    companies = json.loads(f.read())

with open(people_file, 'r') as f:
    people = json.loads(f.read())


def get_person(criteria, field='_id'):
    return next((c for c in people if criteria == c[field]), None)


class CompanySerializer(Serializer):
    index = CharField()
    company = CharField()


class PersonSerializer(Serializer):
    _id = CharField()
    index = IntegerField()
    guid = CharField()
    has_died = BooleanField()
    balance = CharField()
    picture = CharField()
    age = IntegerField()
    eyeColor = CharField()
    name = CharField()
    gender = CharField()
    company_id = IntegerField()
    email = CharField()
    phone = CharField()
    address = CharField()
    about = CharField()
    registered = CharField()
    tags = ListField()
    friends = ListField()


class MiniUserSerializer(Serializer):
    name = CharField()
    email = CharField()
    phone = CharField()
    address = CharField()


class CommonFriendSerializer(Serializer):
    person_1 = MiniUserSerializer()
    person_2 = MiniUserSerializer()
    friends = ListField()


fruits = ('strawberry', 'apple', 'orange', 'banana')
vegetables = ('carrot', 'cucumber', 'celery', 'beetroot')


class FruitField(ListField):
    def to_representation(self, data):
        t = super().to_representation(data)
        return [i for i in t if i in fruits]


class VegetableField(ListField):
    def to_representation(self, data):
        t = super().to_representation(data)
        return [i for i in t if i in vegetables]


class FoodSerializer(Serializer):
    name = CharField()
    age = CharField()
    fruits = FruitField(source='favouriteFood')
    vegetables = VegetableField(source='favouriteFood')
