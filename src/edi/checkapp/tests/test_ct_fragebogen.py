# -*- coding: utf-8 -*-
from edi.checkapp.content.fragebogen import IFragebogen  # NOQA E501
from edi.checkapp.testing import EDI_CHECKAPP_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class FragebogenIntegrationTest(unittest.TestCase):

    layer = EDI_CHECKAPP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_fragebogen_schema(self):
        fti = queryUtility(IDexterityFTI, name='Fragebogen')
        schema = fti.lookupSchema()
        self.assertEqual(IFragebogen, schema)

    def test_ct_fragebogen_fti(self):
        fti = queryUtility(IDexterityFTI, name='Fragebogen')
        self.assertTrue(fti)

    def test_ct_fragebogen_factory(self):
        fti = queryUtility(IDexterityFTI, name='Fragebogen')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IFragebogen.providedBy(obj),
            u'IFragebogen not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_fragebogen_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Fragebogen',
            id='fragebogen',
        )

        self.assertTrue(
            IFragebogen.providedBy(obj),
            u'IFragebogen not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_fragebogen_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Fragebogen')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_fragebogen_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Fragebogen')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'fragebogen_id',
            title='Fragebogen container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
