
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

if __name__ == "__main__":
    sorted_ans = insertion_sort([3,2,1])
    print(sorted_ans)
