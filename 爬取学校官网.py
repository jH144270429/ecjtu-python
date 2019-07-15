import  requests
from lxml import etree
link = "http://www.ecjtu.jx.cn/"
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    }
r = requests.get(link, headers=headers)
html = etree.HTML(r.content.decode('utf-8'))

#爬取官网单个首页当爬取定为list时，解析当前list index类型以及list中需要爬取的内容
# title = html.xpath('//*[@id="navMenu"]/div/ul/li[1]/a')
# for index in range(len(title)):
#     # links[index]返回的是一个字典
#         print(title[index].tag)
#         print(title[index].attrib)
#         print(title[index].text)

#爬取首页，交大新闻，关于交大。。。。
title = html.xpath('//*[@id="navMenu"]/div/ul/li/a/text()')#复制到ul定位ul下面的li下面的a标签，取到a标签下的text
print(title)


# #爬取官网另一个ul
# title = html.xpath('//*[@id="navMenu"]/ul/li/a/text()')
# print(title)
