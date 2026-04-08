---
title: When Satellite Imagery Goes Dark: New Tool Shows Damage in Iran and the Gulf
url: https://www.bellingcat.com/resources/2026/04/07/tool-damage-assessment-destruction-sentinel-satellite-imagery-iran-us-gulf/
source: bellingcat
date: 2026-04-07
fetch_date: 2026-04-08T04:38:40.127772
---

# When Satellite Imagery Goes Dark: New Tool Shows Damage in Iran and the Gulf

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

[![Profile picture for: Jake Godin](https://www.bellingcat.com/app/uploads/2022/08/Screen-Shot-2022-08-30-at-12.02.00-PM-300x300.png)](https://www.bellingcat.com/author/jakegodin/)
[Jake Godin](https://www.bellingcat.com/author/jakegodin/)

Jake Godin is a researcher for Bellingcat. He has covered multiple conflicts with an emphasis on geolocation, munition identification and documenting civilian harm. Prior to joining Bellingcat, he worked at Scripps News on open source reporting, some in partnership with Bellingcat.

[![](https://www.bellingcat.com/app/uploads/2014/07/Bellingcat-logo-avatar-300x283.jpg)](https://www.bellingcat.com/author/conflictandhumanrightsteam/)
[Conflict and Human Rights Team](https://www.bellingcat.com/author/conflictandhumanrightsteam/)

We use open source investigative methods to identify, document and expose human rights abuses as well as to record and explain developments in ongoing conflicts.

# When Satellite Imagery Goes Dark: New Tool Shows Damage in Iran and the Gulf

April 7, 2026

* [Conflict](/tag/conflict)
* [Iran](/tag/iran)
* [Satellite Imagery](/tag/satellite-imagery)

Access to open source visuals of the current Iran conflict, which has spread to many parts of the Middle East, [continues to be sporadic](https://www.bloomberg.com/news/articles/2026-03-20/iran-war-internet-shutdown-limits-civilian-social-media-images?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc3NDAwNTA1MiwiZXhwIjoxNzc0NjA5ODUyLCJhcnRpY2xlSWQiOiJUQzZRMjRLSVAzSlQwMCIsImJjb25uZWN0SWQiOiI1MEU0OTBGQjhDNTM0MkREODAwRUEyNTQ1RjBCMThCOCJ9.wyxKGMZtga0S2Rgww9xGjYWTBB25bJi3MuhojVf5yWA&leadSource=uverify%20wall). Videos and photos from within Iran trickle out on social media as the [Iranian internet blackout](https://bsky.app/profile/netblocks.org/post/3misqxvizzc2h) hinders the flow of digital communication.

In past conflicts, satellite imagery has provided a vital overview of potential damage to both military and civilian infrastructure, especially when there are digital black spots or obstacles to on-the-ground reporting. But imagery from commercial providers is [becoming](https://bsky.app/profile/eliothiggins.bsky.social/post/3miotfqqqqs2j) [increasingly](https://bsky.app/profile/eliothiggins.bsky.social/post/3miotfqqqqs2j) [restricted](https://www.reuters.com/business/aerospace-defense/satellite-firm-extends-middle-east-image-delay-prevent-use-by-us-adversaries-2026-03-10/), leaving even those who have access to the most expensive imagery in the dark.

Shortly after the war in Gaza began in 2023, Bellingcat [introduced a free tool](https://www.bellingcat.com/resources/2023/11/15/a-new-tool-allows-researchers-to-track-damage-in-gaza/) authored by University College London lecturer and Bellingcat contributor, Ollie Ballinger, that was able to estimate the number of damaged buildings in a given area. This helped monitor and map the scale of destruction across the territory as Israel’s military operation progressed.

Bellingcat is now introducing an updated version of the open source tool — called the Iran Conflict Damage Proxy Map — focused on destruction in Iran and the wider Gulf region.

It can be accessed [here](https://bellingcat-ee.projects.earthengine.app/view/middle-east-change).

## How it Works

The tool works by conducting a statistical test on Synthetic Aperture Radar (SAR) imagery captured by the Sentinel-1 satellite which is part of the Copernicus mission developed and operated by the European Space Agency. SAR sends pulses of microwaves at the earth’s surface and uses their echo to capture textural information about what it detects.

The SAR data for the geographic area covered by the tool is put through the [Pixel-Wise T-Test (PWTT)](https://www.sciencedirect.com/science/article/pii/S0034425725004298) damage detection algorithm, which was also developed by Ollie Ballinger. It takes a reference period of one year’s worth of SAR imagery before the onset of the war and calculates a “normal” range within which 99% of the observations fall. It then conducts the same process for imagery in an inference period following the onset of the war, and compares it to the reference period. The core idea is that if a building has become damaged since the beginning of the war, then the “echo” (called backscatter) from that pixel will be consistently outside of the normal range of values for that particular area. Investigators can then further probe potential damage around this highlighted area.

The plot below shows how the process was applied to Gaza and several Syrian, Iraqi and Ukrainian cities. The bars represent the weekly total number of clashes in each place, sourced from the Armed Conflict Location Event (ACLED) dataset. The pre-war reference periods are shaded in blue, spanning one year before the onset of each conflict. The one month inference periods after the respective conflicts  began are shaded in orange. The blue and orange areas are what the tool compares.

![](https://www.bellingcat.com/app/uploads/2026/04/graphirantool.jpg)

The plot below shows an area with a number of warehouses in Tehran’s southwest. Some of the buildings show clear damage in optical Sentinel-2 imagery (something that has to be [accessed outside](https://browser.dataspace.copernicus.eu/) of the tool via the Copernicus Browser).

Clicking on the map within the [tool](https://bellingcat-ee.projects.earthengine.app/view/middle-east-change) generates a chart displaying that pixel’s historical backscatter; the red dotted lines denote a range within which 99% of the pre-war backscatter values fall. In this example, we can see that from March 14 onwards, the backscatter values over this warehouse begin to consistently fall outside of their historical normal range. This could signal that damage has been detected in the area.

![](https://www.bellingcat.com/app/uploads/2026/04/exampleirantooldemo-1200x729.jpg)

Two important aspects of this workflow are that it utilises free and fully open access satellite data, as opposed to commercial satellite services; the second is that it overcomes some key limitations of AI in this domain, the most serious of which is called overfitting. This is where a model trained in one area is deployed in a new unseen area, and fails to generalise. Because we’re only ever comparing each pixel against its own historical baseline, we don’t run into that problem.

## Accuracy

The PWTT has been [published in a scientific journal](https://www.sciencedirect.com/science/article/pii/S0034425725004298) after two years of review.  Its accuracy was  assessed using an original dataset of over two million building footprints labeled by the United Nations, spanning 30 cities across Gaza, Ukraine, Sudan, Syria, and Iraq. Despite being simple and lightweight, the algorithm has been recorded achieving building-level accuracy statistics (AUC=0.87 in the full sample) rivaling state of the art [methods](https://link.springer.com/article/10.1007/s13753-023-00526-6?utm_source=getftr&utm_medium=getftr&utm_campaign=getftr_pilot&getft_integrator=sciencedirect_contenthosting) that use deep learning and high resolution imagery. The plot below compares building-level p...