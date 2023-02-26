from flask import Flask, render_template, request
from pickle import load, dump

app = Flask(__name__)
db = None
id = 1

def load_from_file(file):
  load_from_file = open(file, "rb")
  data = load(load_from_file)
  load_from_file.close()
  return data

def save_to_file(file, data):
  save_to_file = open(file, "wb")
  dump(data,save_to_file)
  save_to_file.close()
  return "complete"
  
def formatId(id):
  return str(id).rjust(3,"0")

#setup section  
db = load_from_file("users")
  
@app.route('/info', methods=["POST","GET"])
def view_people():
    if request.method == "POST":
        # get the input value from the form data
        num_input = request.form.get("num")
        
        # look up the user in the db dictionary based on the input value
        user = db[formatId(num_input)]
        
        # if the user exists in the db, render the view_people template with their information
        if user:
            fname = user["fname"]
            lname = user["lname"]
            return render_template("view_people.html",fname=fname,lname=lname,id=num_input)
        else:
            # if the user doesn't exist in the db, render the view_people template with an error message
            error_message = "User not found"
            return render_template("view_people.html", error_message=error_message)
    else:
        return render_template("view_people.html")
  
@app.route('/')
def main():
  return render_template('index.html')
  
app.run(host='0.0.0.0', port=81)