"""
Module/Script Name: button_templates.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/15/2023

Project: DataDash Application Template

Script Description: This script demonstrates some of the dash core component controls available for the control panel of your DataDash application.

Exceptional notes about this script:
(none)

Callback methods: 3

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "button_templates"

# Import Dependencies
import dash.html

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
            dash.dcc.Markdown(
                id='markdown-text-id',
                children='''**Markdown Text Example:** \n You can use Markdown *here too!* \n# You can make Headers \n## And subheaders \n- and bulleted lists \n- Try it out!''',
            ),
            style={'margin-top' : '15px', 'margin-bottom' : '15px'},
            id='markdown-div-id',
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
    dash.dependencies.Input(component_id, 'hidden')
)
def update_visibility_cascade(hidden):
    return hidden, hidden, hidden, hidden, hidden, hidden, hidden
