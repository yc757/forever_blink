print('Hello World')

def myswap(array, idx1, idx2):
    x = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = x
a = [1, 2, 3, 4]
myswap(a, 0, 2)
print(a)

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
a = [3, 2, 1, 4]
print(bubble_sort(a))

def mysum(array):
    x = 0
    for idx_num in array:
        x = x + idx_num
    return x
a = [1, 2, 3, 4, 5]
print(mysum(a))