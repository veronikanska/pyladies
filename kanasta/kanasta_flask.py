from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Domovská stránka')

@app.route('/games')
def games():
    return render_template('games.html', title='Zadávání her')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html', title='Statistiky')

if __name__ == "__main__":
    app.run()