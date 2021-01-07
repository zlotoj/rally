
url='https://rally1.rallydev.com/#/42853899240d/reports'

# import urllib.request
# page = urllib.request.urlopen(url)
# print(page.read())

import requests
from urllib.request import urlopen
from lxml import etree

# get html from site and write to local file
# url = 'https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life'
response = urlopen(url)
print(response.read())
response = urlopen(url)
print(response.read())
response = urlopen(url)
print(response.read())
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)

text = tree.xpath('//*/tbody/tr[2]/td[3]/div')
print(text)
text = tree.xpath('//p/strong/text()')
print(text)

# # how do you get stuff (really basic)
#text = tree.xpath('//p/strong/text()')
# tree.xpath('//p[contains(text(),"Use")]/text()')
# # get stuff that doesn't have other stuff
# tree.xpath('//p/strong[not(contains(text(),"\xa0"))]/text()')
# # get starts-with
# tree.xpath('//img[starts-with(@class, "alignnone")]/@src')
# # get all the stuff under something (descendant)
# tree.xpath('//header[@class="article header"]/descendant::node()/text()')
# # get stuff based on its index
# tree.xpath('//li[@class="related-post"]/a/@href')
# # get stuff based on its index
# tree.xpath('//li[@class="related-post"]/a[1]/@href')

# print(text)
