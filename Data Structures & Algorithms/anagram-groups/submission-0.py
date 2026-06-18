class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)

        for word in strs:
            sorted_s = ''.join(sorted(word))
            map[sorted_s].append(word)

        result = list(map.values())
        return result






        
        