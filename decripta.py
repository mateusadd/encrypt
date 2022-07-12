import text_chunk
import base64

#Entrada dos dados a serem processados
print('Please enter full path for files!')
source = input('File to be decrypted: ')
output = input('File to fill with decrypted version: ')
keyFile = input('File containing key for encryption: ')

#Abrir arquivos informados
source = open(source).readlines()
output = open(output, 'w')
keyFile = open(keyFile)

keys = keyFile.readlines()

mod = int(keys[0])
key = int(keys[1])

#string a ser preenchida com todo o conteúdo descriptografado
fullText = ''

#Ler arquivo criptografado
for line in source:
    #calcular
    originalChunk = pow(int(line), key, mod)
    #Traduzir BigInt para string
    chunk = text_chunk._int_to_str(originalChunk)
    #Formar a string com conteúdo descriptografado
    fullText += chunk

#Transformar base64 no conteúdo original
plain = base64.b64decode(bytes(fullText.encode())).decode()
    
#Escrever versão descriptografada no arquivo de saída
output.write(str(plain))