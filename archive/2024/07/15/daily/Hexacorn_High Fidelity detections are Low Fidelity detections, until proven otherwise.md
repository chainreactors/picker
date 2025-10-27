---
title: High Fidelity detections are Low Fidelity detections, until proven otherwise
url: https://www.hexacorn.com/blog/2024/07/14/high-fidelity-detections-are-low-fidelity-detections-until-proven-otherwise/
source: Hexacorn
date: 2024-07-15
fetch_date: 2025-10-06T17:40:24.950348
---

# High Fidelity detections are Low Fidelity detections, until proven otherwise

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2024/07/07/writing-a-frida-based-vbs-api-monitor-take-two/)
[Next →](https://www.hexacorn.com/blog/2024/08/01/high-fidelity-detections-are-low-fidelity-detections-until-proven-otherwise-part-2/)

# High Fidelity detections are Low Fidelity detections, until proven otherwise

Posted on [2024-07-14](https://www.hexacorn.com/blog/2024/07/14/high-fidelity-detections-are-low-fidelity-detections-until-proven-otherwise/ "12:08 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

A few days ago [Nas](https://x.com/nas_bench) kicked off an interesting [discussion](https://x.com/nas_bench/status/1808814344286740894) on Xitter about detections’ quality. I liked it, so I offered my personal [insight](https://x.com/Hexacorn/status/1808822427222184408). I then added a stupid [example](https://x.com/Hexacorn/status/1808910092584050690) to illustrate my point to which [DylanInfosec](https://x.com/DylanInfosec) [replied](https://x.com/DylanInfosec/status/1808934236285489313):

```
Would love to set some time aside and gather some OS log dumps, throw em in a SIEM and test that way or something. I guess crowd validation with a trusted diverse group could work too. Not-for-profit or anything but just to share with the community
```

This made me think…

I am an old-school data hoarder; as far as I remember I have always been actively looking for data of interest in a lot of places… And I must confess that the only reason I could immediately provide that stupid mimi-based regex filename search example was because I had an access to my private ‘clean’ file names dataset…

You see… over a decade ago I kicked off a personal project of mine that focused on collecting software data from CLEAN sources. While many people in the cybersecurity industry at that time primarily focused on malware collections, I decided to take a step forward and collect data that was most likely clean. So, I wrote a number of web scrapers, downloaders, used VPN and Tor where necessary and eventually built a large data set of samples that is a a collection of (most likely) clean files downloaded from publicly available sources. I didn’t stop there. I took every single sample that I downloaded and got it decompiled, whenever it was possible… then processed all the decompiled files only to build a modern, full-blown, Windows-centric clean software data collection set that I believed at that time to be far better than [NIST’s](https://www.hexacorn.com/blog/2023/09/16/analysing-nsrl-data-set-for-fun-and-because-curious-part-3/).

Now, it’s been a few years and this set is getting older and older, every single day, so perhaps it’s time for it to win some brownie points in the community…

Many of our threat hunting rules depend on file names. The file I am attaching to this post includes a list of many PE file names in my collection that are known to be ‘clean’ (to be precise, these are all file names ending with the following file extensions: ‘exe’, ‘dll’, ‘drv’, ‘ocx’, ‘sys’). It goes without saying that you must treat this list as very suspicious, but I hope it will help you to write better detections…

[\_files\_of\_interest.su.zip](https://hexacorn.com/d/_files_of_interest.zip)

And to illustrate the point, let’s run a query that is similar to the one I did for my tweet:

```
rg -i "mimi.*?\.(dll|exe|sys)" _files_of_interest.su
```

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/mimi1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/mimi1.png)

Note: you can’t use the \_files\_of\_interest.zip/\_files\_of\_interest.su files for commercial purposes.

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Clustering](https://www.hexacorn.com/blog/category/clustering/), [Threat Hunting](https://www.hexacorn.com/blog/category/threat-hunting/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/07/14/high-fidelity-detections-are-low-fidelity-detections-until-proven-otherwise/ "Permalink to High Fidelity detections are Low Fidelity detections, until proven otherwise").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")