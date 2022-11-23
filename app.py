from flask import Flask, render_template
import ReturnDataFrame

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/line')
def line():
    rdf = ReturnDataFrame.ReturnDataFrame()
    line_labels = rdf.returnDate()
    line_values = rdf.returnValues()
    return render_template('line_chart.html', title='Trends in Atmospheric Carbon Dioxide', max=420, min=330,
                           labels=line_labels,
                           values=line_values)


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True, host='0.0.0.0', port=8080)
