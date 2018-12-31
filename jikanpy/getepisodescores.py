from jikanpy import Jikan
from bs4 import BeautifulSoup
import requests
import matplotlib.pylab as plt
from time import sleep

jikan = Jikan()

anime = jikan.search(search_type='anime', query='death note')
title = anime["results"][0]["title"]
print(title)
mal_id = anime["results"][0]["mal_id"]

rating_list = []
ep_count = 0

for episode in jikan.anime(mal_id, extension="episodes")["episodes"]:
    print(episode)
    if episode["forum_url"] is not None:
        ep_count += 1

        url = episode["forum_url"] + "&pollresults=1"
        response = requests.get(url)
        sleep(3)
        print(response.content)
        soup = BeautifulSoup(response.content, "html.parser")
        results = soup.find_all('td')

        try:
            five_rating = int(results[2].text)
        except ValueError:
            five_rating = 0
        try:
            four_rating = int(results[6].text)
        except ValueError:
            four_rating = 0
        try:
            three_rating = int(results[10].text)
        except ValueError:
            three_rating = 0
        try:
            two_rating = int(results[14].text)
        except ValueError:
            two_rating = 0
        try:
            one_rating = int(results[18].text)
        except ValueError:
            one_rating = 0

        total_votes = five_rating + four_rating + three_rating + two_rating + one_rating
        if total_votes == 0:
            print("No votes found for episode " + str(ep_count))
            avg_ep_rating = None
        else:
            avg_ep_rating = float(5 * five_rating + 4 * four_rating + 3 * three_rating + 2 * two_rating + 1 * one_rating)\
                        / total_votes
        print(avg_ep_rating)

        rating_list.append(avg_ep_rating)

plt.title(title)
plt.xlabel("Episode")
plt.ylabel("Rating")
plt.plot(range(1, ep_count+1), rating_list)
plt.ylim([0, 5])
plt.show()



