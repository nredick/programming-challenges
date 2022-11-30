from typing import List


class Solution:
    # iterative sol
    # O(n+m) time, O(1) space: no extra space allotted, only iterating nums1 once
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # indexers for nums1 and nums2
        i, j = m-1, n-1

        # iter over nums1 backwards
        for pointer in range(len(nums1)-1, -1, -1):
            if j < 0: # if nums2 is empty, break w/o changing nums1
                break
            if i > -1 and nums1[i] > nums2[j]: # nums1 !empty & nums1[i] > nums2[j]
                nums1[pointer] = nums1[i] # set nums1[pointer] to nums1[i]
                i -= 1 # decrement i indexer for nums1
            else:
                nums1[pointer] = nums2[j] # set nums1[pointer] to nums2[j]
                j -= 1 # decrement j indexer for nums2


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    s.merge(nums1, 3, nums2, 3)
    print(nums1)

    nums1 = [0]
    nums2 = [1]
    s.merge(nums1, 0, nums2, 1)
    print(nums1)

    nums1 = [1]
    nums2 = []
    s.merge(nums1, 1, nums2, 0)
    print(nums1)

    nums1 = [2, 0]
    nums2 = [1]
    s.merge(nums1, 1, nums2, 1)
    print(nums1)
