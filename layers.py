#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'












skins = [
'custom',
'c50theme_euroseeds_custom_images',
'c50theme_euroseeds_custom_templates',
'c50theme_euroseeds_styles', 
'tinymce',
'PloneFormGen',
'collective_gallery_theme',
'LanguageTool',
'cmfeditions_views',
'CMFEditions',
'ChangeSet',
'kupu_plone',
'kupu',
'kupu_tests',
'archetypes',
'archetypes_kss',
'mimetypes_icons',
'plone_kss',
'ATContentTypes',
'ATReferenceBrowserWidget',
'ResourceRegistries',
'PasswordReset',
'gruf',
'plone_ecmascript',
'plone_wysiwyg',
'plone_prefs',
'plone_portlets',
'plone_templates',
'plone_styles',
'plone_form_scripts',
'plone_scripts',
'plone_forms',
'plone_images',
'plone_content',
'plone_login',
'plone_deprecated',
'plone_3rdParty',
'cmf_legacy',

]
skins= [

  "custom",
  "mars_skin_custom_images",
  "mars_skin_custom_templates",
  "mars_skin_styles",
  "marsapp_categories_icons",
  "marsapp_content_icons",
  "marsapp_categories", 
  "collective_bibliocustomviews_custom",
  "ZipFileTransport",
  "bibliography",
  "eea_geotags",
  "kupu_tests",
  "kupu_plone",
  "kupu",
  "Maps",
  "plomino_tinymce",
  "cmfplomino_styles",
  "cmfplomino_images",
  "cmfplomino_templates",
  "tinymce",
  "bibliography_deprecated",
  "bibliography_selenium_tests",
  "bibliography_styles",
  "bibliography_list",
  "marsapp_custom",
  "marsapp_styles",
  "csvreplicata_images",
  "csvreplicata_templates",
  "sunburst_images",
  "sunburst_templates",
  "sunburst_styles",
  "referencebrowser",
  "LanguageTool",
  "cmfeditions_views",
  "CMFEditions",
  "at_extensions",
  "archetypes",
  "archetypes_kss",
  "mimetypes_icons",
  "plone_kss",
  "ATContentTypes",
  "PasswordReset",
  "plone_ecmascript",
  "plone_wysiwyg",
  "plone_prefs",
  "plone_templates",
  "plone_styles",
  "plone_form_scripts",
  "plone_scripts",
  "plone_forms",
  "plone_images",
  "plone_content",
  "plone_login",
  "plone_deprecated",
  "plone_3rdParty",
  "cmf_legacy",
]

pref = ''

layers = []
for idx, i in enumerate(skins):
    c=skins[idx]
    n=p=''
    try:
        n=skins[idx+1]
    except:
        p='*'
    try:
        if idx == 0:raise
        if p != '*':p= skins[idx-1]
    except:
        n='*'
    layer=''
    layer+= '    <layer name="%s"'%c
    if p:
        layer+= '\n     insert-after="%s"' % p
    if n:
        layer+= '\n     insert-before="%s"' % n
    layer+= '/>'
    layers.append(layer)

layers.reverse()

print "\n".join(layers)



# vim:set et sts=4 ts=4 tw=80:
