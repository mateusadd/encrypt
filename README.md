# RSA Encryption 

Este é um trabalho para a disciplina Segurança da Informação, 5ª fase do curso Engenharia de Software, da Católica SC - Joinville

Alunos: João Victor Nickler, Mateus Andrade

# Organização
Optamos por realizar a atividade na linguagem Python, por ser a que mais temos afinidade. Além dos métodos-padrão da linguagem, utilizamos o módulo base64, 
para realizar o encode da string contendo o conteúdo do arquivo.
Temos dois scripts que realizam codificação (encripta.py) e decodificação (decripta.py), além de getKeys.py, que gera as chaves pública e privada, text_chunk.py
que converte as chunks geradas a partir das strings em BigIntegers e vice versa. O usuário insere os caminhos para os arquivos contendo o conteúdo a ser tratado, 
o destino da informação criptografada ou descriptografada e o arquivo contendo as chaves a serem utilizadas

# Problemas
Tivemos alguma dificuldade na implementação dos métodos disponíveis em text_chunk, mas foi mais por falta de atenção. Após invocar os métodos da maneira correta,
tudo funcionou sem maiores problemas.

# Testes
Não fizemos nenhuma classe de testes automatizado, a validação foi feita durante o desenvolvimento. Quando algo não funcionou como esperado, trabalhamos para
corrigir qualquer erro que impedisse o funcionamento do script. A única coisa que fugiu do esperado foi no momento de testar com o arquivo dest.txt que o
professor disponibilizou, houve um erro que não conseguimos solucionar. Mas, com os outros arquivos de texto que foram testados após concluir o desenvolvimento,
tudo correu bem.

# Avaliação do projeto
Achamos muito interessante essa parte de criptografia, poder ver tudo funcionando após conhecer e trabalhar no background de todo o processo 
foi muito satisfatório. Existem também muitos outros métodos de criptografia utilizando o Python, como o módulo binascii (que foi uma das tentativas 
nesta atividade), módulos RSA para gerar chaves automaticamente, o próprio Python nativo possui um método encode() para strings. 
De uma maneira geral, foi bem proveitoso desenvolver esta atividade. 
