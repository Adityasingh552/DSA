class Solution:
    def productExceptSelf(self, nums):
        zero_count = 0
        product = 1
        zero_idx = 0

        ans = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                zero_idx = i
                continue

            product *= nums[i]

        if zero_count > 1:
            return ans

        elif zero_count == 1:
            ans[zero_idx] = product
            return ans

        for i in range(len(nums)):
            ans[i] = product // nums[i]

        return ans