from unittest import TestCase
from LinkedInPush import Node,push,build_one_two_three


class TestPush(TestCase):
    def test_push(self):
        self.assertEquals(push(None,1).data,1)
        self.assertEquals(push(None, 1).next, None)
        self.assertEquals(push(Node(1), 2).data, 2)
        self.assertEquals(push(Node(1), 2).next.data, 1)

    def test_build_one_two_three(self):
        self.assertEquals(build_one_two_three().data,1)
        self.assertEquals(build_one_two_three().next.data, 2)
        self.assertEquals(build_one_two_three().next.next.data, 3)
        self.assertEquals(build_one_two_three().next.next.next, None)
