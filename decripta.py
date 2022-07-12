import text_chunk
import base64
import binascii

input = open('./txt_files/codificado.txt').readlines()
output = open('./txt_files/original.txt', 'w')

keyFile = open('./txt_files/private.txt')

keys = keyFile.readlines()

mod = int(keys[0])
key = int(keys[1])
fullText = ''

#Ler arquivo criptografado
for line in input:

    #print(line)
    originalChunk = pow(int(line), mod, key)
    binascii.unhexlify(hex(originalChunk).strip())

    


#Traduzir os inteiros


#Decodificar

#Escrever no arquivo de saída