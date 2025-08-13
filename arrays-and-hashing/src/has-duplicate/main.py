from typing import List

class HasDuplicate:
# Given an integer array nums, return true if any value 
# appears at least twice in the array, and return false if every element is distinct.



    def hasDuplicateBrute(self, nums: List[int]) -> bool:
        # nested for loop comparisons
        for x in range(len(nums)):
            #start inner loop at x+1 to avoid self-comparison
            for y in range(x+1, len(nums)):
                if nums[x] == nums[y]:
                    return True
        return False
# Time Complexity :
#   first loop runs n comparisons from 0 to n-1 (n=len of nums)
#   second loop runs from x+1 to n-1
#   for each x, the second loop runs (n-x-1) times
#   total number of comparisons is n(n-1)/2 for nested for loop pair comparison
#   In Big O notation, we drop constants and lower-order terms
#   n(n-1)/2 = (n^2-n)/2 simplifies to O(n^2)
#   
# Space Complexity:
#   only uses a constant amount of space for the loop variables
#   O(1)



    def hasDuplicateSorting(self, nums: List[int]) -> bool:
        # sort it first, any duplicates will then be beside each other
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
# Time Complexity:
#   this one is O(n log n) because efficient algos use Divide and Conquer:
#   [split array repeatedly into smaller parts (log n splits)
#   and then process all n elements in each split]

#   then a simple for loop is O(n)
#   Dominant term is O(n log n)

# Space Complexity:
#   constant O(1) because it is a sort in-place (Timsort, which is mergesort and insertion sort hybrid)
#   [merge-sort would be O(n) as it stores temporary arrays during the sort]
#   only the loop variables are needed to store



    def hasDuplicateHash(self, nums: List[int]) -> bool:
        # use a set to keep track of elements already seen
        # iterate through each num. if already in set, return True
        # otherwise, add it to the seen set
        seen = set()
        for num in nums:
                if num in seen:
                    return True
                seen.add(num)
        return False
# Time Complexity:
#   O(n) as each lookup and insert is O(1) and there is n elements
#   this is a quick comparison, much quicker than brute force looping for loops
# Space Complexity:
#   worst case O(n) if all elements are unique and thus get stored in the set
  


    def hasDuplicateHashLength(self, nums: List[int]) -> bool:
        # converts list to a set, because a set automatically removes duplicates
        # if the set and list are different lengths, there must have been a duplicate
        return len(set(nums)) < len(nums)
# Time Complexity:
#   takes O(n) to build the set because you must process each element in the list once
#   perform a hash and insert for each element [each of these are O(1)]
#   so for n elements with O(1), its O(n)
# Space Complexity:
#   takes O(n) to store the n elements of the set

  

nums = [1,2,3,4,8,3]
hasDuplicate = HasDuplicate()
print("Brute Force method: " + str(hasDuplicate.hasDuplicateBrute(nums)))
print("Sort method: " + str(hasDuplicate.hasDuplicateSorting(nums)))
print("Hash method: " + str(hasDuplicate.hasDuplicateHash(nums)))
print("Hash Length method: " + str(hasDuplicate.hasDuplicateHashLength(nums)))