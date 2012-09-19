# -*- coding: utf-8 *-*
"""Dexterity behavior to add a local plone.app.registry for
content types, it adds a local component with a layered proxy registry.
"""
from zope.interface import implements, Interface


class ILocalRegistry(Interface):
    """
    """
