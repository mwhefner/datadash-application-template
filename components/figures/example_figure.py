"""
Module/Script Name: example_figure.py
Author: M. W. Hefner

Created: 4/12/2023
Last Modified: 7/16/2023

Project: DataDash Application Template

Script Description: This script defines an example plotly figure using static data from the RIEEE data server.

Exceptional notes about this script:
(none)

Callback methods: N/A

~~~

This figure was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import needed libraries
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import datetime
import plotly.io as pio
import components.utils.sqlconnection as sqlconnection

# Function to retrieve data from data server
def get_static_data():
    sql = '''
    SELECT * FROM static
    '''
    sqlconnection.cursor.execute(sql)
    result = sqlconnection.cursor.fetchall()
    return result

# Example Plotly Figure
def example_figure(theme) :

    example_static_data = get_static_data()

    df = pd.DataFrame(example_static_data, columns=["Time", "Variable1", "Variable2"])

    if theme == 'light' :
        textCol = '#000'
    if theme == 'dark' :
        textCol = '#fff'

    # Create a Plotly time series figure with a range selector
    fig = px.line(
        df, 
        x='Time', 
        y=['Variable1', 'Variable2']
        )

    # Add a range selector
    fig.update_xaxes(rangeslider_visible=True)  # Add a range selector

    fig.update_layout(

        # Make sure the background of figures is transparent so that 
        # theme functionality is extended to the figure
        geo=dict(bgcolor= 'rgba(0,0,0,0)'),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0,0,0,0)',

        # Figure Specific-----------------------------------------
        title = dict(
            text = "Example Plotly Figure of Static Data",
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