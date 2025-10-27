---
title: On (Structured) Data
url: https://posts.specterops.io/on-structured-data-707b7d9876c6?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2023-07-27
fetch_date: 2025-10-04T11:56:47.297855
---

# On (Structured) Data

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F707b7d9876c6&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fon-structured-data-707b7d9876c6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fon-structured-data-707b7d9876c6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-707b7d9876c6---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-707b7d9876c6---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# On (Structured) Data

[![Will Schroeder](https://miro.medium.com/v2/resize:fill:64:64/1*idzSM22ouVWVRLUiU5Kpkg.jpeg)](https://harmj0y.medium.com/?source=post_page---byline--707b7d9876c6---------------------------------------)

[Will Schroeder](https://harmj0y.medium.com/?source=post_page---byline--707b7d9876c6---------------------------------------)

9 min read

·

Jul 26, 2023

--

1

Listen

Share

## Introduction

The offensive security industry is a curious one. On one hand, we are ahead in various trends (or “thought leadership,” as some would have us term it) and are used to **literally** “moving fast and breaking things.” On the other hand, we’re far behind similar disciplines. One major area where offensive security has historically been a bit lacking is proper software engineering for offensive tooling. From proper unit testing to continuous integration/continuous delivery (CI/CD) integration, we’re sometimes behind our more mature industry parallels.

![]()

Why is this? Possibly, it’s that offensive engineering has an asymmetric nature. To make a long story short, a small amount of offensive code can go a long way and many most of us in the offensive industry are not proper software engineers. All it takes is for a real software engineer to come in and show us how it’s really done, but in general we tend to be focused on PoC||GTFO, or read a different way (in practice) IW,SWGAS “It Works, So Who Gives a \*\*\*\*”.

This results in the offensive development landscape diverging from its defensive counterpart. The post-exploitation sector of offensive security has generally given away/open-sourced *a lot of/most code* that other teams can easily work into their workflows and while the defensive industry does have a number of open-source software (OSS) projects, there have historically been more challenges in operationalizing in environments due to scale and workflow/technology integration issues. While there are obviously exceptions to this (and the full reason for why this is the case is enough to fill another blog post), the commercialization opportunities for the defensive industry have far outweighed the offensive industry; at least in the private sector.

In general, with money comes professionalism, and the defensive industry has had money come in spades while the offensive industry has generally been more lacking. This often leads to blind spots, where we as an offensive industry could be benefiting from the established software engineering practices of more major industries.

We believe there is a seemingly minor but effectively major oversight in offensive security, specifically the post-exploitation space: **structured data**. In particular, while the OSINT and scanning side of the house has generally taken advantage of structured data, the post-ex side hasn’t quite kept up. Likewise, the defensive industry has *really* run with structured data due to the scale of what they have to process. We will cover some of the red versus blue data caveats later in this post.

This is the first post in a series where we will cover why this is an important concept, what we think we can do with it, and what we *are* doing about it.

![]()

## On the Red Side

Tools handling OSINT have generally been pretty welcoming of structured data; things like [Shodan](https://www.shodan.io/), [Maltego](https://www.maltego.com/), [recon-ng](https://github.com/lanmaster53/recon-ng), etc., have long been pulling in disparate pieces of information for the purposes of correlation. Likewise, scanning tools like [Nmap](https://nmap.org/book/man-output.html), [Nessus](https://docs.tenable.com/nessus/Content/ScanReportFormats.htm), and the like have had structured output for practically forever; allowing integration of this type of data into other tools and processes (e.g., loading Nmap scans into Metasploit).

Another category is attack simulation tools (e.g., [DeathStar](https://github.com/byt3bl33d3r/DeathStar), [ANGRYPUPPY](https://github.com/vysecurity/ANGRYPUPPY), [ATT&CK’s Caldera](https://github.com/mitre/caldera), etc.) that allow you to execute sequences of offensive actions based on structured data inputs. Some other recent tools like [CISA](https://www.cisa.gov/)’s [RedEye](https://github.com/cisagov/RedEye/) have started to focus on visualization of attack data (like Cobalt Strike logs). And finally, there are the log aggregators, like [RedELK](https://github.com/outflanknl/RedELK), which aim to create a red team SIEM including “[*…a central location where all relevant operational logs from multiple teamservers are collected and enriched*](https://github.com/outflanknl/RedELK/wiki#goal-of-the-project)*”* and *“*[*…where all traffic logs from redirectors are collected and enriched.*](https://github.com/outflanknl/RedELK/wiki#goal-of-the-project)” Additionally, SpecterOps’s own [GhostWriter](https://github.com/GhostManager/Ghostwriter) functions as our security project management and reporting engine. A lot of these are extremely useful but have generally focused on processing, visualization, and indexing/searching of command and control (C2) logs.

When we move to the post-ex realm of tools, things are not quite the same. [BloodHound](https://github.com/BloodHoundAD/BloodHound) has had a lot of success in visualizing attack paths from collected structured data and [JackDaw](https://github.com/skelsec/jackdaw), [Adalanche](https://github.com/lkarlslund/Adalanche), and [ROADTools](https://github.com/dirkjanm/ROADTools) can collect/visualize similar information in a similar way. Some offensive tools like the venerable [Metasploit Framework](https://github.com/rapid7/metasploit-framework) and frameworks like [CrackMapExec](https://github.com/mpgn/CrackMapExec) *do* have [internal databases](https://wiki.porchetta.industries/getting-started/database-general-usage) that store collected information in a fairly structured manner, but this tends to be used more for result tracking and storage.

![]()

In general, output from many offensive tools is currently structured for human analysis versus being structured for computers. *Most* of the most popular C2 frameworks have textual output w...