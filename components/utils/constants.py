"""
Module/Script Name: constants.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 9/08/2023

Contains import and other utility functions for the application.

"""

# Import Dependencies
import pandas as pd
import math

# SETS THE TITLE OF THE APPLICATION
application_title = "RIEEE DataDash Application Template"

# Import static data
example_static_data = pd.read_excel('./assets/example_static_data.xlsx')

# For defining cleaning utilities for static data
def static_utility():
    return NULL
    
# Read Markdown Pages--------------------------------------------------

# About page
with open("readme.md", "r") as file:
    about_content = file.read()
