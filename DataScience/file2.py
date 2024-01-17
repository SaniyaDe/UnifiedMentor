import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from file1 import correlation_matrix, top_market_cap, top_n

# Load the dataset
df = pd.read_csv("Financial Analytics data.csv", encoding='unicode_escape')

# Drop unnamed columns with all NaN values
df_cleaned = df.dropna(axis=1, how='all')

# Convert to numeric
df_cleaned['Mar Cap - Crore'] = pd.to_numeric(df_cleaned['Mar Cap - Crore'], errors='coerce')
df_cleaned['Sales Qtr - Crore'] = pd.to_numeric(df_cleaned['Sales Qtr - Crore'], errors='coerce')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Financial Analytics Dashboard"),

    # Distribution of Mar Cap - Crore
    dcc.Graph(
        id='mar-cap-histogram',
        figure={
            'data': [
                {
                    'x': df_cleaned['Mar Cap - Crore'],
                    'type': 'histogram',
                    'name': 'Mar Cap - Crore',
                    'marker': {'color': 'blue'}
                }
            ],
            'layout': {
                'title': 'Distribution of Mar Cap - Crore',
                'xaxis': {'title': 'Mar Cap - Crore'},
                'yaxis': {'title': 'Frequency'}
            }
        }
    ),

    # Distribution of Quarterly Sales
    dcc.Graph(
        id='sales-histogram',
        figure={
            'data': [
                {
                    'x': df_cleaned['Sales Qtr - Crore'],
                    'type': 'histogram',
                    'name': 'Sales Qtr - Crore',
                    'marker': {'color': 'green'}
                }
            ],
            'layout': {
                'title': 'Distribution of Quarterly Sales',
                'xaxis': {'title': 'Sales (Crore)'},
                'yaxis': {'title': 'Frequency'}
            }
        }
    ),

    # Top N Companies by Market Capitalization
    dcc.Graph(
        id='top-market-cap-bar',
        figure={
            'data': [
                {
                    'x': top_market_cap['Mar Cap - Crore'],
                    'y': top_market_cap['Name'],
                    'type': 'bar',
                    'orientation': 'h',
                    'marker': {'color': 'viridis'}
                }
            ],
            'layout': {
                'title': f'Top {top_n} Companies by Market Capitalization',
                'xaxis': {'title': 'Market Capitalization (Crore)'},
                'yaxis': {'title': 'Company Name'}
            }
        }
    ),

    # Correlation Matrix
    dcc.Graph(
        id='correlation-heatmap',
        figure={
            'data': [
                {
                    'z': correlation_matrix.values,
                    'x': correlation_matrix.columns,
                    'y': correlation_matrix.index,
                    'type': 'heatmap',
                    'colorscale': 'coolwarm'
                }
            ],
            'layout': {
                'title': 'Correlation Matrix'
            }
        }
    ),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
