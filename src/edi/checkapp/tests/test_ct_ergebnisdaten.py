# -*- coding: utf-8 -*-
from edi.checkapp.content.ergebnisdaten import IErgebnisdaten  # NOQA E501
from edi.checkapp.testing import EDI_CHECKAPP_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ErgebnisdatenIntegrationTest(unittest.TestCase):

    layer = EDI_CHECKAPP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Benutzerordner',
            self.portal,
            'ergebnisdaten',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_ergebnisdaten_schema(self):
        fti = queryUtility(IDexterityFTI, name='Ergebnisdaten')
        schema = fti.lookupSchema()
        self.assertEqual(IErgebnisdaten, schema)

    def test_ct_ergebnisdaten_fti(self):
        fti = queryUtility(IDexterityFTI, name='Ergebnisdaten')
        self.assertTrue(fti)

    def test_ct_ergebnisdaten_factory(self):
        fti = queryUtility(IDexterityFTI, name='Ergebnisdaten')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IErgebnisdaten.providedBy(obj),
            u'IErgebnisdaten not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_ergebnisdaten_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Ergebnisdaten',
            id='ergebnisdaten',
        )

        self.assertTrue(
            IErgebnisdaten.providedBy(obj),
            u'IErgebnisdaten not provided by {0}!'.format(
                obj.id,
            ),
        )

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertIn('ergebnisdaten', self.parent.objectIds())

    def test_ct_ergebnisdaten_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Ergebnisdaten')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
