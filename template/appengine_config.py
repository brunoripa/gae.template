appstats_MAX_STACK = 20


def add_wsgi_middleware(app):
    """
    Enables appstats

    :param app: application object
    :return: returns the application object
    """

    from google.appengine.ext.appstats import recording
    app.wsgi_app = recording.appstats_wsgi_middleware(app.wsgi_app)
    return app


#FABENGINE PKG LOADER
def _gae_pkg_loader():
    import sys, os
    package_dir = "packages"
    package_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), package_dir))
    packages = sorted(os.listdir(package_dir_path), key=lambda x:x.lower(), reverse=True)
    for filename in packages:
        filename = os.path.join(package_dir_path, filename)
        if filename.endswith('.whl') or os.path.isdir(filename):
            sys.path.insert(0, filename)
    sys.path.insert(0, package_dir_path)

_gae_pkg_loader()
