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
            html.P('''How do visuals speak, and what do they contribute to humanities scholarship? Visualization has long been recognized as a valuable device for knowledge discovery and communication in scientific research. Studies in science and technology show that visualization serves an epistemic role as "immutable mobiles," transmitting scientific findings and ideas across contexts, and indicating the disciplinarity and evolution of scientific fields. While visual technologies have become a convention in scientific research, their adoption in digital humanities (DH) scholarly communication is relatively recent.''', style=text_style), 
            
            html.P('''We still know little about the functions of visual languages in DH scholarship and their role in creating dynamic scholarly accounts. Understanding this will provide insights into how DH knowledge is built, dispersed, and communicated to wider audiences, and how DH evolves as an interdisciplinary research domain with a collaborative workforce. Our ongoing project takes an important first step by highlighting the evolution of visual concepts in DH and facilitating interactions with these concepts through the dashboard. ''', style=text_style),

            
            html.Div([
                html.H2('Journals', style=intro_style),
                html.Div([
                    html.Div([
                        html.H3("DHQ", style=title_style),
                        html.P("Digital Humanities Quarterly", style=title_style),

                                  html.A(
                        html.Img(src='assets/dhq.png', alt='DHQ Logo', title='DHQ Logo', style={'width': '264px', 'height': '240px', 'margin-right': '10px', 'align-self': 'center'}),
                                        href='https://www.digitalhumanities.org/dhq/',
                target='_blank'),   # This will open the URL in a new tab
                        html.P("""DHQ is a peer-reviewed open-access journal that publishes scholarly work at the intersection of digital technology and the humanities disciplines. DHQ covers a wide range of topics, including digital tools and methods for humanities research, digital humanities projects, and theoretical reflections on the implications of digital technology for humanistic inquiry.
                        """, style={**title_style, 'width': '264px',
                                       'text-align': 'left'}),
                    ], style={'text-align': 'center', 'padding-left': '30px', 'padding-right': '30px'}),
                    
                    html.Div([
                        html.H3("DSH", style=title_style),
                        html.P("Digital Scholarship in the Humanities", style=title_style),
                                  html.A(
                        html.Img(src='assets/dsh.png', alt='DSH Logo', title='DSH Logo', style={'width': '264px', 'height': '240px', 'margin-right': '10px', 'align-self': 'center'}),
                                        href='https://academic.oup.com/dsh',
                target='_blank'),                                               html.P("""DSH publishes peer-reviewed scholarly articles, reviews, and other content related to the intersection of digital technology and humanities research. DSH covers topics such as digital methods and tools for humanities scholarship, computational approaches to analyzing cultural artifacts, and critical reflections on the impact of digital technology on humanistic inquiry.
                        """, style={**title_style, 'width': '264px',
                                       'text-align': 'left'})   # This will open the URL in a new tab),
                    ], style={'text-align': 'center', 'padding-left': '30px', 'padding-right':'30px'}),
                    
                    html.Div([
                        html.H3("JCA", style=title_style),
                        html.P("Journal of Cultural Analytics", style=title_style),

                                  html.A(
                html.Img(
                    src='assets/jca.png',
                    alt='JCA website',
                    title='JCA website',
                    style={'width': '264px', 'height': '240px', 'margin-right': '10px', 'align-self': 'center'}
                ),
                href='https://culturalanalytics.org/',
                target='_blank'   # This will open the URL in a new tab
)
                        
                        ,                        html.P("""JCA is a relatively new but significant publication in the realm of digital humanities and computational cultural studies. It focuses on the intersection of computational methods, data analytics, and cultural research. JCA publishes peer-reviewed articles, essays, and reviews that explore various aspects of cultural analysis using computational techniques.
                        """, style={**title_style, 'width': '264px',
                                       'text-align': 'left'})
                    ], style={'text-align': 'center', 'padding-right': '30px', 'padding-left':'30px'}),
                    
                    html.Div([
                        html.H3("JOCCH", style=title_style),
                        html.P("Journal on Computing and Cultural Heritage", style=title_style),
                                  html.A(

                        html.Img(src='assets/jocch.png', alt='JOCCH Logo', title='JOCCH Logo', style={'width': '264px', 'height': '240px', 'margin-right': '10px', 'align-self': 'center'}),
                        href='https://dl.acm.org/journal/jocch', 
                        target='_blank'),    html.P("""JOCCH is a scholarly publication that focuses on the intersection of computing and the cultural heritage sector. JOCCH publishes articles, case studies, that explore how computational methods, tools, and technologies are applied to the study, preservation, and dissemination of cultural heritage. It includes a range of topics, digital libraries, digital archiving, digital humanities, and more. 
                        """, style={**title_style, 'width': '264px',
                                       'text-align': 'left'})
                    ], style={'text-align': 'center', 'padding-left': '30px'}),
                ], style={'display': 'flex', 'align-items': 'center', 'flex-wrap': 'wrap', 'margin-bottom': '10px',# 'justify-content': 'center'
                         }),
            ]),
                    ], style={'margin-bottom': '30px', 'text-align': 'left', 'padding': '20px'}),
        
html.Div([
    html.Div([
        html.Div([
            html.H2([html.A('Dataset Page', href='/dataset', style=intro_style)]),
            html.P("This page offers a descriptive statistical analysis of published DH articles and the figures included in them. The analysis covers journals such as DHQ, DSH, and JCA, examining data at the journal, year, and figure levels. The featured graphs highlight the distribution of articles and figures and the frequently used words in DH scholarship to describe visual concepts in the articles.", style=text_style)
            
        ], style={'margin-bottom': '20px', 'text-align': 'left'})
    ], style={'flex-basis': '50%', 'margin-right': '70px', 'margin-left': '10px'}),  # This div will take 50% of the width
    
    html.Div([
        html.Div([
            html.H2([html.A('Dashboard Page', href='/dashboard', style=intro_style)]),
            html.P('''The dashboard offers an interactive exploration of the evolution of key visual concepts featured in the DHQ, JOCCH, and JCA journals, allowing users to filter article abstract data by year, journal, and visual concepts.                    
                   ''', style=text_style),
            

        ], style={'margin-bottom': '20px', 'text-align': 'left'})
    ], style={'flex-basis': '50%', 'margin-left': '70px', 'margin-right': '50px'}),  # This div will take 50% of the width
    
], style={'display': 'flex', 'padding': '20px', 'background-color': '#111'})

,
        

        html.Div([
            html.Div([
html.Div([
    html.H2('Methodology', style=intro_style),
    html.P(
        "For identification of Data Visualization keywords, Large Language Models (LLMs) such as GPT 3.5 and GPT 4 were utilized. Through prompt engineering involving diverse techniques, effective prompts were tailored for the domain-specific task. Techniques utilized included:",
        style=text_style
    ),
    html.Ul([
        html.Li("Few-shot learning"),
        html.Li("Persona pattern"),
        html.Li("Chain of thought prompting"),
        html.Li("Retrieval Augmented Generation")
    ], style=text_style),
    html.P(
        ['''To identify key visual concepts, we utilized Large Language Models (LLMs) such as GPT-3.5 and GPT-4. Effective prompts were tailored for the domain-specific task using diverse techniques, including few-shot learning, persona patterns, chain of thought prompting, and retrieval-augmented generation. In addition to identifying and validating key concepts, we scraped, processed, analyzed, and visualized full-text articles published in the four DH journals, providing a statistical overview of our data corpus. This interface was built with Python dashboarding libraries like Dash/Plotly and MatPlotlib. The interface is currently hosted as a web service on the Render platform.  Iterations of the analysis and experiments are documented in
        ''',        html.A('this Github repository', href='https://github.com/rongqianma/DH_KeyConcepts', target='_blank', style={'color': 'white'}),
        ],
        style=text_style
    ),
], style={'margin-bottom': '20px', 'text-align': 'left'})

            ]),

        ], style={'padding': '20px', 'background-color': '#333'})  
    ])
], style={'background-color': 'black'})
