from flask import Flask,render_template,request,session,redirect,url_for
from flask_cors import CORS
import model
import controller

app=Flask(__name__)
CORS(app)
app.secret_key="khan"

@app.route("/")
def home():
    preview,subreddit=model.get_meme()
    data = {"preview":preview,"subreddit":subreddit}
    return render_template("home.html",data=data)

@app.route("/register",methods=["GET","POST"])
def register():
    return controller.controller_register()

@app.route("/login",methods=["GET","POST"])
def login():
    return controller.controller_login()

@app.route("/logout")
def logout():
    return controller.controller_logout()
    
if __name__=="__main__":
    app.run(debug=True)


#res = make_response({"preview":preview,"subreddit":subreddit},200)
#res.headers["access_control_allow_origin"]="*"
#return render_template("home.html",data=res)
