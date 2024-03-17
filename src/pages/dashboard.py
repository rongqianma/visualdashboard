import dash
from dash import html, dcc, callback, Input, Output
import numpy as np

dash.register_page(__name__)


#https://www.youtube.com/watch?v=XWJBJoV5yww&ab_channel=CharmingData

import pandas as pd
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


journal_yearly_dict = {'JCA' : 'JCA_yearly_total',
           'DHQ' : 'DHQ_yearly_total', 
           'JOCCH' : 'JOOCH_yearly_total'}

journal_keyword_dict = {'JCA' : '# of articles keyword DHQ',
           'DHQ' : '# of articles keyword JCA', 
           'JOCCH' : '# of articles keyword JOCCH'}


df_1 = pd.read_csv("viz_1.csv")
df_1 = df_1[df_1["Journal"]!= "Total"]

df_2 = pd.read_csv("updated_viz_2.csv")
df_2["yearly_total"] = df_2["DHQ_yearly_total"] + df_2["JCA_yearly_total"] + df_2["JOOCH_yearly_total"]
df_2["proportion of articles with keyword"] = df_2["# of articles keyword DHQ"] + df_2["# of articles keyword JCA"] + df_2["# of articles keyword JOCCH"]

df_3 = pd.read_csv("viz_table.csv")

distinct_colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',  # Blues, Oranges, Greens, Reds, Purples
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',  # Browns, Pinks, Grays, Yellows, Cyans
    '#1a9850', '#66bd63', '#a6d96a', '#d9ef8b', '#fee08b',  # Greens
    '#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3',  # Blues, Yellows, Purples, Reds, Blues
    '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd',  # Oranges, Greens, Pinks, Grays, Purples
    '#ccebc5', '#ffed6f', '#b15928', '#7cfc00', '#9400d3',  # LawnGreen, DarkViolet
    '#40e0d0', '#da70d6', '#ff634']

df_4 = df_2[["Year","DHQ_yearly_total", "JCA_yearly_total", "JOOCH_yearly_total", "yearly_total"]].drop_duplicates()
df_4.columns = ["Year", "DHQ", "JCA", "JOCCH", "Total"]

final_df_2 = df_2[['Keyword', 'Significance score', 'Rank', 'Year', '# of articles keyword DHQ',
                            '# of articles keyword JCA', '# of articles keyword JOCCH']]

final_df_2.columns = ['Keyword', 'Significance score', 'Rank', 'Year', 'DHQ', 'JCA', 'JOCCH']
final_df_2 = final_df_2.groupby(['Keyword', 'Significance score', 'Rank']).sum().reset_index()
final_df_2 = final_df_2.sort_values(by = 'Rank', ascending = True)


header_style = {
                'textAlign': 'center',
                'color': '#4a90e2',  # Blue color
                'fontSize': '36px',  # Larger font size
                'fontFamily': 'Arial, sans-serif',  # Elegant font family
                'fontWeight': 'bold',  # Bold text
                'textTransform': 'uppercase',  # Uppercase text
                'letterSpacing': '1px',  # Spacing between letters
                'marginBottom': '20px',  # Add bottom margin for spacing
            }

custom_font = {
    'fontFamily': 'Arial, sans-serif'  # You can replace 'Arial, sans-serif' with any other font you prefer
}

drop_down_div = {'textAlign': 'center', 'margin': 'auto', 'color' : '#4a90e2'}

drop_down = {'margin': 'auto','backgroundColor': '#1E1E1E', 
                               'color': '#4a90e2', **custom_font, 'padding-up':'5px'}

years = list(range(2008, 2024))


yaxis_range = None


layout = html.Div(
    style={'backgroundColor': '#1E1E1E'}, 
    children=[
        
    html.Div('<br>', style={'color':'#1E1E1E'}),
        
    # Start & End Year
html.Div([
    html.Div([
        html.Label('Select Start Year (min:2008)', style={'margin-right': '10px', 'color': 'grey', **custom_font}),
        dcc.Input(id='start-year', type='number', value=min(years), placeholder='Start Year',
                  style={'margin-right': '10px', 'padding': '8px', 'border': '1px solid #ccc',
                         'border-radius': '4px', 'outline': 'none', 'width':'10%'}),
        
        html.Label('Select End Year (max:2023)', style={'margin-right': '10px', 'color': 'grey', **custom_font}),
        dcc.Input(id='end-year', type='number', value=max(years), placeholder='End Year',
                  style={'margin-right': '10px', 'padding': '8px', 'border': '1px solid #ccc',
                         'border-radius': '4px', 'outline': 'none', 'width':'10%'})
    ], style={'display': 'inline-block', 'text-align': 'center'}),
], style={'margin-bottom': '10px', 'text-align': 'center'}),
        
    # Slider    
    dcc.RangeSlider(
        id='year-slider',
        min=min(years),
        max=max(years),
        step=1,
        marks={year: str(year) for year in years},
        value=[min(years), max(years)],
        included=True,
        className='slider'
    ),
        
    # Dropdown section 
    html.Div(
    className='row',
    style={'display': 'flex', 'justifyContent': 'center'}, 
    children=[

        #Journal Selection
        html.Div(
            className='four columns',
            style={**drop_down_div, 'width': '50%'},  # Adjust width here
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
                    style={**drop_down})]
        ),
        #Keyword Selection
        html.Div(
            className='four columns',
            style={**drop_down_div, 'width': '50%'},  # Adjust width here
            children=[
                dcc.Dropdown(
                    id='keyword-dropdown',
                    options=[
                        {'label': keyword, 'value': keyword} for keyword in df_2['Keyword'].unique().tolist()
                    ],
                    multi=True,
                    placeholder="Select Data Visualization Concept",
                    style=drop_down)])
        ]
    ),
            
    #html.Div('<br>', style={'color':'#1E1E1E'}),

        
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


    # Table section
    html.Div(className='row', 
             children=[
                 dash_table.DataTable(
                data=[],
                columns=[{'name': col, 'id': col} for col in final_df_2.columns if col!='Year'],
                page_size=11,
                style_table= {
                    'overflowX': 'auto',
                    'border': '1px solid #FFFFFF',
                },
                style_header={
                    'backgroundColor': '#4a90e2',
                    'fontWeight': 'bold',
                    'border': '1px solid #FFFFFF',
                    'color': '#FFFFFF'
                },
                style_data={
                    'whiteSpace': 'normal',
                    'height': 'auto',
                    'border': '1px solid #FFFFFF',
                },
                style_cell={
                    'textAlign': 'left',
                    'fontSize': '14px',
                    'fontFamily': 'Arial, sans-serif',
                    'padding': '8px',
                    'color': '#FFFFFF',
                    'backgroundColor': '#333333',
                },
                id='my-datatable'
                )
        ])
        
])

@callback(
    Output('my-datatable', 'data'),
    [Input('journal-dropdown', 'value'),
     Input('keyword-dropdown', 'value'),
    Input('start-year', 'value'),
    Input('end-year', 'value')    ])

def update_table(selected_journals, selected_keywords, start_year, end_year):
    
    if selected_keywords is None or len(selected_keywords) == 0:
        selected_keywords = df_2['Keyword'].unique().tolist()
        
    if selected_journals is None or len(selected_journals) == 0:
        selected_journals = ["DHQ", "JCA", "JOCCH"]  
                
    selected_years = [start_year, end_year]  

    filtered_df = df_2[(df_2['Year'] >= min(selected_years)) & (df_2['Year'] <= max(selected_years))]
    filtered_df = filtered_df[filtered_df['Keyword'].isin(selected_keywords)]

    filtered_df = filtered_df[['Keyword', 'Significance score', 'Rank', 'Year', '# of articles keyword DHQ',
                                '# of articles keyword JCA', '# of articles keyword JOCCH']]
    filtered_df.columns = ['Keyword', 'Significance score', 'Rank', 'Year', 'DHQ', 'JCA', 'JOCCH']

    final_df = filtered_df.groupby(['Keyword', 'Significance score', 'Rank']).sum().reset_index()

    if selected_journals: 
        final_df = final_df[['Keyword', 'Significance score', 'Rank'] + selected_journals]
    else:  
        final_df = final_df[['Keyword', 'Significance score', 'Rank']]

    final_df = final_df.sort_values(by = "Rank", ascending = True)
    return final_df.to_dict('records')


@callback(
    Output('histo-chart-final', 'figure'),
    [Input(component_id='journal-dropdown', component_property='value'),
     Input('keyword-dropdown', 'value'),
    Input('start-year', 'value'),
    Input('end-year', 'value')])

def update_graph(selected_journals, selected_keywords, start_year, end_year):
    global yaxis_range  # Access the global variable

    if selected_keywords is None or len(selected_keywords) == 0:
        selected_keywords = df_2['Keyword'].unique().tolist()
        
    if selected_journals is None or len(selected_journals) == 0:
        selected_journals = ["DHQ", "JOCCH", "JCA"]
    
    selected_years = [start_year, end_year]  

    plot_df_final = df_2[(df_2['Year'] >= min(selected_years)) & (df_2['Year'] <= max(selected_years))]
    plot_df_final = plot_df_final[plot_df_final["Keyword"].isin(selected_keywords)]

    cols_selected = ["# of articles keyword "+i for i in selected_journals]

    plot_df_final_2 = plot_df_final.groupby(["Keyword", "Significance score", "Rank", "Size"]).sum()[cols_selected]
    df_update = plot_df_final_2.reset_index()
    df_update.fillna(0, inplace = True)

    year_df = df_4[(df_4['Year'] >= min(selected_years)) & (df_4['Year'] <= max(selected_years))][["DHQ", "JCA", "JOCCH"]]

    year_df = year_df.sum()
    

    for i in selected_journals:
        df_update[i] = df_update["# of articles keyword "+i]/year_df[i]

    df_update.replace(np.inf, inplace = True)
    df_update.fillna(0, inplace = True)

    df_update = pd.melt(df_update, id_vars=['Keyword', 'Significance score', 'Rank', 'Size'], 
                value_vars=selected_journals, 
                var_name='Journal', value_name='% of articles')
    filtered_df = df_update.sort_values(by = "Size", ascending = False)


    #category_mapping = {'DHQ': 1, 'JCA': 2, 'JOCCH': 3}


    #filtered_df['jittered_Journal'] = filtered_df['Journal'].map(category_mapping)
    #filtered_df["jittered_Journal"] = filtered_df['jittered_Journal'] + np.random.normal(-0.01, 0.01, len(filtered_df))
    #filtered_df["jittered_prop"] = filtered_df['% of articles'] + np.random.normal(0, 0.001, len(filtered_df))

    #filtered_df['% of articles'] = round(filtered_df['% of articles'], 2)

    #print(filtered_df.head())
    
    filtered_df = filtered_df[filtered_df["% of articles"] > 0]
    filtered_df = filtered_df.sort_values(by = "Rank")
    fig = px.scatter(filtered_df, y='Journal', x="% of articles", size="Size", color="Keyword",
                     size_max=15, opacity = 0.75, hover_data={"Keyword": True, "Significance score": True,
                                              "% of articles": True, "Rank": True, "Size": False,
                                              "Journal": False, 
                                              #'jittered_Journal' : False, 
                                              "Journal":True, 
                                              "% of articles":False,
                                             }, color_discrete_sequence=distinct_colors)

    fig.update_yaxes(title_text="Digital Humanities Journal", showgrid=False)
    fig.update_xaxes(title_text="% of Articles with keyword", tickformat='.2%', 
                     showgrid=True, gridcolor='#404040', gridwidth=1)
    fig.update_traces(showlegend=True)


    fig.update_layout({
        'plot_bgcolor': '#2b2b2b',  # Dark background color of the plot
        'paper_bgcolor': '#2b2b2b',  # Dark background color of the figure
        'font': {'color': '#FFFFFF'},  # Light text color
        'title': {'text': "Graph 1 : Distribution of visualization keywords across journals",  
                   'font': {'size': 16, 'color': '#FFFFFF'}} , # Title of the plot with center alignment
            'margin': dict(l=50, t=75, b=75,r=50)  

    })

    fig.update_layout(legend=dict(
        traceorder='normal',  # Keep the legend items in the order they are traced
        bordercolor='Black',  # Set border color
        borderwidth=2, 
        itemclick =  "toggleothers" #// the important attribute you need!
        #itemclick=False,  # Disable legend item selection
        #itemdoubleclick=False,
        # Disable legend item double click
    ))
    fig.update_layout(title=dict(
        x=0.1  # Set x position of the title to the left
    ))



    #fig.update_yaxes(tickvals=[1,2,3],
     #                ticktext=["DHQ", "JCA", "JOCCH"],
      #               tickformat='%Y',  # Format to display only year
       #              showgrid=False,
        #             zeroline=False)

    return fig

# Callback to update the second graph with provided plot data
@callback(
    Output('second-chart-final', 'figure'),
    [Input(component_id='journal-dropdown', component_property='value'),
    Input('keyword-dropdown', 'value'),
    Input('start-year', 'value'),
    Input('end-year', 'value')
])

def update_second_graph(selected_journals, selected_keywords, start_year, end_year):
    
    if selected_keywords is None or len(selected_keywords) == 0:
        selected_keywords = df_2['Keyword'].unique().tolist()
        
    if selected_journals is None or len(selected_journals) == 0:
        selected_journals = ["DHQ", "JOCCH", "JCA"]
    
    selected_years = [start_year, end_year]  
        
        
    global yaxis_range  # Access the global variable

    plot_df_final = df_2[(df_2['Year'] >= min(selected_years)) & (df_2['Year'] <= max(selected_years))] 
    plot_df_final = plot_df_final[plot_df_final['Keyword'].isin(selected_keywords)]
    
    temp_series_1 = pd.Series(dtype = float)
    temp_series_2 = pd.Series(dtype = float)

    for i in selected_journals:
        if(i == "Total"):
            temp_series_1= plot_df_final[journal_yearly_dict['JCA']] + plot_df_final[journal_yearly_dict['DHQ']] + plot_df_final[journal_yearly_dict['JOCCH']]
            temp_series_2=plot_df_final[journal_keyword_dict['JCA']] + plot_df_final[journal_keyword_dict['DHQ']] + plot_df_final[journal_keyword_dict['JOCCH']]
            break
        else:
            temp_series_1 = temp_series_1.add(plot_df_final[journal_yearly_dict[i]], fill_value=0)
            temp_series_2 = temp_series_2.add(plot_df_final[journal_keyword_dict[i]], fill_value=0)

    plot_df_final['proportion of articles with keyword'] = temp_series_2 / temp_series_1

    #plot_df_final["jittered_year"] = plot_df_final['Year'] + np.random.normal(0, 0.05, len(plot_df_final))
    #plot_df_final["jittered_prop"] = plot_df_final['proportion of articles with keyword'] + 
    #np.random.normal(0, 0.001, len(plot_df_final))
    
    plot_df_final = plot_df_final.sort_values(by = "Rank")
    fig_2 = px.scatter(plot_df_final, x="Year", y="proportion of articles with keyword",
                       size="Size", color="Keyword", size_max=15, opacity = 0.75,
                       #text=plot_df_final['Keyword'],   --- Nice feature
                       hover_data = {'Keyword': True, 'dhq_total_keyword_count': False, 
                                     'jca_total_keyword_count': False, 'jooch_total_keyword_count': False, 
                                     'total_keyword_count': False, 'Significance score': True, 
                                     'Rank': True, 'Year': True, '# of articles keyword DHQ': True, 
                                     '# of articles keyword JCA': True, '# of articles keyword JOCCH': True, 
                                     'proportion of articles with keyword': False, 'Size' : False},
                    color_discrete_sequence = distinct_colors)

    unique_years = sorted(set([date for date in set(list(plot_df_final['Year']))]))

    threshold = 9

    # Check if the number of unique years is below the threshold
    if len(unique_years) <= threshold:
        tickvals = [f'{year}' for year in unique_years]
        ticktext = [str(year) for year in unique_years]
    else:
        # Generating tick values and labels for alternate years
        tickvals = [f'{year}' for year in unique_years][::2]
        ticktext = [str(year) for year in unique_years][::2]

    fig_2.update_xaxes(title_text="Publication Year", showgrid=False, zeroline=False)
    fig_2.update_yaxes(title_text="% of articles across journals")
    fig_2.update_yaxes(tickformat='.2%', showgrid=False, zeroline=False)
    fig_2.update_xaxes(tickvals=tickvals,
                       ticktext=ticktext,
                       tickformat='%Y',  # Format to display only year
                       showgrid=False,
                       zeroline=False)

    fig_2.update_traces(showlegend=True )


    fig_2.update_layout(legend=dict(
        bordercolor='Black',  # Set border color
        borderwidth=1, 
        itemclick =  "toggleothers" #// the important attribute you need!
        #itemclick=False,  # Disable legend item selection
        #itemdoubleclick=False,
        # Disable legend item double click
    ))
    
    fig_2.update_layout({
        'plot_bgcolor': '#2b2b2b',  # Dark background color of the plot
        'paper_bgcolor': '#2b2b2b',  # Dark background color of the figure
        'font': {'color': '#FFFFFF'},
        'title': {'text': 'Graph 2 : Distribution of visualization keywords across years', 
                  'font': {'size': 16, 'color': '#FFFFFF'}},
            'margin': dict(l=35, r=50, t=75, b=75)  
    })

    fig_2.update_layout(title=dict(
    x=0.1  # Set x position of the title to the left
    ))
    return fig_2  


@callback(
    Output('year-slider', 'value'),
    Input('start-year', 'value'),
    Input('end-year', 'value'),
    Input('year-slider', 'value')
)
def update_slider(start_year, end_year, slider_value):
    
    if start_year > end_year:
        end_year = start_year
    if(start_year < 2008):
        slider_value[0] = 2008
    else:
        slider_value[0] = start_year

    if(end_year > 2023):
        slider_value[1] = 2023
    else:
        slider_value[1] = end_year

    return [slider_value[0], slider_value[1]]


@callback(
    [Output('total-articles-card', 'children'),
     Output('dhq-articles-card', 'children'),
     Output('jca-articles-card', 'children'),
     Output('jocch-articles-card', 'children')],
    [Input('journal-dropdown', 'value'),
    Input('start-year', 'value'),
    Input('end-year', 'value')]
)
def update_article_counts(selected_journals, start_year, end_year):
    
    if selected_journals is None or len(selected_journals) == 0:
        selected_journals = ["DHQ", "JOCCH", "JCA"]
        
    # Filter data based on selected journal and year range
    filtered_df = df_4[(df_4['Year'] >= start_year) & 
                       (df_4['Year'] <= end_year)]
    
    
    # Calculate number of articles for each journal
    dhq_articles = 0
    if("DHQ" in selected_journals):
        dhq_articles = int(sum(filtered_df["DHQ"]))
        
    jca_articles = 0
    if("JCA" in selected_journals):
        jca_articles = int(sum(filtered_df["JCA"]))
    
    jocch_articles = 0
    if("JOCCH" in selected_journals):
        jocch_articles = int(sum(filtered_df["JOCCH"]))
    
    total_articles = dhq_articles + jca_articles + jocch_articles
    
    return f'Total Articles: {total_articles}', f'DHQ Articles: {dhq_articles}', f'JCA Articles: {jca_articles}', f'JOCCH Articles: {jocch_articles}'


