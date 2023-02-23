from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    value1 = int(request.form['value1'])
    value2 = int(request.form['value2'])
    timestamp1 = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p")
    timestamp2 = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p")
    color1 = get_color(value1)
    color2 = get_color(value2)
    if value1 == 10 and value2 == 10:
        return render_template('input.html')
    else:
        return render_template('output.html', value1=value1, value2=value2, color1=color1, color2=color2, timestamp1=timestamp1, timestamp2=timestamp2)

def get_color(value):
    r = (value - 1) * 25
    b = 255 - r
    return f'rgb({r}, 0, {b})'

if __name__ == '__main__':
    app.run(debug=True)
