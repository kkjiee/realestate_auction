from flask import Flask
app1 = Flask("my app")
from flask import render_template

@app1.route('/')
def home():
   return 'This is Home!'


@app1.route('/home')
def b_home():
   return render_template('home.html')

@app1.route('/menu1')
def b_1_home():
   return render_template('basic_knowledge.html')

@app1.route('/b-2')
def b_2_home():
   return render_template('b-2.html')

@app1.route('/b-3')
def b_3_home():
   return render_template('b-3.html')

@app1.route('/b-4')
def b_4_home():
   return render_template('b-4.html')

@app1.route('/path1')
def path1():
   return 'This is path1!'


@app1.route('/in')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   app1.run("0.0.0.0", port=5000,debug=True)
