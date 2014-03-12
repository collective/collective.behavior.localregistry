# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '1.0b2'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(name='collective.behavior.localregistry',
      version=version,
      description="Dexterity behavior to add a local plone.app.registry for \
          content types, it adds a local component with a layered \
          proxy registry.",
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Plone',
          'Framework :: Plone :: 4.1',
          'Framework :: Plone :: 4.2',
          'Framework :: Plone :: 4.3',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='plone registry local behavior dexterity',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='https://github.com/collective/collective.behavior.localregistry',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.behavior'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.app.registry',
          'plone.behavior',
          'plone.registry',
          'Products.CMFCore',
          'setuptools',
          'zope.component',
          'zope.event',
          'zope.i18nmessageid',
          'zope.interface',
      ],
      extras_require={
          'develop': [
              'manuel',
              'setuptools-flakes',
              'Sphinx',
          ],
          'test': [
              'interlude',
              'plone.app.dexterity',
              'plone.app.testing',
              'plone.dexterity',
              'plone.testing',
              'unittest2',
          ]
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
