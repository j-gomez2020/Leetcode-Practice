class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        Map = {}
        length = len(nums)

        for i in range(length):
            x = target - nums[i]
            if x in Map:
                return [Map[x], i]
            Map[nums[i]] = i

        return []  # No solution found

        #sudo code
        # if (num1 + num2 = target) return index of num1, index of num2
