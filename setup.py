from setuptools import setup

setup(
        name='ahlure',
        version='1.0',
        long_description=__doc__,
        packages=['ahlure'],
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'Flask==0.9',
            'Jinja2==2.7',
            'MarkupSafe==0.18',
            'Werkzeug==0.8.3',
            'gunicorn==0.17.4',
            'wsgiref==0.1.2',
            ] 
        )
