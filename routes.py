from __main__ import app, render_template

@app.route('/', methods=['GET'])
def test():
    return render_template("home.html")
