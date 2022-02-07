import pandas as pd
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from time import sleep

print('-=-' *30)
print('Script para automatização de escrita de texto sobre imagens.')
sleep(1)
print(' v 1.0 Codado Por Mateus Rodrigues 2022 ')
print('-=-' *30)
sleep(1)
print('Executando o script...')
sleep(1)
print('AGUARDE...')
print('-=-' *30)
ruta_excel = pd.read_excel("list.xlsx", header=None, names=('file_path', 'text1', 'text2'))
"""
    A linha acima ira fazer a leitura do arquivo excel. Header=none porque se não for especificado, ele ira omitir a primeira linha do arquivo.
    file_path esta atribuindo o caminho da imagem de acordo com os dados do arquivo
    text1 sera o texto inserido de acordo com os dados do excel. para adicionar mais textos basta adicionar por exemplo 'text2' e respectivamente
    para que o texto que foi adicionado seja escrito na imagem deve se adcionar no codigo mais uma linha:

    draw.text(xy=(20,550),text= row[2],fill=(255,255,255),font=font_type

    nesse caso adicionei a row[2] que esta de acordo com a coluna 3 no arquivo excel e é onde estara armazenado o text2.
"""
for row in ruta_excel.itertuples(index=False):
    #O print abaixo ajuda a visusalizar a execuçãod do codigo
    print (row) 
    # row is tuple, doing row[0] access to the first item (the first column)
    ruta=row[0]
    image_files = Image.open(ruta)
    font_type = ImageFont.truetype("snes.ttf", 30)#tamano da fonte
    draw = ImageDraw.Draw(image_files)
    # here you use row[1] and row[2]
    draw.text(xy=(140,940),text= row[1],fill=(255,255,255),font=font_type)#fill é a cor
    draw.text(xy=(140,990),text= row[2],fill=(255,255,255),font=font_type)

    image_files.save(ruta, 'JPEG', quality=90)
print('-=-' *30)
print('IMAGENS ALTERADAS C0M SUCESSO!!!')
sleep(1)
print(' v 1.0 Codado Por Mateus Rodrigues 2022 ')
print('-=-' *30)
