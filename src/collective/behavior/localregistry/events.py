from zope.interface import implements
from zope.component.interfaces import ObjectEvent

from interfaces import ILocalRegistryCreatedEvent


class LocalRegistryCreatedEvent(ObjectEvent):
    implements(ILocalRegistryCreatedEvent)
