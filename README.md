# Multiple_text-to_multiple_images_Python
Este script serve para automatizar a escrita de listas de textos em imagens. / This script is used to automate the writing of lists of texts in images.


Este script serve para automatizar a escrita de listas de textos em imagens.
As lista devem estar armazenadas em colunas em um arquivo excel. 
Ele faz a leitura da esquerda para a direita, de cima para baixo, se baseado em tuplas
sendo assim ele inicia a contagem a partir do indice "0" ( 0, 1, 2...) 
sendo a 0 então, a posição inicial da lista.

Como Funciona?
-------------------------------------------------------
Primeiro é necesssario instalar as bibliotecas:

Pandas
Pillow

Como Baixar?
_______________________________________________________

pip install Pandas
pip install Pillow

Antes de inicar atente-se a esses detalhes.

Aconselho a copiar as imagens a serem alteradas para o mesmo local onde o script python está
juntamente com as fontes .ttf e o arquivo excel com os dados.

As imagens devem ser nomeadas de acordo com a primeira coluna do arquivo.

Por exemplo:
 _____________________________
|_Coln.A_|__Coln.B_|__Coln.C_|
|__1.jpg_|__TEXT1__|__TEXT2__|
|__2.jpg_|__TEXT1__|__TEXT2__|
|__3.jpg_|__TEXT1__|__TEXT2__|
|__4.jpg_|__TEXT1__|__TEXT2__|
|__5.jpg_|__TEXT1__|__TEXT2__|
|__6.jpg_|__TEXT1__|__TEXT2__|

A coluna B contem os titulos ou textos (TEXT1) desejados que serão escritos nas imagens, 
a leitura da lista (coluna) é feita de cima pra baixo.
Podem ser inseridos quantos textos forem desejados, bastando apenas adicionar mais colunas,
como por exemplo a coluna C que contem a segunda lista (TEXT2) de texto a ser inserido na imagem.
Basta diconar mais colunas para adiconar mais listas.


#Importando as Bibliotecas

import pandas as pd
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

"""
    A linha abaixo ira fazer a leitura do arquivo excel. Header=none porque se não for especificado, ele ira omitir a primeira linha do arquivo.
    file_path esta atribuindo o caminho da imagem de acordo com os dados do arquivo
    text1 sera o texto inserido de acordo com os dados do excel. para adicionar mais textos basta adicionar por exemplo 'text2' e respectivamente
    para que o texto que foi adicionado seja escrito na imagem deve se adcionar no codigo mais uma linha:

    draw.text(xy=(20,550),text= row[2],fill=(255,255,255),font=font_type

    nesse caso adicionei a row[2] que esta de acordo com a coluna 3 ( C ) no arquivo excel e é onde estara armazenado o text2.
"""
ruta_excel = pd.read_excel("listas.xlsx", header=None, names=('file_path', 'text1', 'text2'))# Aqui serão armazenados os valores extraidos do arquivo.
for row in ruta_excel.itertuples(index=False):
    print (row) # O print ao lado ajuda a visusalizar a execução do codigo
    # row é uma tupla, então escrevendo row[0] acessa o primeiro item (a primeira coluna).
    # Se ecrever row[1] a leitura irá começar da coluna B e não da A.
    ruta=row[0]
    image_files = Image.open(ruta)  #
    font_type = ImageFont.truetype("snes.ttf", 30)# 30 é o tamanho da fonte
    draw = ImageDraw.Draw(image_files)# Parametro para escrever nas imagens. 
    # here you use row[1] and row[2]
    draw.text(xy=(140,940),text= row[1],fill=(255,255,255),font=font_type) #fill é a cor, xy são as coordenadas, altere de acordo com sua imagem
    draw.text(xy=(140,990),text= row[2],fill=(255,255,255),font=font_type)

    image_files.save(ruta, 'JPEG', quality=90) # As imagens serão salvas seguindo os parametros desejados, nesse caso em JPEG com qualidade de 90%.

_______________________________________________

Bom, espero que seja util e por favor se for usar me o devido credito, pois sou iniciante e levei semanas pesquisando detalhes para a escrita desse codigo.
Qualquer duvida estou a disposição.

Contato: teubasf.t@gmail.com LindIn: https://br.linkedin.com/in/mateus-fonseca-810559210
   
