from unittest import TestCase
from LenAndCount import length,count,Node
from Datastructres.PushAndBuild123.LinkedInPush import build_one_two_three


class TestLength(TestCase):
    def test_length(self):
        list = build_one_two_three()
        self.assertEquals(length(None),0)
        self.assertEquals(length(list),3)
        self.assertEquals(length(Node(99)),1)

    def test_count(self):
        list = build_one_two_three()
        self.assertEquals(count(list,1),1)
        self.assertEquals(count(list, 2), 1)
        self.assertEquals(count(list, 3), 1)
        self.assertEquals(count(list, 99), 0)
        self.assertEquals(count(None, 99), 0)