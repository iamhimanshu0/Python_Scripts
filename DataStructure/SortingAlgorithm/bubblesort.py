
'''
	# Himanshu Tripathi #
'''

# bubble sort

# sort in descending order


def bubble_sort(a):
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if a[i] > a[j]:
                # swap values
                a[i], a[j] = a[j], a[i]
    return a


l = [64, 34, 25, 12, 22, 11, 90]

if __name__ == '__main__':
    print(f'Sorted Array: {bubble_sort(l)}')
