import os
import random

listas = []
letra_e = []
letra_oculta =[]
letra_elegida= ''

def read():
    
    with open("./data.txt", 'r',encoding="utf-8") as f:
        for line in f:
            listas.append(line[0:-1])
    
    #for i in listas:
#        print(i)

def letra_random(num):
    pass
    
    #for i in letra_elegida:
#        letra_e.append(i)
#    
            
    print(letra_e)

def run():
    os.system("clear")
    print('----------JUEGO ADIVINA LA PALABRA ----------')
    read()
    #letra_random()
    letra_elegida= str.upper(random.choice(listas))
    letra_e = [i for i in letra_elegida]  
    letra_oculta =["_ " for i in letra_e if i !=""]
    num_letras= 0
    intentos = 12
    limite=0
    for i in letra_e:
        num_letras += 1
    
    #print(letra_e)  
    print(str(num_letras)+ " letras ocultas")
    print(*letra_oculta)
    print("\n")
    
    
    
    while num_letras>0:
        a = str.upper(input("ingrese  una letra : "))
        posicion = -1
        aux= []
        for i in letra_e:
            posicion += 1
            if str(i) == str(a):
                aux.append(posicion)
                letra_oculta[posicion] = a
                letra_e[posicion] = '_'
                num_letras -= 1
        if aux==[]:
           intentos -=1
       
        
       
           
                          
        os.system("clear")
        print('----------JUEGO ADIVINA LA PALABRA ----------')
        print("ingresaste la letra : " + a)
        print(intentos)
        print("\n"+str(num_letras)+ " letras ocultas \n")                 
        
        print(*letra_oculta)
        print('\n')
        print(aux)  
    print('ganasteee !!!\n')
    new = input("escribe 'SI' para volver a jugar : ")
    if new == 'si':
        run()
    #letra_random(num_letras)
    
if __name__ == '__main__':
    run()