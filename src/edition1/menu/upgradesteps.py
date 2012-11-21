import logging

from Products.CMFCore.utils import getToolByName

log = logging.getLogger('edition1.menu.upgrades')


def to0002(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(
        'profile-edition1.menu:default', 'cssregistry')
    log.info('Upgraded edition1.menu to version 0002.')
