from jikanpy import Jikan
from bs4 import BeautifulSoup
import requests
import matplotlib.pylab as plt
from time import sleep

jikan = Jikan()

anime = jikan.search(search_type='anime', query='sao')
title = anime["results"][0]["title"]
print(title)
mal_id = anime["results"][0]["mal_id"]

rating_list = []
ep_count = 0

for episode in jikan.anime(mal_id, extension="episodes")["episodes"]:
    ep_count += 1

    url = episode["forum_url"] + "&pollresults=1"
    response = requests.get(url)
    sleep(3)
    print(response.content)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all('td')

    five_rating = int(results[2].text)
    four_rating = int(results[6].text)
    three_rating = int(results[10].text)
    two_rating = int(results[14].text)
    one_rating = int(results[18].text)

    total_votes = five_rating + four_rating + three_rating + two_rating + one_rating
    avg_ep_rating = float(5 * five_rating + 4 * four_rating + 3 * three_rating + 2 * two_rating + 1 * one_rating)/total_votes
    print(avg_ep_rating)

    rating_list.append(avg_ep_rating)

plt.title(title)
plt.xlabel("Episode")
plt.ylabel("Rating")
plt.plot(range(1, ep_count+1), rating_list)
plt.show()



