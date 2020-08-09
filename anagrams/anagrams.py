# module used for permutations
import itertools
# the user will type a word or words  
word = input("type a word ")
x = word.lower()
# the program will split were it finds a space in the word variable
y = x.split(" ")
#variable
F = 1
permutations = []
repetidos = 1
F1 = 1
letra = [] 
letras = []
multi = 1
#the following loop will take the list (y) and will be looping through all the terms in the list
for posi in y:
    w = str(posi)
#the following loop will take the word (w) that left the list (y) and will go through all the letters of the string (w)
    for char in w:
        letra.append(char)
        #if the letter is not in the list (letras) the program will execute:
        if char not in letras:
            word = x.count(char)
            letras.append(char)
            multi *= word 
            # calculating the factorial
            while multi > 1:
                F1 *= multi
                multi -= 1 
palal = len(x)
#if the system finds space in the name, it will take the number of letters minus the number of spaces
if (" ") in x:
    espa = x.count(" ")
    palal -= espa
quantidade = palal
#factorial algorithm: as long as the number of letters in the word is greater than 1, the program will execute: 
while palal > 1:
    F *= palal
    palal -= 1
#factorial result:
result = F / F1
print(f"the number of letters in: {x} is: {quantidade}")
print(f"the number of anagrams possible with the word(s) {x} is: {result}")
print("do you wish to see all permutations? ")
resp = input()
#if the user answers "yes" to the question, the program will execute:
if resp == ("yes"):
    permut = itertools.permutations(letra)
    for per in permut:
        #if the anagram order is not in the permutations array, execute:
        if per not in permutations:
            permutations.append(per)
            print(per)
else:
    print("thank you for using this program")
stop = input("type anything to stop the program")


