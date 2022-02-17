# Leetcode 719 Hard

# Problem Statement :
#     The distance of a pair of integers a and b is defined as the absolute difference between a and b.
#     Given an integer array nums and an integer k, return the kth smallest distance among all the
#     pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

# Example 1
#     Input: nums = [1,3,1], k = 1
#     Output: 0
#     Explanation: Here are all the pairs:
#     (1,3) -> 2
#     (1,1) -> 0
#     (3,1) -> 2
#     Then the 1st smallest distance pair is (1,1), and its distance is 0.

# Solution 1
# Approach : BinarySearch + SlidingWindow

class Solution(object):
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            # Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) / 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo


# Solution 2
# Approach : BinarySearch + PrefixSum

class Solution(object):
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            # Is there k or more pairs with distance <= guess?
            return sum(prefix[min(x + guess, W)] - prefix[x] + multiplicity[i]
                       for i, x in enumerate(nums)) >= k

        nums.sort()
        W = nums[-1]

        # multiplicity[i] = number of nums[j] == nums[i] (j < i)
        multiplicity = [0] * len(nums)
        for i, x in enumerate(nums):
            if i and x == nums[i - 1]:
                multiplicity[i] = 1 + multiplicity[i - 1]

        # prefix[v] = number of values <= v
        prefix = [0] * (W + 1)
        left = 0
        for i in range(len(prefix)):
            while left < len(nums) and nums[left] == i:
                left += 1
            prefix[i] = left

        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) / 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo
