from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.users import User


#====================================================
#SHOW ALL ROUTE
#====================================================

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users= User.get_all()
    return render_template("index.html", all_users = users)
    
#====================================================
#SHOW ONE USER ROUTE
#====================================================

@app.route("/user/<int:user_id>")
def user(user_id):

    query_data = {
        "user_id" : user_id
    }
    one_user = User.get_one_user(query_data)
    return render_template("user.html",one_user = one_user)


#====================================================
#SHOWS THE CREATE TEMPLATE ROUTE
#====================================================


@app.route("/addUser/")
def Users():
    return render_template("addUser.html")


#====================================================
#REDIRECTS BACK TO SHOW ALL
#====================================================


@app.route("/addUser/create", methods=["POST"])
def addUsers():
#1 - collect the information from our form send to the query
    query_data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
#2 - call on the query from our model file
    new_user_id = User.create_new_user(query_data)
#3-redirect elsewhere once query is done
    return redirect("/")


# can use this to show the dojos info in dojos and ninjas
@app.route("/user/edit/<int:user_id>")
def editUsers(user_id):
    query_data = {
        "user_id" : user_id
    }
    one_user = User.get_one_user(query_data)
    return render_template("editUser.html", one_user = one_user)

@app.route('/user/update', methods=['POST'])
def updateUser():
    query_data = {
        "user_id" : request.form["user_id"],
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.update(query_data)
    return redirect('/')

@app.route('/user/delete/<int:id>')
def delete(id):
    query_data = {
    'user_id' : id
}
    User.delete(query_data)
    return redirect ('/')