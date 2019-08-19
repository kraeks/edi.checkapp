# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from edi.checkapp.testing import EDI_CHECKAPP_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


no_get_installer = False


try:
    from Products.CMFPlone.utils import get_installer
except Exception:
    no_get_installer = True


class TestSetup(unittest.TestCase):
    """Test that edi.checkapp is properly installed."""

    layer = EDI_CHECKAPP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal, self.layer['request'])

    def test_product_installed(self):
        """Test if edi.checkapp is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'edi.checkapp'))

    def test_browserlayer(self):
        """Test that IEdiCheckappLayer is registered."""
        from edi.checkapp.interfaces import (
            IEdiCheckappLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IEdiCheckappLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EDI_CHECKAPP_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal, self.layer['request'])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('edi.checkapp')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if edi.checkapp is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'edi.checkapp'))

    def test_browserlayer_removed(self):
        """Test that IEdiCheckappLayer is removed."""
        from edi.checkapp.interfaces import \
            IEdiCheckappLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IEdiCheckappLayer,
            utils.registered_layers())
