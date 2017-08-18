# coding:utf-8

import url_manager
import re
import time
import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup

# For debug
# from ipdb import set_trace 


from urllib.parse import urljoin
from urllib.parse import quote

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        #driver = webdriver.Chrome('D:\Program Files (x86)\python')
        driver.ger(url)
        response = driver.page_source
        # if response.getcode() != 200:
        #    return None
        return response()


class HtmlParser(object):
    def _get_new_urls(self, page_url):

        userdata = []
        urldata = []
        driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        driver.get(page_url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        filename = soup.find('h2', class_='yahei')
        filename = filename.get_text()
        iframe = soup.find('iframe')
        driver.get(iframe.attrs['src'])
        # driver.find_element_by_xpath("//a[contains(.,'他在百科')]").click()
        time.sleep(3)

        page = 0
        name_count = 0
        # set_trace()
        while (page != 999999):
            soup = BeautifulSoup(driver.page_source, "html.parser")
            current_names = soup.select('div.list_row')
            for current_name in current_names:

                users = current_name.select('td > a')

                for user in users:
                    if (user.text != '查看'):
                        userdata.append(user.text)
                        urldata.append(user.get('href'))
                        name_count = name_count + 1    
                    
            page = page + 1
            if soup.find(class_='pTag next disabled') is None:
			    # driver.find_element_by_xpath("//a[contains(@class,'pTag next disabled')]"):
                driver.find_element_by_xpath("//a[contains(@class,'pTag next')]").click()
            else:
                page = 999999
            
            time.sleep(1)
            
        driver.quit()
        # set_trace()
        # print(filename)
        fout = open(filename+'.html','w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        i = 0
        name_count = name_count-1
        # ii = (name_count - 1) / 3
        # set_trace()
        while i<=name_count:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % userdata[i])
            fout.write('<td>%s</td>' % urldata[i])
            fout.write('</tr>')
            i = i+1
            
        print('output entries number: %d'% i)
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()

    def parse(self, page_url):
        # print('parse_data')
        # print('----')
        # print(html_cont)
        
        if page_url is None:
            return
        # set_trace()
        self._get_new_urls(page_url)
        # print(soup.prettify())
        print('success')



class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        a = 1
        while a == 1:
            try:
                a = 0
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                # print(html_cont)
                obj_s = HtmlParser()
                obj_s.parse(new_url) 
                # print(new_url)        
                # print('mark')  
                if a == 0:
                    break
                count = count + 1
            except:
                print('craw failed')


if __name__=='__main__':
    # the webpage that will be crawed
    root_url = 'https://www.baidu.com/p/%E5%A8%B2%E6%9C%88?from=wk'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
