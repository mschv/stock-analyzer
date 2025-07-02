from flask import Flask, render_template,request
import os

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        symbol=request.form.get("symbol")
        #Placeholder: fetch and analyze stock data
        return render_template("index.html",symbol=symbol)
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)