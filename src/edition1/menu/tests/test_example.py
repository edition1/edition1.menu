import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from edition1.menu.testing import\
    EDITION1_MENU_INTEGRATION


class TestExample(unittest.TestCase):

    layer = EDITION1_MENU_INTEGRATION
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
    
    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        pid = 'edition1.menu'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')
