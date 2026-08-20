class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def insertAtRear(self, value):
        self.items.append(value)

    def insertAtFront(self, value):
        self.items.insert(0, value)

    def deleteFromFront(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.items.pop(0)

    def deleteFromRear(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.items.pop()

    def front(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.items[0]

    def rear(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.items[len(self.items) - 1]