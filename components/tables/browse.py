"""
Module/Script Name: browse.py
Author: M. W. Hefner

Created: 7/15/2023
Last Modified: 7/16/2023

Project: DataDash Application Template

Script Description: This script defines the dash datatable and its container used for a browse table page.

Exceptional notes about this script:
(none)

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
from components.utils import constants as d

def browse_table() :

    return dash.html.Div(
        id = component_id,
        className = "table_container",
        children = [
            # TODO: Look into styling this page better.
            # Do dash.data_table/s play nice with css?
            dash.html.H1('Example Static Data Table'),
            dash.html.P('Use the sidebar dropdowns to select data.  Filter and sort below.  Inequality filters (e.g. ">2005" for Year) are supported.'),
            dash.dash_table.DataTable(
                fill_width = False,
                data=d.example_static_data.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in ["Time", "Variable1", "Variable2"]],
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
                page_action="native",
                page_current= 0,
                page_size= 15,
            )
        ]
    )