#!/usr/bin/python3
"""
Unittest for base class
"""

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Testbaseclass(unittest.TestCase):
    """ test for base"""
    def testcreateelems(self):
        b = Base()
        b1 = Base(76)
        b2 = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(b1.id, 76)
        self.assertEqual(b2.id, 2)

    def testsetid(self):
        """ test for set id"""
        b = Base("h")
        b1 = Base({1: 2})
        b2 = Base((1, 4))
        b3 = Base([3, 6])
        b4 = Base(None)
        b5 = Base(0)
        self.assertEqual(b.id, "h")
        self.assertEqual(b1.id, {1: 2})
        self.assertEqual(b2.id, (1, 4))
        self.assertEqual(b3.id, [3, 6])
        self.assertEqual(b4.id, 4)
        self.assertEqual(b5.id, 0)

#     --------- private attribute of class --------

    def testprivate(self):
        """ test for private attribute"""
        b = Base()
        with self.assertRaises(AttributeError):
            b.__nb_objects

#    -------------- static method to_json_string -----------

    def testtojson(self):
        """ test to json"""
        dic = {'id': 8, 'size': 5, 'x': 6, 'y': 7}
        stdic = json.dumps([dic])
        self.assertEqual(Base.to_json_string([dic]), stdic)
        r = Base.to_json_string(None)
        self.assertEqual(r, "[]")
        r = Base.to_json_string([])
        self.assertEqual(r, "[]")
        dic = [1, 2, 3]
        r = Base.to_json_string([dic])
        self.assertEqual(r, "[[1, 2, 3]]")

    def testtojson1(self):
        """error json"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

#   --------------  save to file -------------------------

    def testsavetofile(self):
        """ test save to file"""
        Base.save_to_file([])
        with open("Base.json") as fd:
            self.assertEqual(fd.read(), "[]")
        Base.save_to_file(None)
        with open("Base.json") as fd:
            self.assertEqual(fd.read(), "[]")

    def testsavetofile1(self):
        """ error save to file"""
        with self.assertRaises(AttributeError):
            Base.save_to_string()

#    ----------------- from json --------------------------

    def testfromjson(self):
        """ test load from json"""
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        lista = [1, 2, 3]
        r = Base.to_json_string(lista)
        self.assertEqual(Base.from_json_string(r), lista)

    def testfromjson1(self):
        """ error save to file"""
        with self.assertRaises(TypeError):
            Base.from_json_string()
