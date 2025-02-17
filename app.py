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




"""

do_you_like_poop = input('do u like poop ')
if do_you_like_poop == 'yes':
    print("tyty")
else:
    print("what's wrong with you? ")
 """



""" 

#input w/ if, else, elif

whatstemp = input("whats the fahreneheit rn: ")
whatstemp = float(whatstemp)
if whatstemp > 68:
    print("warm")
elif whatstemp == 68:
    print("lol")
else:
    print("cold")  """
""" 
#even odd num challenge

def anynumber(number):
    number = int(number)
    if number % 2 == 0:
        return("even")
    else:
        return("odd")
    
number = input("state your number: ")
print(f"your number is: {anynumber(number)}") """
""" 
def how_was_it(service):
    tip = 0
    if service == "bad":
        return(tip + 5)
    elif service == "okay":
        return(tip + 15)
    elif service == "good":
        return(tip + 20)
    else:
        if service == "great":
            return(tip + 25)

service = input("how was your service? ")
print(f"ok, your tip % is {how_was_it(service)}%")
 """
""" def factors_of_number(number):
    number = int(number)  # Convert input to integer
    factors = ""  # Start with an empty string to store factors
    for dividable in range(1, number + 1):  # Loop through numbers from 1 to number
        if number % dividable == 0:  # Check if i is a factor
            factors += str(dividable) + " "  # Add factor to the string with space
    return factors.strip()  # Remove trailing space and return the string

# Ask for user input
number = input("Enter a number: ")
print(f"The factors of {number} are: {factors_of_number(number)}")
 """








""" def hi(number):
    number = int(number)
    factors = []
    for dividing in range(1, number + 1):
        if number % dividing == 0:
            factors += [dividing]
    return factors
    
number = input("state number: ")
print(f"{number} has the factors {hi(number)}") """












""" 
#factors challenge

def factor(number):
    factors = []
    for num in range(1, number + 1): #why _ 1? cuz inclusive. if want 17 it would read as 16
        if number % num == 0:
            factors.append(num)
    return factors

print(factor(0))

 """


#BILL CALCULATOR

""" def calcofbill():
    bill = float(input("what's your bill? "))
    tip = 0
    total = 0
    service = input("how was your meal? ")
    if service == "bad":
        tip = bill * 0
    if service == "okay":
        tip = bill * 0.15
    elif service == "good":
        tip = bill * 0.2
    elif service == "great":
        tip = bill * 0.25
    total = bill + tip
    print(f"Your bill is: {total}")
calcofbill()
 """


















#FACTORS PROJECT

""" def factors(number):
    factors = []
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            factors.append(divisor)
    print(f"The factors are: {factors}")
factors(100000) """
#GCF PROJECT
""" def gcf(x,y):
    if x > y:
        lowest = y
    else:
        lowest = x
    for any in range(1, lowest + 1):
        if x % any == 0 and y % any == 0:
            gcf = any
    print(f"GCF is: {gcf}")
gcf(100,200) """






#ODD EVEN PROJECT

"""

def anynumber(number):
    number = int(number)
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
anynumber(2) """





#madlibs

def madlibs():
    verb1 = input("state a verb ")
    verb2 = input("state your other verb ")
    noun = input("state a noun ")
    food = input("state a food ")
    number = input("state a number ")
    celeb = input("state your celeb ")
    madlibs = (f"you were late, so you {verb1} to class, but suddenly, {celeb} appeared! Everyone started {verb2} in to a {noun} because of this, and they started eating {number} {food}(s)")
    print(madlibs)
madlibs()

#wordcount challenge

""" def userinput():
    sentence = (input("state a sentence "))
    wordcount = 0
    for i in sentence.split():
        wordcount = wordcount + 1
    print(f"your wordcount is {wordcount}")
userinput()
     """