"""
Module/Script Name: advanced_plotly_subfigures.py
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

def randomPlot(s, theme):
    #
    # Plots a random time series
    #
    np.random.seed(s)

    # Define the number of rows
    num_rows = 100

    # Define the start time and time increment
    start_time = pd.Timestamp('2023-10-25 00:00:00')
    time_increment = pd.Timedelta(minutes=15)  # Adjust the increment as needed

    # Create the DataFrame with the 'Time' column
    df = pd.DataFrame({
        'Time': pd.date_range(start=start_time, periods=num_rows, freq=time_increment),
        'y': np.random.rand(num_rows),
        'z': np.random.rand(num_rows)
    })

    if theme == 'light' :
        textCol = '#000'
    if theme == 'dark' :
        textCol = '#fff'

    # Create a Plotly time series
    fig = px.line(
        df, 
        x='Time', 
        y=['y', 'z']
        )

    return fig

def subplot_1(theme):
    fig = randomPlot(1, theme)
    return fig

def subplot_2(theme):
    fig = randomPlot(2, theme)
    return fig

def subplot_3(theme):
    fig = randomPlot(3, theme)
    return fig

def subplot_4(theme):
    fig = randomPlot(4, theme)
    return fig

# Example Plotly Figure
def advanced_plotly_subfigures(theme) :

    if theme == 'light' :
        textCol = '#000'
    if theme == 'dark' :
        textCol = '#fff'

    fig = make_subplots(rows = 2, cols = 2)

    # Each of the subplots
    fig.add_trace(subplot_1(theme).data[0], row=1, col=1)
    fig.add_trace(subplot_2(theme).data[0], row=1, col=2)
    fig.add_trace(subplot_3(theme).data[0], row=2, col=1)
    fig.add_trace(subplot_4(theme).data[0], row=2, col=2)

    fig.update_layout(

        # Make sure the background of figures is transparent so that 
        # theme functionality is extended to the figure
        geo=dict(bgcolor= 'rgba(0,0,0,0)'),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0,0,0,0)',

        # Figure Specific-----------------------------------------
        title = dict(
            text = "Sample Dash Controls and Advanced Plotly Subfigures",
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

