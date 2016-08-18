# coding=UTF-8 
'''
Created on 2016年8月9日

爬虫 url管理器
'''

class UrlManager():
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
    def add_new_url(self , url):
        if url is None : 
            return
        if url not in self.new_urls and url not in self.old_urls : # 既不在待爬取URL里 也不在爬取过的URL中
            self.new_urls.add(url)
    
    def has_new_url(self): # 判断有无待爬URL
        return len(self.new_urls) != 0

    
    def get_new_url(self): # 获取待爬URL
        new_url = self.new_urls.pop() # 从集合中获取一个URl并且移除
        self.old_urls.add(new_url)
        return new_url 

    
    def add_new_urls(self , urls):
        if urls is None or len(urls) == 0 :
            return
        for url in urls : # 循环进行单个添加
            self.add_new_url(url)
    
    
    
    
    
    
    
    



