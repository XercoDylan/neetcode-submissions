class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return 1
        
        frequency = {
            s[0] : 1
        }

        most_frequent = s[0]
        l = 0

        longest = 1


        for r in range(1, len(s)):
            if s[r] in frequency:
                frequency[s[r]] += 1
            else:
                frequency[s[r]] = 1

            if frequency[s[r]] > frequency[most_frequent]:
                most_frequent = s[r]
            
            replacements_needed = (r - l + 1) - frequency[most_frequent]

            print(replacements_needed)

            if replacements_needed > k:
                frequency[s[l]] -= 1
                l += 1

            longest = max(longest, (r - l + 1))

        return longest


