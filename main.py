from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html", map_preview_src = "https://via.placeholder.com/2048")


@app.route("/", methods=['GET', 'POST'])
def form_post():
    placeholder = "https://via.placeholder.com/2048"
    preview_src = placeholder

    if request.method == "POST":

        req = request.form
        
        if 'Preview' in req:
            print("p")
        elif 'Submit' in req:
            print("s")


    return render_template("main.html", map_preview_src = preview_src)

if __name__ == "__main__":
    app.run(debug=True)
