class Node(object):
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

def push(head,data):
      if head == None:
        temp = Node(data)
        temp.next = head
        head = temp
        return head
      else:
        temp = Node(data)
        temp.next = head
        head.next = None
        head = temp
        return head

def build_one_two_three():
    one = Node(1)
    head = one
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    three.next = None
    return head

#print(push(None, 1).data)
#print(push(None, 1).next)
#print(push(Node(1), 2).next.data)