from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/status')
def status():
    return "<h2>All systems are operational.</h2>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method ==  'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return f"Hello {username}, your POST request is successful!"
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)