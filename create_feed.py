from lxml import html
from feedgen.feed import FeedGenerator
import requests
import urllib
page = requests.get('http://www.odysseyscoop.com/episodes/Episodes_free.htm')
tree = html.fromstring(page.content)
i = 0

#Setup feed
fg=FeedGenerator()
fg.load_extension('podcast')
fg.title('Odyssey')
fg.subtitle('Feed of Episodes')
fg.link(href='https://dl.dropboxusercontent.com/s/3apx1963buo6kk0/rss.xml') 



for item in tree.xpath('//a/text()'):
    text = tree.xpath('//a/text()')[i-1]
    link = tree.xpath('//a/@href')[i]
    if ".mp3" in link:
        check = urllib.urlopen(link)
        print check.getcode()
        if check.getcode() != 404:
            text= text.replace('\n','')
            text = ' '.join(text.split())
            print text
            print link
            fe = fg.add_entry()
            fe.id(link)
            fe.title(text)
            fe.enclosure(link,0,'audio/mpeg')
    i=i+1

fg.rss_file('rss.xml')
