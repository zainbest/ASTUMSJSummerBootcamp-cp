class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = []
        for i in nums:
            if i not in x:
                x.append(i)
        for j in range(len(x)):
            nums[j] = x[j]
        return len(x)    

