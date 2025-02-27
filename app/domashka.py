
from flask import request , render_template , redirect, url_for
from app import app
spisok = []
@app.route("/" , methods=["GET" , "POST"])
def rr ():
    if request.method == "POST":
        a = request.form.get("ti")
        b = request.form.get("tg")
        c = request.form.get("tx")
        d = request.form.get("tv")
        if a and b and c and d:
              spisok.append({"a":a, "b":b, "c":c, "d":d})
              return redirect(url_for("rr"))
    return render_template("anketa.html" , spisok = spisok)

