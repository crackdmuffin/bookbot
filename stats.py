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

def sort_on(dict):
    return dict["num"]

def report(data):
    output=[]
    for i in data:
        pair={}
        pair["char"]= i
        pair["num"]= data[i]
        output.append(pair)
    output.sort(reverse=True, key=sort_on)
    return output