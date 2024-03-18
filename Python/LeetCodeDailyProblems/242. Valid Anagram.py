'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 '''
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=list(s)
        t_list=list(t)
        if len(s_list)== len(t_list):
            for letter in s_list:
                for index in range(len(t_list)):
                    if letter in t_list:
                        t_list.remove(letter)
                    break
            if t_list ==[]:
                return True
        return False
    def isAnagramSorted(self, s: str, t: str) -> bool:

        s_list_sorted= sorted(s)
        t_list_sorted= sorted(t)
        if s_list_sorted == t_list_sorted:
            return True
        return False
    def isAnagramSorted2(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)




if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagramSorted2(s, t))