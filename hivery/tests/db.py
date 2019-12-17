from unittest import TestCase
import unittest
from hivery.models import CompanySerializer, PersonSerializer, companies, people
from hivery.app import app


class RestTest(TestCase):

    def test_data_can_be_serialized(self):
        serializer = CompanySerializer(companies[0]).data
        serializer_list = CompanySerializer(companies[:5], many=True).data

        self.assertIsNotNone(serializer)
        self.assertIsNotNone(serializer_list)

        serializer2 = PersonSerializer(people[0]).data
        serializer_list2 = PersonSerializer(people[:5], many=True).data

        self.assertIsNotNone(serializer2)
        self.assertIsNotNone(serializer_list2)

    def test_route_1(self):
        # test the first route
        with app.test_client() as c:
            rv = c.get('/0', json={
                'username': 'flask', 'password': 'secret'
            })
            json_data = rv.get_json()
            assert not json_data

            rv = c.get('/1', json={
                'username': 'flask', 'password': 'secret'
            })
            json_data = rv.get_json()
            assert json_data

    def test_route_2(self):
        return True

    def test_route_3(self):
        return True


if __name__ == '__main__':
    unittest.main()
