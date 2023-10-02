class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        goal = Counter(s1)
        window_count = Counter()

        left, right = 0, 0

        while right < len(s2):
            char = s2[right]
            window_count[char] += 1


            # handle window if larger than len(s1), -1 to left element count, remove empty
            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                left += 1

            # check completion
            if window_count == goal:
                return True

            right += 1

        return False