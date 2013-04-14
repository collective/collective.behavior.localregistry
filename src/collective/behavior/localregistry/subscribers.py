# -*- coding: utf-8 *-*

from collective.behavior.localregistry.events import LocalRegistryCreatedEvent
from collective.behavior.localregistry.proxy import LocalRegistry
from collective.behavior.localregistry.proxy import REGISTRY_NAME
from five.localsitemanager import make_objectmanager_site
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from zope.component import getSiteManager
from zope.component.interfaces import ISite

import zope.event


def enableChildRegistry(context, event):
    """
    """
    if not ISite.providedBy(context):
        make_objectmanager_site(context)
    # reindex so that the object_provides index is aware of our
    # new interface
    catalog = getToolByName(context, 'portal_catalog')
    catalog.reindexObject(
        context,
        idxs=['object_provides']
    )
    sm = getSiteManager(context=context)
    if REGISTRY_NAME not in context.objectIds():
        context[REGISTRY_NAME] = LocalRegistry(REGISTRY_NAME).__of__(context)
    sm.registerUtility(component=context[REGISTRY_NAME], provided=IRegistry)
    zope.event.notify(LocalRegistryCreatedEvent(context))
