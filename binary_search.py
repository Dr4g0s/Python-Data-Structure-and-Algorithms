def binary_search(arr: list, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return 'element not found!'

if '__main__' == __name__:
    arr = [int(i) for i in input(
        'Please enter ordered list elements separated by comma, :').split(',')
        ]
    target = int(input("Please enter target value to find it's index: "))
    print("Sorted list: ", binary_search(arr, target))