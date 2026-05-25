class Solution:
    def getLetters(self, s: str) -> List[int]:
        letters = [0] * 26

        for letter in s:
            letters[ord(letter)%97] += 1


        return tuple(letters)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_hash = {

        }

        groups = []

        for string in strs:
            letters = self.getLetters(string)

            if letters in groups_hash:
                groups_hash[letters].append(string)
            else:
                new_group = [string]

                groups_hash[letters] = new_group
                groups.append(new_group)




        return groups
        