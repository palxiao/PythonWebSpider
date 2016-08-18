# coding=UTF-8 
'''
Created on 2016年8月9日

爬虫 Html解析器
'''
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser():
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set() # 用来存放URL集
        # <a href = "/view/125370.htm">  /question/21154579
        links = soup.find_all('a' ,class_="question_link" , href = re.compile(r"/question/\d"))
        for link in links :
            new_url = link["href"]
            new_full_url = urlparse.urljoin(page_url , new_url)
            new_urls.add(new_full_url)
        
        return new_urls
    
    
    def _get_new_data(self, page_url, soup):
        res_data = {} # 数据存放字典
        # url 链接
        try :
            res_data["url"] = page_url
            # <dd class="lemmaWgt-lemmaTitle-title" h1 标题 /h1
            title_node = soup.find('span' , class_="zm-editable-content")
            # title_node的赋值，在最后find前有个括号).find('h1')
            res_data["title"] = title_node.get_text()
            # <div class="lemma-summary"
            summary_node = soup.find("div" , class_="zm-editable-content clearfix")
            res_data["summary"] = summary_node.prettify()  
        except Exception as e:
            print e
        finally:
            return res_data
    
    
    def parse(self , page_url , html_cont):
        if page_url is None or html_cont is None :
            return
        
        soup = BeautifulSoup(html_cont , "html.parser" , from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url , soup)
        new_data = self._get_new_data(page_url , soup)
        return new_urls , new_data
        
    
    



