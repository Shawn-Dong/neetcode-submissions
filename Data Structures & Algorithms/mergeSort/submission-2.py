# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        mid = len(pairs)//2
        left_half = []
        right_half = []
        i = 0
        while i<mid:
            left_half.append(pairs[i])
            i+=1
        while i<len(pairs):
            right_half.append(pairs[i])
            i+=1
        
        sorted_left = self.mergeSort(left_half)
        sorted_right = self.mergeSort(right_half)
        
        return self.merge(sorted_left,sorted_right)
    
    def merge(self, left:List[Pair], right: List[Pair]) -> List[Pair]:
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
                result.append(left[i])
                i+=1
        while j < len(right):
                result.append(right[j])
                j+=1
        return result


