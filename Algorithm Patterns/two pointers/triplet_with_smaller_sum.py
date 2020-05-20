def triplet_with_smaller_sum(arr, target):
    count = 0
    arr.sort()
    l=[]
    # TODO: Write your code here
    for i in range(len(arr) - 1):
        for left in range(i + 1, len(arr)):
            right = len(arr) - 1
            while arr[i] + arr[left] + arr[right] >= target and left < right:
                right -= 1
            count += right - left
            l.append([arr[i],arr[left],arr[right]])     
    return count
arr = [-1, 0, 2, 3]
target=3 
print(triplet_with_smaller_sum(arr, target))