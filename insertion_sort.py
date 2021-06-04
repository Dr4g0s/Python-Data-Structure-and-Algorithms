def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        prv = i - 1
        while prv >= 0 and arr[prv] > key:
            arr[prv+1], arr[prv] = arr[prv], arr[prv+1]
            prv -= 1
    return arr

if '__main__' == __name__:
    arr = [int(i) for i in input(
        'Please enter list elements separated by comma, :').split(',')
        ]
    print("Sorted list: ", insertion_sort(arr))