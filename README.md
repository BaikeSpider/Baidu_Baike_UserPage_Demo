# Baidu_Baike_UserPage_Demo
Crawl the entry list in the user page

## How to run

python spider_main.py

## How to change the test link

Modify the root_url in the spider_main.py

if __name__=='__main__':
    root_url = 'https://www.baidu.com/p/%E5%A8%B2%E6%9C%88?from=wk'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
