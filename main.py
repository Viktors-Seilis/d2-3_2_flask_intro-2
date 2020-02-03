from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return "Hi!"

@app.route('/home')
def home() :
  return render_template('home.html', aktiva_lapa = 'home')

@app.route('/about')
def about() :
  return render_template('about.html')

@app.route('/contacts')
def contacts() :
  return render_template('contacts.html')

@app.route('/params')
def params():
  args = request.args
 
  return render_template('params_table.html', args = args )

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5555 ,
  threaded = True, debug = True )
