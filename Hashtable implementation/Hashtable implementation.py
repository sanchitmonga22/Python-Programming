from dataclasses import dataclass
from typing import Any, Hashable,Callable,List

@dataclass
class Entry:
    key:Hashable #immutable, frozen
    value:Any

@dataclass
class HashTable:
    table:list
    size:int
    capacity:int
    hash_func:Callable

def create_hash_table(hash_function, capacity):#hTable={}
    table=[]
    for i in range(capacity):
        table.append(None)
    return HashTable(table,0,capacity,hash_function)

def has(hTable,key):#key in hashTable
    index = hTable.hash_func(key) % hTable.capacity
    startIndex = index
    # linear probing
    while hTable.table[index] is not None and hTable.table[index].key != key:
        index = (index + 1) % hTable.capacity
        if startIndex == index:
            raise Exception("hTable is full")
    if hTable.table[index] is None:  # insert
         return False
    elif hTable.table[index].key == key:  # update
        return True

def get(hTable, key):
    index = hTable.hash_func(key) % hTable.capacity
    startIndex = index
    # linear probing
    while hTable.table[index] is not None and hTable.table[index].key != key:
        index = (index + 1) % hTable.capacity
        if startIndex == index:
            raise Exception("hTable is full")
    if hTable.table[index] is None:  # insert
        raise Exception("Key does not esist")
    elif hTable.table[index].key == key:  # update
        return hTable.table[index].value

def put(hTable,key,new_value):#either insert or update
    index=hTable.hash_func(key)%hTable.capacity
    startIndex=index
    #linear probing
    while hTable.table[index]is not None and hTable.table[index].key!=key:
        index=(index+1)%hTable.capacity
        if startIndex==index:
            raise Exception("hTable is full")
    if hTable.table[index] is None:  # insert
        hTable.table[index] = Entry(key, new_value)
        hTable.size+=1
    elif hTable.table[index].key==key:#update
        count=hTable.table[index].value
        hTable.table[index].value=value

def keys(hTable):#returns a list of keys in the given table
    result=[]
    for entry in hTable.table():
        if entry is not None:
            result.append(entry.key)
    return result


def main():
    hTable=create_hash