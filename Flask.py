from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")
def komn ():
    return render_template("home.html")

@app.route("/oborud/")
def nn ():
    return render_template("about.html" )
if __name__ =="__main__":
    app.run()