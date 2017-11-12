import pprint
import array

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        max_indices = (0,0)
        size = len(s)
        dp = [[0] * size for i in range(size)]
        dp = set()
        for diff in range(size):
            for i in range(size - diff):
                if diff == 0:
                    dp.add((i, i+diff))
                elif diff == 1 and s[i] == s[i+diff]:
                    dp.add((i, i + diff))
                    max_indices = (i, i + diff)
                else:
                    if (i+1,i+diff-1) in dp and s[i] == s[i+diff]:
                        dp.add((i, i + diff))
                        max_indices = (i, i+diff)
        # pprint.pprint(dp)
        return s[max_indices[0]:max_indices[1]+1]

if __name__ == '__main__':
    test = Solution()
    print(test.longestPalindrome("babad"))
    print(test.longestPalindrome("cbbd"))
    print(test.longestPalindrome("abcda"))
    print(test.longestPalindrome("lcnvoknqgejxbfhijmxglisfzjwbtvhod"
                                 "wummdqeggzfczmetrdnoetmcydwddmtub"
                                 "cqmdjwnpzdqcdhplxtezctvgnpobnnscr"
                                 "meqkwgiedhzsvskrxwfyklynkplbgefjb"
                                 "yhlgmkkfpwngdkvwmbdskvagkcfsidrdg"
                                 "wgmnqjtdbtltzwxaokrvbxqqqhljszmef"
                                 "syewwggylpugmdmemvcnlugipqdjnriyt"
                                 "hsanfdxpvbatsnatmlusspqizgknabhnq"
                                 "ayeuzflkuysqyhfxojhfponsndytvjpbz"
                                 "lbfzjhmwoxcbwvhnvnzwmkhjxvuszgtqh"
                                 "ctbqsxnasnhrusodeqmzrlcsrafghbqjp"
                                 "yklaaqximcjmpsxpzbyxqvpexytrhwhmr"
                                 "kuybtvqhwxdqhsnbecpfiudaqpzsvfayw"
                                 "vkhargputojdxonvlprzwvrjlmvqmrlft"
                                 "zbytqdusgeupuofhgonqoyffhmartpcbg"
                                 "ybshllnjaapaixdbbljvjomdrrgfeqhwf"
                                 "fcknmcqbhvulwiwmsxntropqzefwboozp"
                                 "hjectnudtvzzlcmeruszqxvjgikcpfcln"
                                 "rayokxsqxpicfkvaerljmxchwcmxhtbwi"
                                 "tsexfqowsflgzzeynuzhtzdaixhjtniel"
                                 "bablmckqzcccalpuyahwowqpcskjencok"
                                 "prybrpmpdnswslpunohafvminfolekdle"
                                 "usuaeiatdqsoatputmymqvxjqpikumgmx"
                                 "axidlrlfmrhpkzmnxjtvdnopcgsiedvtf"
                                 "kltvplfcfflmwyqffktsmpezbxlnjegdl"
                                 "rcubwqvhxdammpkwkycrqtegepyxtohsp"
                                 "easrdtinjhbesilsvffnzznltsspjwuog"
                                 "dyzvanalohmzrywdwqqcukjceothydlgtocukc"))