"""
Merge Quick Sort impementation

Author: Sanchit Monga
"""
import time
import random
import merge_sort
import insertion_sort
import quick_sort

def get_list1(n):
    """
    :param n: the length of a list
    :return: a list with random elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.random()]
    return L

def get_list2(n):
    """
    :param n: the length of a list
    :return: a list with many repeated elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.randint(1, 100)]
    return L

def get_list3(n):
    """
    Expected behavior of quick sort: poor
    :param n: the length of a list
    :return: a list of elements increasing overall
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.random() * i]
    return L

def get_list4(n):
    """
    :param n: the length of a list
    :return: a list with many zeros but neither increasing nor decreasing
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.randint(-8, 8) * i]
    return L

def merge_quick_sort(L):
    """
    This function inputs the value of unsorted list and invokes split function in the file merge_sort to split the list into two halves
    Then the function invokes the quick_sort function, then again it invokes the merge function in the merge_sort file and returns the sorted list
    :param L: The list which has to sorted
    :return: sorted list
    """
    (half1, half2) = merge_sort.split(L)
    (l1, l2) = quick_sort.quick_sort(half1), quick_sort.quick_sort(half2)
    return merge_sort.merge(l1,l2)

def test_merge_quick_sort():
    """
    This function is testing the merge_quick_sort function by passing the unsorted list as the input
    (Not true) Return : My name is Sanchit Monga
    """
    print("Berfore Sorted")
    print([[4, 8, 6, 15, 17, 5, 2, 13, 1, 19, 16, 3, 11, 7, 9, 18, 0, 10, 14, 12]])
    print("After Sorted")
    print(merge_quick_sort([4, 8, 6, 15, 17, 5, 2, 13, 1, 19, 16, 3, 11, 7, 9, 18, 0, 10, 14, 12]))

def test_compare(n):
    """
    :param n: This function takes n as an input for the number of integers to be put in the list
    This function calls the different sorting functions and calculates the time complexity of each sorting algorithm, and prints the time taken by them to sort 10000 elements
    """
    print("List 1")
    lst = get_list1(n)
    c=lst
    start = time.time()
    sorted_list = merge_quick_sort(lst)
    end = time.time()
    print(" Merge_Quick Sort elapsed time:", end - start, "seconds")
    start = time.time()
    sorted_list = quick_sort.quick_sort(lst)
    end = time.time()
    print("Quick Sort elapsed time:", end - start, "seconds")
    start = time.time()
    sorted_list = merge_sort.merge_sort(lst)
    end = time.time()
    print("Merge sort elapsed time:", end - start, "seconds")
    start = time.time()
    sorted_list = insertion_sort.insertion_sort(c)
    end = time.time()
    print("Insertion sort elapsed time:", end - start, "seconds")
    print("List 2")
    lst2 = get_list2(n)
    c2=lst2
    start = time.time()
    sorted_list = merge_quick_sort(lst2)
    end = time.time()
    print(" Merge_Quick Sort elapsed time:", end - start, "seconds")
    start = time.time()
    sorted_list = quick_sort.quick_sort(lst2)
    end = time.time()
    print("Quick sort elapsed time:", end - start, "seconds")
    start = time.time()
    sorted_list = merge_sort.merge_sort(lst2)
    end = time.time()
    print("Merge sort elapsed time:", end - start, "seconds")
    start = time.time()
    sorted_list = insertion_sort.insertion_sort(c2)
    end = time.time()
    print("Insertion sort elapsed time:", end - start, "seconds")
    print("List 3")
    lst3 = get_list3(n)
    c3=lst3
    start = time.time()
    sorted_list = merge_quick_sort(lst3)
    end = time.time()
    print(" Merge_Quick Sort elapsed time:", end - start, "seconds")
    start = time.time()
    sorted_list = quick_sort.quick_sort(lst3)
    end = time.time()
    print("Quick sort elapsed time:", end - start, "seconds")
    start = time.time()
    sorted_list = merge_sort.merge_sort(lst3)
    end = time.time()
    print("Merge sort elapsed time:", end - start, "seconds")
    start = time.time()
    sorted_list = insertion_sort.insertion_sort(c3)
    end = time.time()
    print("Insertion sort elapsed time:", end - start, "seconds")
    start = time.time()
    print("List 4")
    lst4 = get_list4(n)
    c4=lst4
    start = time.time()
    sorted_list = merge_quick_sort(lst4)
    end = time.time()
    print(" Merge_Quick Sort elapsed time:", end - start, "seconds")
    sorted_list = quick_sort.quick_sort(lst4)
    end = time.time()
    print("Quick sort elapsed time:", end - start, "seconds")
    start = time.time()
    sorted_list = merge_sort.merge_sort(lst4)
    end = time.time()
    print("Merge sort elapsed time:", end - start, "seconds")
    start = time.time()
    sorted_list = insertion_sort.insertion_sort(c4)
    end = time.time()
    print("Insertion sort elapsed time:", end - start, "seconds")

test_compare(10000)





