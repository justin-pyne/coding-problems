from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        if 1 car -> 1 fleet base case

        - keep track of maximum time

        order = create list of tuples with (position, speed)
            can achieve this by zipping position list and speed list together
        sort by position -> order.sort(reverse = True)

        methodology to determine if fleet is formed:
            pass
            calculate time to target:
            (target - position)/speed and directly push to stack (stack keeps track of current max time)
            as we iterate from front position to back:
                if time is less than the time b4 it then fleet will be formed -> pop that time from the stack (as its in an existing fleet)

        """

        stack = []
        pair = [(p,s) for p,s in zip(position, speed)]

        pair.sort(reverse=True)

        for p,s in pair:
            time = (target-p)/s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)