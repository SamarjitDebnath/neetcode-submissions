from random import randint
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def _swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def _partition(arr, low, high):
            random_index = randint(low, high)

            # push the pivot to last
            _swap(arr, random_index, high)
            pivot = arr[high]
            
            # smallest tracker
            i = low - 1

            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    _swap(arr, i , j)
            
            # put pivot to correct place
            pi = i + 1
            _swap(arr, pi, high)
            return pi

        def _quickSort(arr, low, high):
            if low < high:
                pi = _partition(arr, low, high)

                _quickSort(arr, low, pi - 1)
                _quickSort(arr, pi + 1, high)

        _quickSort(nums, 0, len(nums)-1)

        return nums
