class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

def length(node):
    ln = 0
    while node != None:
        node = node.next
        ln = ln + 1
    return ln

def count(node,data):
    cnt = 0
    while node != None:
        if node.data == data:
            cnt+=1
        node = node.next
    return cnt
