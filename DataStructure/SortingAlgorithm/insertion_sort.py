'''
	# Himanshu Tripathi #
'''

# insertion sort


def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]

        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


# a = [21, 4, 5, 3, 57, 5, 332, 33, 56, 1]
# a = ['a','c','e','f','g','z','e']

if __name__ == '__main__':
    print(f'Sorted List {insertionSort(a)}')
