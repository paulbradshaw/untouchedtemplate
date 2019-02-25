# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
import scraperwiki
import lxml.html

#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
html = scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")
#print(html)
#
# Find something on the page using css selectors
root = lxml.html.fromstring(html)
#Change "li p a" to a different CSS selector to grab something else
#Look for an a tag inside a p tag inside an li tag
#Store the matches in 'matchedlinks'
matchedlinks = root.cssselect("li p a")
#print that
#print(matchedlinks)
#create a dictionary to store what we find
record = {}
#We start from 3416 beacuse 3417 rows were saved before error
for li in matchedlinks[3415:]:
  #Store the text contents of li in a new variable listtext
  listtext = li.text_content()
  #print that
  #print(listtext.encode('utf-8'))
  record['address'] = listtext
  scraperwiki.sqlite.save(['address'],record)
