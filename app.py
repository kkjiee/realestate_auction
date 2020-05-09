from flask import Flask
app1 = Flask("my app")
from flask import render_template,  request, jsonify

@app1.route('/')
def home():
   return 'This is Home!'

@app1.route('/assignment')
def assignment():
   return render_template('assignment.html')

@app1.route('/dealcharge')
def dealcharge():
   return render_template('dealcharge.html')

@app1.route('/home')
def b_home():
   return render_template('home.html')

@app1.route('/basic_knowledge')
def b_1_home():
   return render_template('basic_knowledge.html')

@app1.route('/b-2')
def b_2_home():
   return render_template('b-2.html')

@app1.route('/b-3')
def b_3_home():
   return render_template('b-3.html')

# @app1.route('/b-4')
# def b_4_home():
#    return render_template('b-4.html')

@app1.route('/path1')
def path1():
   return 'This is path1!'


@app1.route('/calculate_expected_value', methods=['GET'])
def calculate_expected_value():
   input1 = request.args.get('input1')
   input2 = request.args.get('input2')
   input3 = request.args.get('input3')
   input4 = request.args.get('input4')
   input5 = request.args.get('input5')
   input6 = request.args.get('input6')
   input7 = request.args.get('input7')
   input8 = request.args.get('input8')
   input9 = request.args.get('input9')
   input10 = request.args.get('input10')
   input11 = request.args.get('input11')
   input12 = request.args.get('input12')
   input13 = request.args.get('input13')

   expected_value = int(input1) - int(input2) - int(input3) - int(input4) - int(input5) - int(input6) - int(input7) - int(input8) - int(input9) - int(input10) - int(input11) - int(input12) - int(input13)


   print(input1)
   print(input2)
   print(input3)
   print(input4)
   print(input5)
   print(input6)
   print(input7)
   print(input8)
   print(input9)
   print(input10)
   print(input11)
   print(input12)
   print(input13)

   data = {"expected_value": expected_value}
   return jsonify(data)



@app1.route('/assignment_value', methods=['GET'])
def assignment_value():
   input9 = request.args.get('input9')
   input10 = request.args.get('input10')


   expected_value = float(input9) + float(input10)

   print(input9)
   print(input10)


   data = {"expected_value": expected_value}
   return jsonify(data)


   
@app1.route('/calculate_charge_value', methods=['GET'])
def calculate_charge_value():
   input1 = request.args.get('input1')
   input2 = request.args.get('input2')


   expected_value = float(input1) * float(input2) / 100

   print(input1)
   print(input2)


   data = {"expected_value": expected_value}
   return jsonify(data)




@app1.route('/in')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   app1.run("0.0.0.0", port=5000,debug=True)
