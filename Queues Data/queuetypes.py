from collections import deque
from heapq import heappop, heappush
from dataclasses import dataclass
from itertools import count

#QUEUES
class Iterable:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

class Queue(Iterable):
    def __init__(self, *elements):
        self._elements = deque(elements)

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

#STACKS
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()
    
#PRIO
class PriorityQueue(Iterable):
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter),value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements) [-1]