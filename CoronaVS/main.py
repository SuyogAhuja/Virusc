from flask import Flask, escape, request, render_template
import pickle
from flask_mysqldb import MySQL
import hospTrain
import chatbot 

from matplotlib import pyplot as plt

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='corona'

mysql = MySQL(app)



file=open('model.pkl','rb')
clf = pickle.load(file)
file.close()

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method=='POST':
        Dict2=request.form
        username=Dict2['user_name']
        password=Dict2['password']
        con=mysql.connection.cursor()
        con.execute("SELECT Username,Password FROM admin")
        fetchdata1=con.fetchall()
       
        con.close()
        t1=(username,password)
        if t1 in fetchdata1:
               return render_template("index2.html") 
        else:
            return("<h1>ERROR : USER NOT REGISTERED</h1>")

       

        
        
    return render_template("login.html")

@app.route('/corona', methods = ['GET','POST'])
def corona1():
  if request.method=='POST':
    Dict1=request.form
    fname=Dict1['fname']
    lname=Dict1['lname']
    fever=int(Dict1['fever'])
    state=Dict1['state']
    age=int(Dict1['age'])
    b=Dict1['BodyPain']
    bodypain=0
    if b=="yes":
        bodypain=1
    T=Dict1['Travel']
    travel = 0
    if T == "yes":
        travel = 1
    D=Dict1['DiffBreathing']
    breathing = 0
    if D == "high":
        breathing = 1
    if D == "low":
        breathing = -1
    N=Dict1['Runnynose']
    runnynose = 0
    if N == "yes":
        runnynose = 1
    array=[[fever,bodypain,age,runnynose,breathing,travel]]
    print(array)
    Prob=clf.predict_proba(array)[0][1]
    value=clf.predict(array)
    print(value,Prob)
    if value==1:
        Value="POSITIVE"
    else:
        Value="NEGATIVE"

    con=mysql.connection.cursor()
    con.execute('INSERT INTO Patient_data(P_id,Fname,Lname,Fever,BodyPain,Age,Runnynose,DiffBreathing,Travel,Result,State) VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(fname,lname,fever,bodypain,age,runnynose,breathing,travel,Value,state))
    mysql.connection.commit()
 
    con.close()
   
    return render_template ('result.html', Val=Value,Probab=Prob)

  return render_template ('form.html')
@app.route('/database')
def database():
    con=mysql.connection.cursor()
    con.execute("SELECT Fname,Lname,State,Result FROM Patient_data")
    fetchdata=con.fetchall()
 
    con.close()
    con=mysql.connection.cursor()
    con.execute("SELECT Fname,Lname,Result FROM Patient_data WHERE Result='POSITIVE'")
    fetchdata1=con.fetchall()
    con.close()
    
    
    return render_template ('database.html', data=fetchdata, plength=len(fetchdata1),length=(len(fetchdata)))

@app.route('/graph')
def graph():

    return hospTrain.gr1()

@app.route('/afterlogin')
def afterlogin():
    return render_template('index2.html')

@app.route('/chat', methods = ['GET','POST'])
def chat():
    if request.method=='POST':
        Dict1=request.form
        question=Dict1['question']
        return chatbot.run(question)


    else:
     return render_template('chatbot.html')

    




if __name__=="__main__":
    app.run(debug=True)