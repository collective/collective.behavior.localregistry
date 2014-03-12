*********************************
collective.behavior.localregistry
*********************************

.. contents:: Table of Contents

Life, the Universe, and Everything
==================================

Dexterity behavior to add a local plone.app.registry for content types, it
adds a local component with a layered proxy registry.

Mostly Harmless
===============

.. image:: https://secure.travis-ci.org/collective/collective.behavior.localregistry.png?branch=master
    :alt: Travis CI badge
    :target: http://travis-ci.org/collective/collective.behavior.localregistry

.. image:: https://coveralls.io/repos/collective/collective.behavior.localregistry/badge.png?branch=master
    :alt: Coveralls badge
    :target: https://coveralls.io/r/collective/collective.behavior.localregistry

.. image:: https://pypip.in/d/collective.behavior.localregistry/badge.png
    :target: https://pypi.python.org/pypi/collective.behavior.localregistry/
    :alt: Downloads

Got an idea? Found a bug? Let us know by `opening a support ticket`_.

.. _`opening a support ticket`: https://github.com/collective/collective.behavior.localregistry/issues

Don't panic
===========

Installation
------------

To enable this product in a buildout-based installation:

#. Edit your buildout.cfg and add ``collective.behavior.localregistry`` to the
   list of eggs to install::

    [buildout]
    ...
    eggs =
        collective.behavior.localregistry

#. If you are using Plone 4.1 you may need to extend a Dexterity known good
   set (KGS) to make sure that you get the right versions of the packages that
   make up Dexterity::

    [buildout]
    ...
    extends =
        https://good-py.appspot.com/release/dexterity/1.2.1?plone=4.1.6

After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``collective.behavior.localregistry`` and click the
'Activate' button.

.. Note::
    You may have to empty your browser cache and save your resource registries
    in order to see the effects of the product installation.
