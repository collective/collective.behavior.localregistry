# -*- coding: utf-8 *-*

from collective.behavior.localregistry.interfaces import ILocalRegistryCreatedEvent
from zope.component.interfaces import ObjectEvent
from zope.interface import implements


class LocalRegistryCreatedEvent(ObjectEvent):
    implements(ILocalRegistryCreatedEvent)
