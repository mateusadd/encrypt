from asyncore import write
import base64
import text_chunk
import binascii

#Ler os arquivos de entrada e chave pública
input = open('./txt_files/original.txt')
output = open('./txt_files/codificado.txt', 'w')
keyFile = open('./txt_files/public.txt')

keys = keyFile.readlines()

mod = int(keys[0])
key = int(keys[1])

#Formar uma string única com o conteúdo do arquivo de entrada
text = input.readlines()
strText = ''

for line in text:
    strText += line

print(strText)

#Definir chunkSize a partir do módulo
chunkSize = text_chunk.block_size(mod)
print('Defined a ' + str(chunkSize) +' chunkSize')

#Gerar versão codificada da string
mesBytes = strText.encode()
b64Bytes = binascii.hexlify(base64.b64encode(mesBytes))

print('Encoded full string is: '+str(b64Bytes))

#Dividir a versão codificada em chunks com o tamanho definido
chunks = [b64Bytes[i:i+chunkSize] for i in range(0, len(b64Bytes), chunkSize)]
print(chunks)

#Transformar cada chunk em BigInt e gerar versão codificada
for chunk in chunks:
    originalChunk = int(chunk, 32)
    print(originalChunk)
    encodedChunk = pow(originalChunk, key, mod)
    print(encodedChunk)
    
    #Escrever versão codificada no arquivo de saída
    output.write(str(encodedChunk)+'\n')
    