.. contents::

Introduction
============

This package provides a responsive replacement for the
``plone.global_sections`` viewlet. But note that just installing this
theme in itself does not replace anything. You will have to adjust
your theme to make use of this package.

Set up edition1.menu in your theme product
------------------------------------------

Add the package as dependency to you theme product. To do so add edition1.menu to the section install_requires in your setup.py::

     install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'edition1.menu',
      ],


Next, add edition1.menu to your metadata.xml::

    <dependencies>
       <dependency>profile-edition1.menu:default</dependency>
    </dependencies>

Run your buildout.

Next you need to add the viewlet to your browser configure.zcml::

    <!-- Responsive menu -->
    <browser:viewlet
      name="edition1.menu.responsive"
      manager="plone.app.layout.viewlets.interfaces.IPortalHeader"
      class="edition1.menu.viewlets.menu.MenuViewlet"
      layer=".interfaces.IThemeSpecific"
      permission="zope2.View"
    />

Everything is in place. Now you have to hide the global.navigation viewlet, because you use the edition1 responsive menu instead::

    <order manager="plone.portalheader" skinname="Your Theme" purge="True">
       <viewlet name="plone.global_sections" remove="true" />
    </order>

    <hidden manager="plone.portalheader" skinname="Your Theme">
       <viewlet name="plone.global_sections" />
    </hidden>


Start up your instance and go to plone control panel/Add-ons. Install edition1.menu. Go back to control panel and click on "Menu settings" in the section Add-on Configuration. You can configure the minimal width of the wide menu, navigation tree depth and maximal number of items in wide menu.




