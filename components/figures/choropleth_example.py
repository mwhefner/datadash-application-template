"""
Module/Script Name: choropleth_example.py

Author(s): M. W. Hefner

Initially Created: 7/12/2023

Last Modified: 10/29/2023

Script Description: this shows an example of a mapbox choropleth plotly figure given as an example in the plotly documentation here: https://plotly.com/python/mapbox-county-choropleth/

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import needed libraries
import pandas as pd
import json

# Example Plotly Figure
def choropleth_example(theme) :

    if theme == 'light' :
        textCol = '#000'
        map_theme = "carto-positron"
    if theme == 'dark' :
        textCol = '#fff'
        map_theme = "open-street-map"

    # Open the JSON file
    with open('assets/data/geojson-counties-fips.json', 'r') as json_file:
        # Load the JSON data into a Python data structure
        counties = json.load(json_file)

    df = pd.read_csv("assets/data/fips-unemp-16.csv", dtype={"fips": str})

    import plotly.graph_objects as go

    fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df.fips, z=df.unemp,
                                        colorscale="Viridis", zmin=0, zmax=12,
                                        marker_opacity=0.5, marker_line_width=0))
    fig.update_layout(mapbox_style=map_theme,
                    mapbox_zoom=4, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    fig.update_layout(

        # Make sure the background of figures is transparent so that 
        # theme functionality is extended to the figure
        geo=dict(bgcolor= 'rgba(0,0,0,0)'),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0,0,0,0)',

        # Figure Specific-----------------------------------------
        title = dict(
            text="Choropleth Map Example: Switch Theme to Change Base Map",
            xanchor="center",
            xref = "container",
            yref = "container",
            x = 0.5,
            yanchor="top",
            y = .98,
            font = dict(
                size = 32,
                color = "black"
            )
        ),
        xaxis_title="Time",
        yaxis_title="Values",
        font=dict(color=textCol),  # Change axis labels text color
    )

    return fig

