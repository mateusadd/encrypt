import base64
from cgitb import text
from email import utils
from getKeys import getKeys
import text_chunk

input = open('./txt_files/input.txt')
output = open('./txt_files/output.txt')
keyFile = open('./txt_files/public.txt')

keys = keyFile.readlines()

mod = keys[0]
key = keys[1]
text = input.readlines()

chunkSize = text_chunk.block_size(int(mod))

print(chunkSize)