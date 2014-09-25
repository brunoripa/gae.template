from setuptools import setup, find_packages

version = "0.0"

setup(name="gae.template.app",
    version=version,
    description="GAE Application template for PasteScript",
    long_description="""Long description""",
    classifiers=[],
    keywords="",
    author="Bruno Ripa",
    author_email="bruno.ripa@gmail.com",
    url="",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=["PasteScript>=1.3"],
    entry_points="""
    [paste.paster_create_template]
    gae_project=template:GaeProjectTemplate
    """
)