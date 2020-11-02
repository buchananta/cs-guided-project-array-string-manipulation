# how do we implement an array-reverse function in-place?

def reverse(arr):
    i = 0
    while i < (len(arr) / 2):
        # temp = arr[i]
        # arr[i] = arr[-i - 1]
        # arr[-i - 1] = temp
        arr[i], arr[-i -1] = arr[-i -1], arr[i]
        i += 1

def reverseInstructor(arr):
    left = 0
    right = len(arr) -1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

arr = [1,2,3,4,5]
print(arr)
reverse(arr) # in place alteration
print(arr)

