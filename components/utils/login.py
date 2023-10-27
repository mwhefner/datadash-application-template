import flask
import components.utils.sqlconnection as dataserver

# INTERFACING WITH SHIBBOLETH SINGLE SIGN-ON AUTHENTICATION
#
# THESE ARE USED ONLY IN A REQUESTS CONTEXT.
#
# For sign-on.  Checks if the user is signed into 
# their Appalachian account.  If the application is public, this 
# will show the application regardless.  If restricted, this
# application will only show if the user is authorized on the data
# server in the application metadata.
# Define a callback to check user authentication and authorization

def authenticaedLogin():
    # If Remote-User is available in the header 
    if 'Uid' in flask.request.headers:
        
        # Get the username
        username = flask.request.headers['Uid']

        return [True, username]
    
    else :

        return [False, None]

# Access RIEEE Data Server application metadata to determine if
# the user is authorized for this application.
def userIsAuthorized():

    # If there is no request context, ignore and return out
    if not flask.has_request_context():
        return False

    # First grab application metadata.
    metadata = dataserver.get_application_metadata()
    applicationIsPublic = metadata[0][0][0].lower() == "true"

    # If the application is public, return true.
    if applicationIsPublic:
        return True

    # Get Log in information
    login = authenticaedLogin()

    if login[1] is not None :

        metadata = dataserver.get_authorization_metadata(login[1])
        userIsAdmin = metadata[0][0][0].lower() == "true"
        userHasPermission = metadata[1][0][0].lower() == "true"

        if applicationIsPublic or userIsAdmin :
            # USER AUTHORIZED
            return True
        if userHasPermission :
            # USER AUTHORIZED
            return True
    
    # otherwise... USER NOT AUTHORIZED
    return False
