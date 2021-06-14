#function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed

def spin_words(sentence):
    sentence = sentence.split()
    k = 0
    for item in sentence:
        if len(item) > 4:
            n = len(item) - 1
            #python string cant be mutated so we turn the string into a list to iterate 
            item = list(item)
            for i in range(0, n-1):
                if i <= n-1:
                    #swapping
                    item[i], item[n] = item[n], item[i]
                else:
                    break
                n -= 1
            #joining the list back into a string and appending the original list(string)
            item = "".join(item)
            sentence[k] = item
        k += 1
    q = " ".join(sentence)
    return q

