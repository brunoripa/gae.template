from paste.script.templates import Template, var


q = [
    var('version', 'Version (like 0.1)'),
    var('description', 'One-line description of the package'),
    var('long_description', 'Multi-line description (in reST)'),
    var('keywords', 'Space-separated keywords/tags'),
    var('author', 'Author name'),
    var('author_email', 'Author email'),
    var('url', 'URL of homepage'),
    var('license_name', 'License name'),
    var('zip_safe', 'True/False: if the package can be distributed as a .zip file',
        default=False),
    var('deferred', 'True/False: if you want to activate deferrer builtin', default=True),
    var('remote_api', 'True/False: if you want to activate remote_api builtin', default=True),
    var('appstats', 'True/False: if you want to activate appstats builtin', default=True),
    var('bootstrap_version', 'The Bootstrap version you desire, something like: `3.2.0`.',
        default='3.2.0'),
    var('jquery_version', 'The jQuery version you desire, something like: `1.11.1`.',
        default='1.11.1')
]


class GaeProjectTemplate(Template):
    _template_dir = 'template/'
    summary = 'Google Appengine Project template'
    vars = q