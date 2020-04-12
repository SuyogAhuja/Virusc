import pandas as pd
import numpy as np
import pickle
from flask import Flask, escape, request, render_template
from matplotlib import pyplot as plt
from flask_mysqldb import MySQL
import csv

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='corona'
mysql = MySQL(app)

def gr1():
 con=mysql.connection.cursor()
 con.execute("SELECT State,Result FROM Patient_data WHERE Result='POSITIVE'")
 fetchdata=con.fetchall()
 con.close()
 array1= ["A&N",
"Andhra Pradesh",
"Arunachal Pradesh",
"Assam",
"Bihar",
"Chandigarh",
"Chhattisgarh",
"Dadra & Nagar Haveli",
"Daman & Diu",
"Delhi",
"Goa",
"Gujarat",
"Haryana",
"Himachal Pradesh",
"Jammu & Kashmir",
"Jharkhand",
"Karnataka",
"Kerala",
"Lakshadweep",
"Madhya Pradesh",
"Maharashtra",
"Manipur",
"Meghalaya",
"Mizoram",
"Nagaland",
"Odisha",
"Puducherry",
"Punjab",
"Rajasthan",
"Sikkim",
"Tamil Nadu",
"Telangana",
"Tripura",
"Uttar Pradesh",
"Uttarakhand",
"West Bengal"]

 array2=[0]*len(array1)
 c=0
 
 for i in range(len(array1)):
     for j in range(len(fetchdata)):
         if array1[i]==fetchdata[j][0]:
             c=c+1
     array2[i]=c
     c=0

 
 



 df = pd.read_csv('HospitalData.csv')
 
 a=list(df.State)
 b=list((map(int, df.Beds)))
 c=list((map(int, df.Total)))
 d=list((map(int, df.Positive)))
 e=array2

 labels = a
 Beds = b
 Hospitals =c
 Positive=d
 Predicted=e
 
 
 x = np.arange(len(labels))  # the label locations
 width = 0.25  # the width of the bars


 fig=plt.figure(figsize=(18, 10))
 ax = fig.subplots()
 r1 =x
 r2 = [x + width for x in r1]
 r3 = [x + width for x in r2] 

 bars = np.add(Positive, Predicted).tolist()

 rects1 = ax.bar(r1, Beds, width, label='Beds', align='center')
 rects2 = ax.bar(r2, Hospitals, width, label='Hospitals',align='center')
 rects3 = ax.bar(r3, bars, bottom=Predicted, yerr=Positive,width=width, label='Positive cases',align='center')
 
 def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


 autolabel(rects3)
  

# Add some text for labels, title and custom x-axis tick labels, etc.
 ax.set_ylabel('Hospital Availibilty')
 ax.set_title('Hospital Availibilty grouped by state')
 ax.set_xticks(x)
 plt.xticks(rotation = 90)
 ax.set_xticklabels(labels)
 ax.legend()
 
 plt.show()

 return render_template ("aftergraph.html")
