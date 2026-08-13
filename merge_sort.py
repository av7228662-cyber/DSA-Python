from merge import merge


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)


x = int(input("Enter the size of array: "))
arr = []
for i in range(x):
    arr.append(int(input("Enter the element: ")))

sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)
