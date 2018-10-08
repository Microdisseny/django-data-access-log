import os
from setuptools import find_packages, setup

VERSION = '0.1'

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_data_access_log',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Log the access to endpoints of your API',
    long_description=README,
    url='https://github.com/Microdisseny/django-data-access-log/',
    author='Microdisseny Giscube SLU',
    author_email='tech@microdisseny.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
