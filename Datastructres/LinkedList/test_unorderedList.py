from unittest import TestCase
from LinkedList import *


class TestUnorderedList(TestCase):
    def test_isEmpty(self):
        temp = UnorderedList()
        self.assertTrue(temp.isEmpty())

    def test_size(self):
        temp = UnorderedList()
        temp.add(20)
        temp.add(30)
        self.assertEquals(temp.size(),2)

    def test_search(self):
        temp = UnorderedList()
        temp.add(20)
        temp.add(30)
        temp.add(50)
        temp.add(70)
        self.assertEquals(temp.search(30),30)

    def test_delete(self):
        temp = UnorderedList()
        temp.add(20)
        temp.add(30)
        temp.add(50)
        temp.add(70)
        temp.delete(30)
        self.assertEquals(temp.search(30),False)

if __name__ == '__main__':
         unittest.main()