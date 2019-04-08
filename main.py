from flask import Flask, render_template
from datetime import datetime
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

context = {
    'date': datetime.now(),
    'movies': ['The Hunger Games', 'Interstellar', 'The Lion King', 'Spiderman'],
    'total_minutes': 404,
}


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/report')
def route():
    return render_template('jinja_template.html', context=context, title='Report')


if __name__ == '__main__':
    app.run()
