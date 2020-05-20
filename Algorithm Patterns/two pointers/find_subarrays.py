def find_subarrays(arr, target):
    result = []
    # TODO: Write your code here
    for left in range(len(arr)):
        right = left
        product = arr[left]
        while product < target:
            if left == right:
                result.append([arr[left]])
            else:
                result.append([arr[left], arr[right]])
            if right<len(arr)-1:
                right += 1
                product = product * arr[right]
            else:
                break
    return result
arr = [8, 2, 6, 5]
target=50 
print(find_subarrays(arr,target))