def length_of_longest_substring(s, k):
  # TODO: Write your code here
    window_start, max_num, remain,window_length = 0, 0, 0, 0

    char_map = {}
    for window_end in range(len(s)):
        char_end = s[window_end]
        char_start = s[window_start]
        if char_end not in char_map:
            char_map[char_end] = 0
        
        char_map[char_end] += 1
        
        max_num = max(max_num, char_map[char_end])
        remain = window_end - window_start + 1 - max_num
        if remain > k:
            char_map[char_start] -= 1
            if char_map[char_start] == 0:
                del char_map[char_start]
            
            window_start += 1
        window_length = max(window_length, window_end - window_start + 1)
    return window_length
            
s = "abc"
print(length_of_longest_substring(s,1))
