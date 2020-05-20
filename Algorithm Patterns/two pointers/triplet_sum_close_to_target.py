def triplet_sum_close_to_target(arr, target_sum):
    index = 0
    min_num = float('inf') # TODO import math (math.inf)
    result_map = {}
    while index < len(arr) - 1:


    #! diff = target-(a+b+c) smallest=float('inf')
    #! if abs(diff) < abs(smallest) or abs(diff)==abs(smallest) and diff>smallest:
    #!     smallest = deff
        
        left, right = index + 1, len(arr) - 1
        while left < right:
            if abs(arr[index] + arr[left] + arr[right] - target_sum) <= min_num:
                min_num = abs(arr[index] + arr[left] + arr[right] - target_sum)
                key = (arr[index], arr[left], arr[right])
                result_map[key] = min_num
            if arr[index] + arr[left] + arr[right] > target_sum:
                right -= 1
            else:
                left += 1
        index += 1
    result_map_key = min(result_map, key=result_map.get)
    sum_val = result_map_key[0] + result_map_key[1] + result_map_key[2]
    min_val = result_map[result_map_key]
    for item in result_map:
        if result_map[item] == min_val:
            if item[0] + item[1] + item[2] < sum_val:
                result_map_key = (item[0], item[1], item[2])

    return result_map_key


arr = [1, 0, 1, 1]

print(triplet_sum_close_to_target(arr, 100))
