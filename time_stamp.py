#Converter essa informação para o formato de horario de legivel

from datetime import datetime

time_stamp = 1780704002
dataAtualizada = datetime.fromtimestamp(time_stamp)

print (dataAtualizada)