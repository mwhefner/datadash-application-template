"""
Module/Script Name: browse.py
Author: M. W. Hefner

Created: 7/15/2023
Last Modified: 7/16/2023

Project: DataDash Application Template

Script Description: This script defines the dash datatable and its container used for a browse table page.

Exceptional notes about this script:

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""
# Component ID (Should be the same as the title of this file)
component_id = "browse"

# Import Dependencies
import dash.html.Div
import dash.html.P
import dash.dash_table.DataTable
import pandas as pd
import base64
import datetime
import io

def browse_table() :

    return dash.html.Div(
        children=[
        dash.dcc.Upload(
            id='upload-data-table',
            children=dash.html.Div([
                'Drag and Drop or ',
                dash.html.A('Select a CSV or an Excel File')
            ]),
            # Allow multiple files to be uploaded
            multiple=True
        ),
        dash.html.Div(id='output-data-upload'),
    ])

# Callback helper function
def parse_contents(contents, filename, date, theme):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return dash.html.Div([
            'There was an error processing this file.'
        ])
    
    # Set a maximum width for columns and enable word wrap
    style = {
        'maxWidth': 200,
        'whiteSpace': 'normal',
    }

    textColor = "black"
    cellsBackground = "rgba(0,0,0,0)"

    if theme == 'dark' :
        textColor = "white"

    return dash.html.Div(
        children = [
        dash.html.H5(filename),
        dash.html.H6(["Uploaded at: ", datetime.datetime.fromtimestamp(date)]),
            dash.dash_table.DataTable(
                df.to_dict('records'),
                [{'name': i, 'id': i} for i in df.columns],
                style_table={'overflowX': 'auto'},
                style_cell=style,  # Apply style to all cells
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
                page_action="native",
                page_current= 0,
                fill_width = False,
                style_header={
                    'backgroundColor': cellsBackground,
                    'color': textColor
                },
                style_data={
                    'backgroundColor': cellsBackground,
                    'color': textColor
                }
            ),
        ]
    )

@dash.callback(dash.Output('output-data-upload', 'children'),
              dash.Input('upload-data-table', 'contents'),
              dash.State('upload-data-table', 'filename'),
              dash.State('upload-data-table', 'last_modified'),
              dash.Input('theme_toggle', 'className'),
              )
def update_output(list_of_contents, list_of_names, list_of_dates, theme):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d, theme) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children