"""
Module/Script Name: surface_example.py
Author: M. W. Hefner

Created: 7/12/2023
Last Modified: 10/24/2023

Project: DataDash Application Template

Script Description: This script defines an example plotly figure with many subfigures driven by the values of the Dash controls.

Exceptional notes about this script:
(none)

Callback methods: N/A

~~~

This figure was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import needed libraries
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from urllib.request import urlopen
import json


# Example Plotly Figure
def surface_example(theme) :

    if theme == 'light' :
        textCol = '#000'
    if theme == 'dark' :
        textCol = '#fff'

    a, b, d = 1.32, 1., 0.8
    c = a**2 - b**2
    u, v = np.mgrid[0:2*np.pi:100j, 0:2*np.pi:100j]
    x = (d * (c - a * np.cos(u) * np.cos(v)) + b**2 * np.cos(u)) / (a - c * np.cos(u) * np.cos(v))
    y = b * np.sin(u) * (a - d*np.cos(v)) / (a - c * np.cos(u) * np.cos(v))
    z = b * np.sin(v) * (c*np.cos(u) - d) / (a - c * np.cos(u) * np.cos(v))

    fig = make_subplots(rows=1, cols=2,
                        specs=[[{'is_3d': True}, {'is_3d': True}]],
                        subplot_titles=['Color corresponds to z', 'Color corresponds to distance to origin'],
                        )

    fig.add_trace(go.Surface(x=x, y=y, z=z, colorbar_x=-0.07), 1, 1)
    fig.add_trace(go.Surface(x=x, y=y, z=z, surfacecolor=x**2 + y**2 + z**2), 1, 2)
    #fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    fig.update_layout(

        scene = dict(
            xaxis = dict(
                backgroundcolor="rgba(0,0,0,0)",
                gridcolor=textCol,
                showbackground=True,
                zerolinecolor=textCol,),
            yaxis = dict(
                backgroundcolor="rgba(0,0,0,0)",
                gridcolor=textCol,
                showbackground=True,
                zerolinecolor=textCol,),
            zaxis = dict(
                backgroundcolor="rgba(0,0,0,0)",
                gridcolor=textCol,
                showbackground=True,
                zerolinecolor=textCol,),
                ),

        # Make sure the background of figures is transparent so that 
        # theme functionality is extended to the figure
        geo=dict(bgcolor= 'rgba(0,0,0,0)'),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0,0,0,0)',

        # Figure Specific-----------------------------------------
        title = dict(
            text = "Rendering 3D Plots and Data",
            xanchor="center",
            xref = "container",
            yref = "container",
            x = 0.5,
            yanchor="top",
            y = .98,
            font = dict(
                size = 32,
                color = textCol
            )
        ),

        font=dict(color=textCol),  # Change axis labels text color
    )

    return fig

