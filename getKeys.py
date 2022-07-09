import random

def getKeys(primeList):
    
    choices = random.choices(primeList, k=2)
    p = int(choices[0])
    q = int(choices[1])
    n = p*q

    y = (p-1)*(q-1)

    e = random.randint(2, y-1)

    d = pow(e, -y)

    publicKey = {e, n}
    privateKey = {d, n}

    keysGenerated = [publicKey, privateKey]

    return keysGenerated