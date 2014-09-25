Google Appengine Application Template
=====================================

This package is a PasteScript template that creates a fully working GAE application.


Installing the template
-----------------------

In order to install the template, you can install it from Pypi::


    pip install gae.template.app


Creating an application
-----------------------


First, check that the template is correctly available among paster templates::

    paster create --list-templates

    
If all is working correctly, you should see something like::

    [cut]
    gae_project:    Google Appengine Project template
    [cut]
    
and you are sure you can use the newly installed template.

Initializing the application
----------------------------


The application is designed to be used by fabengine (link), so please refer to it to be sure to always have the latest
information available.

Anyway, these are the few steps you need to initialize the app.


Installing the requirements
---------------------------


In order to install the requirements, type::
    
    pip install -r dev_requirements.txt
    
    
Now, slightly modify the virtualenv paths (yes, you should use a virtualenv, it's a really good pratice):

    fab fabengine.fix_virtualenv_paths
    
    
Last, and most important thing, create the dependency wheels for the project:
    
    fab fabengine.bundle_packages
    
    
Run the application
-------------------


To run the application, type::

    fab fabengine.dev_appserver
    
..note:: Note

    Please be aware that the file `fabfile.py` contains directives used by the wrapper dev_appserver.py script.
    
