import json
import requests

def search(ciudad):
        file = requests.get('https://www.el-tiempo.net/api/json/v2/provincias')
        data =file.json()

        json_file = 'list-mun-2012.json'
        with open(json_file, 'r') as date:
            content = json.load(date)
        

        # for x in range(len(data['provincias'])):
        #     if ciudad in data['provincias'][x]['NOMBRE_PROVINCIA'] or ciudad in data['provincias'][x]['COMUNIDAD_CIUDAD_AUTONOMA']:
        #         return [f"https://www.el-tiempo.net/api/json/v2/provincias/{data['provincias'][x]['CODPROV']}", 'provincias']
            
        for y in range(len(content['list-mun'])):
            if ciudad == content['list-mun'][y]['Municipio']:
                print(content['list-mun'][y]['Municipio'])
                print(content['list-mun'][y]['CP'])
                print(content['list-mun'][y]['codine'])
                return [f"https://www.el-tiempo.net/api/json/v2/provincias/{content['list-mun'][y]['CP']}/municipios/{content['list-mun'][y]['codine']}",'municipios']


if __name__=='__main__':
    mi = input('Introduce un nombre: ')
    execute = search(mi)
    if execute is not None:
        print('Municipio encontrado')
        print(str(execute[0]))
    else:
         print('Municipio no encontrado.')