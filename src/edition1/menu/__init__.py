from zope.i18nmessageid import MessageFactory

Edition1MenuMessageFactory = MessageFactory('edition1.menu')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
