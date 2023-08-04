def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    for i in spam_words:
        if space_around == False:
            if i in text:
                return True
            else:
                return False
        elif space_around == True:
            if text.find(f' {i}') != -1 or text.find(i) == 0 and text.rfind('f{i}.') != -1 or text.rfind('f{i} ') != -1:
                return  True
            else:
                return False
    
        

print(is_spam_words("Молох", ["лох"]))
print(is_spam_words("Молох", ["лох"], True))  # False
print(is_spam_words("Ты лох bgb.", ["лох"]))  # True
print(is_spam_words("Ты лох.", ["лох"], True))  # True
