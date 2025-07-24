from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the list to use two-pointer strategy
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:
            # If the lightest and heaviest person can share a boat
            if people[left] + people[right] <= limit:
                left += 1  # move to next lightest
            right -= 1     # heaviest person always goes
            boats += 1     # one boat used

        return boats
