from flask import Flask, request, render_template 
from gemini import genContent

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    method = request.method
    if method == 'GET':
        return render_template('index.html')
    else:
        user_text = request.form['user_text']
        print(user_text)
        genText = genContent(user_text)
        return render_template('index.html', text = user_text, genText = genText)

if __name__ == '__main__':
    app.run(debug = True)