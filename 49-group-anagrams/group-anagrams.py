class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            # Sort the string to use as a key
            key = ''.join(sorted(s))
            if key not in anagrams:
                anagrams[key] = [s]
            else:
                anagrams[key].append(s)
        return list(anagrams.values())