class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None]*size
        self.front = self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return
        elif self.isEmpty():
            self.front = self.rear = 0    
        else:
            self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = value

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def front(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.items[self.front]

    def rear(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.items[self.items[self.rear]]
    