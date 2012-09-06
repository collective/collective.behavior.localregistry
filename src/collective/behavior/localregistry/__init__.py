import zope.i18nmessageid

MessageFactory = \
    zope.i18nmessageid.MessageFactory(u"collective.behavior.localregistry")


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
