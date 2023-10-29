"""
Module/Script Name: button_templates.p

Author(s): M. W. Hefner

Initially Created: 7/01/2023

Last Modified: 10/29/2023

Script Description: This script demonstrates some of the dash core component controls available for the control panel of your DataDash application.

Exceptional notes about this script:
(none)

Callback methods: 3

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "button_templates"

# Import Dependencies
import dash.html
import datetime

# LAYOUT
layout = dash.html.Div(
    id=component_id,
    className="controls",
    hidden=True,

    children=[

        # This is an example of each contol.
        # Usually, controls or small groups of controls get their own
        # file for ease of documentation.

        # Note that is generally easier to position these things
        # by wrapping them in a Div... it's usually teamwork
        # between the in-line python-css styling and what the plotly
        # folks have implemented as function arguments.

        # DROPDOWN MENU-------------------------------------------------

        dash.html.Div(
            dash.dcc.Markdown(
                id='markdown-text-id',
                children='''# Plotly Chorpleth Map \n## with Dash Controls \nThe following controls are available for the control panel at this time, including *this* markdown container.  This markdown can either be specified in-line, or be included in the assets/markdown folder for larger texts.  This can be used to help explain features of your application and how to interact with them.''',
            ),
            style={'margin-top' : '15px', 'margin-bottom' : '15px'},
            id='markdown-div-id',
            hidden=True,
        ),

        dash.html.Div(
            [
                dash.html.H2('Multi-Choice Dropdown'),

                dash.dcc.Dropdown(
                    id='dropdown-id',

                    # Options for a dropdown menu are laid out like this
                    options=[
                        {'label': 'Show Scatter Plot', 'value': 'scatter'},
                        {'label': 'Show Bar Chart', 'value': 'bar'},
                        {'label': 'Show Pie Chart', 'value': 'pie'},
                        {'label': 'Show Line Chart', 'value': 'line'}
                    ],

                    value='scatter',
                    multi=True,
                    # Dropdowns are weird... their text color needs to stay black
                    className="dropdown_light" 
                ),
            ],

            # Styling for container div to position control in control panel
            style={'margin-top' : '15px', 'margin-bottom' : '15px'},
            id='dropdown-div-id',
            hidden=True,
        ),

        dash.html.Div(
            [
                dash.html.H2('Date Range Picker'),
                dash.dcc.DatePickerRange(
                    id='date-range-picker',
                    start_date='2023-01-01',
                    end_date='2023-12-31',
                ),
            ],
            style={'margin-top' : '15px', 'margin-bottom' : '15px'},
            id='date-range-div',  # Fixed the div ID here
            hidden=True,
        ),

        dash.html.Div(
            [
                dash.html.H2('Simple Text Form Input'),
                dash.dcc.Input(
                    id='text-input-id',
                    type='text',
                    value='Enter text',
                ),
            ],
            style={'margin-top' : '15px', 'margin-bottom' : '15px'},
            id='textarea-div-id',  # Fixed the div ID here
            hidden=True,
        ),

        dash.html.Div(
            [
                dash.html.H2('Checklist'),
                dash.dcc.Checklist(
                    id='checklist-id',
                    options=[
                        {'label': 'Option 1', 'value': 'option1'},
                        {'label': 'Option 2', 'value': 'option2'},
                        {'label': 'Option A', 'value': 'optionA'},
                        {'label': 'Option B', 'value': 'optionB'},
                        {'label': 'Option X', 'value': 'optionX'},
                        {'label': 'Option Y', 'value': 'optionY'},
                        {'label': 'Custom Option', 'value': 'customOption'},
                        {'label': 'Select This', 'value': 'selectThis'}
                    ],
                    value=['option1'],
                ),
            ],
            style={'margin-top' : '15px', 'margin-bottom' : '15px'},
            id='checklist-div-id',  # Fixed the div ID here
            hidden=True,
        ),

        dash.html.Div(
            [
                dash.html.H2('Slider'),
                dash.dcc.Slider(
                    id='slider-id',
                    min=0,
                    max=100,
                    step=20,
                    value=50,
                ),
            ],
            style={'margin-top' : '15px', 'margin-bottom' : '15px'},
            id='slider-div-id',  # Fixed the div ID here
            hidden=True,
        ),

        dash.html.Div(
            [
                dash.html.H2('Radio Buttons'),
                dash.dcc.RadioItems(
                    id='radio-items-id',
                    options=[
                        {'label': 'Option A', 'value': 'A'},
                        {'label': 'Option B', 'value': 'B'},
                        {'label': 'Option B1', 'value': 'B1'},
                        {'label': 'Option B2', 'value': 'B2'},
                        {'label': 'Option B3', 'value': 'B3'},
                        {'label': 'Option B4', 'value': 'B4'},
                        {'label': 'Option B5', 'value': 'B5'},
                        {'label': 'Option B6', 'value': 'B6'},
                    ],
                    value='A',
                ),
            ],
            style={'margin-top' : '15px', 'margin-bottom' : '15px'},
            id='radio-items-div-id',  # Fixed the div ID here
            hidden=True,
        ),

        dash.html.Div(
            [
                dash.html.H2('Range Slider'),
                dash.dcc.RangeSlider(
                    id='range-slider-id',
                    min=0,
                    max=100,
                    step=10,
                    value=[30, 70],
                ),
            ],
            style={'margin-top' : '15px', 'margin-bottom' : '15px'},
            id='range-slider-div-id', 
            hidden=True,
        ),

        dash.html.Div(
            children = dash.dcc.Textarea(
                id='textarea-id',
                value='Enter multi-line text here',
            ),
            style={'margin-top' : '15px', 'margin-bottom' : '15px'},
            id='textarea-div-id',  
            hidden=True,
        ),

        # Upload files
        # BUG: There must be something up with the upload control -
        # I cannot for the life of me get it to not show
        # and linger on the panel for a moment at app start-up.
        # Temp fix: consider surrounding the controls with a dcc.Loading
        dash.html.Div(
            id = "upload-contol-container",
            children= [
            
                dash.dcc.Upload(
                    id='upload-image',

                    children = dash.html.Div(
                        id = "inner-upload-container",
                        children = [
                            'Drag and Drop or ',
                            dash.html.A('Select Image(s)'),
                        ]
                    ),

                    # Would ideally be done with the stylesheet!
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    },

                    # Allow multiple files to be uploaded
                    multiple=True
                ),
                dash.html.Div(id='output-image-upload'),
            ]
        )
    ]
)


# CALLBACKS (3)
# Controls the theme
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Input('theme_toggle', 'className')
)
def update_theme(theme):
    return "control_" + theme

# Whether or not to hide entire area 
@dash.callback(
    dash.dependencies.Output(component_id, 'hidden'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value')
)
def update_visibility(navopt):
    return navopt != "example-3"

# Unfortunately, all the others must be hidden to prevent 
# strange visual artifacts on the page
# Whether or not to hide the entire area
@dash.callback(
    dash.dependencies.Output('slider-div-id', 'hidden'),
    dash.dependencies.Output('checklist-div-id', 'hidden'),
    dash.dependencies.Output('radio-items-div-id', 'hidden'),
    dash.dependencies.Output('dropdown-div-id', 'hidden'),
    dash.dependencies.Output('range-slider-div-id', 'hidden'),
    dash.dependencies.Output('markdown-div-id', 'hidden'),
    dash.dependencies.Output('textarea-div-id', 'hidden'),
    dash.dependencies.Output('upload-image', 'hidden'),
    dash.dependencies.Output('upload-contol-container', 'hidden'),
    dash.dependencies.Output('inner-upload-container', 'hidden'),
    dash.dependencies.Input(component_id, 'hidden')
)
def update_visibility_cascade(hidden):
    return hidden, hidden, hidden, hidden, hidden, hidden, hidden, hidden, hidden, hidden

# Helper function for the next callback function
def parse_contents(contents, filename, date):
    return dash.html.Div([
        dash.html.H5(filename),
        dash.html.H6(datetime.datetime.fromtimestamp(date)),

        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        dash.html.Img(src=contents, width=100),
        dash.html.Hr(),
        dash.html.Div('Raw Content'),
        dash.html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

@dash.callback(dash.Output('output-image-upload', 'children'),
              dash.Input('upload-image', 'contents'),
              dash.State('upload-image', 'filename'),
              dash.State('upload-image', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children