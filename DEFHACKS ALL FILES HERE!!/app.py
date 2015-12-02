from flask import Flask, render_template, request

joe = Flask(__name__)


@defhacks.route( "/" )

def index():
    return render_template("base.html")

@defhacks.route( "/teacherpage" )
def teachers():
    return 

@defhacks.route( "/form", methods = ["GET", "POST"] )
def form():
    if request.method == "GET":
        return "please get here from the form"

    else:
        n = request.form["name"]
        return "Hello " + n
         

if __name__ == "__main__":

    defhacks.debug = True

    defhacks.run()




