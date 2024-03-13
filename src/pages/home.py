import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.Div([
        html.H1('Welcome to Our Project', style={'margin-bottom': '20px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '2rem', 'text-align': 'left'}),
    ], style={'padding': '20px', 'background-color': '#222'}),  # Adjust background and text styles

    html.Div([
        html.Div([
            html.H2('Introduction', style={'margin-bottom': '10px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '1.5rem', 'text-align': 'left'}),
            html.P("Welcome to our platform. We're excited to have you here! Our project aims to... (provide a brief description or introduction of your project here).", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
            html.P("Here are some key features of our platform:", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
            html.Ul([
                html.Li("Feature 1", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                html.Li("Feature 2", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                html.Li("Feature 3", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                # Add more features as needed
            ])
        ], style={'margin-bottom': '30px', 'text-align': 'left', 'padding':'20px'}),

        html.Div([
            html.Div([
                html.H2('Subpages', style={'margin-bottom': '10px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '1.5rem', 'text-align': 'left'}),
                html.P("Our platform consists of several subpages that cater to different aspects of our project. Here are some of the main subpages:", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                html.Ul([
                    html.Li(html.A("Home", href="", style={'color': 'white', 'text-decoration': 'none', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'})),  # Adjust link style
                    html.Li(html.A("About", href="/about", style={'color': 'white', 'text-decoration': 'none', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'})),  # Adjust link style
                    html.Li(html.A("Dashboard", href="/dashboard", style={'color': 'white', 'text-decoration': 'none', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'})),
                    # Add more subpages with their respective links
                ])
            ], style={'margin-bottom': '30px', 'text-align': 'left'}),

            html.Div([
                html.Div([
                    html.H2('Contact', style={'margin-bottom': '10px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '1.5rem', 'text-align': 'left'}),
                    html.P("Have questions or feedback? We'd love to hear from you! Contact us via email or social media:", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                    html.Ul([
                        html.Li("Email: example@example.com", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                        html.Li("Twitter: @example", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                        html.Li("Facebook: /example", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                        # Add more contact information as needed
                    ])
                ], style={'margin-bottom': '30px', 'text-align': 'left'})
            ])
        ], style={'padding': '20px', 'background-color': '#333'})  # Adjust background and border styles
    ])
], style={'background-color': 'black'})  # Adjust background color
