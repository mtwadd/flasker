from flask import Flask, render_template

#create Flask Instance
app=Flask(__name__)



### Jinja2 unique Filters ###
### jinja.palletsprojects.com ###
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags

#create route decorator
@app.route('/')
def index():
    stuff="This is Bold text."
    first_name="Bobby"
    favorite_pizza=["Pepperoni", "Mushroom", "Cheese", 41, 38, 100]
    print("Hello " + first_name + " !")
    print("successful load!")
    return render_template("index.html", first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)

#localhost:5000/user/<user_name>
@app.route('/user/<name>')
def user(name):
    print("Hello " + name + " !!")
    return render_template("user.html", user_name=name)

# custom Error Pages
#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    print("Hello this is an error route")
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    print("Hello this is an error route")
    return render_template("500.html"), 500



if __name__ == "__main__":
    app.run(debug=True)