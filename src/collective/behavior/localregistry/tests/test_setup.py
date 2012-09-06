import unittest2 as unittest
import doctest
import pprint
from plone.testing import (
    layered,
    z2,
)

from collective.behavior.localregistry.testing import\
    COLLECTIVE_BEHAVIOR_LOCALREGISTRY_INTEGRATION_TESTING


TESTFILES = [
    ('../proxy.rst', COLLECTIVE_BEHAVIOR_LOCALREGISTRY_INTEGRATION_TESTING),
]

optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
optionflags |= doctest.REPORT_ONLY_FIRST_FAILURE


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([layered(doctest.DocFileSuite(docfile,
                                                 globs={'pprint':
                                                        pprint.pprint,
                                                        'z2': z2,
                                                        },
                                                 optionflags=optionflags,
                                                 ),
                            layer=layer,
                            ) for docfile, layer in TESTFILES])
    return suite
