# coding=UTF-8 
'''
Created on 2016年8月9日

爬虫 html输出器
'''


class HtmlOutputer():
    def __init__(self):
        self.datas = []
    
    def collect_data(self , data):
        if data is None :
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open("output.html" , "w" )
        
        fout.write("<html>")
        fout.write("<meta charset='utf-8'/>")
        fout.write("<body>")
        fout.write("<table border='1' cellpadding='0'>")
        
        for data in self.datas :
            fout.write("<tr>")
            #fout.write("<td>%s</td>" % data["url"])
            fout.write("<td>%s</td>" % data["title"].encode("utf-8"))
            fout.write("<td>%s</td>" % data["summary"].encode("utf-8"))
            fout.write("</tr>")
            
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()
    
    
    
    



