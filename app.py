import pandas as pd
from flask import Flask, render_template
from ReturnDataFrame import ReturnDataFrame
import plotly
import plotly.express as px
import json

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/line')
def line():

    rdf = ReturnDataFrame()
    data = rdf.returnDataframe()

    # Create Bar chart
    fig = px.line(data_frame=data)

    # Create graphJSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('line_chart.html', graphJSON=graphJSON)


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True, host='0.0.0.0', port=8080)
