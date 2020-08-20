from flask import (
    Flask,
    render_template,
    request
)
import requests

app = Flask(__name__)
base_url = "https://api.github.com/users/"

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        githubName = request.form.get("githubname")
        responseUser = requests.get("{}{}".format(base_url, githubName))
        responseRepos = requests.get("{}{}/repos".format(base_url, githubName))

        userInfo = responseUser.json()
        userRepos = responseRepos.json()

        if "message" in userInfo:
            return render_template("index.html", error = "Kullanıcı Bulunamadı")
        return render_template("index.html", profile = userInfo , repos = userRepos)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)