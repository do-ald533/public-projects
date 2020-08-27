#module used:
import math 
#whole expression
def delta():
    global result
    result = (numb[1] ** 2) - (4 * numb[0] * numb[2])
    if result >= 0:
        print(f"it is possible to continue the calculation because ({result}) is greater than -1")
    else:
        print("it's not possible to continue the calculation because the expression:(b² - 4 . a . c) is a negative number")
def positivo():
    RaizPositiva = (-numb[1] + (math.sqrt(result))) / (2 * numb[0])
    print(f"the first root of the expression is: {RaizPositiva} ")
def negativo():
    RaizNegativa = (-numb[1] - (math.sqrt(result))) / (2 * numb[0])
    print(f"the second root of the expression is: {RaizNegativa}")
#incomplete expression (ax² + c)
def resolução():
    if (num[1]) >= 1:
        print("it's not possible to continue, because the number assing to the letter 'C' wasn't a negative number, and there for it can't preforme a square root operation")
    else: 
        resultado = math.sqrt(-num[1] / num[0])
        if resultado < 0:
            print("it's not possible to continue the execution because the root of the expression is less than 0 (x < 0)")
        else:
            print(f"the expression: {letras[0]}x² + {letras[1]} is equal to: {resultado}")
# incomplete expression (ax² + bx)
def resolução1():
    print("the first root of the expression is 0")
    result = (-num2[1] / num2[0])
    if result < 0:
        print("the second root of the expression can't be shown because it is a number less than 0")
    else:
        print(f"the second root of the expression is: {result}")
#start of the program
numb = []
#if the user decides to calculate a complete quadratic expression, it will execute:
resp = input("what kind quadratic operation is it? (incomplete / complete): ")
if resp == ("complete"):
    expression = input("type the values of the expression (ax² + bx + c = 0): ")
#this section creates a lsit called expression by spliting the numbers in the string above(expression) 
    expression = expression.split(' ')
    for i in (expression):
        numb.append(int(i))
    print(f"the expression will be: ({numb[0]})x² + ({numb[1]})x +({numb[2]})=0 ")
    result = 0
    #calling function delta to calculate the square root of the quadratic expression
    delta()
    #if the user wishes to continue the program, it will execute:
    resp = input("do you wish to continue the execution of the expression? ")
    if resp  == ("yes" or "Yes"):
        positivo()
        negativo()
    else:
        print("thank you very much, i hope you enjoyed")
#if the user decides to calculate a incomplete quadratic expression, it will execute:
elif resp == "incomplete":
    print("in the expression(ax² + bx + c=0) which letter is equal to 0? (b/c) ")
    resp2 = input()
    #if the expression the user wishes to calculate a quadratic expression where the B is null it will execute:
    if resp2 == ("b" or "B"):
        letras = ['A','C']
        num = []
        for i in letras:
            num.append(int(input(f"type the number that the letter '{i}' will be equal to in the expression (Ax² + C = 0): ")))
        resolução()
#if the expression the user wishes to calculate a quadratic expression where the C is null it will execute:
    if resp2 == ("c" or "C"):
        num2 = []
        letra = ['A','B']
        for i in letra:
            num2.append(int(input(f"type the number that will be equal to the letter '{i}' in the expression (Ax² + Bx=0): ")))
        resolução1()   
print("thank you for using my program")    
stop = input("click enter to stop the execution")
