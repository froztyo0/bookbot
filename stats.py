def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    words = text.split()
    dict = {}
    for word in words:
        for char in word.lower():
            if char in dict:
                dict[char]+=1
            else:
                dict[char]=1
    return dict