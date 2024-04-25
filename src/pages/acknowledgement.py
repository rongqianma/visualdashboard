import dash
from dash import html

dash.register_page(__name__)

# Common styles
common_style = {
    'color': 'white',
    'font-family': 'Arial, sans-serif',
    'text-align': 'left'
}

# Styles for headings
heading_style = {
    'margin-bottom': '10px',
    'font-weight': 'bold',
    'font-size': '1.5rem',
    **common_style
}

# Styles for paragraphs
paragraph_style = {
    'font-size': '1rem',
    **common_style
}

# Layout
layout = html.Div([
    html.Div([
        html.H1('Funding Agencies & Participants', style=heading_style),
        html.Div([
                    html.Img(src='assets/luddy.png', style={'width': '240px', 'height': '225px', 'margin-right': '10px'}),                    html.Img(src= 'assets/idah.png', style={'width': '240px', 'height': '225px', 'margin-right': '10px'}),


                ], style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '10px'})
    ], style={'padding': '20px', 'background-color': '#222'}),

    html.Div([


        html.Div([
            html.Div([
                html.H2('Team & Collaborators', style=heading_style),
                html.Div([
                    html.Img(src='assets/prof_rongqian_ma.png', style={'width': '220px', 'height': '300px', 'margin-right': '10px'}),                    html.Img(src= 'assets/prof_li.png', style={'width': '220px', 'height': '300px', 'margin-right': '10px'}),
                    html.Img(src= 'assets/ranvir_singh.png', style={'width': '220px', 'height': '300px', 'margin-right': '10px'}),
                    html.Img(src= 'assets/sagar_prabhu.png', style={'width': '220px', 'height': '300px', 'margin-right': '10px'}),
                    html.Img(src= 'assets/amar_ananth.png', style={'width': '220px', 'height': '300px', 'margin-right': '10px'}),

                ], style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '10px'}),

            ], style={'margin-bottom': '10px', **common_style, 'padding': '20px'})
        ], style={'background-color': '#333'}),
            html.Div([
            html.H2('Last Update: internal use only', style=heading_style),
            html.P("04/24/24", style=paragraph_style),
        ], style={'margin-bottom': '10px', **common_style, 'padding': '20px'}),
    ])
], style={'background-color': 'black'})
