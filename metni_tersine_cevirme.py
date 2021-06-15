def cevir(text,number=[]):
    for i in range(len(text)-1,-1,-1):
        number.append(text[i])
    return "".join(number)

sentence=input("Please write a sentence: ")
print("reversed sentence: {} ".format(cevir(sentence)))