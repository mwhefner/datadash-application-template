"""
Module/Script Name: navigation_dropdown.py

Author(s): M. W. Hefner

Initially Created: 6/28/2023

Last Modified: 10/29/2023

Script Description: this script describes the functionality of the navigation dropdown.  Use this script along with the display_container.py together to add pages to your application.

Exceptional notes about this script: 
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "navigation_dropdown"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent

# Two IDs are used - a wrapper around the dropdown, and the controller itself.
# This allows for easier self-reference without worrying about infinite loops,
# though I love hofstadter's work, myself. -MWH

# LAYOUT
layout = dash.html.Div(
    id = component_id,

    children= [

        dash.html.H2('Navigation'),

        dash.dcc.Dropdown(

            id='navigation-dropdown-controler',

            # Provides default (and in the case of navigation, perm) options.

            # NOTE: Simply adding an option here is not sufficient to add
            # a control to the control panel.  Please see the DataDash Development
            # handbook for clarification and design guidance.

            options=[

                {'label': 'About (Example: LaTeX Markdown Display)', 'value': 'about'},

                {'label': 'Example: Plotly Figures of Secure Data Server Data', 'value': 'example-1'},

                {'label': 'Example: Animations', 'value': 'example-6'},

                {'label': 'Example: Simple Data Table of Uploaded Data', 'value': 'example-2'},

                {'label': 'Example: Dash Controls and Mapbox', 'value': 'example-3'},

                #{'label': 'Example: Live Update Figures', 'value': 'example-4'},
                
                {'label': 'Example: 3D Data', 'value': 'example-5'},

            ],

            # Default to the about page
            value = 'about',

            clearable=False,

            # Making this searchable will disturb the tablet experience.
            searchable=False

        )

    ]
)

# CALLBACKS (1)
# Controls the theme of the navigation dropdown
@dash.callback(
    dash.dependencies.Output(component_id, 'className'),
    dash.dependencies.Input('theme_toggle', 'className')
)
def update_source_dropdown(theme):
    return "dropdown_" + theme

'''

come back to the idea of having the page function with hashes (and maybe a tab navigation?)

-m. w. hefner 10/29/2023

@dash.callback(
    dash.dependencies.Output('navigation-dropdown-controler', 'value'),
    dash.dependencies.Input('url', 'hash')
)
def update_source_dropdown(hash):
    if hash in ["example-1", "example-2", "example-3", "example-5", "example-6"] :
        return hash
    elif hash == "" or hash == 'about' :
        return "about"
    else :
        return dash.no_update
'''