#!/usr/bin/python3
"""
Unittest for Rectangle Class
"""
import os
import json
from io import StringIO
from unittest.mock import patch
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    all test for Rectangle class
    """
    def testcreateelems(self):
        """ test for create elements """
        r = Rectangle(1, 1)
        r1 = Rectangle(2, 5, 6)
        r2 = Rectangle(6, 8, 10, 9)
        r3 = Rectangle(1, 1, 1, 1, 90)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 6)
        self.assertEqual(r2.width, 6)
        self.assertEqual(r2.height, 8)
        self.assertEqual(r2.x, 10)
        self.assertEqual(r2.y, 9)
        self.assertEqual(r3.id, 90)

    def testgetandset(self):
        """ test for get and set"""
        r = Rectangle(5, 2)
        self.assertEqual(r.width, 5)
        r.width = 9
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 2)
        r.height = 8
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 0)
        r.x = 8
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 0)
        r.y = 1
        self.assertEqual(r.y, 1)
        r.id = 99
        self.assertEqual(r.id, 99)

#  ---------- tests for width -----------------------

    def testwidth(self):
        """ test of width"""
        with self.assertRaises(TypeError):
            r = Rectangle("hola", 2)

        with self.assertRaises(TypeError):
            r = Rectangle([1, 4], 2)

        with self.assertRaises(TypeError):
            r = Rectangle((1, 1), 4)

        with self.assertRaises(TypeError):
            r = Rectangle({'a': 3}, 5)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 6)

        with self.assertRaises(ValueError):
            r = Rectangle(-6, 8)

        with self.assertRaises(TypeError):
            r = Rectangle(3.6, 9)

#   ---------- tests for height -----------------------

    def testheight(self):
        """ test of height"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, "hola")

        with self.assertRaises(TypeError):
            r = Rectangle(2, [1, 2])

        with self.assertRaises(TypeError):
            r = Rectangle(4, (1, 2))

        with self.assertRaises(TypeError):
            r = Rectangle(5, {'a': 4, 'b': 8})

        with self.assertRaises(ValueError):
            r = Rectangle(6, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(6, -8)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 9.7)

#   ---------- tests for x -----------------------------
    def testx(self):
        """ test of x"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, "hola")

        with self.assertRaises(TypeError):
            r = Rectangle(2, 1, [1, 2])

        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, (1, 2))

        with self.assertRaises(TypeError):
            r = Rectangle(5, 6, {'a': 4, 'b': 8})

        with self.assertRaises(ValueError):
            r = Rectangle(6, 6, -8)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 2, 9.7)

    def testx1(self):
        """ x == 0"""
        r = Rectangle(6, 5, 0)
        self.assertEqual(r.x, 0)

#   ---------- tests for y ---------

    def testy(self):
        """ test of y"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, 5, "hola")

        with self.assertRaises(TypeError):
            r = Rectangle(2, 1, 5, [1, 2])

        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, 6, (1, 2))

        with self.assertRaises(TypeError):
            r = Rectangle(5, 6, 7, {'a': 4, 'b': 8})

        with self.assertRaises(ValueError):
            r = Rectangle(6, 6, 9, -8)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 8, 3, 9.7)

    def testy1(self):
        """ test y == 0"""
        r = Rectangle(6, 5, 0, 0)
        self.assertEqual(r.y, 0)

#    ---------------------- id ----------------------------

    def testid(self):
        """ id values """
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 6)
        r = Rectangle(2, 3, 4, 5, "6")
        self.assertEqual(r.id, "6")
        r = Rectangle(2, 3, 4, 5, {'id': 3})
        self.assertEqual(r.id, {'id': 3})
        r = Rectangle(2, 3, 4, 5, (1, 2))
        self.assertEqual(r.id, (1, 2))
        r = Rectangle(2, 3, 4, 5, [2, 4])
        self.assertEqual(r.id, [2, 4])

#    -----------  Area    ---------------------------------

    def testarea1(self):
        """ test area"""
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)

    def testarea2(self):
        """ error area"""
        r = Rectangle(5, 6)
        with self.assertRaises(TypeError):
            r.area(1)

#    ------------- Display ---------------------------------

    def testdisplay(self):
        """ test with display"""
        with patch('sys.stdout', new=StringIO()) as salida:
            r = Rectangle(2, 3)
            r.display()
            st = "##\n##\n##\n"
            self.assertEqual(salida.getvalue(), st)

        with patch('sys.stdout', new=StringIO()) as salida:
            r = Rectangle(2, 3, 2)
            r.display()
            st = "  ##\n  ##\n  ##\n"
            self.assertEqual(salida.getvalue(), st)

        with patch('sys.stdout', new=StringIO()) as salida:
            r = Rectangle(2, 3, 2, 2)
            r.display()
            st = "\n\n  ##\n  ##\n  ##\n"
            self.assertEqual(salida.getvalue(), st)

    def testdisplay1(self):
        """ error with display"""
        r = Rectangle(1, 3)
        with self.assertRaises(TypeError):
            r.display(1)

#    -------------- __str__ ---------------------------------

    def tesstr(self):
        """ test str"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

#    ----------------- Update -------------------------------

    def testupdate(self):
        """ test update"""
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")
        r.update(2, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 1/1 - 2/1")

        lista = [3, 4, 5]
        r.update(*lista)
        self.assertEqual(str(r), "[Rectangle] (3) 1/1 - 4/5")

        lista = (1, 2, 4, 5)
        r.update(*lista)
        self.assertEqual(str(r), "[Rectangle] (1) 5/1 - 2/4")

        lista = []
        r.update(*lista)
        self.assertEqual(str(r), "[Rectangle] (1) 5/1 - 2/4")

        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 5/1 - 2/4")

        di = {'x': 10, 'y': 20}
        r.update(**di)
        self.assertEqual(str(r), "[Rectangle] (1) 10/20 - 2/4")

        di = {'id': 5, 'width': 5, 'height': 5, 'x': 5, 'y': 5}
        r.update(**di)
        self.assertEqual(str(r), "[Rectangle] (5) 5/5 - 5/5")

        lista = [9, 9, 9, 9, 9]
        dic = {'id': 2, 'width': 2, 'height': 2, 'x': 2, 'y': 2}
        r.update(*lista, **dic)
        self.assertEqual(str(r), "[Rectangle] (9) 9/9 - 9/9")

#    ------------------------- Dictionary -----------------------

    def testdictionary(self):
        """ test dictionary"""
        r = Rectangle(5, 6, 7, 8, 3)
        r1 = r.to_dictionary()
        pr = {'id': 3, 'width': 5, 'height': 6, 'x': 7, 'y': 8}
        for elem in pr:
            self.assertEqual(r1[elem], pr[elem])

    def testdictionary1(self):
        """ error dictionary"""
        r = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            r.to_dictionary(9)

#    ------------------------- no Arguments -------------------------------
    def testfargument1(self):
        """No args"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def testfargument2(self):
        """ just 1 arg"""
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def testfargument3(self):
        """ more than 5 args"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

#    -------------------instance and inheritance ----------------------------

    def testinstandclass(self):
        """ instances, subclases, verifications"""
        r = Rectangle(4, 5)
        self.assertTrue(isinstance(r, Rectangle))
        self.assertTrue(isinstance(r, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(type(r) is Rectangle)
        self.assertTrue(hasattr(r, 'width'))
        self.assertTrue(hasattr(r, 'height'))
        self.assertTrue(hasattr(r, 'x'))
        self.assertTrue(hasattr(r, 'y'))
        self.assertTrue(hasattr(r, 'id'))

#    -------------- static method to_json_string -----------

    def testtojson(self):
        """ test to json"""
        dic = {'id': 8, 'size': 5, 'x': 6, 'y': 7}
        stdic = json.dumps([dic])
        self.assertEqual(Rectangle.to_json_string([dic]), stdic)
        r = Rectangle.to_json_string(None)
        self.assertEqual(r, "[]")
        r = Rectangle.to_json_string([])
        self.assertEqual(r, "[]")
        dic = [1, 2, 3]
        r = Rectangle.to_json_string([dic])
        self.assertEqual(r, "[[1, 2, 3]]")

    def testtojson1(self):
        """error json"""
        with self.assertRaises(TypeError):
            Rectangle.to_json_string()

#   --------------  save to file -------------------------

    def testsavetofile(self):
        """ test save to file"""
        nw = []
        Rectangle.save_to_file(new)
        with open("Rectangle.json") as fd:
            self.assertEqual(fd.read(), "[]")

    def testsavetofile(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as fd:
            self.assertEqual(fd.read(), "[]")

    def testsavetofile1(self):
        """ error save to file"""
        with self.assertRaises(AttributeError):
            Rectangle.save_to_string()

    def testsavetofile3(self):
        r1 = Rectangle(1, 2)
        Rectangle.save_to_file([r1])
        res = '[{"x": 0, "y": 0, "id": 24, "height": 2, "width": 1}]'
        with open("Rectangle.json", "r") as file:
            res2 = file.read()
            self.assertEqual(len(res2), len(res))

    def testsavetofile2(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        res = '\'[{"x": 2, "y": 8, "id": 2, "height": 7, "width": 10},'
        res = res + ' {"x": 0, "y": 0, "id": 3, "height": 4, "width": 2}]\''
        with open("Rectangle.json", "r") as file:
            res2 = file.read()
            self.assertEqual(len(res2), len(res))

#    ----------------- from json --------------------------

    def testfromjson(self):
        """ test load from json"""
        self.assertEqual(Rectangle.from_json_string("[]"), [])
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string(""), [])
        lista = [1, 2, 3]
        r = Rectangle.to_json_string(lista)
        self.assertEqual(Rectangle.from_json_string(r), lista)

    def testfromjson1(self):
        """ error save to file"""
        with self.assertRaises(TypeError):
            Rectangle.from_json_string()

#    ------------------- create ----------------------------

    def testcreate(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual((r1 == r2), False)
        self.assertEqual((r1 is r2), False)

    def testcreate1(self):
        with self.assertRaises(TypeError):
            r = Rectangle.create(None)
        with self.assertRaises(TypeError):
            r = Rectangle.create("holby")
        with self.assertRaises(TypeError):
            r = Rectangle.create([1, 2, 3])
        with self.assertRaises(TypeError):
            r = Rectangle.create(1)
        with self.assertRaises(TypeError):
            r = Rectangle.create(1.0)
        with self.assertRaises(TypeError):
            r = Rectangle.create({1, 2, 3})

    def testcreate2(self):
        r = Rectangle(2, 2, 0, 0, 89)
        r1 = Rectangle.create(**{'id': 89})
        self.assertTrue(r1.width == r.width)
        self.assertTrue(r1.height == r.height)
        self.assertTrue(r1.x == r.x)
        self.assertTrue(r1.y == r.y)
        self.assertTrue(r1.id == r.id)

    def testcreate3(self):
        r = Rectangle(1, 2, 0, 0, 89)
        r1 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertTrue(r1.width == r.width)
        self.assertTrue(r1.height == r.height)
        self.assertTrue(r1.x == r.x)
        self.assertTrue(r1.y == r.y)
        self.assertTrue(r1.id == r.id)

    def testcreate2(self):
        r = Rectangle(1, 2, 0, 0, 89)
        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertTrue(r1.width == r.width)
        self.assertTrue(r1.height == r.height)
        self.assertTrue(r1.x == r.x)
        self.assertTrue(r1.y == r.y)
        self.assertTrue(r1.id == r.id)

    def testcreate3(self):
        r = Rectangle(1, 2, 3, 0, 89)
        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertTrue(r1.width == r.width)
        self.assertTrue(r1.height == r.height)
        self.assertTrue(r1.x == r.x)
        self.assertTrue(r1.y == r.y)
        self.assertTrue(r1.id == r.id)

    def testcreate4(self):
        r = Rectangle(1, 2, 3, 4, 89)
        dict = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dict)
        self.assertTrue(r1.width == r.width)
        self.assertTrue(r1.height == r.height)
        self.assertTrue(r1.x == r.x)
        self.assertTrue(r1.y == r.y)
        self.assertTrue(r1.id == r.id)

#    -------------------- from file --------------------------

    def testloadfromfiles(self):
        if os.path.exists("Rectangle.json") is True:
            Rectangle.save_to_file([])
        rect_list = Rectangle.load_from_file()
        self.assertEqual(rect_list, [])

    def testloadfromfiles2(self):
        if os.path.exists("Rectangle.json") is True:
            os.remove("Rectangle.json")
        rect_list = Rectangle.load_from_file()
        self.assertEqual(rect_list, [])

    def testloadfromfile3(self):
        with self.assertRaises(TypeError):
            rect_list = Rectangle.load_from_file("Hey")
