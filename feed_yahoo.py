import feedparser
feed = feedparser.parse('https://news.yahoo.co.jp')
print(feed)
#for entry in feed['entries']:
#    title = entry['title']
#    link = entry['link']
#    print(title, ',', link)

