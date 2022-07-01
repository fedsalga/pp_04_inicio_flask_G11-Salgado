from flask import Flask, render_template
import sqlite3
conn = sqlite3.connect('co_emissions.db')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/listado')
def listado():
  lista = []
  q = f"""SELECT Value,Country
  From emissions
  WHERE Series = "pcap"
  ORDER BY Value DESC LIMIT 10;  """
  
  resu = conn.execute(q)
  
  for fila in resu:
      lista.append(fila)
    
  return render_template('lista.html',
                         devolver = lista)
    
  conn.close()
  
@app.route('/listado/top')
def top():
  top = []
  q = f"""SELECT Value,Country
  From emissions
  WHERE Series = "total"
  ORDER BY Value DESC LIMIT 10;  """
  
  resu = conn.execute(q)
  
  for fila in resu:
      top.append(fila)
  return render_template('total.html',
                         devolver = top)
    
  conn.close()

@app.route('/listado/argentina')
def argentina():
  pais = []
  q= f"""SELECT DISTINCT Country, value, Series
       FROM emissions
       WHERE Year like 2018;"""

  resu = conn.execute(q)

  for fila in resu:
    pais.append(fila)

  return render_template('paises.html',
                        arg = pais)

@app.route('/ayuda')
def ayuda():
  return render_template('ayuda.html')

app.run(host='0.0.0.0', port=81)  