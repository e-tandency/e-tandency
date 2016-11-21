# -*- coding:utf-8 -*-

from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Browser_init(object):
    """
    Initial Browser
    """
    def __init__(self):
        self.Browser = webdriver.PhantomJS()

class Soup_Page(object):
    """
    SOUP PAGE
    """
    def __init__(self, URL):
        self.URL = URL
        self.Browser = Browser_init().Browser

    def soup_page(self):
        """
        Get URL and return Soup Page
        """
        self.Browser.get(self.URL)
        soup_page = BeautifulSoup(self.Browser.page_source, "lxml")
        return soup_page

    @staticmethod
    def data_render(raw_data=[], indexst='', length=5):
        """
        Render list data with startindex and endindex
        """
        if raw_data == [] or indexst == '':
            print('No start index or No raw_data given!')
        else:
            try:
                S_index = raw_data.index(indexst)
                E_index = S_index + length
                print("return data with start index %s" % indexst)
                data_rendered = raw_data[S_index:E_index]
                return data_rendered
            except Exception as e:
                print("Get data error due to %s" % e)