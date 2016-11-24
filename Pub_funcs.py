# *.* coding: utf-8 *.*
import collections
import subprocess
from Pub_classes import Browser_init
from bs4 import BeautifulSoup

ExecutionResult = collections.namedtuple(
    'ExecutionResult',
    'status, stdout, stderr'
)

def execute(cmd, **kwargs):
    splitted_cmd = cmd.split()
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    try:
        process = subprocess.Popen(splitted_cmd, **kwargs)
        stdout, stderr = process.communicate()
        status = process.poll()
        return ExecutionResult(status, stdout, stderr)
    except OSError as e:
        print("Command exec error: '%s' %s" % (cmd, e))
        return ExecutionResult(1, '', '')


def Char_Rep(str,o_char,n_char):
    """
    Replace character
    """
    if o_char in str.replace(o_char, n_char):
        Char_Rep(str.replace(o_char, n_char),o_char,n_char)
    else:
        return str.replace(o_char, n_char)


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


def soup_page(Browser=Browser_init.Browser, URL=''):
    """
    Get URL and return Soup Page
    """
    try:
        if URL == '':
            soup_page = BeautifulSoup(Browser.page_source, "lxml")
        else:
            Browser.get(URL)
            soup_page = BeautifulSoup(Browser.page_source, "lxml")
    except Exception as e:
        print("Failed got soup_page due to %s" % e)
    else:
        return soup_page