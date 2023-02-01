from flask import render_template , Flask , request


import pandas as pd

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def main_html():

    if request.method == "POST" :
        name_input = request.form["fname"]
        name_input_2 = request.form["lname"]
        print("test******** :",name_input,name_input_2)
        print(request.form)
        print(type(request.form))
        data = {"FNAME":[name_input],"LNAME":[name_input_2]}
        dataframe = pd.DataFrame(data=data)
        print(dataframe)
        dataframe.to_csv("data_log.csv",mode="a",header=False,index=False)


    data = 12
    return render_template("index.html",data=data)

@app.route("/2")
def second_html():
    return "something"

if __name__ == "__main__":
    app.run("0.0.0.0",port=5001)



