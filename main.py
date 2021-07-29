
from textos import binario, texts, encoder, decoder, bitshistogram, bigramshistogram, trigramshistogram, xor

def numEnt():
    correcto = False
    num = 0
    while (correcto != True):
        try:
            num = int(input("Ingrese el número de la opción que desea: "))
            correcto = True
        except ValueError:
            print("No ingreso un numero")
    return num

salir = False
opcion = 0

while (salir != True):
    print("Bienvenido al menu :")
    print("1. Texto a Binario")
    print("2. Binario a Texto")
    print("3. Texto a Base 64")
    print("4. Base 64 a Texto")
    print("5. Texto a Binario con Histograma de Bits")
    print("6. Texto a Binario con Histograma de Bigramas")
    print("7. Texto a Binario con Histograma de Trigramas")
    print("8. XOR de dos numeros")
    print("9. Salir")

    opcion = numEnt()

    if opcion == 1:
        string = input('Ingrese texto para convertir en binario: ')
        resultado = binario(string)

        print("El texto: ", string, ' en binario es: \n', resultado)

    elif opcion == 2:
        binario = input('Ingrese binario separado por espacios para convertir en texto: \n')
        binary = binario.split()
        resultado = texts(binary)

        print("El binario: \n", binario, '\nen binario es: \n', resultado)
    elif opcion == 3:

        mensaje = input('Ingrese textp para convertir a base 64: ')
        resultado = encoder(mensaje)

        print('El texto: ', mensaje, ' en base 64 es: \n', resultado)

    elif opcion == 4:
        mensaje = input('Ingrese texto en base 64 para convertir a texto regular: \n')
        resultado = decoder(mensaje)

        print('El texto en base 64: ', mensaje, ' es el siguiente string: \n', resultado)

    elif opcion == 5:
        string = input('Ingrese el texto que desea convertir a binario y mostrar la distribución de bits: \n')
        converting = binario(string)
        resultado2 = bitshistogram(converting)

    elif opcion == 6:
        string = input('Ingrese el texto que desea convertir a binario y mostrar la distribución de bigramas: \n')
        converting = binario(string)
        resultado2 = bigramshistogram(converting)

    elif opcion == 7:
        string = input('Ingrese el texto que desea convertir a binario y mostrar la distribución de trigramas: \n')
        converting = binario(string)
        resultado2 = trigramshistogram(converting)

    elif opcion == 8: 
        num1 = int(input( "Inserte el primer numero: "))
        num2 = int(input("Inserte el segundo número: "))
        res = xor(num1,num2)
        print("El resultado del XOR de los numeros ingresados es: " + res)
    else:
        print("ingrese una opción válida")



