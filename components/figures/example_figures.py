"""
Module/Script Name: example_figures.py

Author(s): M. W. Hefner

Initially Created: 4/12/2023

Last Modified: 10/29/2023

Script Description: this script connects to the data server and retrieves some sample data.  It then uses that data - and other data it generates - to demonstrate some simple plotly figures.

The top right figure comes from: https://plotly.com/python/histograms/
The bottom left figure comes from: https://plotly.com/python/box-plots/
The bottom right figure comes from: an example on https://plotly.com/python/

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import needed libraries
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import numpy as np
import components.utils.sqlconnection as sqlconnection

# Creates a random plot (for development purposes)
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

# Example of plotting secure research data from the data server
def data_server_data_figure(theme) :

    example_static_data = sqlconnection.get_research_data()

    df = pd.DataFrame(example_static_data, columns=["Time", "Variable1", "Variable2"])

    df['Variable1'] = df['Variable1'] + 3

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

    fig.update_layout(

        # Make sure the background of figures is transparent so that 
        # theme functionality is extended to the figure
        geo=dict(bgcolor= 'rgba(0,0,0,0)'),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0,0,0,0)',

        # Figure Specific-----------------------------------------
        xaxis_title="Time",
        yaxis_title="Values",
        font=dict(color=textCol),  # Change axis labels text color
    )

    return fig

def subplot_2(theme):
    np.random.seed(1)
    x0 = np.random.randn(500)
    # Add 1 to shift the mean of the Gaussian distribution
    x1 = np.random.randn(500) + 1

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=x0))
    fig.add_trace(go.Histogram(x=x1))

    # Overlay both histograms
    fig.update_layout(barmode='overlay')
    # Reduce opacity to see both histograms
    fig.update_traces(opacity=0.75)
    return fig

def subplot_3(theme):
    np.random.seed(1)
    N = 30     # Number of boxes

    # generate an array of rainbow colors by fixing the saturation and lightness of the HSL
    # representation of colour and marching around the hue.
    # Plotly accepts any CSS color format, see e.g. http://www.w3schools.com/cssref/css_colors_legal.asp.
    c = ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, N)]

    # Each box is represented by a dict that contains the data, the type, and the colour.
    # Use list comprehension to describe N boxes, each with a different colour and with different randomly generated data:
    fig = go.Figure(data=[go.Box(
        y=3.5 * np.sin(np.pi * i/N) + i/N + (1.5 + 0.5 * np.cos(np.pi*i/N)) * np.random.rand(10),
        marker_color=c[i]
        ) for i in range(int(N))])

    # format the layout
    fig.update_layout(
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(zeroline=False, gridcolor='white'),
        paper_bgcolor='rgb(233,233,233)',
        plot_bgcolor='rgb(233,233,233)',
    )
    return fig

def subplot_4(theme):
    np.random.seed(1)

    N = 100
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N) - 5

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                        mode='markers',
                        name='markers'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                        mode='lines+markers',
                        name='lines+markers'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                        mode='lines',
                        name='lines'))

    return fig

def simple_example_figures(theme):


    if theme == 'light' :
        textCol = '#000'
    if theme == 'dark' :
        textCol = '#fff'

    fig = make_subplots(rows = 2, cols = 2)

    # Each of the subplots

    # From the data server
    for trace in data_server_data_figure(theme).data:
        fig.add_trace(trace, row=1, col=1)

    # Histogram
    for trace in subplot_2(theme).data:
        fig.add_trace(trace, row=1, col=2)

    for trace in subplot_3(theme).data:
        fig.add_trace(trace, row=2, col=1)

    for trace in subplot_4(theme).data:
        fig.add_trace(trace, row=2, col=2)

    fig.update_layout(

        # Make sure the background of figures is transparent so that 
        # theme functionality is extended to the figure
        geo=dict(bgcolor= 'rgba(0,0,0,0)'),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0,0,0,0)',

        # Figure Specific-----------------------------------------
        title = dict(
            text = "Plotly Figures of Secure Data from Data Server",
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