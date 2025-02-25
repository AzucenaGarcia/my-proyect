"hacer un calendario y que se resalte la fecha actual"

import datetime

now = datetime.datetime.now()
def print_de_numero(x, es_hoy = False):
    if len (x) == 1:
        s =f" {x}"
    if es_hoy:
         return f" *{x}* "
    else:
        return f"  {x} "

texto_salida = " L   M    X   J   V   S   D \n"
dia_inicial_mes = 27

total_num = 7* 6
contador = 0

for i in range(total_num):
    dia = dia_inicial_mes + i
    if dia == 31:
        dia_inicial_mes = 1
    texto_salida = texto_salida + print_de_numero(str(dia))
contad = contador + 1
if contador == 7:
    texto_salida = texto_salida  + "\n"
    contador = 0
print(contador)
print(texto_salida)

