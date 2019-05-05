from flask import Flask ,render_template,jsonify


app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route('/simulation',methods=['POST','GET'])
def simulation():
    return render_template("simulation.html")

@app.route('/home',methods=['POST','GET'])
def home():
    return render_template("home.html")

@app.route('/importanta',methods=['POST','GET'])
def importanta():
    return render_template("importanta.html")

@app.route('/acasa',methods=['POST','GET'])
def acasa():
    return render_template("home1.html")


if __name__=='__main__':
    app.run(debug=True,port=5444)




