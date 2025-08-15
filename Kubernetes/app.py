from flask import Flask, render_template, request


# create a sample app that will take user name as an input and will display on the web browser

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        name = request.form.get("name")
        message = f"Hello {name}, Welcome to K8S test application"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)