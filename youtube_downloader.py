import urllib2
import os


a = raw_input("Enter the video to search : ")
a = a.replace(" ","+")
req = urllib2.Request("http://www.youtube.com/results?search_query="+a)
response = urllib2.urlopen(req)
the_page = response.read()
start = the_page.find("yt-lockup clearfix yt-uix-tile result-item-padding yt-lockup-video yt-lockup-tile vve-check context-data-item")
print start
#start = start+1
#start = the_page.find("yt-lockup clearfix yt-uix-tile result-item-padding yt-lockup-video yt-lockup-tile vve-check context-data-item",start)
#print start
#start = start+67
#print the_page[start:start+200]
#end = the_page.find("data-context",start)
#print end
#print the_page[start:end]
os.system("youtube-dl "+a)
