from flask import Flask, render_template, request
from environs import Env
import requests 
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


from getInputLocation import get_input_user

env = Env()
dir_template = env('BASE_DIR_TEMPLATE') 
dir_static = env('BASE_DIR_STATIC')
app = Flask(__name__, template_folder=dir_template, static_folder= dir_static)


@app.route('/', methods=['GET','POST'])
def index():
    
    if request.method=='POST':
        date_time = datetime.now()
        input = str(request.form['provincia'])
        try:
            valor =get_input_user.get_user_input(input)
            
            json_file= requests.get(valor)
            date = json_file.json()
            
            temp = get_input_user.get_temp_now(valor)
            lista_hora = list(range(24))

            temp_m = get_input_user.get_temp_tomorrow(valor)

            state_skay = get_input_user.estado_cielo(valor)
            
            content={
                    'title':date['municipio']['NOMBRE'], 
                    'temp_act':date['temperatura_actual'], 
                    'temp_min':date['temperaturas']['min'], 
                    'temp_max':date['temperaturas']['max'], 
                    'date_time': date_time.strftime("%A, %d %b").upper(),
                    
                    
            }
            temps_mun=temp[int(temp.index(date['temperatura_actual'])):]
            control_hora = lista_hora[date_time.hour]           
            total_m = len(temp_m)
            total=len(temp[temp.index(date['temperatura_actual']):][:len(temp[temp.index(date['temperatura_actual']):])])-1
            return render_template('provincias/pro.html',
                                   content=content,
                                   lista_hora_m = lista_hora[1:total_m],
                                   lista_hora=lista_hora[date_time.hour:], 
                                   temps_mun=temp[temp.index(date['temperatura_actual']):][:len(temp[temp.index(date['temperatura_actual']):])], 
                                   total=total,
                                   temp_m=temp_m,
                                   total_m = total_m,
                                   state_skay=state_skay,
                                   control_hora=control_hora,
                                   )
        except Exception as e:
            print(e)
    return render_template('Index/index.html')