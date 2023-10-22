import json
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from .models import Person, Parent


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name="test", id="123456789", birthDate="2000-01-01", homeTown="test")
        Person.objects.create(name="test2", id="23456789", birthDate="2008-01-01", homeTown="test")

    def doCleanups(self) -> None:
        try:
            Person.objects.get(id="123456789").delete()
        except ObjectDoesNotExist:
            print("123456789 doesnt exist")
        try:
            Person.objects.get(id="23456789").delete()
        except ObjectDoesNotExist:
            print("23456789 doesnt exist")

    def test_is_adult(self):
        older_person = Person.objects.get(id="123456789")
        younger_person = Person.objects.get(id="23456789")
        cutoff_age = datetime.now().year - 18

        self.assertEqual(older_person.birthDate.year <= cutoff_age, True, "Person is not an adult")
        self.assertEqual(younger_person.birthDate.year <= cutoff_age, False, "Person is an adult")

    # def test_update_person(self):
    #
    #     response = self.client.put("/api/updatePerson/",
    #                                {"id": "123456789",
    #                                 "name": "UpdatedName",
    #                                 "birthDate": "2000-01-01",
    #                                 "homeTown": "UpdatedTown"})

    # data = json.loads(response.content.decode('utf-8'))
    # self.assertEqual(response.status_code, 200)
    #     self.assertEqual(person.name, "test2")
    #     self.assertEqual(person.birthDate, "2000-01-01")
    #     self.assertEqual(person.homeTown, "UpdatedTown")
    # #
    def test_get_all_people(self):
        response = self.client.get("/api/getAllPeople/")
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(json_data), 2)
        self.assertEqual(len(json_data[0]), 4)

    #
    # def test_add_person(self):
    #     response = self.client.post("/api/addPerson/",
    #                                 {"id": 999, "name": "CreatedName", "birthDate": "2023-01-01",
    #                                  "homeTown": "CreatedTown"})
    #
    #     test_person = Person.objects.get(id=999)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(test_person.name, "CreatedName")
    #     self.assertEqual(test_person.birthDate, "2023-01-01")
    #     self.assertEqual(test_person.homeTown, "CreatedTown")
    #
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
        self.assertEqual(len(json_data["Children"]), 1)
