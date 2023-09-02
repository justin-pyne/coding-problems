from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        notes:
            two lists:
            stack = []
            solution = [0] * len(temperatures) #init each index w 0 as default length to higher temp day

            for i, temp in enumerate   (temperatures):
                while stack and temp > stack[-1][0]:
                

                stack.append((t, i))

            example 1:
            append (73, 0)
            pop (73, 0) since 74>73
            sol[0] = 1-0
            append (74,1)

            for (75,2)
            pop(74,1)
            sol[1] = 2-1
            append(75,2)

            for(71,3)
            append(71,3) #stack is [(75,2), (71,3)]

            for(69,4)
            append(69,4) #stack is [(75,2), (71,3), (69,4)]

            for (72,5)
            pop (69,4)
            sol[4] = 5-4 = 1

            pop (71,3)
            sol[3] = 5-3 = 2

            stack is currently: [(75,2)]

            for (72, 6)
            append
        """
        stack = []
        sol = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackI = stack.pop()
                sol[stackI] = i - stackI

            stack.append((temp, i))
        
        return sol

