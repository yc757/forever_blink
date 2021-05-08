"""
for i in range (1,10):
    if i != 5:
        print(end=" ")
        for j in range (1,10):
            print(i,'*',j,'=',i*j,end="  " )
            if j == 9:
                print("\n")
                

def swap(a, idx1, idx2):
    a[idx1] = a[idx1] ^ a[idx2]
    a[idx2] = a[idx2] ^ a[idx1]
    a[idx1] = a[idx1] ^ a[idx2]
a = [1, 2, 3, 4, 5, 6]
swap(a, 1, 4)
print(a)

"""

def xy(x, y):
    while y:
        z = x % y
        x = y
        y = z
    return x
print(xy(14, 18))