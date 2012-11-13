from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from Products.CMFPlone.browser.navigation import CatalogNavigationTabs
from Products.CMFPlone.browser.navigation import get_id
from Products.CMFPlone.browser.navigation import get_view_url
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from zope.component import getMultiAdapter


MAX_CHILD_LEVEL = 2  # Will be dynamic in The Near Future(TM).


class MenuItems(CatalogNavigationTabs):
    """A custom version of the Navigation tabs.

    This version feeds the menu viewlet.
    """

    def _get_link_url(self, child, member):
        if child.Type == 'Link':
            # Handle SwordLinks differently.
            return (get_id(child), child.getObject().getTargetUrl())
        linkremote = child.getRemoteUrl and not member == child.Creator
        if linkremote:
            return (get_id(child), child.getRemoteUrl)
        else:
            return False

    def _get_children_query(self, item):
        navtree_properties = self.navtree_properties

        customQuery = getattr(self.context, 'getCustomNavQuery', False)
        if customQuery is not None and utils.safe_callable(customQuery):
            query = customQuery()
        else:
            query = {}

        path = '/'.join(item.getPhysicalPath())
        query['path'] = {'query': path, 'depth': 1}

        blacklist = navtree_properties.getProperty('metaTypesNotToList', ())
        all_types = self.portal_catalog.uniqueValuesFor('portal_type')
        query['portal_type'] = [t for t in all_types if t not in blacklist]

        sortAttribute = navtree_properties.getProperty('sortAttribute', None)
        if sortAttribute is not None:
            query['sort_on'] = sortAttribute
            sortOrder = navtree_properties.getProperty('sortOrder', None)
            if sortOrder is not None:
                query['sort_order'] = sortOrder

        if navtree_properties.getProperty('enable_wf_state_filtering', False):
            query['review_state'] = navtree_properties.getProperty(
                                                    'wf_states_to_show', [])

        query['is_default_page'] = False

        if self.site_properties.getProperty('disable_nonfolderish_sections',
                                            False):
            query['is_folderish'] = True

        return query

    def get_children(self, item, member, level):
        """Return the children as a list of dictionaries."""
        if MAX_CHILD_LEVEL and level > MAX_CHILD_LEVEL:
            # We're already requesting more children than allowed.
            return []
        query = self._get_children_query(item)
        # Get the children
        rawresult = self.portal_catalog.searchResults(query)
        result = []
        idsNotToList = self.navtree_properties.getProperty('idsNotToList', ())
        for child in rawresult:
            if not (child.getId in idsNotToList or child.exclude_from_nav):
                id, child_url = (self._get_link_url(child, member) or
                                 get_view_url(child))
                children = []
                if (not MAX_CHILD_LEVEL or level < MAX_CHILD_LEVEL):
                    obj = child.getObject()
                    children = self.get_children(obj, member, level + 1)
                data = {'title': utils.pretty_title_or_id(self.context, child),
                        'id': child.getId,
                        'url': child_url,
                        'description': child.Description,
                        'children': children}
                result.append(data)
        return result

    def get_menu_items(self, actions=None, category='portal_tabs'):
        context = aq_inner(self.context)

        mtool = getToolByName(context, 'portal_membership')
        member = mtool.getAuthenticatedMember().id

        portal_properties = getToolByName(context, 'portal_properties')
        self.navtree_properties = getattr(portal_properties,
                                          'navtree_properties')
        self.site_properties = getattr(portal_properties,
                                       'site_properties')
        self.portal_catalog = getToolByName(context, 'portal_catalog')

        if actions is None:
            context_state = getMultiAdapter((context, self.request),
                                            name=u'plone_context_state')
            actions = context_state.actions(category)

        # Build result dict
        result = []
        # first the actions
        if actions is not None:
            for actionInfo in actions:
                data = actionInfo.copy()
                result.append(data)

        # check whether we only want actions
        if self.site_properties.getProperty('disable_folder_sections', False):
            return result

        query = self._getNavQuery()

        rawresult = self.portal_catalog.searchResults(query)

        # now add the content to results
        idsNotToList = self.navtree_properties.getProperty('idsNotToList', ())
        for item in rawresult:
            if not (item.getId in idsNotToList or item.exclude_from_nav):
                obj = item.getObject()
                children = self.get_children(obj, member, 2)
                id, item_url = (self._get_link_url(item, member) or
                                get_view_url(item))

                data = {'title': utils.pretty_title_or_id(context, item),
                        'id': item.getId,
                        'url': item_url,
                        'description': item.Description,
                        'children': children,
                        }
                result.append(data)
        return result


class MenuViewlet(GlobalSectionsViewlet):
    """The responsive menu viewlet."""

    index = ViewPageTemplateFile('menu.pt')

    def update(self):
        context = aq_inner(self.context)
        menu_items_view = getMultiAdapter((context, self.request),
                                           name='menu_items')
        self.menu_items = menu_items_view.get_menu_items()
        self.available = (len(self.menu_items)) > 0
        self.selected_tabs = self.selectedTabs(portal_tabs=self.menu_items)
        self.selected_portal_tab = self.selected_tabs['portal']

    recurse = ViewPageTemplateFile('menu_recurse.pt')
