"""
John Doe's Flask API.
"""

from flask import Flask, render_template, request, send_from_directory, abort
import os
import configparser
import sys

def parse_config(config_paths):
    """ Parses the configuration file like in project 0 """
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

# Get port and debug from the credentials.ini if it exists, and if not then from default.ini
config = parse_config(["credentials.ini", "default.ini"])
port = config["SERVER"]["PORT"]
debug = config["SERVER"]["DEBUG"]


app = Flask(__name__)

# Catch all app route 
@app.route("/<path:filename>")
def catch_all(filename):
    """ Returns corresponding page if it exists or error code page """

    path = 'pages/'+ filename   # Set up the path we will be searching for
    if (".." in path or '~' in path):   # Chekcs for illegal chars no longer suffixes since those were not specified
        abort(403)      # Sends abort code 403 and links to errorhandler(403) --> Forbidden
    elif not os.path.isfile(path):   # Checks if the path does not exist  
        abort(404)      # Sends abort code 404 and links to errorhandler(404) --> File_Not_Found
    else:   # Otherwise
        page = path.split('/')[-1]       # Isolates the suffix
        path = path[:-(len(page))]      # Exclude the file from search
        return send_from_directory(path, page), 200     # If so send the page
    return

''' 
ERROR HANDLERS 
--> Below are the two paths for error handling the first an error handler for 404 in which the page is not found.
The second for 403 in which the user included illegal charchaters in their search. These will transmit an error code header as well 
as the appropriate page corresponding to the error.
'''

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("ERROR 404: Page not found")           # Send error code
    return send_from_directory('pages/', '404.html'), 404   # Display error code html for 404

@app.errorhandler(403)
def forbidden(error):
    app.logger.debug("ERROR 403: Forbidden")                   # Send error code
    return send_from_directory('pages/', '403.html'), 403      # Display error code html for 404

if __name__ == "__main__":
    app.run(port=port, debug=debug, host='0.0.0.0')
