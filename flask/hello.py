from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

#render_template("favorite_form.html")
@app.route('/')
@app.route('/form')
def form():
    return render_template("favorite_form.html")

@app.route('/thanks')
def thanks():
    name = "David"
    s = "Christian"
    a = "being"
    return render_template("tynote.html", name=name, gift = s, noun = a)

if __name__ == '__main__':
   app.run()

