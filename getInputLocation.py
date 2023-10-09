import requests
import json
class get_input_user:
    
    
    def get_user_input(ciudad):
        
        # file = requests.get('https://www.el-tiempo.net/api/json/v2/provincias')
        # data =file.json()

        json_file = 'list-mun-2012.json'
        with open(json_file, 'r') as date:
            content = json.load(date) 
        for y in range(len(content['list-mun'])):
            
            if ciudad.lower() == (content['list-mun'][y]['Municipio']).lower():
                
                return f"https://www.el-tiempo.net/api/json/v2/provincias/{content['list-mun'][y]['CP']}/municipios/{content['list-mun'][y]['codine']}"

    def get_temp_now(ciudad_temporal):
        file = requests.get(f"{ciudad_temporal}")
        data = file.json()
        item = list()
        item =data['pronostico']['hoy']['temperatura']
        return item

    def get_temp_tomorrow(ciudad_temporal):
        file = requests.get(f"{ciudad_temporal}")
        data = file.json()
        item = list()
        item = data['pronostico']['manana']['temperatura']
        return item

    def estado_cielo(estado_cielo_desc):
        file = requests.get(f"{estado_cielo_desc}")
        data = file.json()
        item = list()
        item =data['pronostico']['hoy']['estado_cielo_descripcion'][0]
        return item
    
if __name__=='__main__':
    # mi = input('Introduce un valor: ')
    # execute = get_input_user.get_user_input(mi)
    
    temporal = input('Introduce URL: ')
    exceute_1 = get_input_user.get_rachas_max(temporal)
    print(exceute_1)
    