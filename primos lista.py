limite = int(input("ingrese el limite: "))
primos = [1,2,3]
numero = primos[-1]

while numero < limite:
    numero +=1
    verificador = 0
    for i in range(1, numero + 1):
        if i ==1 or i == numero :
            continue
        if numero % i == 0:
            verificador += 1
    if verificador == 0:
       #  print('primo encontrado')
         primos.append(numero)
  
print(primos)
