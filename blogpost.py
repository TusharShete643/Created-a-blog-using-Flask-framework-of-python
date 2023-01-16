from flask import *
from author import *
from users import *
from blog import *
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register")
def reg():
    return render_template("register.html")
@app.route("/login")
def log():
    return render_template("login.html")
@app.route("/regauthor")
def regauthor():
    return render_template("regauthor.html")   
@app.route("/reguser")
def reguser():
    return render_template("reguser.html")
@app.route("/loginauthor")
def loginauthor():
    return render_template("loginauthor.html")
@app.route("/loginuser")
def loginuser():
    return render_template("loginuser.html")
@app.route("/addpost")
def addpost():    
    return render_template("addpost.html")
@app.route("/showdetailsauthor")
def showdetailsauthor():
    return render_template("showdetailsauthor.html")
@app.route("/showdetailsuser")
def showdetailsuser():
    return render_template("showdetailsuser.html")

@app.route("/registerauthor",methods=["post"])
def addau():
    name=request.form["name"]
    email=request.form["email"]
    contactno=request.form["contactno"]
    password=request.form["password"]
    t=(name,email,contactno,password)
    addauthordetails(t)
    return redirect("/")

@app.route("/regasuser",methods=["post"])
def addus():
    name=request.form["name"]
    email=request.form["email"]
    contactno=request.form["contactno"]
    password=request.form["password"]
    t=(name,email,contactno,password)
    adduserdetails(t)
    return redirect("/")

@app.route("/loginasauthor",methods=["post"])
def logau():
    email=request.form["email"]
    password=request.form["password"]
    t=(email,password)
    t1=checklgau(t)
    if t in t1:
        return redirect("/showdetailsauthor")
    else:
        return redirect("/regauthor")

@app.route("/loginuser",methods=["post"])
def logus():
    email=request.form["email"]
    password=request.form["password"]
    t=(email,password)
    t1 = checklgus(t)
    if t in t1:
        return redirect("/showdetailsuser")
    else:
        return redirect("/reguser")

@app.route("/addnewpost",methods=["post"])
def addnewpost():
    name=request.form["name"]
    blogname=request.form["blogname"]
    blog=request.form["blog"]
    t=(name,blogname,blog)
    addnewblog(t)
    return redirect("/showdetailsauthor")


@app.route('/viewallposts')
def vwposts():
    t=view()
    return render_template("viewpost.html",x=t)
    
if __name__=='__main__':
    app.run(debug=True)