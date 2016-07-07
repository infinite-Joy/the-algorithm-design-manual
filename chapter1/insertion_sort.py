from random import randint

try:
    range = xrange
except:
    pass

def insertion_sort(items_list):
    """
    items_list is the given list that needs to be sorted
    n should be the size of the list
    """
    j = 0
    for i in range(len(items_list)):
        j = i
        while j>0 and (items_list[j] < items_list[j-1]):
            items_list[j], items_list[j-1] = items_list[j-1], items_list[j]
            j -= 1
    return items_list


if __name__ == "__main__":
    unsorted_list = [randint(0,9) for p in range(0,9)]
    print unsorted_list
    sorted_ans = insertion_sort(unsorted_list)
    print sorted_ans
