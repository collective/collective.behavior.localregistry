# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '1.0.dev0'
long_description = (
    open("README.rst").read() + "\n" +
    open(os.path.join("docs", "INSTALL.rst")).read() + "\n" +
    open(os.path.join("docs", "CREDITS.rst")).read() + "\n" +
    open(os.path.join("docs", "HISTORY.rst")).read()
)

setup(name='collective.behavior.localregistry',
      version=version,
      description="Dexterity behavior to add a local plone.app.registry for \
          content types, it adds a local component with a layered \
          proxy registry.",
      long_description=long_description,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Office/Business :: News/Diary",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='plone registry local behavior dexterity',
      author='',
      author_email='',
      url='https://github.com/collective/collective.behavior.localregistry',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.behavior'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.behavior',
          'plone.dexterity',
          'plone.namedfile',
          'rwproperty',
      ],
      extras_require={
          'develop': [
              'Sphinx',
              'manuel',
              'pep8',
              'setuptools-flakes',
          ],
          'test': [
              'interlude',
              'plone.app.testing',
              'plone.app.dexterity',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-
        [z3c.autoinclude.plugin]
        target = plone
      """,
      )
