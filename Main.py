from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# Load the dataset
#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
df1 = pd.read_excel("1.Manufac Estimation.xlsx",sheet_name="manufac_to_csv")
df2 = pd.read_excel("1.Manufac Estimation.xlsx",sheet_name="completion_to_csv")
df3 = pd.read_excel("1.Manufac Estimation.xlsx",sheet_name="wip_to_csv")
df1["EYM_YearMonth"] = df1['EYM_YearMonth'].astype("str")


# Create the app
app = Dash()

# App layout
app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    
    # Dropdown for selecting country
    dcc.Dropdown(
        options=[{'label': value, 'value': value} for value in df.EMC_Column_Name.unique()],
        value='Direct_Labor',
        id='dropdown-selection1'
    ),
    
    # Dropdown for selecting continent
    # Graph to display the data
    dcc.Graph(id='graph-content')
]

# Callback function
@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection1', 'value')
)
def update_graph(value):
    # Filter the dataframe based on the selected continent and country
    dff = df[(df.EMC_Column_Name == value)]
    # Create the line plot
    return px.line(dff, x='EYM_YearMonth', y='ME_Value', title=f'ME_Value of {value} per YM')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


