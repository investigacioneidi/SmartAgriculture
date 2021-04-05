import os
from datetime import datetime
import time
import logging

nombrelog=str(datetime.now())+'.log'

logging.basicConfig(handlers=[logging.FileHandler(filename=nombrelog, 
                              encoding='utf-8', mode='w')],
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s", 
                    datefmt="%F %A %T", 
                    level=logging.INFO)

# esperar los 4 minutos desde que inicia el proceso, es el tiempo de viaje del punto del control al sembrío
time.sleep(240) 

# Inicia el proceso

logging.info('INICIO..')
print ('INICIO..')
print(datetime.now())

#iniciar iteracion para recorrer puntos de toma de fotos
cuadro = 1 
repetir_cuadro = True
while repetir_cuadro:
	# esperar 60 segundos antes de la siguiente secuencia
    time.sleep(60)
	# recorrer bucle para tomar 4 fotos en cada cuadro
    i = 1
    print('PUNTO NUMERO: '+str(cuadro))
    logging.info('PUNTO NUMERO: '+str(cuadro))
    print(datetime.now())
    repetir_bucle = True
    while repetir_bucle: # tomar 4 fotos en cada cuadro
        time.sleep(15)
        now = datetime.now()
        format = now.strftime('%d%m%Y-%H%M%S')
        nombreArchivo=str(cuadro)+'-'+format+'.jpg'
        try:
            os.system('raspistill -r -o '+nombreArchivo)    # toma foto en formato RAW
            logging.info('IMAGEN TOMADA: '+nombreArchivo)
            print(nombreArchivo)
            
        except:
            logging.error("ERROR AL CREAR "+nombreArchivo)
            
        i = i + 1			
        if i>4: # se toma 4 fotos en el mismo punto
            repetir_bucle = False
    cuadro = cuadro + 1 
    if cuadro > 4 : # se dividió el terreno en 4 cuadros
        repetir_cuadro = False
	
print(datetime.now())
print('FIN PROCESO')
logging.info('FIN PROCESO')

