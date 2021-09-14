from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template("home/index.html")

if __name__ == "__main__":
    app.run(debug=True)

""" @app.route('/report')
def hello_world():
    return render_template("home/index.html") """