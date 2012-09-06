from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting

from zope.configuration import xmlconfig


class CollectiveBehaviorLocalregistry(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.behavior.localregistry
        xmlconfig.file('configure.zcml',
                       collective.behavior.localregistry,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        pass

COLLECTIVE_BEHAVIOR_LOCALREGISTRY_FIXTURE = CollectiveBehaviorLocalregistry()
COLLECTIVE_BEHAVIOR_LOCALREGISTRY_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_BEHAVIOR_LOCALREGISTRY_FIXTURE, ),
                       name="CollectiveBehaviorLocalregistry:Integration")
