#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
from keras.models import load_model

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        income = request.form.get("Income")
        age = request.form.get("Age")
        loan = request.form.get("Loan")
        print(income, age, loan)
        model = load_model("creditcard_model")
        pred = model.predict([[float(income), float(age), float(loan)]])
        s = "The predicted credit card default is " + str(pred) 
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=int("1111"))

