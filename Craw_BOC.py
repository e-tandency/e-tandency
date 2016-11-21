# -*- coding:utf-8 -*-
"""
BOC currency rate
BOC gold paper Real-time
"""

Browser = webdriver.PhantomJS()
Browser.get('http://www.boc.cn/sourcedb/whpj/')
el = Browser.find_element_by_id('pjname')
select = Select(Browser.find_element_by_id('pjname'))
select.select_by_visible_text('美元')
bt_find = Browser.find_element_by_css_selector("input[onclick*='search_for_whpj()']")
bt_find.click()
