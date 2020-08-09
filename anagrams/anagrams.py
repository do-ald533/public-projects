# modulo utilizado para permutações
import itertools
# o usuario ira colocar a palavra, o programa executara: 
word = input("digite uma palavra: ")
x = word.lower()
# o programa ira seprar o nome onde tiver espaço
y = x.split(" ")
#variaveis
F = 1
permutations = []
repetidos = 1
F1 = 1
letra = [] 
letras = []
multi = 1
#o loop a seguir irá pegar a lista(y) e ira ficar fazendo loop em todos os termos da lista
for posi in y:
    w = str(posi)
    #o loop a seguir irá pegar a palavra(w) que saiu da lista (y) e ira passar por todas as letras da string(w)
    for char in w:
        letra.append(char)
        #se a letra não estiver na lista(letras) o programa executara:
        if char not in letras:
            word = x.count(char)
            letras.append(char)
            multi *= word 
            #algoritmo de fatorial: 
            while multi > 1:
                F1 *= multi
                multi -= 1 
palal = len(x)
#se o sistema encontrar espaço no nome, ele ira pegar o numero de letras menos o numero de espaços
if (" ") in x:
    espa = x.count(" ")
    palal -= espa
quantidade = palal
#algoritmo de fatorial: enquanto o numero de letras na palavra for maior que 1, o programa ira executar: 
while palal > 1:
    F *= palal
    palal -= 1
#resultado do fatorial:
result = F / F1
print(f"o numero de caracteres em: {x} é igual a {quantidade}")
print(f"o numero de anagramas possiveis com a(s) palavra(s) {x} é igual a {result}")
print("deseja executar todas as possibilidades de anagramas?")
resp = input()
#se o usuario responder "sim" a pergunta, o programa ira executar:
if resp == ("sim"):
    permut = itertools.permutations(letra)
    for per in permut:
        #se a ordem do anagrama não esta no array permutations, executara:
        if per not in permutations:
            permutations.append(per)
            print(per)
stop = input("digite qualquer coisa para terminar a execução")


