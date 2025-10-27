---
title: BloodHound Enterprise Learns Some New Tricks
url: https://posts.specterops.io/bloodhound-enterprise-learns-some-new-tricks-26f0fa89e1d1?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2023-08-04
fetch_date: 2025-10-04T12:04:05.574255
---

# BloodHound Enterprise Learns Some New Tricks

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F26f0fa89e1d1&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fbloodhound-enterprise-learns-some-new-tricks-26f0fa89e1d1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fbloodhound-enterprise-learns-some-new-tricks-26f0fa89e1d1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-26f0fa89e1d1---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-26f0fa89e1d1---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# BloodHound Enterprise Learns Some New Tricks

[![Stephen Hinck](https://miro.medium.com/v2/resize:fill:64:64/1*IBPmVwMDUSbZH-Tj8diR_g.jpeg)](https://medium.com/%40shinck?source=post_page---byline--26f0fa89e1d1---------------------------------------)

[Stephen Hinck](https://medium.com/%40shinck?source=post_page---byline--26f0fa89e1d1---------------------------------------)

4 min read

·

Aug 3, 2023

--

Listen

Share

## Summary

The BloodHound code-convergence project brings some significant and long-desired feature enhancements to BloodHound Enterprise (BHE):

* Cypher search, including pre-built queries for AD and Azure
* Built-in support for offline data collection (i.e., control systems or acquisition use cases)
* Expanded capabilities for pathfinding

BloodHound Enterprise customers will get access to these features on Monday, August 7, 2023, and will receive release notes upon delivery. Existing customers can reach out to their TAM with questions.

Interested in learning more about BloodHound Enterprise? Check out <https://bloodhoundenterprise.io/>.

## Introduction

Our [previous blog](/your-new-best-friend-introducing-bloodhound-community-edition-cb908446e270) discussed our strategy for a converged code base and the opportunities it would bring. Today we’ll focus on all of the new features coming to BHE due to that convergence effort and some that we already have in progress for delivery. Let’s get started!

## Cypher search

When we launched BloodHound Enterprise, we knew every customer familiar with the BloodHound product family would want support for Cypher. There was just one (not so little) problem… As a hosted service, how do we ensure the security and availability of an open query interface that could allow someone (maliciously or otherwise) to [improperly manipulate data or gain access to the database system itself](https://pentester.land/blog/cypher-injection-cheatsheet/).

In preparation for this release, we created a utility within the BloodHound code base called “DAWGS” (short for Database Agnostic Wrapper for Graph Schemas). DAWGS is our middleware layer that handles every query made against BloodHound’s Neo4J database, including custom-written Cypher statements. With DAWGS, we can ensure the safety and security of our hosted tenants by preventing individual queries from taking too long or from consuming too much memory (resulting in critical hangs in Neo4J when exhausting available resources).

DAWGS takes every query written in the BloodHound UI, rips it apart, and rebuilds it safely before issuing the call to the database so that our customers can query their data to their hearts’ content!

Press enter or click to view image in full size

![]()

Identifying the location of all Tier Zero objects utilizing Cypher in BHE

For those interested in the inner workings of DAWGS please stay tuned for an in-depth blog post from our engineering team in the near future

## Offline data collection

Our customers love the ease of collection offered by the enterprise version of SharpHound and AzureHound; they are always online, collecting data as you need. But in certain circumstances, deploying persistent data collection services isn’t always feasible. Whether validating the risk of introducing a domain trust to that newly acquired child organization or analyzing the Attack Paths from an offline industrial controls environment, our customers have long desired the ability to perform offline collections but still take advantage of all of the analysis capabilities offered by their BloodHound Enterprise license.

With this release, these use cases have straightforward, UI-driven workflows to enable our customers to download the most recent version of SharpHound and upload the results via the UI for ingestion and processing. This simplification will enable customers to easily evaluate the risks across their environments with greater flexibility.

Press enter or click to view image in full size

![]()

Ingesting data collected from an offline environment

## Improved pathfinding search

Just like using Google Maps to get to dinner while avoiding tolls, sometimes you want to exclude certain edges from an Attack Path in BloodHound. We’ve brought the ability to filter edge types for both AD and Azure-based Attack Paths to BloodHound Enterprise. We’ve also made it much easier to reverse your current path if you accidentally set your start and endpoints backward!

Press enter or click to view image in full size

![]()

Filtering Attack Paths for pathfinding

## Conclusion and what’s next

Next week’s early access release of BloodHound CE is just the beginning. This convergence project will enable the BloodHound Engineering team to rapidly pursue additional features and deliver them to all of our customers. Our engineering team is already hard at work bringing additional features into the code base and additional Attack Path coverage in both AD and Azure.

Up next in our release blog series is the one everyone has been waiting for. On August 8, 2023, BloodHound CE will be made available in its entirety, complete with a blog post by BloodHound co-founder Andy Robbins covering all the changes. Andy and fellow BloodHound co-founder Rohan Vazarkar will also be hosting a webinar on August 18, 2023 to discuss all of the new changes coming to BloodHound CE. You can register for the webinar [here](https://ghst.ly/3Om0jDo).

[Bloodhound](https://medium.com/tag/bloodhound?source=post_page-----26f0fa89e1d1---------------------------------------)

[Bloodhound Enterprise](https://medium.com/tag/bloodhound-enterprise?source=post_page-----26f0fa89e1d1---------------------------------------)

[Research](https://medium.com/tag/research?source=post_page-----26f0fa89e1d1---------------------------------------)

--

--

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:96:96/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_info--26f0fa89e1d1---------------------------------------)

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:128:128/1*D-F...