from flask import Flask, render_template, request
import hashlib
import utils.register

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register",methods = ['POST'] )
def register():
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
def auth():
    d = utils.register.createDict()
    h = hashlib.sha1()
    h.update(request.form["pass"])
    currPass = h.hexdigest()
    if request.form["user"] not in d.keys():
        print request.form["user"]
        print d.keys()
        return render_template("login.html",m = "Username not Found!")
    
    if currPass != d[request.form["user"]]:
        return render_template("login.html", m = "Password is Incorrect")
    else:
        return render_template("login.html",m = "You have successfully logged in to nothing.")
    
    
if __name__ == "__main__":
    app.run(debug = True)
