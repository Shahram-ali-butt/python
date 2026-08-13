class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self, head = None):
        self.head = head

    def setHead(self, data):
        if(self.head == None):
            self.head = Node(data)
            return
        newNode = Node(data)
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode

    def append(self, data):
        if(self.head == None):
            self.setHead(data)
            return
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def insertAfterElement(self, data, element):
        if(self.head == None):
            print("List is Empty")
            return
        temp = self.head
        newNode = Node(data)
        while(temp is not None):
            if(temp.data == element):
                newNode.next = temp.next
                temp.next = newNode
                newNode.prev = temp
                return
            temp = temp.next
        if(temp is None): print("Element not found")

    def insertAfterIndex(self, data, index):
        if(self.head == None):
            print("List is Empty")
            return
        temp = self.head
        newNode = Node(data)
        idx = 0
        while(temp is not None):
            if(idx == index):
                newNode.next = temp.next
                temp.next = newNode
                newNode.prev = temp
                return
            temp = temp.next
            idx+=1
        if(temp is None): print("Index out of bound")

    def insertAtIndex(self, data, index):
        if(index < 0): 
            print("Negative indeces are not allowed")
            return
        elif(index == 0):
            self.setHead(data)
            return

        temp = self.head
        idx = 0
        while(temp != None):
            if(idx == index):
                prev = temp.prev
                prev.next = temp.next
                return
            idx += 1
            temp = temp.next
        if(temp is None): print("Index out of bound")

    def deleteElement(self, element):
        if(self.head == None):
            print("List is Empty")
            return
        temp = self.head
        if(temp.data == element):
            self.head = self.head.next
            self.head.prev = None
            return
        while(temp is not None):
            if(temp.data == element):
                prev = temp.prev
                prev.next = temp.next
                return
            temp = temp.next
        if(temp is None): print("Element not found")

    def printDLL(self):
        if(self.head == None):
            print("Empty list")
            return
        temp = self.head
        while(temp.next is not None):
            print(temp.data, end=" <-> ")
            temp = temp.next
        print(temp.data, end="")

# --------------------
#        Usage
# --------------------

list = DLL()
list.setHead(0)
list.append(1)
list.append(2)
list.append(3)
list.insertAfterElement(4, 3)
list.insertAfterIndex(5, 4)
list.deleteElement(0)
list.insertAtIndex(0, 1)
list.printDLL()