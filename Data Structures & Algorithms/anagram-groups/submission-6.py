class Solution:
    def getOrd(self, s: str):
        order = [0 for i in range(26)]

        for string in s:
            order[ord(string)%ord("a")] += 1

        return tuple(order)

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        groups_hash = {}


        for string in strs:
            order = self.getOrd(string)

            if order in groups_hash:
                groups_hash[order].append(string)
            else:
                new_group = [string]
                groups.append(new_group)
                groups_hash[order] = new_group
        
        return groups

    


        