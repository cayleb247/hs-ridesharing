from flask import Flask, render_template, jsonify

app = Flask(__name__)

RIDES = [
    {
        'id': 1,
        'name': 'Caleb',
        'location': '4512, Example St.',
        'ETA': '12 minutes'
    },
    {
        'id': 2,
        'name': 'Minh',
        'location': '3989, Example St.',
        'ETA': '14 minutes'
    },
    {
        'id': 3,
        'name': 'Matthew',
        'location': '4543, Example St.',
        'ETA': '13 minutes'
    },
    {
        'id': 4,
        'name': 'Fuller',
        'location': '4259, Example St.'
    }
]

@app.route('/') #path of the url after domain name
def hello_world():
    return render_template('home.html', rides=RIDES)

@app.route('/api/rides') #Makes a json endpoint that can be accessed to see RIDES data
def list_rides():
    return jsonify(RIDES)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)