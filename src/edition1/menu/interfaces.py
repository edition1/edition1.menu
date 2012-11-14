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
