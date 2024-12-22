from app import render_template,request,session,redirect,url_for
import model
import mysql.connector
try:
    config={
        "user":"root",
        "host":"localhost",
        "password":"97",
        "port":"3306"
    }
    connection=mysql.connector.connect(**config)
    if connection.is_connected():
        print("connect")
except Exception as e:
    print("unable to connect:", e)

mycursor=connection.cursor()
mycursor.execute("SHOW DATABASES")
cursor=mycursor.fetchall()
db=[]
for i in cursor:
    db.append(i[0])
if "myproject" in db:
    mycursor.execute("USE myproject")
else:
    mycursor.execute("CREATE DATABASE myproject")
    mycursor.execute("USE myproject")
    mycursor.execute("CREATE TABLE users(name VARCHAR(255), email VARCHAR(255), password VARCHAR(255))") 
connection.commit()

def controller_register():
    if (request.method=="GET"):
        return render_template("register.html")
    else:
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        mycursor.execute("INSERT INTO users(name,email,password) values(%s,%s,%s)",(name,email,password))
        connection.commit()
        session['name']= request.form['name']
        session['email']= request.form['email']
        return redirect(url_for("home"))
    
def controller_login():
    if request.method=="POST":
        email=request.form['email']
        password=request.form['password']
        mycursor.execute("SELECT * FROM users WHERE email=%s",(email,))
        user =mycursor.fetchone()
        if user is not None:
            if password==user[2]:
                session['name']=user[0]
                session['email']=user[1]
                preview,subreddit=model.get_meme()
                data = {"preview":preview,"subreddit":subreddit}
                return render_template("home.html",data=data)
            else:
                return "Error password is not matched"
        else:
            return "User not found"
    else:
        return render_template("login.html")

def controller_logout():
    session.clear()
    preview,subreddit=model.get_meme()
    data = {"preview":preview,"subreddit":subreddit}
    return render_template("home.html",data=data)
