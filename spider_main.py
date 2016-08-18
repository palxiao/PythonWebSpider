# coding=UTF-8 
'''
Created on 2016年8月9日

爬虫 调度器
'''
# main函数 
from my_spider import url_manager, html_downloader, html_parser, html_outputer

 
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()        
    
    def craw(self , root_url):
        count = 1 # 用于记录爬取数
        self.urls.add_new_url(root_url) # 将入口URL扔进URL管理器
        
        while self.urls.has_new_url(): # 有待爬取URL 启动循环
            try :
                new_url = self.urls.get_new_url() # 取得一个URL
                print u'爬取第 %d 条 : %s' %(count,new_url)
    
                html_cont = self.downloader.download(new_url) # 下载页面
                new_urls , new_data = self.parser.parse(new_url , html_cont) # 解析得到新的URL 和新的数据
                self.urls.add_new_urls(new_urls) # 补充新的待爬URL集扔给URL管理器
                self.outputer.collect_data(new_data) # 收集数据
                
                if count == 5 : # 爬取数
                    break
                
                count = count + 1
                # 循环结束
            except Exception as e:
                print e
            
        self.outputer.output_html() # 输出


if __name__ == "__main__":
    # 爬虫入口
    root_url = "https://www.zhihu.com/question/41978715"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url) # 启动爬虫