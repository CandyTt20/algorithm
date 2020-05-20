class Solution(object):

    def circularArrayLoop(self, nums):
        isTrue = False
        for i in range(len(nums)):
            isTrue = isTrue or self.isCircle(nums, i)
        return isTrue
    def isCircle(self, nums, init):
        # N = len(nums)
        if nums == []:
            return False
        length = 1
        slow, fast = init, init
        while True:
            slow = self.ge_next(nums, slow)
            fast = self.ge_next(nums, self.ge_next(nums, fast))
            if slow == fast:
                break
        tag, sign, isForward = slow, nums[slow], True

        while self.ge_next(nums, slow) != tag:
            length += 1
            slow = self.ge_next(nums, slow)
            if (sign >= 0 and nums[slow] >= 0) or (sign < 0 and nums[slow] < 0):
                isForward = isForward and True
            else:
                isForward = isForward and False

        if (sign >= 0 and nums[slow] >= 0) or (sign < 0 and nums[slow] < 0):
            isForward = isForward and True
        else:
            isForward = isForward and False

        if length > 1 and isForward:
            return True
        else:
            return False

    def ge_next(self, nums, index):
        length_nums = len(nums)
        next_index = index + nums[index]
        if next_index >= length_nums or next_index < 0:
            return next_index % length_nums
        else:
            return next_index


x = Solution()
arr = []
print(x.circularArrayLoop(arr))
