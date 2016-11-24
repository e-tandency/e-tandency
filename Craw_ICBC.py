# -*- coding:utf-8 -*-

from multiprocessing import Pool
from Pub_funcs import soup_page, data_render

ICBC_GOLD_URL = 'http://www.icbc.com.cn/ICBCDynamicSite/Charts/GoldTendencyPicture.aspx'
ICBC_CURRENCY_URL = ''

class ICBC_DATA(object):
    def __init__(self,GOLD_URL=ICBC_GOLD_URL,CURRENCY_URL=ICBC_CURRENCY_URL):
        self.GOLD_URL = GOLD_URL
        self.CURR_URL = CURRENCY_URL

    def ICBC_GOLD(self):
        """
        ICGC
        RMBG '人民币账户黄金'
        RMBS '人民币账户白银'
        USAG '美元账户黄金'
        USAS '美元账户白银'
        """
        try:
            soup_page(URL=ICBC_GOLD_URL)
            S_index = soup_page.text.split().index('人民币账户黄金')
            E_index = soup_page.text.split().index('代理实物贵金属递延行情')
            raw_data =  soup_page.text.split()[S_index:E_index]
            pool = Pool()
            RMBG = pool.apply_async(data_render, args=(raw_data, '人民币账户黄金', 5,))
            RMBS = pool.apply_async(data_render, args=(raw_data, '人民币账户白银', 5,))
            USAG = pool.apply_async(data_render, args=(raw_data, '美元账户黄金', 5,))
            USAS = pool.apply_async(data_render, args=(raw_data, '美元账户白银', 5,))
            pool.close()
            pool.join()
        except Exception as e:
            print("Get final data failed as %s" % e)

