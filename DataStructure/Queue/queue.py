'''
The order is First In First Out (FIFO).
Operations on Queue:
Mainly the following four basic operations are performed on queue:

Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.
Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition.
Front: Get the front item from queue.
Rear: Get the last item from queue.
'''


class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    # Queue is full when size becomes equal to the capacity
    def isFull(self):
        return self.size == self.capacity

    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    # Function to add an item to the queue.
    # It changes rear and size
    def EnQueue(self, item):
        if self.isFull():
            print("full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        # print(self.rear)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print(f'{str(item)} Enqueue to Queue')

    # Function to remove an item from Queue.
    # It changs front and size
    def DeQueue(self):
        if self.isEmpty():
            print('Empty')
            return
        print(f'{str(self.Q[self.front])} Dequeue from Queue')
        self.size = self.size - 1

    # Function to get front of Queue
    def que_front(self):
        if self.isEmpty():
            print('Queue is Empty')

        print("Front Item is", self.Q[self.front])

    # Function to get rear of queue
    def que_rear(self):
        if self.isEmpty():
            print('Queue is Empty')
        print('Rare item is', self.Q[self.rear])


# Driver Code
if __name__ == '__main__':

    queue = Queue(30)
    queue.EnQueue(55)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()
