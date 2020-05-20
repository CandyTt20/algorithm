def f(s):
    windowStart, windowEnd, maxLen = 0, 0, 0
    while windowEnd < len(s):
        if s[windowEnd] not in s[windowStart:windowEnd]:
            windowEnd += 1
        else:
            maxLen = max(maxLen, windowEnd-windowStart)
            windowStart += s[windowStart:windowEnd].find(s[windowEnd])+1
            windowEnd += 1
    maxLen = max(maxLen, windowEnd-windowStart)
    return maxLen


def non_repeat_substring(s):
    # TODO hashmap
    windowStart, windowLen = 0, 0
    hashmap = {}
    for windowEnd in range(len(s)):
        charEnd = s[windowEnd]
        if charEnd not in hashmap:
            hashmap[charEnd] = windowEnd
        elif charEnd in hashmap and hashmap[charEnd] >= windowStart:
            windowLen = max(windowLen, windowEnd - windowStart)
            windowStart = hashmap[charEnd] + 1
            hashmap[charEnd] = windowEnd
            
    return windowLen

def non_repeat_substring_02(s):
    # TODO hashmap

    windowStart, windowLen = 0, 1
    hashmap = {}
    if s == '':
        windowLen=0
    for windowEnd in range(len(s)):
        charEnd = s[windowEnd]
        if charEnd in hashmap:
            windowLen = max(windowEnd - windowStart, windowLen)
            windowStart = max(windowStart, hashmap[charEnd] + 1)
        hashmap[charEnd]=windowEnd
            
    return windowLen

s = ""
print(non_repeat_substring_02(s))
