from plone.app.portlets import PloneMessageFactory as PMF
from zope import schema
from zope.interface import Interface

from edition1.menu import Edition1MenuMessageFactory as _


class IMenuSettings(Interface):
    """Global menu settings."""

    edition1_menu_min_width = schema.Int(
        title=_(u'label_min_width',
                default=u'Minimal width (in px) for the wide menu'),
        description=_(u'help_min_width',
                      default=u'If the width of the browser window size is '
                              u'below this value, the small version of the '
                              u'menu is shown. The default value (0) makes '
                              u'sure the wide menu is always shown.'),
        default=0,
        required=True,)

    edition1_menu_navigation_depth = schema.Int(
        title=PMF(u"label_navigation_tree_depth",
                default=u"Navigation tree depth"),
        description=PMF(u"help_navigation_tree_depth",
                      default=u"How many folders should be included "
                      "before the navigation tree stops. 0 "
                      "means no limit. 1 only includes the "
                      "root folder."),
        default=0,
        required=False)

    edition1_menu_max_items = schema.Int(
        title=_(u'label_max_items',
                default=u'Maximal number if items in wide menu'),
        description=_(u'help_max_items',
                      default=u'If there are more than this number of items '
                              u'in the menu, always show the small version. '
                              u'The default value (0) disables this feature.'),
        default=0,
        required=False)
