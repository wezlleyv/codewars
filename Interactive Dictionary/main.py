class Dictionary():
    def __init__(self):
        self.dic = {}
        
    def newentry(self, word, definition):
        self.dic.update({word: definition})
        
    def look(self, key):
        return self.dic.get(key, f"Can't find entry for {key}")
        