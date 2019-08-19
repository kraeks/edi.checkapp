# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import edi.checkapp


class EdiCheckappLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=edi.checkapp)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edi.checkapp:default')


EDI_CHECKAPP_FIXTURE = EdiCheckappLayer()


EDI_CHECKAPP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDI_CHECKAPP_FIXTURE,),
    name='EdiCheckappLayer:IntegrationTesting',
)


EDI_CHECKAPP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDI_CHECKAPP_FIXTURE,),
    name='EdiCheckappLayer:FunctionalTesting',
)


EDI_CHECKAPP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDI_CHECKAPP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EdiCheckappLayer:AcceptanceTesting',
)
