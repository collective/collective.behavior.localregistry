# -*- coding: utf-8 *-*

from zope.interface import Interface


class ILocalRegistry(Interface):
    """Dexterity behavior to add a local plone.app.registry for content types,
    it adds a local component with a layered proxy registry.
    """
