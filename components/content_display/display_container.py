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
from components.utils import constants as d
from components.figures.example_figure import simple_example_figure
from components.figures.advanced_plotly_subfigures import advanced_plotly_subfigures
from components.tables.browse import browse_table

# LAYOUT
layout = dash.html.Div(
    id = component_id,
    children= [
        dash.dcc.Graph(id='plotly-figure')
    ]
)

# CALLBACKS (2)
# The first callback decides what content should be in the display container.
@dash.callback(
    dash.dependencies.Output(component_id, 'children'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value'),
)
def update_container(nav_opt):
    
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
                className="table-container"
                )
        ]
    else :
        return [
            # Displays all plotly-figure navigation options
            dash.dcc.Graph(id='plotly-figure', style = {'height' :  '100%'})
        ]
    
# Updates the graph or map displayed in the content area's plotly figure
@dash.callback(
    dash.dependencies.Output('plotly-figure', 'figure'),
    dash.dependencies.Input('navigation-dropdown-controler', 'value'),
    # Other interactive controls' values can be included here as input 
    # to the figure
    dash.dependencies.Input('theme_toggle', 'className')
)
def update_fig_or_table(nav_opt, theme):

    if nav_opt == 'example-1' :

        # Simple Example Figure 

        return simple_example_figure(theme)

    if nav_opt == 'example-3' :

        # Controls Demo

        return advanced_plotly_subfigures(theme)

    else :

        # If you're not changing the content_display to a different plotly figure,
        # or changing one of the inputs,
        # don't update the figure

        return dash.no_update
