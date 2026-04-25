class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict= {}
        for i in strs:
            sorted_element = "".join(sorted(i))
            if anagram_dict.get(sorted_element):
                anagram_dict[sorted_element].append(i)
            else:
                anagram_dict[sorted_element]=[i]
        return [anagram_dict[element] for element in anagram_dict]

        