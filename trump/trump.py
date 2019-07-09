from twitter_scraper import get_tweets
import pandas as pd 
import markovify, requests
from bs4 import BeautifulSoup as bs
from typing import Dict 
import operator

list_o_tweets, list_o_a, list_o_links = [], [], []
#f = open("trumps_tweets.csv", "w+")
base_html = "https://factba.se/transcripts"


for tweet in get_tweets('BarackObama', pages = 10):
    list_o_tweets.append(tweet['text'])

h_map = {str:0}

for t in list_o_tweets:
    l = t.split(" ") 
    for word in l:
        if word in h_map.keys():
            h_map[word] += 1
        else:
            h_map[word] = 1

sort_ed = sorted(h_map.items(), key=operator.itemgetter(1)) 
for tup in sort_ed:
    if (tup[1] < 49) and (tup[1] > 2):
        print (tup)


"""
req = requests.get(base_html, "html.parser")
soup = bs(req.content, features="lxml")

list_o_a = soup.find_all("a")

for link in list_o_a: 
    if link is not None:
        list_o_links.append(link.get("href"))
new_f = open("trump_transcripts.csv", "w+")
i = 0
for link in list_o_links:
    if link is not None and "transcript/d" in link:
        i += 1
        new_f.write("="*80)
        new_f.write("\n")
        new_f.write("\t\t\t\t\ttranscript #%i\n" % i)
        new_f.write("="*80)
        new_f.write("\n")
        new_f.write("\n")
        req = requests.get(link, "html.parser")
        soup = bs(req.content, features="lxml")
        list_o_a = soup.find_all("a")
        for l in list_o_a:
            if l is None:
                continue
            ret_val = l.get("name")
            if ret_val is not None and "seq" in ret_val:
                new_f.write("*")
                new_f.write(l.string)
                new_f.write("**\n\n")
        new_f.write("="*80)
        new_f.write("\n")
        new_f.write("\t\t\t\t\ttranscript #%i\n" % i)
        new_f.write("="*80)
        new_f.write("\n")

for link in list_o_links:
    if link is not None and "transcript/d" in link:
        req = requests.get(link, "html.parser")
        soup = bs(req.content, features="lxml")
        list_o_a = soup.find_all("a")
        for l in list_o_a:
            if l is None:
                continue
            ret_val = l.get("name")
            if ret_val is not None and "seq" in ret_val:
                s = l.string.split(" ")
                for word in s:
                    if word in h_map.keys():
                        h_map[word] += 1
                    else:
                        h_map[word] = 1

"""
