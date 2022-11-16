from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>/<age>/<email>/<college>')
def success(name,age,email,college):
   return f'welcome {name} \n your age is {age} , your email is {email} & your college is {college}' 

@app.route('/login',methods = ['POST'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      ages = request.form['age']
      emails = request.form['email']
      colleges = request.form['college']
      return redirect(url_for('success',name = user,age = ages, email = emails, college=colleges))
   else:
      user = request.args.get('name')
      return redirect(url_for('success',name = user,age = ages, email = emails, college=colleges))

if __name__ == '__main__':
   app.run(debug = True)