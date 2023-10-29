"""
Module/Script Name: animation_example.py

Author(s): M. W. Hefner

Initially Created: 7/12/2023

Last Modified: 10/29/2023

Script Description: this is an example of an animation with plotly figures.  This figure example comes from https://plotly.com/python/imshow/ (combining animations and facets).

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import needed libraries
import plotly.express as px
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

