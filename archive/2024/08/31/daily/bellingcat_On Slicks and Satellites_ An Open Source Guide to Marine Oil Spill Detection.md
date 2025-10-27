---
title: On Slicks and Satellites: An Open Source Guide to Marine Oil Spill Detection
url: https://www.bellingcat.com/resources/how-tos/2024/08/30/marine-oil-spill-detection-guide/
source: bellingcat
date: 2024-08-31
fetch_date: 2025-10-06T18:08:21.748021
---

# On Slicks and Satellites: An Open Source Guide to Marine Oil Spill Detection

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)

* EN
  + [Русский](https://ru.bellingcat.com)
  + [Français](https://fr.bellingcat.com)
  + [Español](https://es.bellingcat.com)
  + [Deutsch](https://de.bellingcat.com)
  + [Українська](https://uk.bellingcat.com)
* [Donate](https://www.bellingcat.com/donate)

Search for:

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)
* [Donate](/donate)

[![Profile picture for: Wim Zwijnenburg](https://www.bellingcat.com/app/uploads/2020/07/Wim-300x238.png)](https://www.bellingcat.com/author/wim-zwijnenburg/)
[Wim Zwijnenburg](https://www.bellingcat.com/author/wim-zwijnenburg/)

Wim Zwijnenburg is a Humanitarian Disarmament Project Leader for PAX.  He works on conflict and environment related issues in the Middle East, the use and proliferation of emerging military technologies and arms trade @wammezz

# On Slicks and Satellites: An Open Source Guide to Marine Oil Spill Detection

August 30, 2024

* [Conflict](/tag/conflict)
* [Environment](/tag/environment)

Almost every week, oil spills are reported somewhere in the world. From ships dumping contaminating ballast water or breaking down on coral reefs, to direct attacks on oil pipelines and tankers. The larger the spill, the bigger the media attention.

This year alone, off the coast of Trinidad and Tobago, a Bellingcat investigation found that [1,000 tonnes of oil contaminated protected wetlands and wildlife sanctuaries](https://www.bellingcat.com/news/2024/02/20/how-a-leaking-barge-became-an-oil-spill-disaster-off-the-tobago-coast/) after a barge capsized. In the Middle East, the [Houthis targeted the Liberia-flagged tanker](https://www.thenationalnews.com/news/mena/2024/07/17/houthi-attack-on-chios-lion-oil-tanker-leaves-40-kilometre-oil-slick-in-red-sea/), Chios Lion. Carrying a cargo of crude oil, the strike resulted in a 200-kilometre-long oil slick. And in South-East Asia, in late July, the tanker, MT Terra Nova, carrying 1.4 million litres of industrial oil, [capsized off the coast of Manila in the Philippines](https://www.theguardian.com/world/article/2024/jul/25/taiwan-typhoon-gaemi-landfall-death-toll-path-tracker-latest-today), causing a four-km-long engine oil spill.

[![](https://www.bellingcat.com/app/uploads/2024/08/Screenshot-2024-08-28-at-16.31.49-1200x683.png)](https://www.bellingcat.com/app/uploads/2024/08/Screenshot-2024-08-28-at-16.31.49.png)

*Screenshot from [Cerulean](https://cerulean.skytruth.org/), SkyTruth, one of several free global monitoring systems that aims to detect oil pollution from vessels and offshore oil platforms*

The sheer scale of ocean oil pollution is staggering. In Europe, a suspected 3,000 major illegal oil dumps take place annually, with an estimated release of between [15,000 and 60,000 tonnes of oil ending up in the North Sea.](https://link.springer.com/book/10.1007/978-3-319-23901-9) In the Mediterranean, figures provided by [the Regional Marine Pollution](https://www.rempec.org/en/news-media/rempec-news/study-trends-and-outlook-of-marine-pollution)[Emergency Response Centre](https://www.rempec.org/en/news-media/rempec-news/study-trends-and-outlook-of-marine-pollution) estimate there are 1,500 to 2,000 oil spills every year.

The impact of any single oil spill on a marine or coastal ecosystem can be [devastating and long-lasting](https://www.noaa.gov/education/resource-collections/ocean-coasts/oil-spills). Animals such as birds, turtles, dolphins and otters can [suffer from ingesting or inhaling oil](https://oceana.org/blog/how-oil-spills-impact-ocean-animals/), as well as getting stuck in the slick. The loss of water and soil quality can be toxic to both flora and fauna. [Heavy metals enter the food chain](https://www.ukpandi.com/media/files/imports/13108/articles/8441-tip-11-effects-of-oil-pollution-on-fisheries-and-mariculture.pdf), poisoning everything from plankton to shellfish, which in turn affects the livelihoods of [coastal communities dependent on fishing and tourism](https://darrp.noaa.gov/oil-spills/how-can-spill-affect-your-community#:~:text=Habitat%20losses%20may%20alter%20migration,and%20recreational%20and%20commercial%20fisheries.).

However, with a wealth of open source earth observation tools at our fingertips, during such environmental disasters it’s possible for us to identify and monitor these spills, highlight at-risk areas, and even hold [perpetrators accountable](https://www.propublica.org/article/how-oil-companies-avoided-environmental-accountability-after-10.8-million-gallons-spilled).

## A Spectrum of Slicks

Oil spills come in many forms and shapes, depending on the oil type, water and weather conditions.

Most frequent are small spills, mid-sea, often from vessels dumping contaminated waste or ballast water. Larger spills can result from collisions between boats, capsizing in bad weather, or during ship to ship transfer of crude oil and petroleum products.

[![](https://www.bellingcat.com/app/uploads/2024/08/Visualisation-oil-spills-Automatisch-opgeslagen-12.png)](https://www.bellingcat.com/app/uploads/2024/08/Visualisation-oil-spills-Automatisch-opgeslagen-12.png)

*The Princess Empress oil tanker was carrying industrial fuel when it sank in a storm. The distinct rainbow coloured slick seen in the Sentinel-2 image indicates a diesel oil spill*

In the last decade there have been a number of larger incidents, with oil tankers being targeted during[covert operations](https://www.nytimes.com/2021/03/26/world/middleeast/israel-iran-shadow-war.html) or by [non-state armed groups](https://www.reuters.com/world/middle-east/yemens-houthis-target-fuel-tanker-torm-thor-gulf-aden-2024-02-24/). There have been numerous accidents at mooring stations, whilst loading or unloading oil products along pipelines. As well as spills that originated in-land, from dumping or accidents at storage sites.

## How to Identify an Oil Spill

The National Oceanic and Atmospheric Administration (NOAA) [toolkit](https://response.restoration.noaa.gov/sites/default/files/OWJA_2016.pdf) offers solid guidance on how to recognise and label different types of oil and how they might appear on the water.

[![](https://www.bellingcat.com/app/uploads/2024/08/image12-1-1200x674.png)](https://www.bellingcat.com/app/uploads/2024/08/image12-1.png)

*Screenshot from the [NOAA toolkit](https://response.restoration.noaa.gov/sites/default/files/OWJA_2016.pdf). By labelling the different colours and formations, responders are better able to identify what type of oil they are dealing with and what could happen next*

Diesel oil, being much lighter than other types, disperses and evaporates more easily, often creating **rainbow** formations (see above) on the surface of the water. It is more likely to evaporate in open water compared to thicker composites, such as crude oil or heavy fuel oil used in engines. When viewed from above, **metallic** or **silver sheens** will be seen emanating from **darker** areas.

Additional tools to [NOAA](https://response.restoration.noaa.gov/sites/default/files/OWJA_2016.pdf) include the [Australian Marine Authorities  Oil Spill Aerial Observation and Identification guide](https://www.amsa.gov.au/sites/default/files/2014-01-mp-amsa22-identification-oil-on-water.pdf) and the [International Petroleum Industry Environmental Conservation Association (IPIECA) Guidelines](https://www.ipieca.org/resources/aerial-observation-of-oil-spills-at-sea).

[![](https://www.bellingcat.com/app/uploads/2024/08/image13-1.png)](https://www.bellingcat.com/app/uploads/2024/08/image13-1.png)

*Screenshot from the International Marine Organization (IMO) [guidelines on incide...