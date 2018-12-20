from jikanpy import Jikan
from bs4 import BeautifulSoup
import requests

jikan = Jikan()


tokyo = jikan.search(search_type='anime', query='tokyo ghoul')
id = tokyo["results"][0]["mal_id"]
#for itm in jikan.anime(id, extension="episodes")["episodes"]:
itm = jikan.anime(id, extension="episodes")["episodes"][0]
print(itm["forum_url"] + "&pollresults=1")
url = itm["forum_url"] + "&pollresults=1"
xpath = '//*[@id="contentWrapper"]/div[4]/table/tbody/tr[1]/td[3]'
response = requests.get(url)

soup = BeautifulSoup(response.text)

results = soup.find_all('td')
five_rating = int(results[2].text)
four_rating = int(results[6].text)
three_rating = int(results[10].text)
two_rating = int(results[14].text)
one_rating = int(results[18].text)
total_votes = five_rating + four_rating + three_rating + two_rating + one_rating
avg_ep_rating = float(5 * five_rating + 4 * four_rating + 3 * three_rating + 2 * two_rating + 1 * one_rating)/total_votes
print(avg_ep_rating)
