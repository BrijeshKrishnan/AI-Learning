import numpy as np


class OrderedArray:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    def print(self):
        if self.last_position == -1:
            print('the array is empty !')
        else:
            for i in range(self.last_position + 1):
                print(i, '-', self.values[i])

    def insert(self, value):
        if self.last_position == self.capacity - 1:
            print("maximum capacity reached")
            return
        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i] > value:
                break
            if i == self.last_position:
                position = i + 1
        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1
        self.values[x + 1] = value
        self.last_position += 1


array = OrderedArray(10)
array.insert(6)
array.insert(4)
array.insert(3)
array.insert(2)
array.insert(1)
array.print()
