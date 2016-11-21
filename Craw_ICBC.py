# -*- coding:utf-8 -*-

from Pub_classes import Soup_Page
from multiprocessing import Pool

ICBC_URL = 'http://www.icbc.com.cn/ICBCDynamicSite/Charts/GoldTendencyPicture.aspx'

def ICBC_GOLD(URL):
    """
    ICGC
    RMBG '人民币账户黄金'
    RMBS '人民币账户白银'
    USAG '美元账户黄金'
    USAS '美元账户白银'
    """
    try:
        SP = Soup_Page(URL)
        soup_page = SP.soup_page()
        S_index = soup_page.text.split().index('人民币账户黄金')
        E_index = soup_page.text.split().index('代理实物贵金属递延行情')
        raw_data =  soup_page.text.split()[S_index:E_index]
        pool = Pool()
        RMBG = pool.apply_async(SP.data_render, args=(raw_data, '人民币账户黄金', 5,))
        RMBS = pool.apply_async(SP.data_render, args=(raw_data, '人民币账户白银', 5,))
        USAG = pool.apply_async(SP.data_render, args=(raw_data, '美元账户黄金', 5,))
        USAS = pool.apply_async(SP.data_render, args=(raw_data, '美元账户白银', 5,))
        pool.close()
        pool.join()
    except Exception as e:
        print("Get final data failed as %s" % e)

