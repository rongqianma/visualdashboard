import numpy as np
import pandas as pd
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import dash
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__)



# Read data from CSV files
df_1 = pd.read_csv("viz_1.csv").query("Journal != 'Total'")
df_2 = pd.read_csv("updated_viz_2.csv")
df_3 = pd.read_csv("viz_table.csv")

# Calculate total yearly and proportion of articles with keyword
df_2["yearly_total"] = df_2["DHQ_yearly_total"] + df_2["JCA_yearly_total"] + df_2["JOOCH_yearly_total"]
df_2["proportion of articles with keyword"] = df_2["# of articles keyword DHQ"] + df_2["# of articles keyword JCA"] + df_2["# of articles keyword JOCCH"]

# Data cleaning for table
df_table = df_2[['Keyword', 'Significance score', 'Rank', 'Year', '# of articles keyword DHQ',
                 '# of articles keyword JCA', '# of articles keyword JOCCH']].rename(columns={
    'Keyword': 'Keyword', 'Significance score': 'Significance score', 'Rank': 'Rank', 
    'Year': 'Year', '# of articles keyword DHQ': 'DHQ', '# of articles keyword JCA': 'JCA', 
    '# of articles keyword JOCCH': 'JOCCH'
})

# List of unique keywords
unique_keywords = df_2['Keyword'].unique().tolist()

# Define dictionaries for journal data
journal_yearly_dict = {'JCA' : 'JCA_yearly_total',
           'DHQ' : 'DHQ_yearly_total', 
           'JOCCH' : 'JOOCH_yearly_total'}

journal_keyword_dict = {'JCA' : '# of articles keyword DHQ',
           'DHQ' : '# of articles keyword JCA', 
           'JOCCH' : '# of articles keyword JOCCH'}

distinct_colors = [
    '#FF5733', '#FFC300', '#FFA500', '#008000', '#008080',  # Reds, Yellows, Gold, Green, Teal
    '#0000FF', '#800080', '#FF00FF', '#808080', '#000000',  # Blue, Purple, Magenta, Gray, Black
    '#00FF00', '#00FFFF', '#00008B', '#6A5ACD', '#FF1493',  # Lime, Cyan, Dark Blue, Slate Blue, Deep Pink
    '#FF69B4', '#FF6347', '#FFA07A', '#4682B4', '#556B2F',  # Hot Pink, Tomato, Light Salmon, Steel Blue, Dark Olive Green
    '#8A2BE2', '#8B008B', '#000080', '#4B0082', '#7FFF00',  # Blue Violet, Dark Magenta, Navy, Indigo, Chartreuse
    '#FF4500', '#00BFFF', '#00FA9A', '#6495ED', '#B22222'   # Orange Red, Deep Sky Blue, Medium Spring Green, Medium Purple, Fire Brick
]



df_4 = df_2[["Year","DHQ_yearly_total", "JCA_yearly_total", "JOOCH_yearly_total", "yearly_total"]].drop_duplicates()
df_4.columns = ["Year", "DHQ", "JCA", "JOCCH", "Total"]

table_columns = ['Keyword','Significance score', 'Rank', 'DHQ', 'JCA', 'JOCCH' ]

header_style = {'textAlign': 'center',
                'color': '#4a90e2',  # Blue color
                'fontSize': '36px',  # Larger font size
                'fontFamily': 'Arial, sans-serif',  # Elegant font family
                'fontWeight': 'bold',  # Bold text
                'textTransform': 'uppercase',  # Uppercase text
                'letterSpacing': '1px',  # Spacing between letters
                'marginBottom': '20px'}

custom_font = {'fontFamily': 'Arial, sans-serif'}
drop_down_div = {'textAlign': 'center', 'margin': 'auto', 'color' : '#4a90e2'}
drop_down = {'margin': 'auto','backgroundColor': '#1E1E1E', 
                               'color': '#4a90e2', **custom_font, 'padding-up':'5px'}

years = list(range(2008, 2024))

layout = html.Div(
    style={'backgroundColor': '#1E1E1E'}, 
    children=[

        
    html.Div('<br>', style={'color':'#1E1E1E'}),
        
            # Slider
    html.Div(className='row', 
    children=[
        html.Div(className='twelve columns', 
            children=[

                html.Div([
                    
                    html.Div(id='slider-tooltip', style={'color': 'white',
                                                        'font-weight': 'bold', 'text-align': 'center'}),
                    
                    html.Div('<br>', style={'color':'#1E1E1E'}),

                    #Slider
                    dcc.RangeSlider(
                        id='year-range-slider',
                        min=df_2['Year'].min(),
                        max=df_2['Year'].max(),
                        step=1,
                        value=[df_2['Year'].min(), df_2['Year'].max()],
                        marks={str(year): {'label': str(year), 'style': {#'fontWeight': 'bold', 
                                                                         'fontSize': '120%',
                                                                         'color': 'white'
                                                                        }} for year in df_2['Year'].unique()}


                    ),

                    
                    #html.P('Use the slider above to select the start year and end year of publication',
                    #    style={'color': '#FFFFFF', 'font-size': '14px', 'text-align': 'center', 'margin-bottom': '10px'}
                    #)
                ], style={'width': '60%', 'margin': 'auto'})
            ])]),
        
        html.Div('<br>', style={'color':'#1E1E1E'}),

        html.Div(
            className='four columns',
            style={**drop_down_div, 'width': '58%'},  # Adjust width here
            children=[
                dcc.Dropdown(
                    id='journal-dropdown',
                    options=[
                        {'label': 'DHQ', 'value': 'DHQ'},
                        {'label': 'JCA', 'value': 'JCA'},
                        {'label': 'JOCCH', 'value': 'JOCCH'}
                    ],
                    multi=True,
                    placeholder="Select Humanities Journal",
                    style={**drop_down, 'margin-bottom' : '5px', 'margin-up' : '5px'})]
        ),
        
        html.Div(
            className='four columns',
            style={**drop_down_div, 'width': '58%'},  # Adjust width here
            children=[
                dcc.Dropdown(
                    id='keyword-dropdown',
                    options=[
                        {'label': keyword, 'value': keyword} for keyword in unique_keywords
                    ],
                    multi=True,
                    placeholder="Select Data Visualization Concept",
                    style={**drop_down, 'margin-bottom' : '5px'})]),
            

        
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
                    html.Div(className='twelve columns', style={'display': 'inline-block','width':'99%',
                                                            'padding-left': '5px',
                                                            'padding-right': '5px',
                                                              'padding-bottom': '5px'}, 
                             children=[dcc.Graph(id='histo-chart-final')
                    ]),
                    # Graph 2
                    html.Div(className='twelve columns', style={'padding-left': '5px', 
                                                                'padding-right':'5px','width':'99%',
                                                                'display': 'inline-block',
                                                                'padding-bottom': '5px'}, 
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
                    'Keyword': {'value': '''Keyword: Top 30     
                    The data visualization keyword is identified from article abstracts. OpenAI GPT 3.5 was used in order to identify relevant keywords.''', 'type': 'markdown'},
                    
                    'Significance score': {'value': '''Significance score: [0,1]     
                    The significance score is computed using OpenAI GPT 4. Higher the value, the more relevant it is in the context of data visualization.''', 'type': 'markdown'},

                    'Rank': {'value': '''Rank: [1,30]    
                    Computed based on a keyword\'s significance score and its occurrence across all journals. If two keywords have the same significance score, the keyword that occurs more frequently has a lower rank.''', 'type': 'markdown'}
                    ,

                    'DHQ': {'value': '''DHQ:     
                    This signifies the number of times a specific keyword occurred in DHQ in the selected year range.''', 'type': 'markdown'},

                    'JCA': {'value': '''JCA:     
                    This signifies the number of times a specific keyword occurred in JCA in the selected year range.''', 'type': 'markdown'},

                    'JOCCH': {'value': '''JOCCH:     
                    This signifies the number of times a specific keyword occurred in JOCCH in the selected year range.''', 'type': 'markdown'}}
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
        'font-weight': 'bold',
        'padding': '10px',
        'border': '1px solid white',
        'border-radius': '5px',
        'display': 'inline-block',
        'background-color': '#282c34',  # Lighter shade of #282c34 with increased opacity (80%)

    }
    return html.Div([
        html.Div([
            html.Div(f'Publication Year Start: {value[0]}', style={'margin-bottom': '5px'}),
            html.Div(f'Publication Year End: {value[1]}')
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

    selected_journals = selected_journals or ["DHQ", "JOCCH", "JCA"]
    final_df = final_df[['Keyword', 
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
    
    selected_journals = selected_journals or ["DHQ", "JOCCH", "JCA"]
    cols_selected = ["# of articles keyword "+ journal for journal in selected_journals]
    df_update = filtered_df.groupby(["Keyword", 
                                     "Significance score", 
                                     "Rank", 
                                     "Size"]).sum()[cols_selected].reset_index().fillna(0)

    year_df = df_4[(df_4['Year'] >= year_range[0]) & (df_4['Year'] <= year_range[1])][["DHQ","JCA", "JOCCH"]].sum()
        
    for journal in selected_journals:
        df_update[journal] = df_update["# of articles keyword " + journal] / year_df[journal]

    
    df_update.replace(np.inf, 0, inplace = True)
    df_update = pd.melt(df_update, id_vars=['Keyword', 'Significance score', 'Rank', 'Size'], 
                value_vars=selected_journals, 
                var_name='Journal', value_name='% of articles')
    
    
    filtered_df = df_update[df_update["% of articles"] > 0]
    filtered_df = filtered_df.sort_values(by = "Rank")


    #category_mapping = {'DHQ': 1, 'JCA': 2, 'JOCCH': 3}
    #filtered_df['jittered_Journal'] = filtered_df['Journal'].map(category_mapping)
    #filtered_df["jittered_Journal"] = filtered_df['jittered_Journal'] + np.random.normal(-0.01, 0.01, len(filtered_df))

    fig = px.scatter(filtered_df, 
                     y='Journal', 
                     #y='jittered_Journal', 
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
                                 #'jittered_Journal' : False,
                                 "Journal":True,
                                 "% of articles":False
                                }, 
                     color_discrete_sequence=distinct_colors)

    fig.update_traces(marker=dict(line=dict(width=0.2)))
    fig.update_yaxes(title_text="Digital Humanities Journal",
                     showgrid=False)
    
    fig.update_xaxes(title_text="% of Articles with keyword",
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
        margin=dict(l=50, t=75, b=75, r=50),  
        legend=dict(
            traceorder='normal',  
            bordercolor='Black',  
            borderwidth=1, 
            itemclick="toggleothers"
            #itemclick=False, 
            #itemdoubleclick=False
        )
    )

    #fig.update_yaxes(tickvals=[1,2,3], ticktext=["DHQ", "JCA", "JOCCH"], tickformat='%Y', showgrid=False, zeroline=False)
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

    selected_journals = selected_journals or ["DHQ", "JOCCH", "JCA"]
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
                                     'jca_total_keyword_count': False, 'jooch_total_keyword_count': False, 
                                     'total_keyword_count': False, 'Significance score': True, 
                                     'Rank': True, 'Year': True, '# of articles keyword DHQ': True, 
                                     '# of articles keyword JCA': True, '# of articles keyword JOCCH': True, 
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
            itemclick="toggleothers" #// the important attribute you need!
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
        margin=dict(l=35, r=50, t=75, b=75)
    )

    return fig_2  





@callback(
    [Output('total-articles-card', 'children'),
     Output('dhq-articles-card', 'children'),
     Output('jca-articles-card', 'children'),
     Output('jocch-articles-card', 'children')],
    [Input('journal-dropdown', 'value'),
    Input('year-range-slider', 'value')]
)
def update_article_counts(selected_journals, year_range):
    
    filtered_df = df_4[(df_4['Year'] >= year_range[0]) & (df_4['Year'] <= year_range[1])]
    
    selected_journals = selected_journals or ["DHQ", "JOCCH", "JCA"]
    dhq_articles = int(filtered_df["DHQ"].sum()) if "DHQ" in selected_journals else 0
    jca_articles = int(filtered_df["JCA"].sum()) if "JCA" in selected_journals else 0
    jocch_articles = int(filtered_df["JOCCH"].sum()) if "JOCCH" in selected_journals else 0
    total_articles = dhq_articles + jca_articles + jocch_articles
    
    return f'Total Articles: {total_articles}', f'DHQ Articles: {dhq_articles}', f'JCA Articles: {jca_articles}', f'JOCCH Articles: {jocch_articles}'


