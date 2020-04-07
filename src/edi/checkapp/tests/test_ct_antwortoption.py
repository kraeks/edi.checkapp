# -*- coding: utf-8 -*-
from edi.checkapp.content.antwortoption import IAntwortoption  # NOQA E501
from edi.checkapp.testing import EDI_CHECKAPP_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class AntwortoptionIntegrationTest(unittest.TestCase):

    layer = EDI_CHECKAPP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Fragestellung',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_antwortoption_schema(self):
        fti = queryUtility(IDexterityFTI, name='Antwortoption')
        schema = fti.lookupSchema()
        self.assertEqual(IAntwortoption, schema)

    def test_ct_antwortoption_fti(self):
        fti = queryUtility(IDexterityFTI, name='Antwortoption')
        self.assertTrue(fti)

    def test_ct_antwortoption_factory(self):
        fti = queryUtility(IDexterityFTI, name='Antwortoption')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IAntwortoption.providedBy(obj),
            u'IAntwortoption not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_antwortoption_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Antwortoption',
            id='antwortoption',
        )

        self.assertTrue(
            IAntwortoption.providedBy(obj),
            u'IAntwortoption not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('antwortoption', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('antwortoption', parent.objectIds())

    def test_ct_antwortoption_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Antwortoption')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
