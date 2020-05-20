def shortest_window_sort(arr):
    # TODO: Write your code here
    low, high = 0, len(arr) - 1
    while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
        low += 1
    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1
    if low - 1 < 0:
        min_num = -float('inf')
        min_index = low - 1
    else:
        min_num = arr[low - 1]
        min_index = low - 1
    if high + 1 > len(arr) - 1:
        max_num = float('inf')
        max_index = high+1
    else:
        max_num = arr[high+1]
        max_index = high+1

    for i in range(low, high + 1):
        while arr[i] < min_num:
            min_index -= 1
            if min_index < 0:
                min_num = -float('inf')

        while arr[i] > max_num:
            max_index += 1
            if max_index > len(arr) - 1:
                max_num = float('inf')

    return arr[min_index + 1: max_index]



arr = [1,2,3,1]
print(shortest_window_sort(arr))
