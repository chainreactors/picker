---
title: Sustainable Cloud Delivery
url: https://blogs.sap.com/2022/12/15/sustainable-cloud-delivery/
source: SAP Blogs
date: 2022-12-16
fetch_date: 2025-10-04T01:39:57.796587
---

# Sustainable Cloud Delivery

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Sustainable Cloud Delivery

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158653&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Sustainable Cloud Delivery](/t5/technology-blog-posts-by-sap/sustainable-cloud-delivery/ba-p/13552520)

![hannah_meierhofer](https://avatars.profile.sap.com/f/5/idf5161b3baf4e262a8df1ece20194abd5cc9a3c47f2c1543628ae80dd9d141bba_small.jpeg "hannah_meierhofer")

[hannah\_meierhofer](https://community.sap.com/t5/user/viewprofilepage/user-id/632173)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158653)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158653)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552520)

‎2022 Dec 15
10:31 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158653/tab/all-users "Click here to see who gave kudos to this post.")

745

* SAP Managed Tags
* [Cloud](https://community.sap.com/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)

* [Cloud

  Topic](/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)

View products (1)

![](/legacyfs/online/storage/blog_attachments/2022/12/295319_GettyImages-1384950048_small_jpg-1.jpg)

One thing I love about working in SAP’s (Global Cloud Services) Multicloud team is knowing that if I do my job well, I’m also having a positive impact on the environment. Why, you ask? Well, the more efficiently SAP runs its Cloud infrastructure on the hyperscalers (aka public cloud providers) the more sustainable our workloads are, and our team has influence on this through what we do. To be more precise: Cost and operational effectiveness equal sustainability in the Cloud. This is a win-win for everyone involved.

Not too long ago a large SAP customer reached out to ask if our team can determine the carbon footprint of their SAP workloads. In collaboration with our department’s Technology Office, one of my colleagues, Georgina, decided to start analyzing what data they can pull from the hyperscalers to get an idea of what the footprint of certain workloads looked like and if we could get more transparency into this. They pulled available data from Google Cloud Platform, pushed it into a database and did some data diving to understand what they could learn from the data. They also started researching what data Amazon Web Services and Microsoft Azure had on offer seeing how she could link it to SAP internal data sources to understand what SAP solutions were responsible for what part of the footprint.

After a while of researching this, the colleagues were asked to start driving this as an official project in collaboration with some data scientists from our sister team. Georgina and the team also got in touch with stakeholders across the organization with similar goals to understand the reporting requirements of these groups across the organization.

**Two Challenges in Gaining Carbon Footprint Transparency**

Georgina and the data scientists are faced with many challenges, but two stand out.

1. Granularity

An issue we are quite familiar with in dealing with 3 hyperscalers in our day to day is that each provider has their own way of doing things. It’s similar when it comes to data logic and structure, but also the granularity provided. One provider will provide information at service (say all VM’s in a region in an account for given month) level while another provides data at account level. There are only two ways to address this – one is to reach out to the hyperscalers and ask for better and more granular data sources, which we obviously did, but also to combine existing data with internal data to be able to drill down enough to get comparable data of our own.

2.  Multitenancy

Another issue is the multitenancy of Cloud in general. You often have many customers with workloads on a single Azure subscription or even many customers using one HANA database, which is a single resource in the Cloud, making measuring carbon footprint per customer guesswork. Some of this can be addressed with some effort which is currently being tackled.

For account level multitenancy, we have resource tagging. All hyperscalers offer customers the ability to tag resources with key/value pairs. This is one way to achieve transparency of carbon footprint at resource level. For HANA databases shared by a few customers, this isn’t as straight forward, but there are workarounds to approximate footprint data thus addressing multitenancy at resource level which we are exploring.

It is an adventure, and as the data pipelines are set up and reports and dashboards are created, and we start being able to slice and dice the data provided, a fuzzy picture of SAP’s carbon footprint in the Public Cloud space is emerging, and hopefully one day very soon we’ll be able to tell you more.

**Two Ways to Lower your Carbon Footprint in the Cloud**

We may not have full transparency yet, but there are still great ways to start working on this in your own environment now. And believe me, SAP leverages these methods even if we don’t have a full picture of their impact.

1. Region Strategy

The regions you choose to deploy to in the Cloud have an impact not only on latency and costs (some regions are closer to your customers lowering latency and others are less expensive), but also on your carbon footprint. Hyperscalers are starting to share information on the carbon intensity of their data centers in different regions. Google now has a little leaf next to the regions that are more carbon efficient and provides carbon intensity numbers in gm/kwh of services in their console for instance. Info from AWS is still emerging, but they suggest picking regions close to one of their renewable energy projects.

2.  Reduce Waste

Running efficiently is the name of the game. Unused or orphaned resources should be purged periodically. Cleaning up snapshots or other no longer needed artifacts not only reduces costs, but also carbon footprint. Another tactic is rightsizing your machines. Often when we don’t have transparency into how much compute, memory, or storage capacity we need we overprovision, but as we monitor our usage over time, we can reduce the amount provisioned and even automate the rightsizing process. Resource scheduling is also a way to reduce waste. If you know the traffic is only high on weekdays, you can often spin non-critical parts of the workload down on the weekend. All these ways to save money also add up to a lower carbon footprint overall.

When we think of IT, we often don’t immediately think of high carbon emissions like we do for tangible goods and services or industries like travel and mobility. Data centers, however, make up a lot of an IT company’s carbon footprint and that is why we want to find ways to run them more efficiently, i.e., in a more sustainable manner. Do you have any other ideas to share or thoughts on lowering data center carbon footprint? Let me know in the comments below.

Labels

* [Life at SAP](/t5/technology-blog-posts-by-sap/bg-p/techn...