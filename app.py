""" name = "Nelson" #strings represent names, word, etc
age = 15 #integers for WHOLE nums
graduated = False #boolean = true/false , typically ysed for evaluations
tall = True
money = 10000.15 #floats for decimals14

bill = float(input("how bill"))
total = 15 + float(bill)
print(total) """

""" def wordsinsentence(sentence):
    words = sentence.split()
    wordcount = 0
    for i in words:
        wordcount += 1
    return wordcount



sentence = input("state your words")
print ("Number of words in sentence: ", wordsinsentence(sentence) ) """






def amt_words(input_sentence):
    words = 0
    for i in input_sentence.split():
        words += 1
    return words

input_sentence = input("sentence pls: ")
print("so ur word count is...........: ", input_sentence)











""" 

def idklikewhat(sentence):
    word_count = 0
    for words in sentence.split():
        word_count += 1
    return word_count

sentence = input("any sentence: ")
print ("words = ", idklikewhat(sentence))
    
 """





