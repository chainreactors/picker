---
title: Geolocating street art via GEOSINT &#38; SOCMINT
url: https://www.osinord.com/post/geolocating-street-art-via-geosint-socmint
source: Over Security - Cybersecurity news aggregator
date: 2024-11-30
fetch_date: 2025-10-06T19:17:45.022809
---

# Geolocating street art via GEOSINT &#38; SOCMINT

top of page

[![OSINord - The Nordic OSINT Community](https://static.wixstatic.com/media/aee2e4_c78ac2ad35194f4f98b4829b816916ba~mv2.png/v1/fill/w_231,h_86,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/aee2e4_c78ac2ad35194f4f98b4829b816916ba~mv2.png)](https://www.osinord.com)

[Become Member](https://www.osinord.com/join-osinord)

* [Who We Are](https://www.osinord.com/who-we-are)
* [Founders](https://www.osinord.com/founders)
* [Events](https://www.osinord.com/events)
* [Webinars](https://www.osinord.com/webinars)
* [Blogs](https://www.osinord.com/blogs)
* [OSINT Volunteering](https://www.osinord.com/volunteering)
* [Contact](https://www.osinord.com/contact)
* More

Use tab to navigate through the menu items.

* [All Posts](https://www.osinord.com/blogs)

Search

# Geolocating street art via GEOSINT & SOCMINT

* ![Writer: Ron Kaminsky]()

  Ron Kaminsky
* Oct 25, 2024
* 5 min read

Hey, investigators!

**I am so glad to be back** and share new content with [you.In](http://you.In) today’s blog, I will write about another spontaneous OSINT/GEOINT challenge I performed, during which I had to find an image's exact geolocation.

This challenge was posted by [**UnShelledSec**](https://x.com/UnShelledSec), an all-source intelligence analyst and the co-founder of [HACKTORIA](https://hacktoria.com/) , on his X profile. As you already know, I couldn’t resist taking on the OSINT challenge; it’s just not my nature to let things go without digging deeper.

**To begin**, I carefully analyzed the posted image to gather my first impressions of the background, objects, and overall atmosphere. My objective was to identify any clues that might help pinpoint the exact geolocation of the challenge image.

In the red marking, we can see street art, which will be our main focus. Additionally, there is a large main road (highway) highlighted in pink. In green, high mountains are visible on the horizon, with palm trees lining the road, suggesting a tropical location. We also observe white-on-black and black-on-yellow license plates, which may provide clues about the geographic location. Furthermore, there is a road sign that reads ‘KEEP CLEAR’ in English, indicating that this is an official English-speaking country. **Additionally**, we can clearly see the road’s line pattern, which consists of white sidelines and a yellow center line.

![ree](https://static.wixstatic.com/media/aee2e4_fed8ac1178f24eda86c25b72e12644f0~mv2.png/v1/fill/w_49,h_31,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_fed8ac1178f24eda86c25b72e12644f0~mv2.png)

I used a great tool that I usually use in my investigations called — [**GeoHint**](https://geohints.com/).

You can find different hints about geolocation patterns of pretty much everything, **super** **recommended**!

Accordingly, the yellow center line is common in some European countries, but it is especially prevalent in North America and **nearby islands**.

![ree](https://static.wixstatic.com/media/aee2e4_a92c9cc9f4f84d719602e0821fe04c96~mv2.png/v1/fill/w_49,h_24,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_a92c9cc9f4f84d719602e0821fe04c96~mv2.png)

**My initial step** was to use Google Lens, which I find excellent for situations like this when you want to identify street art, for example.

**However**, there’s a catch with image searches on Google; sometimes they return a number of unrelated or similar-looking places. For instance, in my case, it showed potential tropical matches in locations like Puerto Rico and Mauritius. **To refine your search results**, I suggest experimenting with different objects in the image to get the most relevant results possible — so, I focused on the wall graffiti to find the same pattern and drawing.

I found two matches of the same wall with windows above.

![ree](https://static.wixstatic.com/media/aee2e4_e969a9b788c24a9ea730307d075df6f0~mv2.png/v1/fill/w_49,h_28,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_e969a9b788c24a9ea730307d075df6f0~mv2.png)

Unfortunately, the first LinkedIn result showed the exact graffiti, but the link led to a completely different post.

![ree](https://static.wixstatic.com/media/aee2e4_c73a882feef64072a22c60500627c879~mv2.png/v1/fill/w_49,h_38,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_c73a882feef64072a22c60500627c879~mv2.png)

So I decided to use some Google dorking to find the post where the graffiti appears. I tried so search for results that are painted on the wall and I found the same wall and zoomed in to try to identify the author of the painting. It appears to be connected to the other two paintings, as all of them are created by ‘Protected Natural Assets’ and share a similar pattern, in my opinion.

Another interesting detail I noticed is that the author seems to emphasise certain objects in the graffiti, which might provide clues about the location. We can clearly see mountains, a river, and many rooted trees, contributing to a tropical vibe.

![ree](https://static.wixstatic.com/media/aee2e4_00671a8d657540358ac0b29961f72109~mv2.png/v1/fill/w_49,h_20,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_00671a8d657540358ac0b29961f72109~mv2.png)

While searching on Google with various word combinations such as

“river” AND “roots” AND “tropical” in one query, I came across a Pinterest post with clues about the location. It appears to be Dominica, and the hashtags include **‘Indian River’ and ‘Portsmouth’.**

Well, thats a big progression!

![ree](https://static.wixstatic.com/media/aee2e4_df448186257f47bda8bca2397c4af1f4~mv2.png/v1/fill/w_49,h_27,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_df448186257f47bda8bca2397c4af1f4~mv2.png)

Remember the Google image search? It mentioned ‘Dominica’ as well, so I will refocus my investigation on that specific location.

![ree](https://static.wixstatic.com/media/aee2e4_dfe180ceb77e4d44a9a75403c11a4268~mv2.png/v1/fill/w_89,h_55,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_dfe180ceb77e4d44a9a75403c11a4268~mv2.png)

I threw my thoughts to ChatGPT and asked to help me with matching this location with the license plates from the original picture, and it really indicates with a high severity that this is the pattern we saw in the pictures.

![ree](https://static.wixstatic.com/media/aee2e4_c68d28fe4e4d4ad6810dd15e9ed2dd3d~mv2.png/v1/fill/w_49,h_6,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_c68d28fe4e4d4ad6810dd15e9ed2dd3d~mv2.png)

And also used this great website/tool http://www.worldlicenseplates.com/.

World License Plates is a comprehensive online database showcasing vehicle registration plates from around the world. It provides images and details about:

• Plate Designs: Examples of license plates from various countries and regions.

• Formats and Regulations: Information on plate sizes, colors, and formats.

• Historical Changes: Details on how plate designs and rules have evolved.

• Regional Variations: Insights into differences in plate designs within a country.

It indeed matches the license plates I observed in the challenge picture.

![ree](https://static.wixstatic.com/media/aee2e4_329dec53151847f4b68a799d2f1c14cd~mv2.png/v1/fill/w_49,h_25,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_329dec53151847f4b68a799d2f1c14cd~mv2.png)

![ree](https://static.wixstatic.com/media/aee2e4_514345ccba9e4a1b9ec904e4171d9089~mv2.png/v1/fill/w_49,h_25,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_514345ccba9e4a1b9ec904e4171d9089~mv2.png)

Here’s another useful [map](https://www.reddit.com/r/geoguessr/comments/y3xfwi/i_didnt_find_any_licence_plate_world_map_so_i/#lightbox) I found on the GeoGuessr community on Reddit, which shows the matching black-and-white plate patterns in the island area.

![ree](https://static.wixstatic.com/media/aee2e4_b2cb75b998094bb8ba51add7b5f2ecba~mv2.png/v1/fill/w_49,h_28,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto...