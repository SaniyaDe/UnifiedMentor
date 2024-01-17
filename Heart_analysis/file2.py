import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "Heart Disease data/Heart Disease data.csv"
df = pd.read_csv(file_path)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Heart Disease Dataset Dashboard"),

    # Basic statistics
    html.Div([
        html.H2("Basic Statistics"),
        html.Pre(id='basic-stats', children=df.describe().to_string())
    ]),

    # Distribution of target variable
    html.Div([
        html.H2("Distribution of Target Variable"),
        dcc.Graph(
            id='target-distribution',
            figure={
                'data': [
                    {'x': df['target'].value_counts().index, 'y': df['target'].value_counts().values, 'type': 'bar'}
                ],
                'layout': {
                    'title': 'Distribution of Target Variable'
                }
            }
        )
    ]),

    # Histogram of numerical features
    html.Div([
        html.H2("Distribution of Numerical Features"),
        dcc.Graph(
            id='numerical-features-histogram',
            figure={
                'data': [
                    {'x': df[column], 'type': 'histogram', 'name': column} for column in ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
                ],
                'layout': {
                    'title': 'Distribution of Numerical Features'
                }
            }
        )
    ]),

    # Scatterplots for individual features against the target
    html.Div([
        html.H2("Scatterplots of Numerical Features against Target"),
        dcc.Dropdown(
            id='scatter-feature-dropdown',
            options=[{'label': col, 'value': col} for col in ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']],
            value='age'
        ),
        dcc.Graph(id='scatterplot')
    ]),
])

# Define callback for updating scatterplot based on dropdown selection
@app.callback(
    Output('scatterplot', 'figure'),
    [Input('scatter-feature-dropdown', 'value')]
)
def update_scatterplot(selected_feature):
    return {
        'data': [
            {
                'x': df[selected_feature],
                'y': df['target'],
                'type': 'scatter',
                'mode': 'markers',
                'marker': {'size': 8},
            }
        ],
        'layout': {
            'title': f'Scatterplot of {selected_feature} against Target',
            'xaxis': {'title': selected_feature},
            'yaxis': {'title': 'Target'}
        }
    }

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
