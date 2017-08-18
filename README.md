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

## Note
`百科投诉专员01.html` and `xuonx.html` are the test data from [百科投诉专员01](https://www.baidu.com/p/%E7%99%BE%E7%A7%91%E6%8A%95%E8%AF%89%E4%B8%93%E5%91%9801?from=wk) and [xuonx](https://www.baidu.com/p/xuonx?from=wk)

~百科投诉专员.png· is the demo of textual analysis
