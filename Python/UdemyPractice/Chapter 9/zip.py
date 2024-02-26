'''
import zipfile
mi_zipfile = zipfile.ZipFile("Proyecto+Dia+9.zip","r")

mi_zipfile.extractall()

'''
import math
import os
from datetime import datetime
import re
import time

class TextSearch():
    def __init__(self, pattern, directory):
        self.pattern = pattern
        self.directory = directory


    def search(self):
        inicio=time.time()

        date= datetime.today()
        current_route=os.getcwd()
        full_path=current_route+'\\'+self.directory
        results={}
        for route in os.walk(full_path, topdown=True):
            for name in route[2]:

                file = open(route[0] + "\\" + name)
                text = file.read()

                busqueda = re.search(pattern, text)
                if busqueda:
                    results[name] = busqueda.group()

                file.close()


        analiys_date=f'Fecha de busqueda ' + str(date)
        table='\nArchivo      Nro de serie'
        for key, value in results.items():
            table=table+'\n'+key+'  '+value

        elements=f'\n\nNumeros Encontrados  {len(results)} '
        final=time.time()

        search_duration=f'\nTiempo transcurrido {str(math.ceil(final-inicio))} segunndos'
        return analiys_date+table+elements + search_duration


pattern = r'[N]{1}\w{3}-\d{5}'
directory='Mi_Gran_Directorio'

searcher= TextSearch(pattern, directory)
print(searcher.search())
