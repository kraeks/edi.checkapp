# -*- coding: utf-8 -*-
from edi.checkapp.content.hinweistext import IHinweistext  # NOQA E501
from edi.checkapp.testing import EDI_CHECKAPP_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class HinweistextIntegrationTest(unittest.TestCase):

    layer = EDI_CHECKAPP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Fragebogen',
            self.portal,
            'hinweistext',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_hinweistext_schema(self):
        fti = queryUtility(IDexterityFTI, name='Hinweistext')
        schema = fti.lookupSchema()
        self.assertEqual(IHinweistext, schema)

    def test_ct_hinweistext_fti(self):
        fti = queryUtility(IDexterityFTI, name='Hinweistext')
        self.assertTrue(fti)

    def test_ct_hinweistext_factory(self):
        fti = queryUtility(IDexterityFTI, name='Hinweistext')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IHinweistext.providedBy(obj),
            u'IHinweistext not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_hinweistext_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Hinweistext',
            id='hinweistext',
        )

        self.assertTrue(
            IHinweistext.providedBy(obj),
            u'IHinweistext not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_hinweistext_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Hinweistext')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
