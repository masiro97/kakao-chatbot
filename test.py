import requests
from bs4 import BeautifulSoup
import random
import re

# url = "https://movie.naver.com/movie/running/current.nhn"
# res = requests.get(url).text
# doc = BeautifulSoup(res, "html.parser")

# pick = doc.select("#content > div.article > div > div.lst_wrap > ul > li > dl > dt > a")
# for movieNm in pick:
#     print(movieNm.text)

# movieNm_doc = doc.select('dt.tit > a')
# movieResv_doc = doc.select('div.star_t1 > a > span.num')
# movieStar_doc = doc.select('div.star_t1.b_star > span.num')

# movieNm_list = []
# movieResv_list = []
# movieStar_list = []

# for movieNm in movieNm_doc:
#     movieNm_list.append(movieNm.text)
#     # print(movieNm.text)
    
# for movieResv in movieResv_doc:
#     movieResv_list.append(movieResv.text)

# for movieStar in movieStar_doc:
#     movieStar_list.append(movieStar.text)
    
# print(movieStar_list)

# title_tag = doc.select('dt.tit > a')
# star_tag = doc.select('div.star_t1 > a > span.num')
# reserve_tag = doc.select('div.star_t1.b_star > span.num')
# img_tag = doc.select('div > a > img')

# print(len(title_tag))
# print(len(star_tag))
# print(len(reserve_tag))

# movie_dic = {}

# for i in range(0,10):
#     movie_dic[i+1] = {
#         "title" : title_tag[i].text,
#         "star" : star_tag[i].text,
#         "reserve" : reserve_tag[i].text,
#         "img_url" : img_tag[i]['src'] # img_tag[i].get('src')
#     }

# pick_movie = movie_dic[random.randrange(0,10)]

# print(pick_movie)

url = "https://twitter.com/MBC_entertain"
res = requests.get(url).text
doc = BeautifulSoup(res, "html.parser")

img_list = []

pick = doc.select('div.tweet.js-stream-tweet.js-actionable-tweet.js-profile-popup-actionable.dismissible-content.original-tweet.js-original-tweet.has-cards.has-content')

for pickNum in pick:
    img_tag = pickNum.select('img')
    for imgNum in img_tag:
        img_list.append(imgNum['src'])
        # print(imgNum['src'])
        
pick_img = img_list[random.randrange(0,len(img_list))]
print(pick_img)