from datetime import datetime
from flask import Flask, render_template
from ReturnInputData import ReturnDataFrame
import plotly
import plotly.express as px
import json

app = Flask(__name__)


# Flask test
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/')
def chart():

    # Import data from DataFrame
    rdf = ReturnDataFrame()
    data = rdf.returnDataframe()

    # Current time to mark today on the plot
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y")

    # Create Line chart
    fig = px.line(data, x="Date", y=["Measurement", "Prediction"])

    # Create vertical line
    fig.add_vline(x=datetime.strptime(date_time, "%m/%d/%Y").timestamp() * 1000,
                  line_width=3, line_dash="dash", line_color="green",
                  annotation_text="Today", annotation_position="bottom left")

    # Chart layout parameters
    fig.update_layout(title_text='Global Monthly Mean CO₂ Concentration', title_x=0.5,
                      width=1600, height=800,
                      xaxis_title="Date",
                      yaxis_title="CO₂ mole fraction (ppm)",
                      legend=dict(
                          yanchor="top",
                          y=0.99,
                          xanchor="left",
                          x=0.01,
                          title=""),
                      font=dict(
                          family="Courier New, monospace",
                          size=24,
                          color="RebeccaPurple"
                      ))
    fig.update_yaxes(automargin=True)

    # Create graphJSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('line_chart.html', graphJSON=graphJSON)


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True, host='0.0.0.0', port=8080)
