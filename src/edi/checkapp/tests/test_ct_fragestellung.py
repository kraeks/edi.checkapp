# -*- coding: utf-8 -*-
from edi.checkapp.content.fragestellung import IFragestellung  # NOQA E501
from edi.checkapp.testing import EDI_CHECKAPP_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class FragestellungIntegrationTest(unittest.TestCase):

    layer = EDI_CHECKAPP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Fragebogen',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_fragestellung_schema(self):
        fti = queryUtility(IDexterityFTI, name='Fragestellung')
        schema = fti.lookupSchema()
        self.assertEqual(IFragestellung, schema)

    def test_ct_fragestellung_fti(self):
        fti = queryUtility(IDexterityFTI, name='Fragestellung')
        self.assertTrue(fti)

    def test_ct_fragestellung_factory(self):
        fti = queryUtility(IDexterityFTI, name='Fragestellung')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IFragestellung.providedBy(obj),
            u'IFragestellung not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_fragestellung_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Fragestellung',
            id='fragestellung',
        )

        self.assertTrue(
            IFragestellung.providedBy(obj),
            u'IFragestellung not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('fragestellung', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('fragestellung', parent.objectIds())

    def test_ct_fragestellung_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Fragestellung')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_fragestellung_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Fragestellung')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'fragestellung_id',
            title='Fragestellung container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
