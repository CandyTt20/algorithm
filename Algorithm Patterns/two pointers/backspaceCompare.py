class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.del_backspace(S, 0) == self.del_backspace(T, 0)

    def del_backspace(self, s, init):
        low, high = init, init+1
        if s == '':
            return s
        elif s[low] == '#':
            return self.del_backspace(s[low+1:], 0)
        while high < len(s):

            if s[high] != '#':
                low, high = low + 1, high + 1
            else:
                low, high = low - 1, high + 1
                if high == len(s):
                    return self.del_backspace(s[0:low + 1], low)
                elif s[high] != '#':
                    return self.del_backspace(s[0:low + 1] + s[high:], low)
                elif low < 0:
                    return self.del_backspace(s[high:], 0)

        if low == len(s) - 1 and high == len(s):
            return s


x = Solution()
print(x.backspaceCompare('a#', ''))

class Solution_2(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.del_backspace(S) == self.del_backspace(T)

    def del_backspace(self, s):
        result = []
        for i in range(len(s)):
            if s[i] != '#':
                result.append(s[i])
            elif s[i] == '#' and result != []:
                result.pop()
        return result


s = '#av#'
t = 'av#'
x = Solution()
print(x.backspaceCompare(s, t))
