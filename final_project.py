# Final project code
from flask import Flask
from flask import request
from werkzeug.utils import secure_filename
from markupsafe import escape
import random
import os

# the upload folder needs to be there, so create a folder upload
UPLOAD_FOLDER = "/var/www/app/code/upload"
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
port=int(os.environ.get("PORT",5000))


@app.route("/status")
def show_status():
    # show the servers status (hard coded :-) )
    return "Alive!"


@app.route("/login", methods=["POST"])
def return_usercreds():
    # return the user and length of the password
    if request.method == "POST":
        content = request.json
        return "Login success for user {} with password from length: {}!".format(
            content["username"], len(content["password"])
        )


@app.route("/predict/<int:seller_avaible>/<month>/<int:customer_visiting_website>")
def guess_what(seller_avaible, month, customer_visiting_website):
    # return a prediction
    return "my prediction {}".format(random.randint(2000, 5000))


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    # receives the file and put it in the upload dir
    if request.method == "POST":
        if "file1" not in request.files:
            return "there is no file1 in form!"
        file1 = request.files["file1"]
        path = os.path.join(app.config["UPLOAD_FOLDER"], file1.filename)
        file1.save(path)
        return path
        return "ok"
    return """
        <h1>Upload new File</h1>
        <form method="post" enctype="multipart/form-data">
        <input type="file" name="file1">
        <input type="submit">
        </form>
     """


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=port)
