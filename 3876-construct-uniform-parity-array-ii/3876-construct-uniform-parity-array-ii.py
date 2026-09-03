class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = 0
        even = 0
        size = len(nums1)

        min_odd = float('inf')
        for x in nums1:
            if x % 2 == 1:
                min_odd = min(min_odd, x)
                odd += 1
            else:
                even += 1
        if odd == size or even == size:
            return True
        for x in nums1:
            if x % 2 == 0:
                if x < min_odd:
                    return False

        return True