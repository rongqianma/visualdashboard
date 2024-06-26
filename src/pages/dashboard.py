import numpy as np
import pandas as pd
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import dash
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc


dash.register_page(__name__)


keywords_to_exclude = []  # Add your keywords here
# Read data from CSV files
df_1 = pd.read_csv("viz_1.csv").query("Journal != 'Total'")
df_1 = df_1[~df_1["Keyword"].isin(keywords_to_exclude)]

df_2 = pd.read_csv("updated_viz_2.csv").iloc[:, 1:]
df_2 = df_2[~df_2["Keyword"].isin(keywords_to_exclude)]

df_3 = pd.read_csv("viz_table.csv")
df_3 = df_3[~df_3["Keyword"].isin(keywords_to_exclude)]

# Calculate total yearly and proportion of articles with keyword
df_2["yearly_total"] = df_2["DHQ_yearly_total"] + df_2["JCA_yearly_total"] + df_2["JOOCH_yearly_total"] +  df_2["DSH_yearly_total"]

df_2["proportion of articles with keyword"] = round( (df_2["# of articles keyword DHQ"] + df_2["# of articles keyword JCA"] + df_2["# of articles keyword JOCCH"] + df_2["# of articles keyword DSH"]) / df_2["yearly_total"], 3)

# Data cleaning for table
df_table = df_2[['Keyword', 'Significance score', 'Rank', 'Year', '# of articles keyword DHQ',
                 '# of articles keyword JCA', '# of articles keyword JOCCH', '# of articles keyword DSH']].rename(columns={
    'Keyword': 'Keyword', 'Significance score': 'Significance score', 'Rank': 'Rank', 
    'Year': 'Year', '# of articles keyword DHQ': 'DHQ', '# of articles keyword JCA': 'JCA', 
    '# of articles keyword JOCCH': 'JOCCH', '# of articles keyword DSH': 'DSH'
}).drop_duplicates()

# List of unique keywords
unique_keywords = df_2['Keyword'].unique().tolist()

# Define dictionaries for journal data
journal_yearly_dict = {'JCA' : 'JCA_yearly_total',
           'DHQ' : 'DHQ_yearly_total', 
           'JOCCH' : 'JOOCH_yearly_total',
                      'DSH' : 'DSH_yearly_total'}

journal_keyword_dict = {'JCA' : '# of articles keyword JCA',
           'DHQ' : '# of articles keyword DHQ', 
           'JOCCH' : '# of articles keyword JOCCH',
                       'DSH' : '# of articles keyword DSH'}

distinct_colors = [
    '#FF5733', '#FFA500', '#B22222', '#008080',  # Reds, Yellows, Gold, Green, Teal
    '#0000FF', 'lightgreen', '#FF00FF', '#808080', '#000000',  # Blue, Purple, Magenta, Gray, Black
    '#00FF00', '#00FFFF', 'white', '#6A5ACD', 'darkred',  # Lime, Cyan, Dark Blue, Slate Blue, Deep Pink
    '#FF69B4', 'red', 'yellow', '#4682B4', '#556B2F',  # Hot Pink, Tomato, Light Salmon, Steel Blue, Dark Olive Green
    '#8A2BE2', '#8B008B', '#000080', '#4B0082', 'lightblue',  # Blue Violet, Dark Magenta, Navy, Indigo, Chartreuse
    'lightpink', '#00BFFF', '#00FA9A', '#6495ED', '#008000',  # Orange Red, Deep Sky Blue, Medium Spring Green, Medium Purple, Fire Brick
    '#800080', '#A52A2A', '#5F9EA0', '#D2691E', '#FF1493',  # Purple, Brown, Cadet Blue, Chocolate, Deep Pink
    '#7FFF00', '#BDB76B', '#8FBC8F', '#FF4500', '#00FF7F', '#FFC300'  # Crimson, Turquoise, Dark Red, Spring Green, Green Yellow
]

df_4 = df_2[["Year","DHQ_yearly_total", "JCA_yearly_total", "JOOCH_yearly_total", "DSH_yearly_total", "yearly_total"]].drop_duplicates()
df_4.columns = ["Year", "DHQ", "JCA", "JOCCH", "DSH", "Total"]

table_columns = ['Visualization Keyword','Significance score', 'Rank', 'DHQ', 'JCA', 'JOCCH' ,'DSH']

header_style = {'textAlign': 'center',
                'color': '#4a90e2',  # Blue color
                'fontSize': '36px',  # Larger font size
                'fontFamily': 'Arial, sans-serif',  # Elegant font family
                'fontWeight': 'bold',  # Bold text
                'textTransform': 'uppercase',  # Uppercase text
                'letterSpacing': '1px',  # Spacing between letters
                'marginBottom': '20px'}

custom_font = {'fontFamily': 'Arial, sans-serif'}
drop_down_div = {#'textAlign': 'center', 
    'margin': 'auto', 'fontcolor' : 'red', 
                 'backgroundColor': '#1E1E1E',  **custom_font}


drop_down = {'margin': 'auto','backgroundColor': '#1E1E1E', 
                               'color': '#4a90e2', **custom_font, 'padding-up':'5px'}


layout = html.Div(
    style={'backgroundColor': '#1E1E1E'}, 
    children=[

        
        html.Div('<br>', style={'color':'#1E1E1E'}),

        # Slider
        html.Div(className='row', 
        children=[
            html.Div(className='twelve columns', 
                children=[
                        # Text for Slider
                        html.Div([
                            html.Div(id='slider-tooltip', 
                                     style={'color': 'white', **custom_font, 
                                            'padding-left':'8px'}
                                ),
                        #Slider
                        dcc.RangeSlider(
                            id='year-range-slider',
                            min=2007,
                            max=2024,
                            step=1,
                            value=[2007, 2024],
                            marks={str(year): {'label': str(year), 
                                               'style': {'fontSize': '120%','color': 'white'}} 
                                   for year in range(2007, 2025)}


                            ),
                        ], style={'width': '60%', 'margin': 'auto'})])]
                ),
        
        html.Div('<br>', style={'color':'#1E1E1E'}),
        
        # Journal Dropdown
        html.Div(
            className='four columns',
            style={**drop_down_div, 'width': '58%','color' : 'red'},  # Adjust width here
            children=[
                dmc.MantineProvider(
                    inherit=True,
                    theme={
                        "components": {
                            "InputWrapper": {
                                "styles": {
                                    "label": {
                                        "color": "white",
                                        "font-size": "20px",
                                    },
                                    "description": {
                                        "color": "white",
                                       "font-size": "14px",
                                    },
                                }
                            },
                            "Input": {
                                "styles": {
                                    "placeholder": {"color": "red"}
                                },
                            },
                        }
                    },
                    
                    children=[
                dmc.MultiSelect(
                    label="Select Journal",
                    description="You can select mutliple journals.",
                    id='journal-dropdown',
                    data=[
                        {'label': 'DHQ', 'value': 'DHQ'},
                        {'label': 'JCA', 'value': 'JCA'},
                        {'label': 'JOCCH', 'value': 'JOCCH'},
                        {'label': 'DSH', 'value': 'DSH'}

                    ],
                    clearable=True,
                    searchable=True,
                    nothingFound="No options found",
                    #multi=True,
                    placeholder="Select Humanities Journal",
                    style={'margin-bottom' : '5px', 'margin-up' : '5px'
                          })
                    ],
                )
            ]),
            
        html.Div('<br>', style={'color':'#1E1E1E'}),

        # Keyword Drop down
        html.Div(
            className='four columns',
            style={**drop_down_div, 'width': '58%'},  # Adjust width here
            children=[                
                dmc.MantineProvider(
                    inherit=True,
                    theme={
                        "components": {
                            "InputWrapper": {
                                "styles": {
                                    "label": {
                                        "color": "white",
                                        "font-size": "20px",

                                        #"backgroundColor": dmc.theme.DEFAULT_COLORS["yellow"][1],
                                    },
                                    "description": {
                                        "color": "white",
                                       "font-size": "14px",

                                        #"backgroundColor": dmc.theme.DEFAULT_COLORS["yellow"][1],
                                    },
                                }
                            },
                            "Input": {
                                "styles": {
                                    "hidden": {"color": dmc.theme.DEFAULT_COLORS["violet"][4]}
                                },
                            },
                        }
                    },
                    
                    children=[
                dmc.MultiSelect(
                    label="Select Visualization Keyword",
                    description="You can select multiple keywords ",
                    id='keyword-dropdown',
                    data=[
                        {'label': keyword, 'value': keyword} for keyword in unique_keywords
                    ],
                    clearable=True,
                    searchable=True,
                    nothingFound="No options found",

                    #multi=True,
                    placeholder="Select Visualization Keyword",
                    style={'margin-bottom' : '5px', 'color':'red'})])]),
            

        html.Div('<br>', style={'color':'#1E1E1E'}),

        # Cards for displaying number of articles for each journal
        html.Div(className='row', 
                 style={'display': 'flex', 'justify-content': 'space-between',
                        'width': '100%', 'padding-bottom': '5px','padding-top': '5px' }, 
                 children=[
                    # Card 1: Total no. of articles
                    html.Div(className='three columns', style={'paddingLeft': '1px',  'width': '100%'}, 
                             children=[html.Div(id='total-articles-card', style={'background-color':'#333333',
                                                                                 'padding' : '10px',
                                                                                 'text-align': 'center',
                                                                                 'border': '0.3px solid #FFFFFF',
                                                                                 **drop_down,
                                                                                'color':'white'})]
                    ),
                    # Card 2: DHQ no. of articles
                    html.Div(className='three columns', style={'width': '100%'}, 
                             children=[html.Div(id='dhq-articles-card', style={'background-color': '#333333', 
                                                                               'color': '#FFFFFF','padding' : '10px',
                                                                               'text-align': 'center',
                                                                               'border': '0.3px solid #FFFFFF', **drop_down,
                                                                                'color':'white'})]
                    ),
                    # Card 3: JCA no. of articles
                    html.Div(className='three columns', style={'width': '100%'}, 
                             children=[html.Div(id='jca-articles-card', style={'background-color': '#333333', 
                                                                               'color': '#FFFFFF','padding' : '10px',
                                                                               'text-align': 'center',
                                                                               'border': '0.3px solid #FFFFFF', **drop_down,
                                                                                'color':'white'})]
                    ),                    
                     # Card 4: DSH no. of articles
                    html.Div(className='three columns', style={'width': '100%'}, 
                             children=[html.Div(id='dsh-articles-card', style={'background-color': '#333333', 
                                                                               'color': '#FFFFFF','padding' : '10px',
                                                                               'text-align': 'center',
                                                                               'border': '0.3px solid #FFFFFF', **drop_down,
                                                                                'color':'white'})]
                    ),
                    # Card 4: JOCCH no. of articles
                    html.Div(className='three columns', style={'paddingRight': '1px', 'width': '100%'}, 
                             children=[html.Div(id='jocch-articles-card', style={'background-color': '#333333', 
                                                                                 'color': '#FFFFFF','padding' : '10px',
                                                                                 'text-align': 'center',
                                                                                 'border': '0.3px solid #FFFFFF', **drop_down,
                                                                                'color':'white'})]
                )]
        ),
        
        
        html.Div('<br>', style={'color':'#1E1E1E'}),

        #Graphs Div
        html.Div(
            className='row',
            children=[
                html.Div(className='twelve columns', 
                         children=[
                        # Graph 1
                        html.Div(className='twelve columns', style={'display': 'inline-block','width':'100%',
                                                                #'padding-left': '5px',
                                                                #'padding-right': '5px',
                                                                  'padding-bottom': '5px'}, 
                                 children=[dcc.Graph(id='histo-chart-final')
                        ]),
                        # Graph 2
                        html.Div(className='twelve columns', style={#'padding-left': '5px', 
                                                                    #'padding-right':'5px',
                                                                    'width':'100%',
                                                                    'display': 'inline-block',
                                                                    #'padding-bottom': '5px'
                        }, 
                                 children=[dcc.Graph(id='second-chart-final')
                        ])])
            ]),

        html.Div('<br>', style={'color':'#1E1E1E'}),
        # Table section
        html.Div(className='row', 
            children=[
                dash_table.DataTable(
                    data=[],
                    columns=[{'name': col, 'id': col} for col in table_columns],
                    tooltip_header={
                        'Visualization Keyword': {'value': '''Visualization Keyword:      
                        The data visualization keyword is identified from article abstracts. 
                        OpenAI GPT 3.5 was used in order to identify relevant concepts.''', 'type': 'markdown'},

                        'Significance score': {'value': '''Significance score: [0,1]     
                        The significance score is computed using OpenAI GPT 4. 
                        Higher the value, the more relevant it is in the context of data visualization.''', 'type': 'markdown'},

                        'Rank': {'value': '''Rank: [1,30]    
                        Computed based on a visualizaion keyword\'s significance score and its occurrence across all journals. 
                        If two keywords have the same significance score, the keyword that occurs more frequently 
                        has a lower rank.''', 'type': 'markdown'}
                        ,

                        'DHQ': {'value': '''DHQ:     
                        This signifies the number of times a specific keyword occurred in DHQ in the selected year range.''',
                                'type': 'markdown'},

                        'JCA': {'value': '''JCA:     
                        This signifies the number of times a specific keyword occurred in JCA in the selected year range.''',
                                'type': 'markdown'},

                        'JOCCH': {'value': '''JOCCH:     
                        This signifies the number of times a specific keyword occurred in JOCCH in the selected year range.''',
                                  'type': 'markdown'},
                        'DSH': {'value': '''DSH:     
                        This signifies the number of times a specific keyword occurred in DSH in the selected year range.''',
                                  'type': 'markdown'}}
                    ,

                    # Style headers with a dotted underline to indicate a tooltip
                    style_header_conditional=[{
                        'if': {'column_id': col},
                        'textDecoration': 'underline',
                        'textDecorationStyle': 'dotted',
                    } for col in table_columns],

                    # Overflow into ellipsis
                    style_cell={
                        'overflow': 'hidden',
                        'textOverflow': 'ellipsis',
                        'maxWidth': 0,
                        'textAlign': 'center',  # Center align cell content
                        'fontSize': '14px',
                        'fontFamily': 'Arial, sans-serif',
                        'padding': '8px',
                        'color': '#FFFFFF',
                        'backgroundColor': '#333333',  # Cell background color
                    },
                    tooltip_delay=0,
                    tooltip_duration=None,
                    page_size=11,
                    style_table={
                        'overflowX': 'auto',
                        'border': '1px solid #FFFFFF',
                        'background-color': '#333333',  # Dark background color
                        'color': '#FFFFFF',  # Text color
                    },
                    style_header={
                        'backgroundColor': '#1E1E1E',  # Header background color
                        'fontWeight': 'bold',
                        'border': '1px solid #FFFFFF',
                        'color': '#FFFFFF',  # Header text color
                        'text-align': 'center',  # Center align header text
                    },
                    style_data={
                        'whiteSpace': 'normal',
                        'height': 'auto',
                        'border': '1px solid #FFFFFF',
                        'text-align': 'center',  # Center align data cells
                    },
                    id='my-datatable'
                ),

            ]
        )


        
])








# Callback to update tooltip
@callback(
    Output('slider-tooltip', 'children'),
    [Input('year-range-slider', 'value')]
)
def update_tooltip(value = None):
    tooltip_style = {
        'color': 'white',
        #'font-weight': 'bold',
        'padding': '10px',
        'display': 'inline-block',
        'font-size': '20px',
        'font-weight': '500',
        'word-break': 'break-word',
        #'border': '1px solid white',
        #'border-radius': '5px',
        #'display': 'inline-block',
        #'background-color': '#282c34',  # Lighter shade of #282c34 with increased opacity (80%)

    }
    return html.Div([
        html.Div([
            html.Div(f'Select Year Range', style={'margin-bottom': '3px'}),
            html.Div(f'You can drag slider to set start and end year.', style={'margin-bottom': '5px',
                                                                            'font-size': '14px'}),
            #html.Div(f'{value[0]} - {value[1]}', style={'font-size': '12px',
             #                                                  'font-weight': 'bold',})
        ], style=tooltip_style)
    ])

@callback(
    Output('my-datatable', 'data'),
    [Input('journal-dropdown', 'value'),
     Input('keyword-dropdown', 'value'),
    Input('year-range-slider', 'value'),
    ])

def update_table(selected_journals, selected_keywords, year_range):
    
    filtered_df = df_table[(df_table['Year'] >= year_range[0]) & (df_table['Year'] <= year_range[1])]

    selected_keywords = selected_keywords or unique_keywords
    final_df = filtered_df[filtered_df['Keyword'].isin(selected_keywords)].groupby(['Keyword', 
                                                                                    'Significance score',
                                                                                    'Rank']).sum().reset_index()

    selected_journals = selected_journals or ["DHQ", "JOCCH", "JCA", "DSH"]
    

    
    final_df.rename(columns={"Keyword": "Visualization Keyword"}, inplace=True)
    
    final_df = final_df[['Visualization Keyword', 
                         'Significance score', 
                         'Rank'] + selected_journals].sort_values(by = "Rank")
    return final_df.to_dict('records')


@callback(
    Output('histo-chart-final', 'figure'),
    [Input(component_id='journal-dropdown', component_property='value'),
     Input('keyword-dropdown', 'value'),
    Input('year-range-slider', 'value'),
    ])

def update_graph(selected_journals, selected_keywords, year_range):
    
    filtered_df = df_2[(df_2['Year'] >= year_range[0]) & (df_2['Year'] <= year_range[1])]
    
    selected_keywords = selected_keywords or unique_keywords
    filtered_df = filtered_df[filtered_df["Keyword"].isin(selected_keywords)]
    
    selected_journals = selected_journals or ["DHQ", "JOCCH", "JCA", "DSH"]
    cols_selected = ["# of articles keyword "+ journal for journal in selected_journals]
    df_update = filtered_df.groupby(["Keyword", 
                                     "Significance score", 
                                     "Rank", 
                                     "Size"]).sum()[cols_selected].reset_index().fillna(0)

    year_df = df_4[(df_4['Year'] >= year_range[0]) & (df_4['Year'] <= year_range[1])][["DHQ","JCA", "JOCCH", "DSH"]].sum()
        
    for journal in selected_journals:
        df_update[journal] = df_update["# of articles keyword " + journal] / year_df[journal]

    
    df_update.replace(np.inf, 0, inplace = True)
    df_update = pd.melt(df_update, id_vars=['Keyword', 'Significance score', 'Rank', 'Size'], 
                value_vars=selected_journals, 
                var_name='Journal', value_name='% of articles')
    
    
    filtered_df = df_update[df_update["% of articles"] > 0]
    filtered_df = filtered_df.sort_values(by = "Rank")


    fig = px.scatter(filtered_df, 
                     y='Journal', 
                     x="% of articles", 
                     size="Size", 
                     color="Keyword",
                     size_max=30, 
                     opacity = 0.5,
                     hover_data={"Keyword": True, 
                                 "Significance score": True,
                                 "% of articles": True, 
                                 "Rank": True, 
                                 "Size": False,
                                 "Journal": False,
                                 "Journal":True,
                                 "% of articles":False
                                }, 
                     color_discrete_sequence=distinct_colors)

    fig.update_traces(marker=dict(line=dict(width=0.2)))
    fig.update_yaxes(title_text="Digital Humanities Journal",
                     showgrid=False)
    
    fig.update_xaxes(title_text="% of Articles with Visualization Keyword",
                     tickformat='.2%', 
                     showgrid=True,
                     gridcolor='#404040',
                     gridwidth=0.1)
    
    fig.update_traces(showlegend=True)
    for trace in fig.data:
        trace.marker.line.width = 0
        
    fig.update_layout(
        plot_bgcolor='#2b2b2b',  # Dark background color of the plot
        paper_bgcolor='#2b2b2b',  # Dark background color of the figure
        font={'color': '#FFFFFF'},  # Light text color
        title={'text': "<b> Graph 1 : Distribution of visualization keywords across journals <b>",  
               'font': {'size': 16, 'color': '#FFFFFF'},
               #'x': 0.1
              },  # Title of the plot with center alignment
        margin=dict(l=100, t=75, b=75, r=200),  
        legend=dict(
            traceorder='normal',  
            bordercolor='Black',  
            borderwidth=1, 
            itemclick="toggleothers",
            x = 0.99
            #itemclick=False, 
            #itemdoubleclick=False
        )
    )

    return fig

# Callback to update the second graph with provided plot data
@callback(
    Output('second-chart-final', 'figure'),
    [Input(component_id='journal-dropdown', component_property='value'),
    Input('keyword-dropdown', 'value'),
    Input('year-range-slider', 'value'),
])

def update_second_graph(selected_journals, selected_keywords, year_range ):
        
    plot_df_final = df_2[(df_2['Year'] >= year_range[0]) & (df_2['Year'] <= year_range[1])] 

    selected_keywords = selected_keywords or unique_keywords
    plot_df_final = plot_df_final[plot_df_final['Keyword'].isin(selected_keywords)]
    
    temp_series_1 = pd.Series(dtype = float)
    temp_series_2 = pd.Series(dtype = float)

    selected_journals = selected_journals or ["DHQ", "JOCCH", "JCA", "DSH"]
    for i in selected_journals:
        temp_series_1 = temp_series_1.add(plot_df_final[journal_yearly_dict[i]], fill_value=0)
        temp_series_2 = temp_series_2.add(plot_df_final[journal_keyword_dict[i]], fill_value=0)

    plot_df_final['proportion of articles with keyword'] = temp_series_2 / temp_series_1    
    plot_df_final = plot_df_final.sort_values(by = "Rank")
    
    unique_years = sorted(set(plot_df_final['Year']))
    threshold = 9

    if len(unique_years) <= threshold:
        tickvals =  [f'{year}' for year in unique_years]
    else:
        tickvals = [f'{year}' for year in unique_years][::2]
    
    fig_2 = px.scatter(plot_df_final, x="Year", y="proportion of articles with keyword",
                       size="Size", color="Keyword", size_max=30, opacity = 0.5, 
                       #text=plot_df_final['Keyword'],   --- Nice feature
                       hover_data = {'Keyword': True, 'dhq_total_keyword_count': False, 
                                     'jca_total_keyword_count': False, 'jooch_total_keyword_count': False, 'dsh_total_keyword_count': False, 
                                     'total_keyword_count': False, 'Significance score': True, 
                                     'Rank': True, 'Year': True, '# of articles keyword DHQ': True, 
                                     '# of articles keyword JCA': True,'# of articles keyword DSH': True, '# of articles keyword JOCCH': True, 
                                     'proportion of articles with keyword': False, 'Size' : False},
                    color_discrete_sequence = distinct_colors)

    fig_2.update_traces(marker=dict(line=dict(width=0.2)))

    fig_2.update_xaxes(title_text="Publication Year", 
                       tickvals=tickvals,
                       ticktext=tickvals,
                       tickformat='%Y', 
                       showgrid=False,
                       zeroline=False)
    
    fig_2.update_yaxes(title_text="% of articles across journals", 
                       tickformat='.2%', 
                       showgrid=False, 
                       zeroline=False)

    fig_2.update_traces(showlegend=True)
    for trace in fig_2.data:
        trace.marker.line.width = 0

    fig_2.update_layout(
        legend=dict(
            bordercolor='Black',  # Set border color
            borderwidth=1, 
            itemclick="toggleothers",
                        x = 0.99
#// the important attribute you need!
            #itemclick=False,  # Disable legend item selection
            #itemdoubleclick=False,
            # Disable legend item double click
        ),
        plot_bgcolor='#2b2b2b',  # Dark background color of the plot
        paper_bgcolor='#2b2b2b',  # Dark background color of the figure
        font={'color': '#FFFFFF'},
        title={'text': '<b> Graph 2 : Distribution of visualization keywords across years <b>', 
               'font': {'size': 16, 'color': '#FFFFFF'},
               #'x': 0.1
              },  # Set x position of the title to the left
        margin=dict(l=110, r=200, t=75, b=75)
    )

    return fig_2  





@callback(
    [Output('total-articles-card', 'children'),
     Output('dhq-articles-card', 'children'),
    Output('jca-articles-card', 'children'),

        Output('dsh-articles-card', 'children'),

     Output('jocch-articles-card', 'children')],
    [Input('journal-dropdown', 'value'),
    Input('year-range-slider', 'value')]
)
def update_article_counts(selected_journals, year_range):
    
    filtered_df = df_4[(df_4['Year'] >= year_range[0]) & (df_4['Year'] <= year_range[1])]
    
    
    selected_journals = selected_journals or ["DHQ", "JOCCH", "JCA", "DSH"]
    
    dhq_articles = int(filtered_df["DHQ"].sum()) if "DHQ" in selected_journals else 0
    
    #if((year_range[0] == 2007) and ("DHQ" in selected_journals)):
     #   dhq_articles+=13
        
    jca_articles = int(filtered_df["JCA"].sum()) if "JCA" in selected_journals else 0
    jocch_articles = int(filtered_df["JOCCH"].sum()) if "JOCCH" in selected_journals else 0
        
    #if((year_range[1] == 2024) and ("JOCCH" in selected_journals)):
     #   jocch_articles+=16
    
    dsh_articles = int(filtered_df["DSH"].sum()) if "DSH" in selected_journals else 0
    
    

    total_articles = dhq_articles + jca_articles + jocch_articles + dsh_articles
    
    return f'Total Abstracts: {total_articles}', f'DHQ Abstracts: {dhq_articles}', f'JCA Abstracts: {jca_articles}', f'DSH Abstracts: {dsh_articles}',  f'JOCCH Abstracts: {jocch_articles}'


