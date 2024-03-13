import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([
    html.Div([
        html.H1('About Us: Exploring Cutting-Edge Research', style={'margin-bottom': '20px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '2rem', 'text-align': 'left'}),
    ], style={'padding': '20px', 'background-color': '#222'}),  # Adjust background and text styles

    html.Div([
        html.Div([
            html.H2('Our Agenda', style={'margin-bottom': '10px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '1.5rem', 'text-align': 'left'}),
            html.P("At [Your Organization], our mission is to delve into the forefront of research, exploring innovative ideas, and sharing valuable insights with the world. We aim to foster a community of curious minds and facilitate the exchange of knowledge to drive progress and innovation.", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
        ], style={'margin-bottom': '30px', 'text-align': 'left', 'padding':'20px'}),

        html.Div([
            html.Div([
                html.H2('Journals', style={'margin-bottom': '10px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '1.5rem', 'text-align': 'left'}),
                html.P("Our platform provides access to a curated selection of prestigious academic journals, covering a wide array of disciplines. From the latest advancements in science and technology to groundbreaking social and humanitarian research, our journals offer comprehensive insights into various fields of study.", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                html.P("Through our platform, users can stay updated on the most recent publications, explore interdisciplinary connections, and engage with scholarly discourse.", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
            ], style={'margin-bottom': '30px', 'text-align': 'left'}),

            html.Div([
                html.Div([
                    html.H2('Our Team', style={'margin-bottom': '10px', 'color': 'white', 'font-family': 'Arial, sans-serif', 'font-weight': 'bold', 'font-size': '1.5rem', 'text-align': 'left'}),
                    html.P("Behind [Your Organization] is a dedicated team of researchers, educators, and enthusiasts passionate about advancing knowledge and promoting intellectual exchange.", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                    html.P("Our team members bring diverse expertise and backgrounds, ranging from academia to industry, united by a common goal of facilitating access to cutting-edge research and fostering a culture of lifelong learning.", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                    html.P("We are committed to providing our users with a seamless and enriching experience, continuously improving our platform to meet the evolving needs of our community.", style={'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '1rem', 'text-align': 'left'}),
                ], style={'margin-bottom': '30px', 'text-align': 'left'})
            ])
        ], style={'padding': '20px', 'background-color': '#333'})  # Adjust background and border styles
    ])
], style={'background-color': 'black'})  # Adjust background color

