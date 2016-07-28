from lxml import html
import requests
import urllib
page = requests.get('http://feeds.feedburner.com/CordkillersOnlyVideo?format=xml')
tree = html.fromstring(page.content)
i = 0
print 

for item in tree.xpath('//item'):
    print item.xpath('./title')[0].text       
    print item.xpath('./pubdate')[0].text
    print item.xpath('./enclosure/@url')[0]
    print item.xpath('./description')[0].text

        
