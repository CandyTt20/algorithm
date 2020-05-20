def longest_substring_with_k_distinct(s, k):
    # TODO use count
    windowStart, windowEnd, windowLen, count = 0, 0, 0, 1
    
    while windowEnd<len(s)-1:
        while count <= k:
            windowEnd += 1
            if s[windowEnd] not in s[windowStart:windowEnd]:
                count += 1
                
        windowLen = max(windowLen, windowEnd - windowStart)

        while count > k:
            if s[windowStart] not in s[windowStart + 1:windowEnd + 1]:
                count -= 1
            windowStart += 1
    return windowLen

def longest_substring_with_k_distinct_HashMap(s, k):
    # TODO use hashmap

    hashmap = {}
    windowStart, windowLen = 0, 0
    
    for windowEnd in range(len(s)):
        charEnd = s[windowEnd]
        if charEnd not in hashmap:
            hashmap[charEnd] = 0
        hashmap[charEnd] += 1
        
        while len(hashmap) > k:
            windowLen = max(windowLen, windowEnd - windowStart)
            charStart = s[windowStart]
            hashmap[charStart] -= 1
            if hashmap[charStart] == 0:
                del hashmap[charStart]
            windowStart += 1
            
    return windowLen
            




s="cbbebi"
print(longest_substring_with_k_distinct_HashMap(s, 3))
