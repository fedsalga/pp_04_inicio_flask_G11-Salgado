from flask import Flask
import random

app = Flask(__name__)



lista =["amarillo","azul","rojo","negro","blanco","violeta","rosa","naranja","gris","celeste"]
colores = lista[random.randint(1,10)]

@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/dado')
def dados():
  numero = random.randint(1, 6)
  return str(numero)


@app.route('/fecha')
def fecha():
  dia = random.randint(1, 30)
  mes = random.randint(1, 12)
  año = random.randint(1970, 2100)
  elegido = str(dia) + "/" + str(mes) + "/" + str(año)
  return elegido

@app.route('/color')
def color():
  return colores

@app.route('/dado/<n>')
def repetir_dado(n):
  
  serie = []
  i=0
  nro = int(n)
  if nro <= 0 or nro>10:
    return "Numero ingresado no valido"
  else:
    for i in range(nro):
      serie.append((random.randint(1,6)))
      i = i + 1
      
    return str(serie)


@app.route('/fecha/<y>')
def año_fecha(y):
  dia = random.randint(1, 30)
  mes = random.randint(1, 12)
  año = int(y)
  elegido = str(dia) + "/" + str(mes) + "/" + str(año)
  return elegido


@app.route('/fecha/<y>/<m>')
def año_mes(y,m):
  dia = random.randint(1, 30)
  mes = int(m)
  año = int(y)
  elegido = str(dia) + "/" + str(mes) + "/" + str(año)
  return elegido
  
app.run(host='0.0.0.0', port=81)
