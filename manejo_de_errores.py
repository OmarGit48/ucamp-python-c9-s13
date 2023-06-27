# numerador = 10
# denominador = 0
# cadena = '3'
# numerico = 5

# print( numerador / denominador)
# print( cadena + numerador)

# try :
#     print(numerador / denominador)
# except ZeroDivisionError:
#     print('Ha ocurrido una división entre cero')
    
# try: 
#     print( cadena + numerico)
# except TypeError:
#     print('Ha ocurrido un error de tipo')
    
# print('Fin del programa')

# try:
#     print(10/0)
# except TypeError:
#     print('Ha ocurrido un error de tipo')
# except:
#     print('Ha currido un error desconocido')
    
    
    
    
    
############################################
# Manejo de errores con exceptciones y ciclos

while True:
    try:
        dividendo = int(input('Ingrese el dividendo: '))
        divisor = int(input('Ingrese el divisro: '))
        print('El resultado es: ', dividendo / divisor)
        break
    except ValueError:
        print('Debe ingresarse un número')
    except ZeroDivisionError:
        print('No se puede dividir entre cero')
    
print('Fin del programa')
    
        
