
def smallest_subarray_with_given_sum(s, arr):
  # TODO: Write your code here
    windowStart, windowSum, windowLen = 0, 0, len(arr)+1
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        while windowStart <= windowEnd:
            if windowSum >= s:
                if windowEnd - windowStart + 1 <= windowLen:
                    windowLen = windowEnd - windowStart + 1
                windowSum -= arr[windowStart]
                windowStart += 1
            else:
                break
    if windowLen == len(arr)+1:

        return - 1
    else:
        return windowLen


l = [2, 1, 5, 2, 8]
print(smallest_subarray_with_given_sum(7, l))
