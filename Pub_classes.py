# -*- coding:utf-8 -*-

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class Browser_init(object):
    """
    Initial Browser
    """
    def __init__(self):
        self.Browser = webdriver.PhantomJS()




















