#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pywikibot

site = pywikibot.Site('cs', 'wikipedia')
page = pywikibot.Page(site, u"Wikipedista:UrbanecmBot/DisambigLinks")
page.text = u""
page.save(u"vyprázdnění stránky")
