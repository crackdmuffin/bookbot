def word_count(text):
    count = len(text.split())
    return count

def letter_count(text):
    letters = text[:]
    letters = letters.lower()
    letter_dic={}
    for i in letters:
        if i not in letter_dic:
            letter_dic[i] = 1
        else:
            letter_dic[i] += 1
    return letter_dic