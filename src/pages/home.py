import dash
from dash import html

# Define styles
intro_style = {
    'margin-bottom': '10px',
    'color': 'white',
    'font-family': 'Arial, sans-serif',
    'font-weight': 'bold',
    'font-size': '1.5rem',
    'text-align': 'left'
}

text_style = {
    'color': 'white',
    'font-family': 'Arial, sans-serif',
    'font-size': '1rem',
    'text-align': 'left'
}

link_style = {
    'color': 'white',
    'text-decoration': 'none',
    'font-family': 'Arial, sans-serif',
    'font-size': '1rem',
    'text-align': 'left'
}

title_style = {
    'color': 'white',
    'text-align': 'center',
        'margin': '5px'  # Adjusted margin to decrease padding

}

# Create layout
dash.register_page(__name__, path='/')

layout = html.Div([
    html.Div([
        html.Div([
            html.H2('Introduction', style=intro_style),
            html.P("Welcome to our platform. We're excited to have you here! Our project aims to understand the influence of data visualization in the field of Humanities research.", style=text_style),

            
            html.Div([
                html.H2('Journals', style=intro_style),
                html.Div([
                    html.Div([
                        html.H3("DHQ", style=title_style),
                        html.P("Digital Humanities Quarterly", style=title_style),

                        html.Img(src='assets/dhq.png', alt='DHQ Logo', title='DHQ Logo', style={'width': '264px', 'height': '240px', 'margin-right': '10px', 'align-self': 'center'}),
                    ], style={'text-align': 'center', 'padding-left': '30px', 'padding-right': '30px'}),
                    
                    html.Div([
                        html.H3("DSH", style=title_style),
                        html.P("Digital Scholarship in Humanities", style=title_style),

                        html.Img(src='assets/dsh.png', alt='DSH Logo', title='DSH Logo', style={'width': '264px', 'height': '240px', 'margin-right': '10px', 'align-self': 'center'}),
                    ], style={'text-align': 'center', 'padding-left': '30px', 'padding-right':'30px'}),
                    
                    html.Div([
                        html.H3("JCA", style=title_style),
                        html.P("Journal of Cultural Analytics", style=title_style),

                        html.Img(src='assets/jca.png', alt='JCA Logo', title='JCA Logo', style={'width': '264px', 'height': '240px', 'margin-right': '10px', 'align-self': 'center'}),
                    ], style={'text-align': 'center', 'padding-right': '30px', 'padding-left':'30px'}),
                    
                    html.Div([
                        html.H3("JOCCH", style=title_style),
                        html.P("Journal on Computing and Cultural Heritage", style=title_style),

                        html.Img(src='assets/jocch.png', alt='JOCCH Logo', title='JOCCH Logo', style={'width': '264px', 'height': '240px', 'margin-right': '10px', 'align-self': 'center'}),
                    ], style={'text-align': 'center', 'padding-left': '30px'}),
                ], style={'display': 'flex', 'align-items': 'center', 'flex-wrap': 'wrap', 'margin-bottom': '10px',# 'justify-content': 'center'
                         }),
            ]),
                    ], style={'margin-bottom': '30px', 'text-align': 'left', 'padding': '20px'}),

        html.Div([
            html.Div([
                html.Div([
                    html.H2('Methodology', style=intro_style),
                    html.P("For identification of Data Visualization keywords, Large Language Models (LLMs) such as GPT 3.5 and GPT 4 were utilized. Through prompt engineering involving diverse techniques, effective prompts were tailored for the domain-specific task.", style=text_style),
                    html.P("Following the identification of keywords, data aggregation and summarization was performed across journals and years of publish. Within the dashboard interface, users have the capability to filter by year, journal, and visualization keyword, facilitating the visualization of keyword usage trends across year ranges.", style=text_style),
                ], style={'margin-bottom': '20px', 'text-align': 'left'})
            ]),

        ], style={'padding': '20px', 'background-color': '#333'})  
    ])
], style={'background-color': 'black'})
