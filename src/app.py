import dash
from dash import Dash, html, dcc



import __main__ as main
main.__file__ = "main_file"

app = Dash(__name__, use_pages=True)
server = app.server



header_style = {
                'textAlign': 'center',
                'color': '#4a90e2',  # Blue color
                'fontSize': '36px',  # Larger font size
                'fontFamily': 'Arial, sans-serif',  # Elegant font family
                'fontWeight': 'bold',  # Bold text
                'letterSpacing': '1px',  # Spacing between letters
                'marginBottom': '20px',  # Add bottom margin for spacing
            }



layout = html.Div([
    html.Div(className='row',
        style={'background-color': '#282c34', 'padding': '10px'},  # Background color and padding adjusted for a clean look
        children=[
            html.Div(className='twelve columns',
                style = {'textAlign': 'center'},
                children = [
                    html.H2('KEYWORD ANALYSIS ON HUMANITIES JOURNAL ARTICLES',  
                        style = header_style)
                         ]
        )]),
html.Div(
    [
        html.Div(
            dcc.Link(
                f"{page['name']}",
                href=page["relative_path"],
                style={**header_style, 'text-decoration': 'none', 'margin-right': '20px', 'font-size': '18px',
                      'color': 'white'}
            )
        ) 
        for page in sorted(dash.page_registry.values(), key=lambda x: x['name'], reverse = True)
    ], 
    style={
        'display': 'flex',
        'flexWrap': 'wrap',
        'background-color': '#282c34',
        'color': 'white',
        'padding': '10px',
                'justify-content': 'center',  # Center align the links

    }
)


    ,
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)
