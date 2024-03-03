# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return [w for w in word_list if sorted(w.lower()) == sorted(self.word.lower()) and w.lower() != self.word.lower()]
    
    def is_anagram(self, candidate):
        return sorted(candidate.lower()) == sorted(self.word.lower())