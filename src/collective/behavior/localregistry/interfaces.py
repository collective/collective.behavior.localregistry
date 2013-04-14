# -*- coding: utf-8 *-*

from zope.interface import Interface


class ILocalRegistryCreatedEvent(Interface):
    """An event that is fired after a local registry is created
    """
