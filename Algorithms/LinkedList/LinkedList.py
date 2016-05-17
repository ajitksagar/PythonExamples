class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def display(self):
        current = self.head
        while current != None:
            print (current.data)
            current = current.next

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count+=1
            current = current.next

        return count

    def search(self,item):
        current = self.head
        found = False
        while current.next != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        if found:
            return item
        else:
            return False

    def delete(self,item):
        current = self.head
        found = False
        previous = None
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next

        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next