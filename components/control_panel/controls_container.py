"""
Module/Script Name: controls_container.py
Author: M. W. Hefner

Created: 6/28/2023
Last Modified: 7/14/2023

Project: CDIAC at AppState

Script Description: This script defines the style, layout, and callback functionality of the controls_container.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "controls_container"

# Import Dependencies
import dash.html.Div
import components.control_panel.controls.navigation_dropdown as navigation_dropdown
import components.control_panel.controls.theme_toggle as theme_toggle
import components.control_panel.backtodatadash as backtodatadash

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    children= [

        # THEME TOGGLE
        theme_toggle.layout,
        
        # NAVIGATION SELECTION
        navigation_dropdown.layout,

        # INFO / BACK TO DATADASH
        backtodatadash.layout,

    ]
)

# CALLBACKS (0)