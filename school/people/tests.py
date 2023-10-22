import json
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from .models import Person, Parent


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name="test", id="123456789", birthDate="2000-01-01", homeTown="test")
        Person.objects.create(name="test2", id="23456789", birthDate="2008-01-01", homeTown="test")

    def test_is_adult(self):
        older_person = Person.objects.get(id="123456789")
        younger_person = Person.objects.get(id="23456789")
        cutoff_age = datetime.now().year - 18

        self.assertTrue(older_person.birthDate.year <= cutoff_age, "Person is an adult")
        self.assertFalse(younger_person.birthDate.year <= cutoff_age, "Person is not an adult")

    def test_update_person(self):
        data = {"id": "123456789", "name": "UpdatedName", "birthDate": "2030-01-01", "homeTown": "UpdatedTown"}
        response = self.client.put("/api/updatePerson/", json.dumps(data), content_type="application/json")
        person = Person.objects.get(id="123456789")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(person.name, "UpdatedName")
        self.assertEqual(person.birthDate, datetime.strptime("2030-01-01", "%Y-%m-%d").date())
        self.assertEqual(person.homeTown, "UpdatedTown")

    def test_get_all_people(self):
        response = self.client.get("/api/getAllPeople/")
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(json_data), 2)
        self.assertEqual(len(json_data[0]), 4)

    def test_add_person(self):
        data = {"id": "999", "name": "CreatedName", "birthDate": "2023-01-01", "homeTown": "CreatedTown"}

        response = self.client.post("/api/addPerson/", json.dumps(data), content_type="json")

        test_person = Person.objects.get(id=999)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(test_person.name, "CreatedName")
        self.assertEqual(test_person.birthDate, datetime.strptime("2023-01-01", "%Y-%m-%d").date())
        self.assertEqual(test_person.homeTown, "CreatedTown")

    def test_delete_person(self):
        response = self.client.delete("/api/deletePerson/123456789")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Successfully deleted person with ID: 123456789")
        with self.assertRaises(ObjectDoesNotExist):
            Person.objects.get(id="123456789")


class ParentTestCase(TestCase):
    def setUp(self):
        child1 = Person.objects.create(name="testChild", id="9001", birthDate="2000-01-01", homeTown="testTown")
        Person.objects.create(name="testChild2", id="9002", birthDate="2000-01-01", homeTown="testTown")
        parent = Parent.objects.create(name="testParent", id="8001", birthDate="1970-01-01", homeTown="testTown",
                                       work="testWork", baseSalary=50000)
        parent.children.add(child1)

    def test_get_all_parents(self):
        response = self.client.get("/api/getAllParents/")
        self.assertEqual(response.status_code, 200)

        json_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(json_data), 1)
        self.assertEqual(len(json_data[0]), 7)

    def test_get_parent_info(self):
        response = self.client.get("/api/getParentInfo/8001")
        self.assertEqual(response.status_code, 200)

        json_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(json_data), 2)
        self.assertEqual(len(json_data["Parent"]), 7)
        self.assertEqual(len(json_data["Children"]), 1)
        self.assertEqual(len(json_data["Children"][0]), 4)
        self.assertEqual(type(json_data["Children"]), list)

    def test_get_rich_children(self):
        response = self.client.get("/api/getRichChildren/")
        self.assertEqual(response.status_code, 200)

        json_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(json_data), 1)
        self.assertEqual(len(json_data["Rich Children"]), 1)
        self.assertEqual(len(json_data["Rich Children"][0]), 4)
        self.assertEqual(type(json_data["Rich Children"]), list)

    def test_get_parents_from_child(self):
        response = self.client.get("/api/getParentsFromChild/9001")
        self.assertEqual(response.status_code, 200)

        json_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(json_data), 1)
        self.assertEqual(len(json_data["Parents"]), 1)
        self.assertEqual(len(json_data["Parents"][0]), 7)

    def test_get_children_from_parents(self):
        response = self.client.get("/api/getChildrenFromParent/8001")
        self.assertEqual(response.status_code, 200)

        json_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(json_data), 1)
        self.assertEqual(len(json_data["Children"]), 1)
        self.assertEqual(len(json_data["Children"][0]), 4)

    def test_get_grandparents(self):
        response = self.client.get("/api/getGrandParents/9001")
        self.assertEqual(response.status_code, 200)

        json_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(json_data), 1)
        self.assertEqual(len(json_data["GrandParents"]), 0)
        self.assertEqual(json_data["GrandParents"], [])

    def test_get_siblings(self):
        response = self.client.get("/api/getSiblings/9001")
        self.assertEqual(response.status_code, 200)

        json_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(json_data), 1)
        self.assertEqual(len(json_data["Siblings"]), 0)
        self.assertIsInstance(json_data["Siblings"], list)

    def test_connect_child(self):
        data = {"parent_id": "8001", "child_id": "9002"}
        response = self.client.put("/api/connectChild/", json.dumps(data), content_type="json")

        self.assertEqual(response.status_code, 201)
        parent = Parent.objects.get(id="8001")
        self.assertEqual(len(parent.children.all()), 2)
        self.assertEqual(parent.children.all()[1].id, "9002")

    def test_add_parent(self):
        data = {"id": "8002", "name": "CreatedName", "birthDate": "1970-01-01", "homeTown": "CreatedTown", "work": "CreatedWork", "baseSalary": 50000}
        response = self.client.post("/api/addParent/", json.dumps(data), content_type="json")

        self.assertEqual(response.status_code, 201)
        parent = Parent.objects.get(id="8002")
        self.assertEqual(parent.name, "CreatedName")
        self.assertEqual(parent.birthDate, datetime.strptime("1970-01-01", "%Y-%m-%d").date())
        self.assertEqual(parent.homeTown, "CreatedTown")
        self.assertEqual(parent.work, "CreatedWork")
        self.assertEqual(parent.baseSalary, 50000)

    def test_update_parent(self):
        data = {"id": "8001", "name": "UpdatedName", "birthDate": "1970-01-01", "homeTown": "UpdatedTown", "work": "UpdatedWork", "baseSalary": 50000}
        response = self.client.put("/api/updateParent/", json.dumps(data), content_type="json")

        self.assertEqual(response.status_code, 200)
        parent = Parent.objects.get(id="8001")
        self.assertEqual(parent.name, "UpdatedName")
        self.assertEqual(parent.birthDate, datetime.strptime("1970-01-01", "%Y-%m-%d").date())
        self.assertEqual(parent.homeTown, "UpdatedTown")
        self.assertEqual(parent.work, "UpdatedWork")
        self.assertEqual(parent.baseSalary, 50000)

    def test_delete_parent(self):
        response = self.client.delete("/api/deleteParent/8001")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Successfully deleted Parent with ID: 8001")
        with self.assertRaises(ObjectDoesNotExist):
            Parent.objects.get(id="8001")
