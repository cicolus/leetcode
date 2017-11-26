class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        similar_words = set()
        for pair in pairs:
            similar_words.add((pair[0], pair[1]))
        for i in range(len(words1)):
            word1 = words1[i]
            word2 = words2[i]
            if not (word1 == word2 or (word1, word2) in similar_words or (word2, word1) in similar_words):
                return False

        return True