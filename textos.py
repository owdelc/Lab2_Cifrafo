import pandas as pd
import matplotlib.pyplot as plt
import math
import base64

def binario(texto):
    asc = []
    bnr = []

    for x in texto:
        asc.append(ord(x))

    for y in asc:
        bnr.append(int(bin(y)[2:]))

    return bnr

def texts(mensaje):
    asc = []
    texto = ""
    for x in mensaje:
        x = int(x)
        a = 0
        b = 0
        c = int(math.log10(x))+1
        for y in range(c):
            a = ((x%10)*(2**y))
            x = x//10
            b = b + a
        asc.append(b)
    for x in asc:
        texto = texto + chr(x)
    return texto




def encoder(mensaje):
    bytes = mensaje.encode('ascii')
    bytes2 = base64.b64encode(bytes)
    message = bytes2.decode('ascii')

    return message

def decoder(mensaje):
    bytes = mensaje.encode('ascii')
    bytes2 = base64.b64decode(bytes)
    message = bytes2.decode('ascii')

    return message

def bitshistogram(mensaje):
    strint = [str(int) for int in mensaje]

    data = "".join(strint)

    n = 1

    newdata = [data[i:i+n] for i in range(0, len(data), n)]

    bits = list(newdata)

    dataframe = pd.DataFrame({'chars': bits})
    dataframe['num'] = 1
    dataframe = dataframe.groupby('chars').sum().sort_values('num', ascending=False) / len(dataframe)

    plt.bar(dataframe.index, dataframe.num, width=0.5, color='g')
    plt.show()

def bigramshistogram(mensaje):
    strint = [str(int) for int in mensaje]

    data = "".join(strint)

    n = 2

    newdata = [data[i:i+n] for i in range(0, len(data), n)]

    bits = list(newdata)
    
    dataframe = pd.DataFrame({'chars': bits})
    dataframe['num'] = 1
    dataframe = dataframe.groupby('chars').sum().sort_values('num', ascending=False) / len(dataframe)

    plt.bar(dataframe.index, dataframe.num, width=0.5, color='g')
    plt.show()

def trigramshistogram(mensaje):
    strint = [str(int) for int in mensaje]

    data = "".join(strint)

    n = 3

    newdata = [data[i:i+n] for i in range(0, len(data), n)]

    bits = list(newdata)
    
    dataframe = pd.DataFrame({'chars': bits})
    dataframe['num'] = 1
    dataframe = dataframe.groupby('chars').sum().sort_values('num', ascending=False) / len(dataframe)

    plt.bar(dataframe.index, dataframe.num, width=0.5, color='g')
    plt.show()