from Products.CMFCore.utils import getToolByName


def to0002(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(
        'profile-edition1.menu:default', 'cssregistry')
    setup.runImportStepFromProfile(
        'profile-edition1.menu:default', 'plone.app.registry')
