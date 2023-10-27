"""
Module/Script Name: defaultbuttonarea.py
Author: M. W. Hefner

Created: 6/29/2023
Last Modified: 7/14/2023

Project: DataDash Application Template

Script Description: This script defines the style, layout, and callback functionality of the defaultbuttonarea link area, which includes the back-to-datadash button and the theme toggle.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "defaultbuttonarea"

# Import Dependencies
import dash.html.Div
# import components.examplesubcomponent as examplesubcomponent
import components.control_panel.controls.theme_toggle as theme_toggle
import components.utils.constants as constants

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    children= [

        # Theme and Go-Back-To-DataDash buttons
        dash.html.Div(

            # So that the default buttons can be styled appropriately together
            id = "defaultbuttons",

            children = [

                # THEME TOGGLE
                theme_toggle.layout,

                # Go-Back-To-DataDash button
                dash.html.Div([
                    dash.html.A(
                        dash.html.Button("Go to DataDash", className="universal_button"),
                        href="/",
                        target="_blank",  # Opens the link in a new tab
                    )
                ])

            ]
        ),

        # Statement of RIEEE support and source code link
        dash.html.P(
            [
                "This application is made possible by the ",
                dash.html.A(
                    "Research Institute for Environment, Energy, and Economics", 
                    href = "https://rieee.appstate.edu", 
                    style={"color" : "white"}
                ),
                " at Appalachian State University through the RIEEE DataDash secure research web application platform. License information and source is avaiable ",
                dash.html.A(
                    "here on GitHub.", 
                    href = "https://github.com/mwhefner/datadash-application-template", 
                    style={"color" : "white"}
                ),
            ]
        ),

        # Displays the RIEEE logo, which serves as a link to the RIEEE mainpage
        dash.html.A(
            dash.html.Img(
                src='assets/images/RIEEE_LOGO.png', height=200
            ), 
            href = "https://rieee.appstate.edu",
            style={'display': 'block', 'margin': 'auto'}
        ),

        # Statement of RIEEE support and source code link
        dash.html.P(
            [
                "DOI: ",
                constants.app_doi
            ]
        ),

    ]
)

# CALLBACKS (0)
