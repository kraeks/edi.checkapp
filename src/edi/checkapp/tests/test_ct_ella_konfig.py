# -*- coding: utf-8 -*-
from edi.checkapp.content.ella_konfig import IEllaKonfig  # NOQA E501
from edi.checkapp.testing import EDI_CHECKAPP_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class EllaKonfigIntegrationTest(unittest.TestCase):

    layer = EDI_CHECKAPP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_ella_konfig_schema(self):
        fti = queryUtility(IDexterityFTI, name='EllaKonfig')
        schema = fti.lookupSchema()
        self.assertEqual(IEllaKonfig, schema)

    def test_ct_ella_konfig_fti(self):
        fti = queryUtility(IDexterityFTI, name='EllaKonfig')
        self.assertTrue(fti)

    def test_ct_ella_konfig_factory(self):
        fti = queryUtility(IDexterityFTI, name='EllaKonfig')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IEllaKonfig.providedBy(obj),
            u'IEllaKonfig not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_ella_konfig_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='EllaKonfig',
            id='ella_konfig',
        )

        self.assertTrue(
            IEllaKonfig.providedBy(obj),
            u'IEllaKonfig not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('ella_konfig', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('ella_konfig', parent.objectIds())

    def test_ct_ella_konfig_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='EllaKonfig')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_ella_konfig_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='EllaKonfig')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'ella_konfig_id',
            title='EllaKonfig container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
