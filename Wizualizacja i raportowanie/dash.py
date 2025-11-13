import dash
from dash import dcc, html, Input, Output, dash_table
from dash.dash_table.Format import Format
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
import pandas as pd
import plotly.express as px

# Inicjalizacja aplikacji Dash
app = dash.Dash(__name__)

# Funkcja ładowania danych w zależności od wyboru
def load_data(dataset_name):
    if dataset_name == 'iris':
        data = load_iris()
    elif dataset_name == 'wine':
        data = load_wine()
    elif dataset_name == 'breast_cancer':
        data = load_breast_cancer()
    
    df = pd.DataFrame(data.data, columns=data.feature_names)
    return df

# Layout aplikacji
app.layout = html.Div([
    html.H1("Lab Dash App"),

    # Dropdown do wyboru datasetu
    dcc.Dropdown(
        id='dataset-dropdown',
        options=[
            {'label': 'Iris', 'value': 'iris'},
            {'label': 'Wine', 'value': 'wine'},
            {'label': 'Breast Cancer', 'value': 'breast_cancer'}
        ],
        value='iris'
    ),
    
    # DataTable do wyświetlania danych
    dash_table.DataTable(
        id='table',
        style_table={'overflowX': 'auto'},
        page_size=5,  # Maksymalnie 5 wierszy na stronie
        style_cell={'textAlign': 'center'},
    ),
    
    # Radiobutton do wyboru kolumny do histogramu
    dcc.RadioItems(
        id='column-radio',
        value='sepal length (cm)',  # Domyślnie pierwsza kolumna
        labelStyle={'display': 'block'},
    ),

    # Wykres histogramu
    dcc.Graph(id='histogram')
])

# Callback do aktualizacji tabeli na podstawie wybranego zbioru danych
@app.callback(
    [Output('table', 'columns'),
     Output('table', 'data'),
     Output('column-radio', 'options')],
    [Input('dataset-dropdown', 'value')]
)
def update_table(dataset_name):
    df = load_data(dataset_name)
    columns = [{'name': col, 'id': col} for col in df.columns]
    options = [{'label': col, 'value': col} for col in df.columns]
    return columns, df.to_dict('records'), options

# Callback do aktualizacji histogramu na podstawie wybranej kolumny
@app.callback(
    Output('histogram', 'figure'),
    [Input('column-radio', 'value'),
     Input('dataset-dropdown', 'value')]
)
def update_histogram(selected_column, dataset_name):
    df = load_data(dataset_name)
    fig = px.histogram(df, x=selected_column, nbins=20, title=f'Histogram of {selected_column}')
    return fig

# Uruchomienie aplikacji
if __name__ == '__main__':
    app.run_server(debug=True)


