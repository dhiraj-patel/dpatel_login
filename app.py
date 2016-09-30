from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
@app.route("/login/")

def login():
    print request
    print request.headers
    print app
    return render_template("input.html")

@app.route("/authenticate/", methods = ['POST'])
def auth():
    print app
    print "\n"
    print request
    print "\n"
    print request.headers
    print "\n"
    print request.method
    print "\n"    
    print request.form['pass']
    print "\n"
    if(request.form['user'] == "dhiraj" and request.form['pass'] == "patel"):
        return render_template("accept.html",status = "YOU'VE LOGGED IN")
    else:
        return render_template("accept.html",status = "YOU LOSER HAHA")
    
if __name__ == "__main__":
    app.run(debug = True)
