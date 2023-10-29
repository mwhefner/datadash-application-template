"""
Module/Script Name: content_display.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/16/2023

Project: DataDash Application Template

Script Description: This script defines the logical layout and callback functionality of the content_display.

Exceptional notes about this script:
(none)

Callback methods: 2

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "display_container"

# Import Dependencies
import dash.html.Div
import plotly.graph_objs as go
from components.utils import constants as d
from components.figures.example_figures import simple_example_figures
from components.figures.choropleth_example import choropleth_example
from components.figures.three_d_example import three_d_example
from components.figures.animation_example import animation_example
from components.tables.browse import browse_table
import time

# LAYOUT
layout = dash.html.Div(
    id = component_id,
)

# CALLBACKS (2)
# The first callback decides what content should be in the display container.
@dash.callback(
    dash.dependencies.Output(component_id, 'children'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value'),
    dash.dependencies.Input('theme_toggle', 'className'),
)
def update_container(nav_opt, theme):
    
    # for displaying all non-plotly figure navigation options

    if nav_opt == "about" :
        return [
            # About page: Markdown
            dash.dcc.Markdown(
                children = d.about_content, 
                className = "markdown", 
                mathjax=True)
        ]
    if nav_opt == "example-2" :
        return [
            dash.dcc.Loading(
                children=browse_table(),
                )
        ]
    
    else :

        if nav_opt == 'example-1' :

            # Simple Example Figure 

            return dash.dcc.Loading(
                children= dash.dcc.Graph(
                    figure=simple_example_figures(theme), 
                    className='plotly-figure', 
                    style = {'height' :  '100vh'})
            )

        if nav_opt == 'example-3' :

            # Controls Demo
            return dash.dcc.Loading(
                children=dash.dcc.Graph(
                    figure=choropleth_example(theme), 
                    className='plotly-figure', 
                    style = {'height' :  '100vh'})
            )

        if nav_opt == 'example-5' :

            # Surface Demo
            return dash.dcc.Loading(
                children=dash.dcc.Graph(
                    figure=three_d_example(theme), 
                    className='plotly-figure', 
                    style = {'height' :  '100vh'})
            )
        
        if nav_opt == 'example-6' :

            # Animation Demo
            return dash.dcc.Loading(
                children=dash.dcc.Graph(
                    figure=animation_example(theme), 
                    className='plotly-figure', 
                    style = {'height' :  '100vh'})
            )

        else :
            return dash.dcc.Loading(
                children=dash.dcc.Graph(
                    figure=go.Figure(), 
                    className='plotly-figure', 
                    style = {'height' :  '100vh'}))



