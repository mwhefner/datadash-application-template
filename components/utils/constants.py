"""
Module/Script Name: constants.py

Author(s): M. W. Hefner

Initially Created: 06/28/2023

Last Modified: 10/29/2023

Script Description: this script contains constants and calls for locally stored (on the application server) data.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import Dependencies
import pandas as pd
import math

# IN-LINE APPLICATION METADATA----------------------------------------

# SETS THE TITLE OF THE APPLICATION
application_title = "RIEEE DataDash Application Template"

# SET THE APPLICATION ID (APPLICATION METADATA USED FOR AUTHORIZATION)
app_id = 8

# SET THE REPO TITLE (APPLICATION METADATA USED FOR AUTHORIZATION)
repo_title = "datadash-application-template"

app_doi = "NONE_FOR_TEMPLATE"

developers = "Matt Hefner"

version = "1.0.0"

# Import static data
example_static_data = pd.read_excel('./assets/data/example_static_data.xlsx')

# For defining cleaning utilities for static data
def static_utility():
    return NULL
    
# Read Markdown Pages--------------------------------------------------

# About page
with open("readme.md", "r") as file:
    about_content = file.read()
