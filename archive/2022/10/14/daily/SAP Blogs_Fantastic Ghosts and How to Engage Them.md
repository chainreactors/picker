---
title: Fantastic Ghosts and How to Engage Them
url: https://blogs.sap.com/2022/10/13/fantastic-ghosts-and-how-to-engage-them/
source: SAP Blogs
date: 2022-10-14
fetch_date: 2025-10-03T19:49:39.158699
---

# Fantastic Ghosts and How to Engage Them

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)
* Fantastic Ghosts and How to Engage Them

CRM and CX Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-sap/article-id/12699&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Fantastic Ghosts and How to Engage Them](/t5/crm-and-cx-blog-posts-by-sap/fantastic-ghosts-and-how-to-engage-them/ba-p/13541293)

![eddiebautista](https://avatars.profile.sap.com/a/d/idad284eae8fbd5ea31936abe63e61d93e6c54915f0f89718aae54aa39e14a8f5f_small.jpeg "eddiebautista")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[eddiebautista](https://community.sap.com/t5/user/viewprofilepage/user-id/37999)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-sap&message.id=12699)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-sap/article-id/12699)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13541293)

‎2022 Oct 13
10:33 PM

[6
Kudos](/t5/kudos/messagepage/board-id/crm-blog-sap/message-id/12699/tab/all-users "Click here to see who gave kudos to this post.")

4,257

* SAP Managed Tags
* [SAP Customer Data Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Customer%2520Data%2520Cloud/pd-p/73555000100800001231)
* [SAP Customer Data Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Customer%2520Data%2520Platform/pd-p/73554900100800002991)

* [SAP Customer Data Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BCustomer%2BData%2BCloud/pd-p/73555000100800001231)
* [SAP Customer Data Platform

  Software Product](/t5/c-khhcw49343/SAP%2BCustomer%2BData%2BPlatform/pd-p/73554900100800002991)

View products (2)

The writing in the book was the first sign; the voices we heard were the second.  Although we had an idea of the kind of ghost we were facing, we were killed as soon as the lights went out.

According to [Phasmophobia](https://kineticgames.co.uk/), the psychological PC game my friends and I were playing, the ghost was a Mare and not the Spirit we had assumed. Mares, as it turns out, hate the light and like to hunt in the dark.

![](/legacyfs/online/storage/blog_attachments/2022/10/phasmophobia-butcher.jpg)

Phasmophobia: Progressive profiling gone wrong

It’s a costly, yet common enough error to make in a game that challenges players to identify ghosts based on their unique attributes and paranormal behaviors demonstrated while haunting various locations.

I’m a paranormal investigator at night and an SAP functional consultant during the day, but recently the two roles have started feeling eerily similar. In both my virtual and real-life occupations, I work with people who want to leverage services that make it easier to learn more about their visitors. And the game's core concepts of centralizing the capturing, segmenting and activating data are highlights of my customer conversations.

What I realized is that Phasmophobia has a whole lot in common with [SAP Customer Data Platform](https://www.sap.com/products/crm/customer-data-platform.html) (or CDP for short)--a tool that businesses use for gaining customer insights--and can teach us lessons about improving the customer experience.

## The Book of Afterlife

Much like CDP, the player’s journal in Phasmophobia acts as a central repository for ghost information, activities and behaviors that help identify the type of ghost and determine what appropriate actions the player should take next. While the data transferred from sources (haunted locations) to the journal is more of a manual transaction than what you’d typically set up with CDP and external databases, the key concept around activating the data collected is the same.

Here's an illustration of how the data flows from one system to the next and influences the actions taken:

![](/legacyfs/online/storage/blog_attachments/2022/10/phasmaphobia-architecture-1.png)

Phasmophobia architecture

## Paranormal Activity

Data can come from different sources in both CDP and Phasmophobia.

At the start of each assignment, players are given a small set of information about the ghost including their first and last name, the address or name of the house being haunted, and (sometimes) whether the ghost only responds if the player is alone.

From there, it's up to players to use the tools at their disposal such as thermometers, UV flashlights, and cameras to capture even more behavioral data within the haunted area. Understanding the kind of evidence available is key to each investigation.

Similarly, the first step in setting up CDP is data ingestion: using connectors, batch ingestion, and APIs to collect basic contact information and key events such as purchases, subscriptions and activities captured from multiple resources during a customer journey.

While players need not worry about setting up the ghost data model in the game, admins do need to create the customer schema and events that populate this data in CDP. I'd imagine a CDP configuration for Phasmophobia would look something like this:

![](/legacyfs/online/storage/blog_attachments/2022/10/Screen-Shot-2022-10-12-at-4.28.27-PM.png)

A spooky CDP schema

## I See Dead People

Establishing the data model in both CDP and Phasmophobia makes it easier to gain insights about customers or ghosts.

In CDP, administrators use two types of insights:

* [Activity Indicators](https://help.sap.com/docs/SAP_CUSTOMER_DATA_PLATFORM/8438f051ded544d2ba1303e67fc5ff86/bf9afd16cc2841dbb9eac8f5d42d3959.html?q=activity%20indicators&locale=en-US) - calculated or predictive fields based on customer activities

* [Segments](https://help.sap.com/docs/SAP_CUSTOMER_DATA_PLATFORM/8438f051ded544d2ba1303e67fc5ff86/07df802c92034afbb7c75039f60d76be.html?q=segments&locale=en-US) - categories of customers based on behaviors, activities and demographics

Both are strong tools for segmenting and learning more about customers.

In Phasmophobia, players have their handy journal, which is smart enough to automatically highlight potential ghost types based on evidence found during the investigation. For example, a ghost that leaves fingerprints and freezing room temperatures would likely be a Demon, Hantu, Jinn or a Mimic.

![](/legacyfs/online/storage/blog_attachments/2022/10/journal1-1.jpg)

Phasmophobia Journal: 10x smarter than a Rocketbook

While these basic mechanisms for segmentation and prediction are useful, I do see opportunities for the game developers to accelerate investigations by updating the journal with new CDP-like calculated fields that capture:

* the volume and frequency of ghost events

* the amount of player sanity lost after each ghost event

* the duration of a hunt

* the volume and frequency of objects thrown

## Ghost Whisperer

Once players gather enough information about ghosts (or customers), they're better equipped to engage them. Of course, what those engagements look like differ between the in-game objectives and typical CDP use cases (Ghosts aren't interested in email discounts and follow-up calls, for example.), but the central point is that enough information exists to take the next action....