"""
setup.py - Setup file to distribute the library

See Also:
    https://github.com/pypa/sampleproject
    https://packaging.python.org/en/latest/distributing.html
    https://pythonhosted.org/an_example_pypi_project/setuptools.html
"""
import os
import glob
from setuptools import setup, Extension, find_packages

import numpy


def read(fname):
    """Read in a file"""
    with open(os.path.join(os.path.dirname(__file__), fname), 'r') as file:
        return file.read()


def get_meta(filename):
    """Return the metadata dictionary from the given filename."""
    with open(filename, 'r') as f:
        meta = {}
        exec(compile(f.read(), filename, 'exec'), meta)
        return meta


if __name__ == "__main__":
    # Variables
    meta = get_meta('np_rw_buffer/__meta__.py')
    name = meta['name']
    version = meta['version']
    description = meta['description']
    url = meta['url']
    author = meta['author']
    author_email = meta['author_email']
    keywords = 'read write ring circular buffer'
    packages = find_packages(exclude=('tests', 'bin'))

    # Extensions
    extensions = [
        Extension('np_rw_buffer._circular_indexes',
                  # define_macros=[('MAJOR_VERSION', '1')],
                  # extra_compile_args=['-std=c99'],
                  sources=['src/circular_indexes.c'],
                  include_dirs=['src', numpy.get_include()]),
        ]

    setup(name=name,
          version=version,
          description=description,
          long_description=read('README.rst'),
          keywords=keywords,
          url=url,
          download_url=''.join((url, '/archive/v', version, '.tar.gz')),

          author=author,
          author_email=author_email,

          license='MIT',
          platforms='any',
          classifiers=['Programming Language :: Python',
                       'Programming Language :: Python :: 3',
                       'Operating System :: OS Independent'],

          scripts=[file for file in glob.iglob('bin/*.py')],  # Run with python -m Scripts.module args

          ext_modules=extensions,  # C extensions
          packages=packages,
          include_package_data=True,
          package_data={pkg: ['*', '*/*', '*/*/*', '*/*/*/*', '*/*/*/*/*']
                        for pkg in packages if '/' not in pkg and '\\' not in pkg},

          # Data files outside of packages
          # data_files=[('my_data', ['data/my_data.dat'])],

          # options to install extra requirements
          install_requires=[
              'numpy>=1.13.0',
              ],
          extras_require={
              },

          # entry_points={
          #     'console_scripts': [
          #         'plot_csv=bin.plot_csv:plot_csv',
          #         ],
          #     'gui_scripts': [
          #         'baz = my_package_gui:start_func',
          #         ]
          #     }
          )
