from datetime import datetime
from flask import Flask, render_template
from ReturnInputData import ReturnDataFrame
import plotly
import plotly.express as px
import json
import plotly.graph_objects as go

app = Flask(__name__)
rdf = ReturnDataFrame()

layout = dict(
    xaxis=dict(
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='white',
        linewidth=2
    ),
    yaxis=dict(
        titlefont=dict(
            family='Rockwell',
            size=12,
            color='white',
        ),
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='white',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Rockwell',
            size=12,
            color='white',
        ),
    ),
    showlegend=True,
    template='plotly_dark',
    xaxis_title="Date",
    yaxis_title="CO₂ mole fraction (ppm)",
    height=800,
    legend_title_text="",
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01,
        font_size=20)
)

annotations = [dict(xref='paper', yref='paper', x=0.5, y=1.05,

                    xanchor='center', yanchor='bottom',
                    font=dict(family='Rockwell',
                              size=26,
                              color='white'),
                    showarrow=False)]


# Flask test
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/')
def chart():
    # Import data from DataFrame
    data = rdf.returnDataframe()

    # Current time to mark today on the plot
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y")

    # Create Line chart
    fig = px.line(data, x="Date", y=["Measurement", "Prediction"])

    # Chart layout parameters
    fig.update_layout(layout, annotations=annotations)

    fig.update_annotations(text="Global Monthly Mean CO₂ Concentration")

    # Create vertical line
    fig.add_vline(x=datetime.strptime(date_time, "%m/%d/%Y").timestamp() * 1000
                  , line_width=3, line_dash="dash", line_color="green"
                  , annotation_text="Today", annotation_font_size=20
                  , annotation_position="bottom left"
                  )

    # Create graph_json
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('line_chart.html', graphJSON=graph_json)


@app.route('/testData')
def testDataChart():
    # Import data from DataFrame
    data = rdf.returnTestDataframe()

    # Current time to mark today on the plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(go.Scatter(x=data['Date'], y=data["Train prediction"],
                                        mode='lines',
                                        name='Train prediction')))
    fig.add_trace(go.Scatter(x=data['Date'], y=data["Test prediction"],
                             mode='lines',
                             name='Test prediction'))
    fig.add_trace(go.Scatter(go.Scatter(x=data['Date'], y=data["Actual Value"],
                                        mode='lines',
                                        name='Actual Value')))
    # Chart layout parameters
    fig.update_layout(layout, annotations=annotations)
    fig.update_annotations(text="Global Monthly Mean CO₂ Concentration - Test")

    # Create graph_json
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('line_chart.html', graphJSON=graph_json)


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True, host='0.0.0.0', port=8080)
