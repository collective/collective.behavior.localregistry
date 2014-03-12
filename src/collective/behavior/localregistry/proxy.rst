Testing the Layered Proxy Registry
==================================

Basic Setup
-----------

Create ```child``` folder for tests::

    >>> portal = layer.get('app').plone
    >>> z2.login(portal['acl_users'], 'manager')

    >>> from plone.dexterity.fti import DexterityFTI
    >>> fti = DexterityFTI('My Dexterity Container')
    >>> portal.portal_types._setObject('My Dexterity Container', fti)
    'My Dexterity Container'
    >>> fti.klass = 'plone.dexterity.content.Container'
    >>> fti.schema = 'collective.behavior.localregistry.tests.test_setup.IMyDexterityContainer'
    >>> fti.behaviors = ('collective.behavior.localregistry.behavior.ILocalRegistry',)

    >>> childid = portal.invokeFactory("My Dexterity Container", "child")
    >>> child = portal['child']

    >>> import transaction
    >>> savepoint = transaction.savepoint(optimistic=True)

Check registry creation
-----------------------

::

    >>> from zope.component import getSiteManager
    >>> csm = getSiteManager(child)
    >>> csm
    <PersistentComponents child>

XXX: Here test is cheating: We need to check if ```getUtility(IRegistry)```
returns the childs sitemanager registry. Well, this needs publishers traversal
as far as i know. No idea how to do this in a test. To be done.

What actually happens is::

    >>> from zope.component.hooks import setSite
    >>> setSite(child)

An now we can go on as if we are after publishers traversal::

    >>> from zope.component import getUtility
    >>> from plone.registry.interfaces import IRegistry
    >>> child_registry = getUtility(IRegistry)
    >>> child_registry
    <LocalRegistry at /plone/child/local_registry>

Rename support
--------------

We should be able to rename our existing object and have the utility
query still function without errors::

    >>> from zope.component import queryUtility
    >>> portal.manage_renameObject('child', 'renamed')
    >>> child_registry = queryUtility(IRegistry)
    >>> child_registry
    <LocalRegistry at /plone/renamed/local_registry>

Restore the original child name::

    >>> portal.manage_renameObject('renamed', 'child')

Check parent
------------

Searching parent registry::

    >>> child_registry._parent_registry
    <Registry at /plone/portal_registry used for /plone/child/local_registry>

    >>> psm = getSiteManager(portal)
    >>> portal_registry = psm.getUtility(IRegistry)
    >>> child_registry._parent_registry.aq_base is portal_registry.aq_base
    True

Records Read/Write
------------------

Prepare data::

    >>> from plone.registry import Record
    >>> from plone.registry import field

    >>> portal_registry.records['collective.behavior.localregistry.tests.cms'] = \
    ...     Record(field.TextLine(title=u"CMS of choice"), u"Plone")

Read from portal registry values from child registry::

    >>> child_registry.records
    <collective.behavior.localregistry.proxy._LocalRecords object at 0x...>

    >>> child_registry.records['collective.behavior.localregistry.tests.cms'].value
    u'Plone'

Write ...::

    >>> child_registry.records['collective.behavior.localregistry.tests.cms'] = \
    ...     Record(field.TextLine(title=u"CMS of choice"), u"Plone + collective.behavior.localregistry")

... and read back::

    >>> child_registry.records['collective.behavior.localregistry.tests.cms'].value
    u'Plone + collective.behavior.localregistry'

    >>> portal_registry.records['collective.behavior.localregistry.tests.cms'].value
    u'Plone'

Iter::

    >>> [_ for _ in child_registry.records if _ == 'collective.behavior.localregistry.tests.cms']
    ['collective.behavior.localregistry.tests.cms']

    >>> len([_ for _ in child_registry.records]) > 1
    True

Remove, contains, keys::

    >>> 'collective.behavior.localregistry.tests.cms' in child_registry.records.keys()
    True

    >>> del child_registry.records['collective.behavior.localregistry.tests.cms']
    >>> 'collective.behavior.localregistry.tests.cms' in child_registry.records.keys()
    True

    >>> portal_registry.records['collective.behavior.localregistry.tests.cms'].value
    u'Plone'

    >>> child_registry.records['collective.behavior.localregistry.tests.cms'].value
    u'Plone'

    >>> del portal_registry.records['collective.behavior.localregistry.tests.cms']
    >>> 'collective.behavior.localregistry.tests.cms' in child_registry.records
    False
    >>> 'collective.behavior.localregistry.tests.cms' in child_registry.records.keys()
    False

    >>> child_registry.records['collective.behavior.localregistry.tests.cms'] = \
    ...     Record(field.TextLine(title=u"CMS of choice"), u"Plone + collective.behavior.localregistry")

    >>> 'collective.behavior.localregistry.tests.cms' in child_registry.records
    True
    >>> 'collective.behavior.localregistry.tests.cms' in child_registry.records.keys()
    True

    >>> child_registry.records['collective.behavior.localregistry.tests.cms'].value
    u'Plone + collective.behavior.localregistry'

XXX Todo: minKey, maxKey, _getField

Access via registry
-------------------

::

    >>> child_registry['collective.behavior.localregistry.tests.cms']
    u'Plone + collective.behavior.localregistry'

