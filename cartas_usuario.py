cartas_usuario = []

'''Recebe as cartas do usuário e add em um array'''
N_CARTAS = 13

for i in range(N_CARTAS):
    carta = input("Qual é a próxima carta do seu baralho? Caso seja uma letra, escreva de forma maiúscula") 
    
    
    ''' Muda letras para numeros '''
    if carta=="A":
          carta=1 
   
    elif carta=="J":
          carta=11 
            
    elif carta=="Q":
          carta=12
    
    elif carta=="K":
          carta=13  
    
    cartas_usuario.append(int(carta))
    


'''Ordena os numeros'''
cartas_ordenadas=[]
    
c=1
d=0
while(c<=13):
   
    if cartas_usuario[d]==c:
         cartas_ordenadas.append(cartas_usuario[d])
         c=c+1
         d=0
         
    elif d < len(cartas_usuario) -1:
         d=d+1
         
    else:
        d=0
        c=c+1
        

''' Muda os numeros de volta pra letras '''
for i in range(len(cartas_ordenadas)):
    
    if cartas_ordenadas[i]==1:
          cartas_ordenadas[i]='A'
   
    elif cartas_ordenadas[i]== 11:
          cartas_ordenadas[i]='J'
            
    elif cartas_ordenadas[i]==12:
          cartas_ordenadas[i]="Q"
    
    elif cartas_ordenadas[i]==13:
          cartas_ordenadas[i]="K"
            
#exibe as cartas ordenadas
print('\n', cartas_ordenadas)
