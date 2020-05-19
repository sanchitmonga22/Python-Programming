from dataclasses import dataclass
from priority_queue import *

@dataclass
class Task:
    name: str
    priority: int

def make_task(name, priority):
    """
    This function creates  a task instant and returns it
    """
    return Task(name, priority)

q = make_priority_queue()

enqueue(q, Task("Task1", 3))
enqueue(q, Task("Task1", 9))
enqueue(q, Task("Task2", 2))
enqueue(q, Task("Task2", 8))
enqueue(q, Task("Task2", 11))
enqueue(q, Task("Task2", 4))
q=s_que(q)
t = front(q)

print("Highest priority task is", t.name, "with priority",t.priority)
t = back(q)
print("Lowest priority task is", t.name, "with priority",t.priority)
while not is_empty(q):
    t = front(q)
    dequeue(q)