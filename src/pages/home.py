import dash
#from dash import html
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([


    html.Div([
        html.Div([
            html.H2('Introduction', style={'margin-bottom': '10px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '1.5rem', 'text-align': 'left'}),
            html.P("Welcome to our platform. We're excited to have you here! Our project aims to understand the influence of data visualization in the field of Humanities research.", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
            html.P('''Our platform allows users to analyze keywords related to Data Visualization in Humanities journal articles. Users can filter based on their liking to understand how different keywords have been used. Our platform covers 3 Humanities journals''', style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
            html.Ul([
                html.Li("DHQ - Digital Humanities Quarterly", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                html.Li("JCA - Journal of Cultural Analytics", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                html.Li("JOCCH - Journal on Computing and Cultural Heritage", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                
                
                # Add more features as needed
            ]),
            
                        html.P('''WIP''', style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'})
        ], style={'margin-bottom': '30px', 'text-align': 'left', 'padding':'20px'}),
        
        

        html.Div([
                        html.Div([
                html.Div([
                    html.H2('Methodology', style={'margin-bottom': '10px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '1.5rem', 'text-align': 'left'}),
                    html.P(''' Prompt Engineering, LLM : OpenAI GPT 3.5, GPT 4
                    ''', style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                    html.P(''' Vector Database, Pinecone
                    ''', style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                    html.P(''' Programming tools, Python & Plotly Dash
                    ''', style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),                    

                ], style={'margin-bottom': '20px', 'text-align': 'left'})
            ]),
            html.Div([
                html.H2('Subpages', style={'margin-bottom': '10px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '1.5rem', 'text-align': 'left'}),
                html.P("Our platform consists of several subpages that cater to different aspects of our project. Here are some of the main subpages:", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                html.Ul([
                    html.Li(html.A("Home", href="", style={'color': 'white', 'text-decoration': 'none', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'})),  # Adjust link style
                    html.Li(html.A("About", href="/about", style={'color': 'white', 'text-decoration': 'none', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'})),  # Adjust link style
                    html.Li(html.A("Dashboard", href="/dashboard", style={'color': 'white', 'text-decoration': 'none', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}))
                    # Add more subpages with their respective links
                ])
            ], style={'margin-bottom': '30px', 'text-align': 'left'})
        ], style={'padding': '20px', 'background-color': '#333'})  # Adjust background and border styles
    ])
], style={'background-color': 'black'})  # Adjust background color
