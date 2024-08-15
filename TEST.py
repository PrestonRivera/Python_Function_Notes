import json

class Trie:


    def find_matches(self, document):
        word_matches = set()
        
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                char = document[j]
                if char not in level:
                    break
                level = level[char]
                if self.end_symbol in level:
                    word_matches.add(document[i:j+1])
        return word_matches
    
    
    def exists(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            elif letter in current:
                current = current[letter]
        if self.end_symbol in current:
            return True
        return False


    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True


    def words_with_prefix(self, prefix):
        words_list = []
        current = self.root
        for letter in prefix:
            if letter not in current:
                return []
            else:
                current = current[letter]
        return self.search_level(current, prefix, words_list)
    

    def search_level(self, cur, cur_prefix, words):
        if self.end_symbol in cur:
            words.append(cur_prefix)
        current_keys = sorted(cur.keys())
        for key in current_keys:
            if key != self.end_symbol:
                self.search_level(cur[key], cur_prefix + key, words)
        return words
    

    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        
        while True:
            if current != None:
                children = current.keys()
                if self.end_symbol in current:
                    break
                if len(children) == 1:
                    prefix += list(children)[0]
                child_key = list(children)[0]
                current = current[child_key]
                if len(children) > 1 or len(children) == None:
                    break
        return prefix

    
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"


trie = Trie()

words = ["apple", "appetizer", "apricot", "anything", "anywhere", "always", "everything", "everyday"]
for word in words:
    trie.add(word)
print(json.dumps(trie.root, indent=2))






