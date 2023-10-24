"""
Module/Script Name: application.py
Author: M. W. Hefner
Created: 6/28/2023
Last Modified: 10/24/2023

Project: DataDash Application Template

Script Description: This script initializes the dash application. It loads in needed libraries, reads the data server configuration, loads style sheets, and initializes the server.

It also contains the scripting that authorizes a user to access the application.

Exceptional notes about this script:

1. This script is for development on a local machine: after loading into a python environment with the dependencies in requirements.txt, found in this directory, installed, run this script to run the application server on local host at port 8050.

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Import Dependencies
import dash
import configparser
from flask import Flask, request, redirect, url_for
from functools import wraps
import components.main_container as mc
import components.utils.login as login
from components.utils.constants import application_title, repo_title

# Read data server configuration
cfg = configparser.ConfigParser()
cfg.read('/etc/rieee/rieee.conf')
cfg.read('rieee.conf')

# Import Styles that _have_ to be CSS;
external_stylesheets = {
    'light_theme' : [
        "./assets/externalstylesheets/dynamic_styling.css",
        "./assets/externalstylesheets/themes.css"
    ]
}

# Initialize Dash Application
app = dash.Dash(
    __name__, 
    external_stylesheets = external_stylesheets['light_theme'],
    title = application_title,
    update_title = None,
    url_base_pathname=cfg.get('app', 'url_prefix', fallback='/'),
    suppress_callback_exceptions=True
)

app.config.suppress_callback_exceptions = True

# Define Layout as a div
app.layout = dash.html.Div(
        children = [
            dash.dcc.Location(id='url'),
            dash.html.Div(id='secure-div')
            ],
    )

# This callback gets ran when a user loads the page or
# the url is altered in some way.  This checks that
# the user is authorized to view the application (main container)
@dash.callback(
    dash.Output('secure-div', 'children'),
    dash.Input('url', 'pathname')
)
def authorize(pathname):
    if login.userIsAuthorized() :
        return mc.layout
    else :
        return dash.html.P(
            [
                "Please ",
                dash.html.A(
                    "sign in with Shibboleth", 

                    # To be changed for new applications!
                    href = "/Shibboleth.sso/Login?target=/" + repo_title, 
                ),
                " to access this DataDash application."
            ],
            style={'text-align' : 'center'}
        )

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

server = app.server

# Main script execution for (local development only)
# Uncomment this to develop locally on the local host
# Comment the following out before re-committing to the repo
if __name__ == '__main__':
    app.run_server(debug = True)
