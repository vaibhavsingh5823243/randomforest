from flask import Flask,request,render_template

import pickle
app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def index():
    if request.method =="POST":

        crime=request.form['crime']
        zn=request.form['zn']
        indus=request.form['indus']
        chas=request.form['chas']
        nox=request.form['nox']
        rm=request.form['age']
        dis=request.form['dis']
        rad=request.form['rad']
        tax=request.form['tax']
        ptratio=request.form['ptratio']
        b=request.form['b']
        age=request.form['age']
        lstat=request.form['lstat']
        data=[crime, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]
        scaler=pickle.load(file=open('scaler.pickle','rb'))
        data=scaler.transform([data])
        model=pickle.load(file=open('randomforest.pickle','rb'))
        price=model.predict(data)
        print(price)
        return render_template('success.html',price=round(price[0],2))
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)
