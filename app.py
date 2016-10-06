from flask import Flask, render_template, request, url_for, session, redirect
import hashlib
import utils.register

app = Flask(__name__)
app.secret_key = "pineapples"


@app.route("/")
def main():
    if len(session.keys())>0 or len(session.keys())<0:
        return redirect(url_for("lo"))
    return render_template("login.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register",methods = ['POST'] )
def register():
    if len(session.keys())>0 or len(session.keys())<0:
        return redirect(url_for("lo"))
    
    h = hashlib.sha1()
    x = utils.register.createDict()
    if request.form["user"] in x:
        return render_template("login.html", m = "username is already taken")
    else:
        h.update(request.form["pass"])
        newPass = h.hexdigest()
        utils.register.add(request.form["user"], newPass)
        return render_template("login.html",title = "Account Registration", m="you have successfully register your account")



@app.route("/authenticate", methods = ['POST'])
def authenticate():
    if len(session.keys())>0 or len(session.keys())<0:
        return redirect(url_for("lo"))
    d = utils.register.createDict()
    h = hashlib.sha1()
    h.update(request.form["pass"])
    currPass = h.hexdigest()
    if request.form["user"] not in d.keys():
        print request.form["user"]
        print d.keys()
        return render_template("login.html",m = "Username not Found!")
    elif currPass != d[request.form["user"]]:
        return render_template("login.html", m = "Password is Incorrect")
    else:
        print("jesus take the wheel")
        session[app.secret_key] = request.form["user"]
        return redirect(url_for("li"))

@app.route("/li")
def li():
    if len(session.keys()) == 0:
        return redirect(url_for("main"))
    print "YO MAMMA FAT"
    return render_template("welcome.html", username = session[app.secret_key])

@app.route("/logout")
def lo():
    session.pop(app.secret_key)
    return redirect(url_for("main"))
    
    
if __name__ == "__main__":
    app.run(debug = True)
