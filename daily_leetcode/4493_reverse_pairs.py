class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        out = 0
        def mergeSort(left, right):
            if left >= right: return
            mid = (right + left) // 2
            mergeSort(left, mid)
            mergeSort(mid+1, right)
            merge(left, mid, right)

        def merge(left, mid, right):
            nonlocal out
            # count
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > nums[j] * 2:
                    j += 1
                out += j - mid - 1

            # regular merge sort!
            res = []
            i = left
            j = mid + 1
            while i <= mid and j <= right:
                if nums[i] < nums[j]:
                    res.append(nums[i])
                    i += 1
                else:
                    res.append(nums[j])
                    j += 1
            while i <= mid:
                res.append(nums[i])
                i += 1
            while j <= right:
                res.append(nums[j])
                j += 1
            nums[left: right+1] = res

        mergeSort(0, len(nums) - 1)
        return out