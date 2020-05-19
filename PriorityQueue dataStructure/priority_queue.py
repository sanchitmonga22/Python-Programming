"""
author: Sanchit Monga
lang: Pyhton
Description: This program takes the value of various tasks and arranges them according to their priority level
"""
from node import Node
from dataclasses import dataclass
from typing import Union

@dataclass
class PriorityQueue:
    size: int
    front: Union[None, Node]
    back: Union[None, Node]

def make_priority_queue():
    """
    This function returns the value of the empty queue
    """
    return PriorityQueue(0,None,None)

def enqueue(queue, element):
    """
    This function takes the value of the element and takes the queue and inserts the element according to its priority
    """
    newnode=Node(element, None)
    if is_empty(queue):
        queue.front=newnode
    else:
        queue.back.rest=newnode
    queue.back=newnode
    queue.size=queue.size+1
def dequeue(queue):
    """
    This function returns the element at the front of the queue
    """
    if is_empty(queue):
        raise IndexError("dequeue on empty queue")
    removed = queue.front.value
    queue.front = queue.front.rest
    if is_empty(queue):
        queue.back = None
    queue.size = queue.size - 1
    return removed
def front(queue):
    """
    This function returns the value of the front value of the function
    """
    if is_empty(queue):
        raise IndexError("front on empty queue")
    return queue.front.value

def back(queue):
    """
    This function returns the back of the queue
    """
    if is_empty(queue):
        raise IndexError("back on empty queue")
    return queue.back.value

def is_empty(queue):
    """
    This function checks whether the queue is empty or not
    """
    return queue.front == None

def s_que(queue):
    """
    Sorts the queue in the order accordning to the priority
    """
    final = make_priority_queue()
    while True:
        if queue.size == 1:
            break
        frof=dequeue(queue)
        s= queue.size
        while(s>=0):
            if frof.priority < front(queue).priority:
                frof1 = dequeue(queue)
                enqueue(queue,frof)
                frof= frof1
            else:
                frof1= dequeue(queue)
                enqueue(queue,frof1)
            s-=1
        enqueue(final,frof)
    v = front(queue)
    enqueue(final, v)
    return final