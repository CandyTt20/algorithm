def max_sub_array_of_size_k(arr, k):
    windowStart, arrSum = 0, 0
    
    maxSum = sum(arr[0:k - 1])
    
    for windowEnd in range(len(arr)):
        arrSum += arr[windowEnd]
        if windowEnd > k - 1:
            arrSum -= arr[windowStart]
            if arrSum > maxSum:
                maxSum = arrSum
                
            windowStart += 1
    return maxSum

l = [2, 3, 4, 1, 5]
print(max_sub_array_of_size_k(l,2))
