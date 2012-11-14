from plone.app.registry.browser import controlpanel

from edition1.menu import Edition1MenuMessageFactory as _
from edition1.menu.interfaces import IMenuSettings


class MenuSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IMenuSettings
    label = _(u'Menu settings')
    description = _(u'help_menu_settings',
                    default=u'Configuration for the responsive menu.')

    def updateFields(self):
        super(MenuSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(MenuSettingsEditForm, self).updateWidgets()


class MenuSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = MenuSettingsEditForm
