import os
import random


def read():
    a = []
    
    with open("./data.txt", 'r',encoding="utf-8") as f:
        for line in f:
           
            a.append(line.replace('\n',""))
            a[-1] = a[-1].replace('á','a')
            a[-1] = a[-1].replace('é','e')
            a[-1] = a[-1].replace('í','i')
            a[-1] = a[-1].replace('ó','o')
            a[-1] = a[-1].replace('ú','u')
    return a
    #for i in listas:
#        print(i)


    #for i in letra_elegida:
#        letra_e.append(i)


def run():
    os.system("clear")
    print('----------JUEGO ADIVINA LA PALABRA ----------\n')
    listas = read()
  
    letra_elegida= str.upper(random.choice(listas))
    letra_e = [i for i in letra_elegida]  
    letra_oculta =["__" for i in letra_e]
    num_letras= len(letra_e)
    intentos = 12
    
    
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
        print('----------JUEGO ADIVINA LA PALABRA ----------\n')
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