import random

def getKeys():

    primeList = open('./txt_files/primeList.txt').readlines()
    private = open('./txt_files/private.txt', 'w')
    public = open('./txt_files/public.txt', 'w')
    
    choices = random.choices(primeList, k=2)
    p = int(choices[0])
    q = int(choices[1])
    n = p*q

    y = (p-1)*(q-1)

    e = random.randint(2, y-1)

    d = pow(e, -y)

    public.write(str(d) + '\n' + str(n))
    public.close()

    private.write(str(e) + '\n' + str(n))
    private.close()

    #publicKey = {e, n}
    #privateKey = {d, n}

getKeys()