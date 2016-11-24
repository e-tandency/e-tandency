# -*- coding:utf-8 -*-
"""
BOC currency rate
BOC gold paper Real-time
"""

from Pub_classes import Browser_init
from selenium.webdriver.support.ui import Select
from Pub_funcs import soup_page

BOC_GOLD_URL = ''
BOC_CURRENCY_URL = 'http://www.boc.cn/sourcedb/whpj/'

class BOC_DATA(object):
    def __init__(self, GOLD_URL=BOC_GOLD_URL, CURRENCY_URL=BOC_CURRENCY_URL):
        self.GOLD_URL = GOLD_URL
        self.CURR_URL = CURRENCY_URL

    def BOC_CURR(self,currency=''):
        """
        default: USD/JPY/POD
        """
        if currency != '':
            try:
                Browser = Browser_init().Browser
                Browser.get(self.CURR_URL)
                select = Select(Browser.find_element_by_id('pjname'))
                select.select_by_visible_text(currency)
                bt_find = Browser.find_element_by_css_selector("input[onclick*='search_for_whpj()']")
                bt_find.click()
                sp = soup_page(Browser)
                
            except Exception as e:
                print("Failed to get %s currency due to %s" % (currency, e))
        else:
            try:
                Browser = Browser_init().Browser
            except Exception as e:







