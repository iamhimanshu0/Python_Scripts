'''
	# Himanshu Tripathi #
'''

# Selection Sort
'''
# The selection sort algorithm sorts an array by repeatedly 
# finding the minimum element (considering ascending order) 
# from unsorted part and putting it at the beginning.
# The algorithm maintains two subarrays in a given array.
'''


def selectionSort(a):
    for i in range(len(a)):

        # finding the minimum element in remaining
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j

        # swap the element
        a[i], a[min_idx] = a[min_idx], a[i]

    return a


a = [1, 4, 56, 24, 53, 2, 34]

if __name__ == '__main__':
    print(f'Sorted list {selectionSort(a)}')
