from typing import List

arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]
def intersection(nums1: List[float], nums2: List[float]) -> List[float]:
        return list(set(nums1) & set(nums2))
print(intersection(arr1,arr2))