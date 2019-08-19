# -*- coding: utf-8 -*-
from edi.checkapp.content.frage import IFrage  # NOQA E501
from edi.checkapp.testing import EDI_CHECKAPP_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class FrageIntegrationTest(unittest.TestCase):

    layer = EDI_CHECKAPP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Fragebogen',
            self.portal,
            'frage',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_frage_schema(self):
        fti = queryUtility(IDexterityFTI, name='Frage')
        schema = fti.lookupSchema()
        self.assertEqual(IFrage, schema)

    def test_ct_frage_fti(self):
        fti = queryUtility(IDexterityFTI, name='Frage')
        self.assertTrue(fti)

    def test_ct_frage_factory(self):
        fti = queryUtility(IDexterityFTI, name='Frage')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IFrage.providedBy(obj),
            u'IFrage not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_frage_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Frage',
            id='frage',
        )

        self.assertTrue(
            IFrage.providedBy(obj),
            u'IFrage not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_frage_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Frage')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
