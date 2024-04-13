import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([
    html.Div([
        html.H1('Funding Agencies & Participants', style={'margin-bottom': '20px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '2rem', 'text-align': 'left'}),
    ], style={'padding': '20px', 'background-color': '#222'}),  # Adjust background and text styles

    html.Div([
        html.Div([
            html.H2('Learn more about the group here:', style={'margin-bottom': '10px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '1.5rem', 'text-align': 'left'}),
            html.P("04/12/24", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
            html.P("Home & About Page are a WIP", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
            html.P("Please come back again!", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
        ], style={'margin-bottom': '30px', 'text-align': 'left', 'padding':'20px'}),

        html.Div([

            html.Div([
                html.Div([
                    html.H2('Team & Collaborators', style={'margin-bottom': '10px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '1.5rem', 'text-align': 'left'}),
                    html.P("Prof. Rongqian Ma, Assistant Professor, Luddy School of Informatics", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                    html.P("Amar Ananth, Data Science Graduate, Luddy School of Informatics", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),

                ], style={'margin-bottom': '30px', 'text-align': 'left'})
            ])
        ], style={'padding': '20px', 'background-color': '#333'})  # Adjust background and border styles
    ])
], style={'background-color': 'black'})  # Adjust background color

