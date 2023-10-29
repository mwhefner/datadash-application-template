"""
Module/Script Name: three_d_example.py

Author(s): M. W. Hefner

Initially Created: 7/12/2023

Last Modified: 10/29/2023

Script Description: this script defines some 3D example figures.  These examples come directly from plotly's documentation, though arranged differently.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import needed libraries
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
from plotly import express as px

# Surface Visualization
def surface_viz(textCol) :

    a, b, d = 1.32, 1., 0.8
    c = a**2 - b**2
    u, v = np.mgrid[0:2*np.pi:100j, 0:2*np.pi:100j]
    x = (d * (c - a * np.cos(u) * np.cos(v)) + b**2 * np.cos(u)) / (a - c * np.cos(u) * np.cos(v))
    y = b * np.sin(u) * (a - d*np.cos(v)) / (a - c * np.cos(u) * np.cos(v))
    z = b * np.sin(v) * (c*np.cos(u) - d) / (a - c * np.cos(u) * np.cos(v))

    return go.Surface(x=x, y=y, z=z, colorbar_x=-0.07)

# Volume Density Visualization
def density_viz(textCol) :
    X, Y, Z = np.mgrid[-1:1:30j, -1:1:30j, -1:1:30j]
    values =    np.sin(np.pi*X) * np.cos(np.pi*Z) * np.sin(np.pi*Y)

    fig = go.Volume(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=-0.1,
    isomax=0.8,
    opacity=0.1, # needs to be small to see through all surfaces
    surface_count=21, # needs to be a large number for good volume rendering
    )

    return fig


# Example Plotly Figure
def three_d_example(theme) :

    if theme == 'light' :
        textCol = '#000'
    if theme == 'dark' :
        textCol = '#fff'

    # Init the plot
    fig = make_subplots(rows=1, cols=2,
                        specs=[[{'is_3d': True}, {'is_3d': True}]],
                        subplot_titles=['Color corresponds to z value', 'Seamlessly Integrate 3D Data'],
                        )

    # Add the surface
    fig.add_trace(surface_viz(textCol), 1, 1)

    # Add the MRI viz
    fig.add_trace(density_viz(textCol), 1, 2)

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

        scene2 = dict(
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

