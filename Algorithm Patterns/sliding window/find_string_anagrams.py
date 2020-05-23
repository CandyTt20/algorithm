def find_string_anagrams(s, pattern):
    result_indexes = []
    window_start = 0

    # TODO: Write your code here
    password_map, frequency_map = {}, {}

    for key in pattern:
        if key not in password_map:
            password_map[key] = 0
        password_map[key] += 1

    for window_end in range(len(s)):
        char_end = s[window_end]
        char_start = s[window_start]

        if char_end not in frequency_map:
            frequency_map[char_end] = 0
        frequency_map[char_end] += 1
        if window_end - window_start + 1 > len(pattern):
            frequency_map[char_start] -= 1
            if frequency_map[char_start] == 0:
                del frequency_map[char_start]
            window_start += 1
        if frequency_map == password_map:
            result_indexes.append(window_start)

    return result_indexes



s = "abab"
p = "c"
print(find_string_anagrams(s, p))
