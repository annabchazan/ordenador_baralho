cartas_usuario = []

'''Recebe as cartas do usuário e add em um array'''

i=1
while (i<=13):
    carta = input("Qual é a próxima carta do seu baralho? Caso seja uma letra, escreva de forma maiúscula") 
    cartas_usuario.append(carta)
    i=i+1
    

'''Define os valores das letras'''
a = 0
b=0
while(a<=12):
   
    if cartas_usuario[a]=="A":
          cartas_usuario[a]=1 
   
    if cartas_usuario[a]=="J":
          cartas_usuario[a]=11 
            
    if cartas_usuario[a]=="Q":
          cartas_usuario[a]=12
    
    if cartas_usuario[a]=="K":
          cartas_usuario[a]=13  
    
    else: #forma que arrumei para tornar os valores inteiros
        b=cartas_usuario[a]
        cartas_usuario[a]=b
    a=a+1



cartas_ordenadas=[]
    
c=1
d=0
while(c<=13):
    if cartas_usuario[d]==c:
         cartas_ordenadas.append(cartas_usuario[d]
         c=c+1
         d=o
    else:
         d=d+1
         d=d+1
 
print(cartas_ordenadas)
