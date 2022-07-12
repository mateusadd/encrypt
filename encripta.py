import base64
import text_chunk

#Entrada dos dados a serem processados
print('Please enter full path for files!')
source = input('File to be encrypted: ')
output = input('File to fill with encrypted version: ')
keyFile = input('File containing key for encryption: ')

#Abrir arquivos informados
source = open(source)
output = open(output, 'w')
keyFile = open(keyFile)

keys = keyFile.readlines()

#Módulo e chave pública
mod = int(keys[0])
key = int(keys[1])

#Formar uma string única com o conteúdo do arquivo de entrada
text = source.readlines()
strText = ''

for line in text:
    strText += line

print('String to be encrypted: '+strText)

#Definir chunkSize a partir do módulo
chunkSize = text_chunk.block_size(mod)
print('Defined a ' + str(chunkSize) +' chunkSize')

#Gerar versão codificada da string
encoded = base64.b64encode(bytes(strText.encode())).decode()

#Dividir a versão codificada em chunks com o tamanho definido
chunks = [encoded[i:i+chunkSize] for i in range(0, len(encoded), chunkSize)]
print(chunks)

#Transformar cada chunk em BigInt e gerar versão codificada
for chunk in chunks:
    
    #Gerar BigInt
    originalChunk = text_chunk.TextChunk(chunk).int_value()

    #Calcular
    encodedChunk = pow(originalChunk, key, mod)
    
    #Escrever versão codificada no arquivo de saída
    output.write(str(encodedChunk)+'\n')