import math
'''
op1 = int(input("Operando "))
op2 = input("Operando ")
op3 = int(input("Operando "))

res =0

if op2 == "+" :
   res =  op1 + op3
elif op2 == "-":
   res =  op1 + op3
elif op2 == "*":
   res =  op1 * op3
elif op2 == "/":
   res =  op1 // op3

print(f"El resultado de la operacon {op1} {op2} {op3} = {res}")
'''

#Los operadores boleanos se escriben con mayusculas

#******************* ej 2************************

'''
num = int(input("Ingrese un numero : "))

if num % 2  == 0:
    print("El numero es par")
else : 
        print("El numero no es par")

'''

#******************* ej 3************************

edad = float(input("Ingrese la   edad : "))
altura =float(input("Ingrese la   altura : "))
peso =float(input("Ingrese la    peso : "))
imc = (peso /( altura **2))

if edad <45 and imc >=22.0 :
    print("Su imc es medio")

elif edad >45 and imc >=22.0 :
    print("Su imc es alto")
elif edad <45 and imc <22.0 :
    print("Su imc es bajo")
else :
     print("Su imc es medio")

