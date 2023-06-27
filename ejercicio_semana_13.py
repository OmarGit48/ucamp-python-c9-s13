# Buscar como evitar los errores de alguien que no llena correctamente lso espacios
while True:
    nombre = input('Introduce tu nombre: ')
    apellido =input('Introduce tu apellido: ')
    if nombre == '':
        print('No has introducido tu nombre')
    elif apellido == '':
        print('No has introducido tu apellido')
    else:
        break
    
while True:
    try: 
        edad = int(input('Introduce tu edad: '))
        break
    except ValueError:
        print('Debes introducir un número')
        
correo = input('Introduce tu email: ')

while True:    
    try:
        telefono = input('Introduce tu numero telefónico: ')
        int(telefono)
        break
    except ValueError:
        print('Debes introducir un numero')
        
print('Nomnbre:' + nombre)
print('Apellido:' + apellido)
print('Tengo ' + str(edad) + ' años')
print('Correo: ' + correo)
print('Teléfono: ' + telefono)