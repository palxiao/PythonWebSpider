# coding=UTF-8 
'''
Created on 2016年8月9日

爬虫 html下载器
'''
import urllib2


class HtmlDownloader():
    
    
    def download(self , url):
        if url is None :
            return None
        
        resp = urllib2.urlopen(url)
        
        if resp.getcode() != 200 :
            return None
        
        return resp.read()
    



