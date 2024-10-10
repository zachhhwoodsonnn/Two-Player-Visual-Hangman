class Hangman:
    
    def easy_list(self):
        easy_list = []
        with open('easy.txt', 'r') as words:
            for word in words:
                easy_list.append(word.strip())  # Strip newline characters from words
            
        return easy_list                        # Return the list of words
    
    def medium_list(self):
        medium_list = []
        with open('medium.txt', 'r') as words:
            for word in words:
                medium_list.append(word.strip())  # Strip newline characters from words
            
        return medium_list                        # Return the list of words
        
    def hard_list(self):
        hard_list = []
        with open('hard.txt', 'r') as words:
            for word in words:
                hard_list.append(word.strip())  # Strip newline characters from words
            
        return hard_list                        # Return the list of words
    
    def place_holder(self, word):
        place_holder = ""
        for char in word:
            place_holder += "_ "
        return place_holder
    
    def stages(self, lives):
        stages = ['''
                  +---+
                  |   |
                  O   |
                 /|\  |
                 / \  |
                      |
                =========
                ''', '''
                  +---+
                  |   |
                  O   |
                 /|\  |
                 /    |
                      |
                =========
                ''', '''
                  +---+
                  |   |
                  O   |
                 /|\  |
                      |
                      |
                =========
                ''', '''
                  +---+
                  |   |
                  O   |
                 /|   |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                  |   |
                      |
                      |
                =========
                ''', '''
                  +---+
                  |   |
                  O   |
                      |
                      |
                      |
                =========
                ''', '''
                  +---+
                  |   |
                      |
                      |
                      |
                      |
                =========
                ''']
        return stages[lives]
