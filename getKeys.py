import random

def getKeys():

    primeList = open('./txt_files/primeList.txt').readlines()
    private = open('./txt_files/private.txt', 'w')
    public = open('./txt_files/public.txt', 'w')
    
    choices = random.choices(primeList, k=2)
    p = int(choices[0])
    q = int(choices[1])

    n = p*q

    print(n)

    y = (p-1)*(q-1)

    print(y)

    d = pow(3, -1, y)

    print(d)

    public.write(str(n) + '\n' + str(3))
    public.close()

    private.write(str(n) + '\n' + str(d))
    private.close()

    #publicKey = {e, n}
    #privateKey = {d, n}

getKeys()