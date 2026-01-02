class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        """
        Find the element that appears N times in an array of size 2N.
      
        Since there are 2N elements total and one element appears N times,
        the other N elements must be unique. Therefore, the first duplicate
        we encounter must be the element that appears N times.
      
        Args:
            nums: List of integers containing 2N elements
          
        Returns:
            The element that appears N times
        """
        # Set to track elements we've already seen
        seen_elements = set()
      
        # Iterate through each element in the array
        for num in nums:
            # If we've seen this element before, it must be the one repeated N times
            if num in seen_elements:
                return num
          
            # Add the current element to our set of seen elements
            seen_elements.add(num)