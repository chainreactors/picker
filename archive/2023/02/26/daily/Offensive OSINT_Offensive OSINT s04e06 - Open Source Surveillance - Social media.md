---
title: Offensive OSINT s04e06 - Open Source Surveillance - Social media
url: https://www.offensiveosint.io/offensive-osint-s04e06-open-source-surveillance-social-media/
source: Offensive OSINT
date: 2023-02-26
fetch_date: 2025-10-04T08:08:36.266289
---

# Offensive OSINT s04e06 - Open Source Surveillance - Social media

[![Offensive OSINT](https://www.offensiveosint.io/content/images/2020/07/OffensiveOsint-logo-RGB-2.png)](https://www.offensiveosint.io)

* [Home](/)
* [About me](/about-me/)
* [Open Source Surveillance](https://www.os-surveillance.io)
* [kamerka.io](https://www.kamerka.io)
* [Sign up](/signup/)
* [Account](/account/)
* [Sign in](/signin/)
* [Patreon](https://patreon.com/offensiveosint)

##### Search Here

×

## Offensive OSINT s04e06 - Open Source Surveillance - Social media

* Wojciech

  [![Wojciech](/content/images/size/w100/2023/02/OffensiveOsint-logo-RGB-2.png)](/author/wojciech/)

[Wojciech](/author/wojciech/)
25 Feb 2023 • 16 min read

![Offensive OSINT s04e06 - Open Source Surveillance - Social media](/content/images/2023/02/raphael-lopes-HVibVDQVwbM-unsplash.jpg)

In today's episode we discuss missing 411 cases, selfies with tanks and where are the best places to run in your city.

This if the first part of Open Source Surveillance research that focuses only on social media aspect of location based investigation.

Read tutorial to get familiar with the tool

[Offensive OSINT s04e04 - Open Source Surveillance

Open Source Surveillance takes intelligence gathering and cyber espionage to a whole new level. It can be used for offensive security, but from the other hand can be also helpful in OSINT and law enforcement investigations. Thanks to 18 modules, OSS can show real-time view of the city from variety

![](https://www.offensiveosint.io/content/images/size/w256h256/2020/07/oo.png)Offensive OSINTWojciech

![](https://www.offensiveosint.io/content/images/2023/01/01_OSS_logo_podstawowe-1.png)](https://www.offensiveosint.io/offensive-osint-s04e04-open-source-surveillance/)

*TL;DR I will show how to write new module for the Platform, reveal new updates - Strava, VKontakte and SportsTracker, also present research how to gather intelligence based on social media from the OSS.*

**Disclaimer**

**Originally, article was published on 16th of April, exclusively for Patreon subscribers, and presents outdated screenshots and interface. Since then, the Platform has been improved significantly in terms of stability, features and user experience. It also supports clustering, sidebars instead of info windows and multi selection.**

You can get a small preview how it looks now from my tweets

> Gather geo intel in a blink of an eye with new Open Source Surveillance update. It brings new modules, improved interface and enhanced performance to collect data even more efficiently. Now it's easier than ever to detect, track, and monitor potential threats in real-time. [#OSINT](https://twitter.com/hashtag/OSINT?src=hash&ref_src=twsrc%5Etfw&ref=offensiveosint.io) [pic.twitter.com/WekVAgx9GZ](https://t.co/WekVAgx9GZ?ref=offensiveosint.io)
>
> — Offensive OSINT (@the\_wojciech) [March 30, 2023](https://twitter.com/the_wojciech/status/1641502920901287942?ref_src=twsrc%5Etfw&ref=offensiveosint.io)

[Open Source Surveillance: Location based real-time intelligence

Location based real-time intelligence gathering system

![](https://betalist.com/assets/favicon-618a2bdd0eda7c547f0488b2f97ebc773a50db4351f7ba222f8f1f864e301895.png)Algolia

![](https://img.betalist.com/GxL3zwbX25JmnjamDlOaKIc-desYlcDo5uulKOpANNM/plain/s3://assets.betalist.com/z7nuarbzfmi6f7hj1rjphnzz55lj)](https://betalist.com/startups/open-source-surveillance?ref=offensiveosint.io)

# REGISTER

[Open Source Surveillance

![](https://os-surveillance.io/oss/static/oss_logo.png)Links Other projects & Social Offensive OSINTwww.offensiveosint.io PatreonPatreon Kamerka.iokamerka.io Twitter@the\_wojciech Githubwoj-ciech

![](https://www.offensiveosint.io/content/images/2020/07/OffensiveOsint-logo-RGB-2.png)](https://os-surveillance.io/?ref=offensiveosint.io)

## Introduction

I don't need to convince anyone that Social Media Intelligence (SOCMINT) is one the most popular OSINT field and broadly discussed in community. Basically, in many professions person needs to find and research social media profiles of individuals - investigative journalists, LE officers, lawyers, there are many more jobs that require searching for leads in people online footprint.

Beside obvious information, like where individual works, his friends, photos or hobby, sometimes we can obtain his location, based on the geotags or hints shown on photos. In Open Source Surveillance it's not about who, but rather what and where, and by that I mean it does not focus on particular person but on the territory where photos were taken.

It's possible to take an inside look on the ongoing live events, get help with geolocating pictures or look for people that were present during specific time range and place. It's not only about surveillance but also about finding witnesses or estimate crowd.

Currently, there are plenty of photos & videos sharing platforms like Youtube, Instagram, Twitter, Flickr but not all of them supports geotags, so these three have been implemented. Moreover, Snapchat is also included, but works differently based on map.snapchat.com, which I will talk about later.

## Instagram

It's one of the simplest check but hardest to maintain in terms of scalability, from various reasons. As previously stated, I want this tool to be plug & play, so no input from user is not required, including API keys. Just simply register and start your research out of the box.

To achieve that, I need to maintain accounts on Instagram and checking whether they are alive and can or cannot be used. It's case with majority of checks that some authentication in form of cookie, token or API key is mandatory to retrieve the data. But first let's take a look on the logic.

```
@shared_task(bind=False)
def instagram_module_geo_search(id, lat, lon, user):

    user = User.objects.get(id=user)
    coordinates = Coordinates(id=id, user=user)

    results = []

    url = "https://www.instagram.com/location_search/"
    params = {"latitude": lat, "longitude": lon, "__a": 1}
    headers = {"Cookie": instagram_cookie}

    try:
        r = requests.get(url, params=params, headers=headers, proxies=proxies)
        r_json = json.loads(r.text)
    except Exception as e:
        return {'current': 100, 'total': 100, 'percent': 100, 'error': "Connection error, please try again", "results": [],
                "type": "instagram"}

    if 'venues' in r_json:
        for counter, location in enumerate(r_json['venues']):
            try:
                external_id = location['external_id']
                current_task.update_state(state='PROGRESS',
                                          meta={'current': counter, 'total': len(r_json['venues']),
                                                'percent': int((float(counter) / len(r_json['venues'])) * 100)})
                check_duplicates = InstagramPlace.objects.filter(external_id=external_id, search_main=coordinates).exists()
                if not check_duplicates:
                    name = location['name']
                    lat = location['lat']
                    lon = location['lng']
                    address = location['address']
                    place_db = InstagramPlace(search_main=coordinates, name=name, external_id=external_id,
                                              lat=lat, lon=lon, address=address, timestamp=now)
                    place_db.save()
                    results.append(dict(id=place_db.id,name=name, external_id=external_id,
                                        lat=lat, lon=lon, address=address))

            except Exception as e:
                pass

        return {'current': 100, 'total': 100, 'percent': 100, "results": results, "type": "instagram"}
    else:
        return {'current': 100, 'total': 100, 'percent': 100, "results": [], "type": "instagram"}
```

Instagram geo check

Above simplified code is responsible for checking Instagram places near given latitude and longitude.

Endpoint [https://www.instagram.com/location\_search/](https://www.instagram.com/location_sea...