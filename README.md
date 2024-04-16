# UOCIS322 - Project 2 Pageserver


# Descriptions


## Application


 This is a simple pageserver project in which a server is hosted on port 5000 using a docker container system. From there the program serves three possible codes and pages using flask, the first option is a 200 message that is okay and sends a green page with red text if the user requested a valid page. The second option is a 403 STATUS_IS_FORBIDDEN page if the user requested a page using illegal characters ('..' or '~'). The third and final option is if the user requested a page with legal characters, but the page was not found eliciting a 404 STATUS_NOT_FOUND error page and code. The project is similar to project 1, but is initialized within the web directory, uses docker and flask, and can serve pages within subdirectories given the user provided a valid path to such file. 


# Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani. Completed by Ellison Schilling.

## Contact Address

ellisons@uoregon.edu
