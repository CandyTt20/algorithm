class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        return self.merge(self.newList(intervals, newInterval))

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals == []:
            return []
        merged = []
        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                merged.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        merged.append([start, end])
        return merged

    def newList(self, intervals, new_interval):
        ret = []
        i = 0
        while i < len(intervals):
            if intervals[i][0] <= new_interval[0]:
                ret.append(intervals[i])
                i += 1
            else:
                break

        ret.append(new_interval)
        j = i
        while j < len(intervals):
            ret.append(intervals[j])
            j += 1

        return ret


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
x = Solution()

print(x.insert(intervals, newInterval))

