import dash
from dash import Dash, html, dcc



import __main__ as main
main.__file__ = "main_file"

app = Dash(__name__, use_pages=True)
server = app.server




header_style = {
                'textAlign': 'center',
                #'color': '#4a90e2',  # Blue color
                'color': 'white',  # Blue color

                'fontSize': '27px',  # Larger font size
                'fontFamily': 'Arial, sans-serif',  # Elegant font family
                'fontWeight': 'bold',  # Bold text
                'letterSpacing': '1px',  # Spacing between letters
                'marginBottom': '30px',  # Add bottom margin for spacing
                'marginTop': '30px',  # Add bottom margin for spacing

            }



app.layout = html.Div([
    html.Div(className='row',
        style={'background-color': '#2b2b2b', 'padding': '5px'},  # Background color and padding adjusted for a clean look
        children=[
            html.Div(className='twelve columns',
                #style = {'textAlign': 'center'},
                children = [
                    html.H2('Computational Analysis of the Visual Key Concepts in Digital Humanities Research Communication',  
                        style = header_style)
                         ]
        )]),
html.Div(

    [
        html.Div(
            
            dcc.Link(
                f"{page['name']}",
                href=page["relative_path"],
                style={'textAlign': 'center',
                'fontFamily': 'Arial, sans-serif',  # Elegant font family
                'fontWeight': 'bold',  # Bold text
                'letterSpacing': '1px',  # Spacing between letters
               'border': '1px solid white',  # Adding border
                'padding': '5px 15px',  # Adding padding around the border

                       'text-decoration': 'none', 'font-size': '18px',
                      'color': 'white'}
            )
        ) 
        for page in sorted(dash.page_registry.values(), key=lambda x: x['name'], reverse = True)
    ], 
    style={
        'display': 'flex',
        'flexWrap': 'wrap',
        'background-color': '#2b2b2b',
        'color': 'white',
        'padding-bottom': '5px',
        'padding-top': '5px',
        'justify-content': 'center', 
        # Center align the links

    }
)


    ,
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)
