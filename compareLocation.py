import requests 
json_file_provi = requests.get('https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/provincias-espanolas/records?limit=20&refine=provincia%3A%22Alacant%22')


class GetCurrentLocation:
    
    def getLocation(data_post):
        data = json_file_provi.json()
        get_data_post = data_post
        for i in data['results']:
            if (i['geo_shape']):
                for x in range(len(i['geo_shape']['geometry']['coordinates'])):
                    print(get_data_post['longitud'])
                    print(i['geo_shape']['geometry']['coordinates'][x][0][0][0])
                    # print(i['geo_shape']['geometry']['coordinates'][9][0][0][0])
                # latitud
                    # a = i['geo_shape']['geometry']['coordinates'][0][0][0][0]
                    # b = i['geo_shape']['geometry']['coordinates'][9][0][0][0]
                    # # longitud
                    # a1 =i['geo_shape']['geometry']['coordinates'][0][0][0][1]
                    # b1= i['geo_shape']['geometry']['coordinates'][9][0][0][1]
                    # if float(get_data_post['latitud']) <=a1 and float(get_data_post['latitud']) >= b1:   
                        
                    #     if float(get_data_post['longitud']) >=a and float(get_data_post['longitud']) <= b:
                    #         print('Coordenadas encontradas')
                    #     break
                    # else:
                    #     print('Coordenadas no encontradas')
                    
                            
                    # if float(data_post['latitud']) in e[0]:
                    #     print('Primer elemento encontrado')
                    #     for o in i['geo_shape']['geometry']['coordinates'][0][0][1]:
                    #         if float(data_post['longitud']) in o[1]:
                    #             print('Segundo elemento encontrado')
                    #             print('El usuario es de Alicante')
                    #             break
            break
        