"""
Module/Script Name: animation_example.py
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
from skimage import io


# Example Plotly Figure
def animation_example(theme) :

    if theme == 'light' :
        textCol = '#000'
    if theme == 'dark' :
        textCol = '#fff'

    data = io.imread("assets/data/cells.tif")

    data = data.reshape((15, 4, 256, 256))[5:]

    fig = px.imshow(data, animation_frame=0, facet_col=1, binary_string=True)

    #fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    fig.update_layout(

        # Make sure the background of figures is transparent so that 
        # theme functionality is extended to the figure
        geo=dict(bgcolor= 'rgba(0,0,0,0)'),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0,0,0,0)',


        # Figure Specific-----------------------------------------
        title = dict(
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
        xaxis_title="Time",
        yaxis_title="Values",
        font=dict(color=textCol),  # Change axis labels text color
    )

    return fig

