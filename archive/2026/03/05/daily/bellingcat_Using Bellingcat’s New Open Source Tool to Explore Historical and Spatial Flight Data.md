---
title: Using Bellingcat’s New Open Source Tool to Explore Historical and Spatial Flight Data
url: https://www.bellingcat.com/resources/2026/03/05/turnstone-flight-tracking-tool/
source: bellingcat
date: 2026-03-05
fetch_date: 2026-03-06T04:04:54.629533
---

# Using Bellingcat’s New Open Source Tool to Explore Historical and Spatial Flight Data

* [Investigations](https://www.bellingcat.com/category/news/)
* [Resources](https://www.bellingcat.com/category/resources/)
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
* [Resources](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)
* [Donate](/donate)

[![Profile picture for: Logan Williams](https://www.bellingcat.com/app/uploads/2021/11/DSCF9308-300x300.jpg)](https://www.bellingcat.com/author/loganwilliams/)
[Logan Williams](https://www.bellingcat.com/author/loganwilliams/)

Logan Williams is Bellingcat's technology officer and a senior data scientist and researcher on Bellingcat's Investigative Tech Team. He has a background in cartography, data visualisation, optics and signal processing.

# Using Bellingcat’s New Open Source Tool to Explore Historical and Spatial Flight Data

March 5, 2026

* [Flight Tracking](/tag/flight-tracking)
* [Tools](/tag/tools)

Flight tracking data is [an important tool](https://www.bellingcat.com/resources/how-tos/2019/10/15/a-beginners-guide-to-flight-tracking/) in open source research, but with [100,000 daily flights](https://easbcn.com/en/how-many-planes-fly-per-day-around-the-world/), it can be difficult to contextualise what a particular aircraft’s movements indicate.

Bellingcat has developed a tool called Turnstone to make it easier to visualise historical trends in flight data and spot unusual patterns. It also allows users to filter by parameters such as aircraft type or a geographic region of interest.

![](https://www.bellingcat.com/app/uploads/2026/02/turnstone_image8-1200x779.jpg)

*Source: ZUMA Press Wire via Reuters Connect; overlays of Turnstone by Bellingcat*

This tool primarily uses Automatic Dependent Surveillance–Broadcast (ADS-B) data, the technology that enables open source investigators and enthusiasts to track flights.

Most aircraft are equipped with transmitters that broadcast ADS-B data to comply with global aviation regulations, though regulations [vary by jurisdiction](https://www.aopa.org/go-fly/aircraft-and-ownership/ads-b/where-is-ads-b-out-required), and military aircraft [might not always transmit](https://nbaa.org/aircraft-operations/communications-navigation-surveillance-cns/ads-b/faa-permits-ads-b-off-military-sensitive-flights/). ADS-B data includes information about an aircraft’s identity and type, as well as its precise position, speed and altitude.

Popular flight-tracking websites such as [Flightradar24](https://www.flightradar24.com/) and [ADS-B Exchange](https://globe.adsbexchange.com/) typically display historical data for a particular time or aircraft. However, Turnstone aggregates ADS-B data for multiple aircraft over time, and allows users to search for flights across two areas of interest at once. These features provide additional context for open source investigators to better understand flight behaviour.

*Watch the video for a demonstration of how the tool works, using the example of* [*Black Hawk helicopter patrols*](https://www.cbc.ca/news/canada/british-columbia/black-hawk-patrols-1.7454474) *near one of the borders between the US and Canada:*

You can view Turnstone’s source code and information about hosting it yourself on Bellingcat’s [GitHub](https://github.com/bellingcat/adsb-history).

We also have a web-based instance of the tool that journalists and academics can access. Due to data hosting and processing costs, we can only grant access on a selective basis. If you would like to apply, please fill in [this form](https://docs.google.com/forms/d/e/1FAIpQLSct-l5hl7OiLJ65bIaAYub5uGrDziHFnry6wxVshSP8r2e_JA/viewform?usp=preview). Priority will be given to researchers conducting open source investigations [aligned with Bellingcat’s goals](https://www.bellingcat.com/about/who-we-are/).

Read on for more examples of how Turnstone can be used for investigations, as well as some limitations of the tool.

## Spotting Unusually High US Tanker Activity Before Iran Strikes

The US and Israel launched [joint air strikes](https://www.cbsnews.com/live-updates/iran-war-us-israel-day-4-trump-gives-no-timeline-as-gulf-states-attacked/) across Iran on Feb. 28, 2026, [reportedly](https://www.aljazeera.com/news/2026/3/4/death-toll-in-iran-surpasses-1000-as-israel-us-strikes-continue) killing [more than 1,000 people](https://www.cbc.ca/news/world/tracking-deaths-iran-israel-united-states-middle-east-9.7114340), including [members of the Iranian leadership](https://edition.cnn.com/2026/02/28/middleeast/maps-iran-tehran-attack-vis-intl), in five days.

This marked a dramatic escalation since the US and Israel [bombed three Iranian nuclear sites](https://news.un.org/en/story/2025/06/1164741) in June 2025.

Flight data before both the [June 2025](https://www.airnavradar.com/blog/massive-us-tanker-deployment-spotted-over-atlantic-likely-supporting-middle-east-troop-movement) and [February 2026](https://x.com/vcdgf555/status/2027421469421310432) strikes showed a large number of American [aerial tankers](https://simpleflying.com/top-tanker-aircraft-list/) leaving the US and crossing the Atlantic towards Iran. Aerial tankers such as the [KC-135](https://www.af.mil/About-Us/Fact-Sheets/Display/Article/1529736/kc-135-stratotanker/) and [KC-46A](https://www.boeing.com/defense/tankers-and-transports/kc-46-pegasus) can refuel military aircraft in-flight, making them [essential](https://simpleflying.com/roles-kc-135-stratotanker-us-military-missions/) for most long-range combat missions.

> The 9 KC-46As that went to Ben Gurion.
>
> All came direct from the eastern U.S. [pic.twitter.com/izANyrqi4Q](https://t.co/izANyrqi4Q)
>
> — Evergreen Intel (@vcdgf555) [February 27, 2026](https://twitter.com/vcdgf555/status/2027421469421310432?ref_src=twsrc%5Etfw)

With Turnstone, it is possible to interrogate the baseline level of movement and see how unusual this activity is.

To do this, three filters are set on the search: a geographic region of interest, set to the North Atlantic, a filter on the aircraft type, to search only for tankers, and a filter on the aircraft heading, to search only for eastbound traffic.

![](https://www.bellingcat.com/app/uploads/2026/02/heading.gif)

**Filtering a search by aircraft type, region of interest, and heading range that captures eastbound traffic. Source: Turnstone/Bellingcat**

[Note: For the aircraft category designations, [Bellingcat used](https://github.com/bellingcat/adsb-history?tab=readme-ov-file#augmenting-tar1090-db) a custom-prompted large language model (LLM), [Claude Sonnet 4.0](https://www.anthropic.com/news/claude-4), to assign a category label using aircraft type code data. There may be some inaccuracies in the classifications, as LLMs are prone to hallucinations. We discuss this further in the “Limitations of the Data” section of this piece.]

This search finds over 40,000 aircraft locations that match these filter queries. However, a look at the summary table shows that this data includes non-American tankers as well.

![](https://www.bellingcat.com/app/uploads/2026/02/turnstone_image3-1200x480.jpg)

*Results from a filtered search, showing tankers owned by the French Air Force and the United States Air Force. Source: Turnstone/Bellingcat*

We can filter this data to include only aircraft associated with the US by typing “United States” into the search box in the table. Note that ownership data is not 100 percent accurate – it may be out of date, especially for privately owned aircraft, and new aircraft might not have any data at all. However, especial...