---
title: Geolocating a barrier wall via GEOSINT &#38; SOCMINT
url: https://www.osinord.com/post/geolocating-a-barrier-wall-via-geosint-socmint
source: Over Security - Cybersecurity news aggregator
date: 2024-11-30
fetch_date: 2025-10-06T19:17:52.124211
---

# Geolocating a barrier wall via GEOSINT &#38; SOCMINT

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

# Geolocating a barrier wall via GEOSINT & SOCMINT

* ![Writer: Ron Kaminsky]()

  Ron Kaminsky
* Oct 25, 2024
* 5 min read

Hey, my beloved investigators!

In today’s blog, I will write about another spontaneous OSINT/GEOINT challenge I performed during which I had to find the exact geolocation of an image.

This challenge was posted by [Baptiste Robert](https://twitter.com/fs0c131y) a legendary French Security Researcher & the CEO of [Predicta Lab](https://medium.com/u/a6c108c58824?source=post_page-----29a44177f61a--------------------------------) on his X profile. As always, I couldn’t resist taking on the challenge; it’s just not my nature to let things go without digging in, even tho it was **hella hard**.

**First and foremost**, I looked into the posted image to gather initial impressions regarding the background, objects, and overall atmosphere. The goal was to identify indicators that could provide clues leading to the precise geolocation of the challenge image.

In tackling this particular challenge, **it’s crucial to highlight** the complexity of searching for visual objects. Unlike many other places globally, the Gaza Strip lacks Google Street View and recent photos, making the investigative process notably challenging. Compounded by the fact that it’s a war zone, certain areas have undergone significant changes, rendering past satellite photos irrelevant. In navigating this challenge, the key was leveraging a variety of tools, cross-referencing information, and, most importantly, thinking creatively beyond conventional approaches.

![ree](https://static.wixstatic.com/media/aee2e4_a86cb30c6f6042debefff661848f38ab~mv2.png/v1/fill/w_49,h_24,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_a86cb30c6f6042debefff661848f38ab~mv2.png)

Given the limited number of indicators in this picture, my primary focus centered on the **white and red painted barrier wall** lining the road. Additionally, **a bench** resembling that of a bus stop/station is observable.This suggests that the location might be in a public area, such as a school, university, city center, or a similar public space.

My initial step involved navigating to the URL path of the original photo to utilize an online **EXIF tool**, aiming to gather **metadata**.

![ree](https://static.wixstatic.com/media/aee2e4_daedeffb679a4f1d9141a8e8f732993a~mv2.png/v1/fill/w_49,h_1,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_daedeffb679a4f1d9141a8e8f732993a~mv2.png)

I decided to use a great online EXIF data viewer tool named [**Jimpl**](https://jimpl.com/)**.**

While it’s occasionally possible to extract the exact geolocation from image metadata, this time it didn’t contain any location data. However, it did provide other valuable information, including the **DateTimeOriginal** of the image, **the city**, the **author’s name**, image **description**, and various camera settings such as the lens used and the camera model.

**This data could prove useful in the later stages of the investigation.**

![ree](https://static.wixstatic.com/media/aee2e4_75467aa6d9d84ffa8b2ca437268f75bb~mv2.png/v1/fill/w_49,h_27,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_75467aa6d9d84ffa8b2ca437268f75bb~mv2.png)

![ree](https://static.wixstatic.com/media/aee2e4_78a957ec02df495ba518672f70d6ab6d~mv2.png/v1/fill/w_49,h_21,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_78a957ec02df495ba518672f70d6ab6d~mv2.png)

![ree](https://static.wixstatic.com/media/aee2e4_1de5657f42ee41a1a0a8a9b91b922beb~mv2.png/v1/fill/w_71,h_25,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_1de5657f42ee41a1a0a8a9b91b922beb~mv2.png)

From this wealth of information, we can deduce that the picture was taken by Bashar Taleb, an AP News photographer, on 22/01/2024 at 12:38 PM in Khan Younis, Gaza Strip.

Following this, I opted to visit the AP Newsroom website to explore photos captured by the photographer Bashar Taleb. I discovered 9 additional images taken on the same day, potentially in the same area as the original picture, providing further insight.

![ree](https://static.wixstatic.com/media/aee2e4_d8c12eab761d44a99ba76c3af8798505~mv2.png/v1/fill/w_49,h_37,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_d8c12eab761d44a99ba76c3af8798505~mv2.png)

**Khan Younis** proves to be a considerably large area to investigate, especially considering the absence of street views, pictures, and up-to-date satellite imagery. Furthermore, it’s a densely populated and overcrowded location. The city spans a total area of **54.56 km2.**

![ree](https://static.wixstatic.com/media/aee2e4_ab3616b57ad5448092c3bfc6f9b08527~mv2.png/v1/fill/w_49,h_31,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_ab3616b57ad5448092c3bfc6f9b08527~mv2.png)

The strategy I employed in this specific challenge involved leveraging the information obtained from the image and its metadata effectively. To achieve this, I turned to a highly influential tool that gained prominence during the Russia-Ukraine war named [**Liveuamap**](https://liveuamap.com/). Live Universal Awareness Map, commonly known as Liveuamap, is an online tool/website designed to monitor and display activities on interactive geographic maps, with a primary focus on areas **experiencing ongoing armed conflicts**.

There is an option to specifically search for incidents based on date and time, so I searched for **January 22, 2024,** and found a lot of incidents in the Khan Yunis area which potentially show thatOn that day, the primary focus of the battles, according to news sources, was there.

As per news sources, the attacks were aimed at **Nasser Hospital**.

![ree](https://static.wixstatic.com/media/aee2e4_b9d0f3b2382840dc9509cc1ed4685069~mv2.png/v1/fill/w_49,h_21,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_b9d0f3b2382840dc9509cc1ed4685069~mv2.png)

![ree](https://static.wixstatic.com/media/aee2e4_15f4a6c1a13b4c73bc84ef7fa817afa2~mv2.png/v1/fill/w_68,h_20,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_15f4a6c1a13b4c73bc84ef7fa817afa2~mv2.png)

Upon examining other pictures taken by the photographer, I observed a prominent, lengthy road where people were both walking and driving cars. Consequently, I chose to search for the main road in Khan Yunis, as it would aid in identifying the approximate area.

I visually identified three main roads with the assistance of Google Maps: El Baheer Road, Salah Al Deen Road, and Gamal Abdel Nasser Road. The bombings in the vicinity of Nasser Hospital were near **El Baheer Road**.

Furthermore, I opted to manually search for other incidents of bombings in Khan Yunis and engage in some dumpster diving and SOCMINT.

After a long and tough search, I found that there were bombings near **Al-Aqsa University** in Khan [Yunis.In](http://Yunis.In) this particular challenge, I chose to use Arabic to access more specialized news sources. ( I translated it to English so you will be able to read it).

![ree](https://static.wixstatic.com/media/aee2e4_82fcb1583d5649e0b6a81c1f4b314ab1~mv2.png/v1/fill/w_49,h_33,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/aee2e4_82fcb1583d5...