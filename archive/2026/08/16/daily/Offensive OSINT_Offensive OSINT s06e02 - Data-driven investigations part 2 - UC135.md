---
title: Offensive OSINT s06e02 - Data-driven investigations part 2 - UC135
url: https://www.offensiveosint.io/offensive-osint-s06e02-data-driven-investigations-part-2-uc135/
source: Offensive OSINT
date: 2026-08-16
fetch_date: 2026-08-17T02:54:14.251500
---

# Offensive OSINT s06e02 - Data-driven investigations part 2 - UC135

[![Offensive OSINT](https://storage.ghost.io/c/b5/22/b52265eb-d44c-4ae8-8456-954cfb01f918/content/images/2020/07/OffensiveOsint-logo-RGB-2.png)](https://www.offensiveosint.io)

[About me](/about-me/)
[Sign in](/signin/)

##### Search Here

×

![Offensive OSINT s06e02 - Data-driven investigations part 2 - UC135](https://storage.ghost.io/c/b5/22/b52265eb-d44c-4ae8-8456-954cfb01f918/content/images/size/w2000/2026/08/levon-vardanyan-I36JZ3l0T1E-unsplash-2.jpg)

Offensive OSINT
16.08.2026

# Offensive OSINT s06e02 - Data-driven investigations part 2 - UC135

This episode walks through scraping, enriching, and cross-checking ten thousand Warsaw Airbnb listings against pretty much every registry Poland has, just to find out who actually owns this market, and the results turned out to be boring and completely unsurprising.

Go directly to the scrollytelling

[10 047 ofert Airbnb w Warszawie: właściciele, fundusze i ustawa UC135

![](https://storage.ghost.io/c/b5/22/b52265eb-d44c-4ae8-8456-954cfb01f918/content/images/icon/faviconV2-ef4dafae-1618-4cf5-8208-f6d84b1bf1df)

![](https://storage.ghost.io/c/b5/22/b52265eb-d44c-4ae8-8456-954cfb01f918/content/images/thumbnail/OffensiveOsint-logo-RGB-2-f4a228f2-2621-446e-ae29-07bba85c4e22.png)](https://woj-ciech.github.io/viz/airbnb/storytelling.html?ref=offensiveosint.io)

If you haven't seen part one yet, it's still up

[Spółki posłów - Storytelling

Immersive scroll-driven animations with D3 visualizations.

![](https://storage.ghost.io/c/b5/22/b52265eb-d44c-4ae8-8456-954cfb01f918/content/images/icon/faviconV2-6c0a41e2-6274-4fd6-8b14-42612c0516b6)Storytelling

![](https://storage.ghost.io/c/b5/22/b52265eb-d44c-4ae8-8456-954cfb01f918/content/images/thumbnail/OffensiveOsint-logo-RGB-2-799b39f8-451c-4a32-b45f-a17978c86df9.png)](https://woj-ciech.github.io/viz/story.html?ref=offensiveosint.io)[Offensive OSINT s05e10 - Interactive investigative stories part 1

There were three main forces that pushed me to write this story: inspiration from the Uncovered + International Journalism Forum in Athens, experimenting with ChatGPT-5’s ability to support data-driven visual storytelling, and a desire to create an interactive narrative. In this article, I’ll walk you through how

![](https://storage.ghost.io/c/b5/22/b52265eb-d44c-4ae8-8456-954cfb01f918/content/images/icon/oo-4731adf4-5df3-4d0a-9b11-39935e4f37ff.png)Offensive OSINTWojciech

![](https://storage.ghost.io/c/b5/22/b52265eb-d44c-4ae8-8456-954cfb01f918/content/images/thumbnail/ciaran-o-brien-jCXMsJQTsQw-unsplash-6b258ae7-01bf-44b8-96c5-227e68aafcaf.jpg)](https://www.offensiveosint.io/offensive-osint-s05e10-interactive-investigative-stories-part-1/)

If you follow this blog, you already know I like data, and I like it even more when it tells a story, presented in a format people can actually follow, not just a spreadsheet dump. This episode picks up the lead from part one and takes a look at short-term rental apartments in Warsaw.

Think of it as a guided tour through the sources, the annoying obstacles, the data clean up, and the visualization decisions behind a Airbnb in Warsaw.

But before any of that, thank you to everyone who came to my workshop on critical infrastructure. Great students, great questions, and I appreciated the chance to be there.

![](https://storage.ghost.io/c/b5/22/b52265eb-d44c-4ae8-8456-954cfb01f918/content/images/2026/08/oo-1.jpg)

I know you would preferer food tasting though.

# Introduction

Part one focused on politicians and their ownership stakes in companies, with a particular eye on a real estate. It's a topic that matters well beyond Poland. Access to housing is a hot subject across most of the West right now. That piece was about figuring out which politician holds the biggest stake in real estate, and how you could go about pulling and cross-referencing that kind of data yourself.

This time we're staying in real estate, but narrowing in to short-term rentals specifically, the segment the Polish government is currently trying to fight with

[https://legislacja.rcl.gov.pl/projekt/12405554/katalog/13177393](https://legislacja.rcl.gov.pl/projekt/12405554/katalog/13177393?ref=offensiveosint.io)

so far without much success. The draft law (known in the legislative process as **UC135**) would introduce no-rental zones in residential buildings, require sign-off from fellow residents before a unit can be listed short term, and generally try to shrink the grey area the market currently operates in. It's been bouncing between committees and public consultations for months.

Instead of starting from people and their companies like in part one, this time we're flipping the approach and start from the listings themselves. Who has the most apartments up on Airbnb, follow the corporate trail behind them, and look for connections between companies that share an address, a phone number, or an email, then present all of it as clean, understandable scrollytelling in D3.js.

![](https://storage.ghost.io/c/b5/22/b52265eb-d44c-4ae8-8456-954cfb01f918/content/images/2026/08/image-1.png)

# Methodology

Sometimes I get a thought stuck in my head and the only way to get rid of it is to go find the actual answer. What share of Warsaw's short-term rental listings belongs to companies, and what share to private individuals, and who actually runs this market? Chasing that question meant I first needed to get my hands on every single listing.

That's harder than it sounds. Airbnb doesn't expose a clean "give me everything" endpoint, and the map view caps out at 15 pages of 18 results each (270 listings, tops) no matter how many hundreds or thousands actually exist in the area you're looking at. My workaround was to grab Warsaw's official bounding box coordinates, chop it into 6 smaller tiles, and paginate through each tile separately (zooming in further wherever a tile still hit the cap on its own). That's how I ended up with 10,047 short-term rental listings in Warsaw. For context, a DELab UW

[https://delab.uw.edu.pl/wp-content/uploads/2024/09/prezentacja\_airbnb\_delab\_v3\_compressed.pdf](https://delab.uw.edu.pl/wp-content/uploads/2024/09/prezentacja_airbnb_delab_v3_compressed.pdf?ref=offensiveosint.io)

on the same city put the number at 9,631. So the market's grown by roughly 400 listings in a year and a half, which is its own small story.

Worth calling out that none of this research would even be possible without a fairly recent EU rule that forces platforms like Airbnb to collect and display a business registration number for any host operating as a company. Without that, there'd be nothing to enrich in the first place: just a name and a phone number. That data only shows up on the individual listing page, not in the search results, so I still needed a decent chunk of horsepower (and proxies) to pull it at scale.

![](https://storage.ghost.io/c/b5/22/b52265eb-d44c-4ae8-8456-954cfb01f918/content/images/2026/08/asdfadsfasdf.png)

Getting the initial dataset together wasn't too painful once the tile-splitting trick was sorted. Here's roughly what one raw record looked like straight out of the scrape (trimmed for readability, the real ones carry a full photo gallery and more host metadata)

```
{
  "listing_id": "1698446444052177806",
  "url": "https://www.airbnb.com/rooms/1698446444052177806",
  "title": "Apartment in Mokotów",
  "subtitle": "Comfortable flat next to SGH and Pole Mokotowskie",
  "rating": "5.0 (5)",
  "price": "zł 1,070",
  "latitude": 52.2086,
  "longitude": 20.9994,
  "photos": ["https://a0.muscache.com/im/pictures/hosting/.../original/....jpeg", "..."],
  "host": {
    "name": "Aleksander",
    "is_superhost": false,
    "is_verified": true,
    "rating_average": 4.62,
    "rating_count": 3828,
    "years_hosting": { "years": 8, "months": 11 },
    "is_airbnb_managed": false
  },
  "is_business": true,
  "business_details": {
    "business_name": "XXXXXXXXX Spółka Z Ograniczoną Odpowiedzialnością",
    "email": "XXX@gmail.com",
    "phon...