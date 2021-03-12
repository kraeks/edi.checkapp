# -*- coding: utf-8 -*-
from edi.checkapp.content.servicebutton import IServicebutton  # NOQA E501
from edi.checkapp.testing import EDI_CHECKAPP_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ServicebuttonIntegrationTest(unittest.TestCase):

    layer = EDI_CHECKAPP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Service',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_servicebutton_schema(self):
        fti = queryUtility(IDexterityFTI, name='Servicebutton')
        schema = fti.lookupSchema()
        self.assertEqual(IServicebutton, schema)

    def test_ct_servicebutton_fti(self):
        fti = queryUtility(IDexterityFTI, name='Servicebutton')
        self.assertTrue(fti)

    def test_ct_servicebutton_factory(self):
        fti = queryUtility(IDexterityFTI, name='Servicebutton')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IServicebutton.providedBy(obj),
            u'IServicebutton not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_servicebutton_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Servicebutton',
            id='servicebutton',
        )

        self.assertTrue(
            IServicebutton.providedBy(obj),
            u'IServicebutton not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('servicebutton', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('servicebutton', parent.objectIds())

    def test_ct_servicebutton_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Servicebutton')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
