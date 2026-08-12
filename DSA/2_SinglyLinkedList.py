class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self, head = None):
        self.head = None
        self.setHead(head)

    def setHead(self, value):
        if(value != None):
            temp = self.head
            self.head = self.__typeCheckNSetNode__(value)
            self.head.next = temp
        
    def __typeCheckNSetNode__(self, value):
        if(type(value) != Node):
            node = Node(value)
        else:
            node = value
        return node

    def append(self, data):
        if(self.head == None):
            self.head = self.__typeCheckNSetNode__(data)
        else:
            tail = self.head
            while(tail.next != None):
                tail = tail.next
            tail.next = self.__typeCheckNSetNode__(data)

    def insertAtIndex(self, data, index):
        idx = 0
        orignalNode = self.head
        prevNode = None

        if(index == 0): 
            self.setHead(data) 
            return
        elif(index < 0): 
            print("Negative Index is not allowed")
            return

        while((orignalNode is not None) and (idx <= index)): 
            idx+=1
            prevNode = orignalNode
            orignalNode = orignalNode.next

        if(orignalNode is not None):
            newNode = self.__typeCheckNSetNode__(data)
            newNode.next = orignalNode
            prevNode.next = newNode
        else: 
            print("Error: Index out of bound")
            
    def insertAfterIndex(self, data, index):
        if self.head is None:
            print("The list is empty.")
            return
        elif(index < 0): 
            print("Negative Index is not allowed")
            return

        idx = 0
        orignalNode = self.head

        while((orignalNode is not None) and (idx < index)):
            orignalNode = orignalNode.next
            idx+=1

        if(orignalNode is not None):
            newNode = self.__typeCheckNSetNode__(data)
            newNode.next = orignalNode.next
            orignalNode.next = newNode
        else: print("Error: Index out of bound of list")

    def insertAfterElement(self, data, element):
        if self.head is None:
            print("The list is empty.")
            return

        tail = self.head
        found = False
        while(tail is not None):
            if(tail.data == element):
                newNode = self.__typeCheckNSetNode__(data)
                newNode.next = tail.next
                tail.next = newNode
                found = True
                break
            tail = tail.next
        if(not found): print("Element Not Found")

    def deleteElement(self, element):
        if self.head is None:
            print("The list is empty.")
            return
        
        requiredNode = self.__typeCheckNSetNode__(element)
        currentNode = self.head
        prevNode = None
        found = False

        if(currentNode.data == requiredNode.data): 
            self.head = currentNode.next
            return

        while(currentNode is not None):
            if(currentNode.data == requiredNode.data):
                prevNode.next = currentNode.next
                found = True
                break
            prevNode = currentNode
            currentNode = currentNode.next
            
        if(not found): print("Element Not Found")

    def deleteIndex(self, index):
        if(self.head == None):
            print("The list is empty.")
            return
        elif(index == 0):
            self.head = self.head.next
            return

        idx = 0
        prevNode = None
        currentNode = self.head
        while(currentNode is not None):
            if(idx == index):
                prevNode.next = currentNode.next
                break
            idx+=1
            prevNode = currentNode
            currentNode = currentNode.next
        if(currentNode is None): print("Error: Index Out of Bound")

    def printList(self):
        if(self.head == None): print("Empty List")
        else:
            tail = self.head
            while(tail.next != None):
                print(tail.data, end=" ")
                tail = tail.next
            print(tail.data, end=" ")

# --------------------
#        Usage
# --------------------

list = SLL()
list.append(Node(0))
list.append(1)
list.append(2)
list.append(3)
list.append("a")
list.setHead(-1)

# list.insertAtIndex(12, 6)
# list.insertAfterIndex(12, 5)
# list.insertAfterElement(12, 5)
# list.deleteElement(0)
# list.deleteIndex(0)

list.printList()
print("\n")