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
        html.H1('Distributions of Articles', style=heading_style),
        html.Div([
                    html.Img(src='assets/article_pc.png', style={'width': '500px', 'height': '500px', 'margin-right':'10px'}),                            
            html.Img(src='assets/article_sb.png', style={'width': '850px', 'height': '500px', 'margin-right': '10px'})

                ], style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '10px'}),

    ], style={'padding': '20px', 'background-color': '#222'}),

    html.Div([


        html.Div([
            html.Div([
                html.H2('Distribution of Figures', style=heading_style),
                html.Div([

                    html.Img(src= 'assets/FL_bc.png', style={'width': '1000px', 'height': '500px', 'margin-left': '180px'}),

                ], style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '10px'}),

            ], style={'margin-bottom': '0px', **common_style, 'padding': '20px'})
        ], style={'background-color': '#333'}),
    ]),
    
html.Div([


        html.Div([
            html.Div([
                html.H2('Word Clouds by Journal', style=heading_style),
                html.Div([

                    html.Img(src= 'assets/WC_DHQ.png', style={'width': '450px', 'height': '300px', 'margin-right': '10px'}),
                    html.Img(src= 'assets/WC_DSH.png', style={'width': '450px', 'height': '300px', 'margin-right': '10px'}),
                    html.Img(src= 'assets/WC_JCA.png', style={'width': '450px', 'height': '300px', 'margin-right': '10px'}),

                ], style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '10px'}),

            ], style={'margin-bottom': '10px', **common_style, 'padding': '20px'})
        ], style={'background-color': 'black'})
    ])
], style={'background-color': 'black'})
