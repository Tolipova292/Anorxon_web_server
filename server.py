from flask import Flask, render_template_string

app = Flask(name)

@app.route('/')
def home():
    html = open("index.html").read()
    return render_template_string(html)

if name == 'main':
    app.run(host='0.0.0.0', port=8880)
