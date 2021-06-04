def merge(left_half: list, right_half: list):
    sorted_arr = []
    while left_half and right_half:
        if left_half[0] < right_half[0]:
            sorted_arr.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            sorted_arr.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        sorted_arr = sorted_arr + right_half
    else:
        sorted_arr = sorted_arr + left_half
    return sorted_arr

def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])
    return merge(left_half, right_half)

if '__main__' == __name__:
    arr = [int(i) for i in input(
        'Please enter list elements separated by comma, :').split(',')
        ]
    print("Sorted list: ", merge_sort(arr))