from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it a secret!'

@app.route('/')
def counter():
    if not 'counter' in session:
        session['counter'] = 0
        session['counter'] += 1
    return render_template('index.html')

@app.route('/increment_counter', methods=['POST'])
def increment():
    session['counter'] += 1

    return redirect('/')

@app.route('/reset_counter', methods=['POST'])
def reset_counter():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)