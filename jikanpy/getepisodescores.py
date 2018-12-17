from jikanpy import Jikan

jikan = Jikan()

tokyo = jikan.search(search_type='anime', query='tokyo ghoul')
id = tokyo["results"][0]["mal_id"]
for itm in jikan.anime(id, extension="episodes")["episodes"]:
    print(itm["forum_url"] + "&pollresults=1")
