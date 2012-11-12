from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import edition1.menu


EDITION1_MENU = PloneWithPackageLayer(
    zcml_package=edition1.menu,
    zcml_filename='testing.zcml',
    gs_profile_id='edition1.menu:testing',
    name="EDITION1_MENU")

EDITION1_MENU_INTEGRATION = IntegrationTesting(
    bases=(EDITION1_MENU, ),
    name="EDITION1_MENU_INTEGRATION")

EDITION1_MENU_FUNCTIONAL = FunctionalTesting(
    bases=(EDITION1_MENU, ),
    name="EDITION1_MENU_FUNCTIONAL")
