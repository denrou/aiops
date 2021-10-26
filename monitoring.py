import dash
from dash import html, dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Output, Input
from predictions import predict

app = dash.Dash(__name__)


class Predictions:
    def __init__(self):
        self.has_predictions = False
        self.predictions = None

    def predict(self, data):
        self.has_predictions = True
        self.predictions = predict(data)

    def get_predictions(self):
        if not self.has_predictions:
            return None
        return self.predictions


p = Predictions()


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "AIOPs - Monitoring"

app.layout = html.Div(
    [
        html.Div(
            [
                html.P(children="〽️", className="header-emoji"),
                html.H1(children="AIOPs", className="header-title"),
                html.P(
                    children="My Monitoring Application.",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            [
                dcc.Interval(id="interval", interval=1 * 1000, n_intervals=0),
                dcc.Graph(id="graph", style={"height": "700px"}),
            ],
            className="graph",
        ),
    ]
)


@app.callback([Output("graph", "figure")], [Input("interval", "n_intervals")])
def update_graph(n):
    df = pd.read_csv("data/agent.log", sep=" ", names=["ds", "y"])
    df["ds"] = pd.to_datetime(df["ds"], unit="s")

    fig = go.Figure()

    if n % 60 == 10:
        p.predict(df)

    if p.has_predictions:
        preds = p.get_predictions()
        if preds is not None:
            fig.add_trace(
                go.Scatter(
                    x=preds["ds"],
                    y=preds["yhat_lower"],
                    fill=None,
                    mode="lines",
                    line={"width": 0},
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=preds["ds"],
                    y=preds["yhat_upper"],
                    fill="tonexty",
                    mode="lines",
                    line={"width": 0},
                )
            )
    fig.add_trace(
        go.Scatter(
            x=df["ds"],
            y=df["y"],
            fill=None,
            mode="lines",
            name="data",
            line_color="indigo",
        )
    )
    fig.update_traces(showlegend=False)
    return [fig]


if __name__ == "__main__":
    app.run_server(debug=True)
