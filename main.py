import requests
from datetime import datetime

class APIFeriados:
    def __init__(self, uri) -> None:
        self.uri = uri
        
    def get_feriados(self, year):
        # Extrae las fechas de feriados desde la API, correspondiente al valor que viene por parametro.
        headers =  {"User-Agent":"Mozilla/5.0"}
        uri = f'{self.uri}/{year}'
        response = requests.get(uri, headers = headers)
        if response.status_code == 200:
            return response.json()
        else:
            return "Error al obtener datos"

    def json_to_list(self, feriados):
        #extrae las fechas de feriados desde los datos obtenidos en la respuesta de la API 
        #Luego verifica que no exista un valor Nulo y retorna usando list comprehension.
        
        return [str(data.get('fecha')) for data in feriados if data.get('fecha') is not None]
        
def main():
# Trae las fechas de dias feriados para chile, desde una API, 
# convirtiendo el resultado en una lista de elementos no repetidos.

        uri_feriados_chile = 'https://apis.digital.gob.cl/fl/feriados'
        feriados_chile = APIFeriados(uri_feriados_chile)
        
        fecha_init = 2020
        now = datetime.now()
        fecha_fin = now.year+1
        feriados_set = set()
        # iniciamos un ciclo para obtener los años desde el 2020 hasta el actual
        for aggno in range(fecha_init, fecha_fin ):
            feriados = feriados_chile.get_feriados(aggno)
            if feriados:
                feriados_set.update(feriados_chile.json_to_list(feriados))
        return list(feriados_set)
        
if __name__ == "__main__":
    result = sorted(main())
    print(result)

    
    