---
title: SAP Community meets e-ink display: an RSS story
url: https://blogs.sap.com/2023/01/22/sap-community-meets-e-ink-display-an-rss-story/
source: SAP Blogs
date: 2023-01-23
fetch_date: 2025-10-04T04:35:43.150610
---

# SAP Community meets e-ink display: an RSS story

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Welcome Corner](/t5/welcome-corner/gh-p/welcome-corner)
* [Blog Posts](/t5/welcome-corner-blog-posts/bg-p/welcome-cornerblog-board)
* SAP Community meets e-ink display: an RSS story

Welcome Corner Blog Posts

Go a little bit deeper into the Welcome Corner with blog posts. Learn how to get started in SAP Community and get tips on maximizing your participation.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/welcome-cornerblog-board/article-id/36028&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Community meets e-ink display: an RSS story](/t5/welcome-corner-blog-posts/sap-community-meets-e-ink-display-an-rss-story/ba-p/13548462)

![ajmaradiaga](https://avatars.profile.sap.com/b/f/idbf9c7e7bec7d4fb5e87726eeb695bd40061688b3db602601682d6c4c7b907dbc_small.jpeg "ajmaradiaga")

![Developer Advocate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Developer Advocate")
[ajmaradiaga](https://community.sap.com/t5/user/viewprofilepage/user-id/107)

Developer Advocate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=welcome-cornerblog-board&message.id=36028)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/welcome-cornerblog-board/article-id/36028)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548462)

‎2023 Jan 22
9:28 PM

[12
Kudos](/t5/kudos/messagepage/board-id/welcome-cornerblog-board/message-id/36028/tab/all-users "Click here to see who gave kudos to this post.")

2,073

* SAP Managed Tags
* [API](https://community.sap.com/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)
* [Python](https://community.sap.com/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)
* [SAP Community](https://community.sap.com/t5/c-khhcw49343/SAP%2520Community/pd-p/486157991894093153608181816584982)

* [SAP Community

  Topic](/t5/c-khhcw49343/SAP%2BCommunity/pd-p/486157991894093153608181816584982)
* [API

  Programming Tool](/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)
* [Python

  Programming Tool](/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)

View products (3)

*In this blog post, I will share a project that I worked on during the X-mas break. The project involves a Raspberry Pi, an [e-ink display](https://www.waveshare.com/product/pico-epaper-7.5-b.htm), the SAP Community RSS (***R**eally **S**imple **S**yndication*) feed (<https://blogs.sap.com/feed/>), some python ![:snake:](/html/@198D7BD5D723BCAA7656EC38F4ABA958/emoticons/1f40d.png ":snake:"), and even a 3D printer.*

![](/legacyfs/online/storage/blog_attachments/2023/01/device.jpg)

SAP Community blog posts feed in e-ink display

I personally love RSS. For me, there isn't a better way to be informed of what's going on on my preferred websites/blogs than by reading the RSS entries on my favourite feed reader - [Miniflux](https://miniflux.app/) (of course [self-hosted](https://blogs.sap.com/2021/03/24/running-sap-hana-express-edition-vm-in-unraid-os/) :-).
> **RSS** (**RDF Site Summary** or **Really Simple Syndication**) is a [web feed](https://en.wikipedia.org/wiki/Web_feed "Web feed") that allows users and applications to access updates to websites in a [standardized](https://en.wikipedia.org/wiki/Standardization "Standardization"), computer-readable format. Subscribing to RSS feeds can allow a user to keep track of many different websites in a single [news aggregator](https://en.wikipedia.org/wiki/News_aggregator "News aggregator"), which constantly monitor sites for new content, removing the need for the user to manually check them. Source: [Wikipedia](https://en.wikipedia.org/wiki/RSS).

I remember fondly the days when every single website published an RSS feed and it was simple to subscribe to them. [Google Reader](https://en.wikipedia.org/wiki/Google_Reader) was the most popular feed reader at that time until big G decided [to kill the product](https://www.forbes.com/sites/tristanlouis/2013/06/29/google-kills-reader-helps-rss/?sh=6cf4be6b47d1). A sad day, if you ask me. Unfortunately, RSS lost some momentum when this happened and its adoption slowed down significantly. That said, there are still many websites that publish an RSS feed. In some websites, you'll find a link/icon to the RSS feed visible in the UI but I would say that most have it somewhat hidden/not that accessible. I found myself going to the source of the web page (*Right click > Web Page source*) to find a link to the RSS feed. You'll normally find it in the head section of the HTML.

![](/legacyfs/online/storage/blog_attachments/2023/01/rss-feed.png)

SAP Community - RSS feed link

As you can imagine, I'm subscribed to the SAP Community blogs section RSS feed. This is to learn from what other members of the community share/write about. Now, whenever I want to know what's happening in SAP Community, I go to my feed reader and select the SAP Community feed and I can see all the blog posts published since the last time I checked my feed.
> There is a lot going on in SAP Community and it is possible to filter your feed by you favourite tag, e.g. SAP Buiness Technology Platform - [https://content.services.sap.com/feed?type=blogpost&tags=8077228b-f0b1-4176-ad1b-61a78d61a847&title=...](https://content.services.sap.com/feed?type=blogpost&tags=8077228b-f0b1-4176-ad1b-61a78d61a847&title=Latest%20blog%20posts%20for%20SAP%20Business%20Technology%20Platform). To get a topic feed go to to <https://blogs.sap.com>, select a tag you are interested and copy the link from the RSS link that's in the header.

I'm able to read the entries on Miniflux but I was thinking if there was a way to consume the feed in a passive way and not have to go and check a website. Enter an e-ink display.

## e-ink display

![](/legacyfs/online/storage/blog_attachments/2023/01/prototype.jpg)

Prototype - Raspberry Pi inside the cardboard box

I do most of my reading on an e-ink device (Kindle). I've had a couple and have always enjoy the experience of reading on an e-ink display. Unfortunately, there is no SDK for the device so it is not possible to create an app/program to extend its capabilities. That said, I've always wanted to play with an e-ink display but I just never had a nice little project to justify buying one.

Given my new "want" to check the feed in a passive way, I thought it will be cool to use an e-ink display to keep me informed of what's going on in SAP Community. Obviously, some coding is required to display something on the display which add to the fun of the project.

The e-ink display that I got for my project is a Waveshare - [7.5inch E-Paper E-Ink Display Module (B) for Raspberry Pi Pico, 800×480, Red / Black / White](https://www.waveshare.com/product/pico-epaper-7.5-b.htm). Its size is similar to a photo frame, so it will easily be on my desk (yes, I also have a photo of my family on my desk ![:red_heart:](/html/@2530077551F6C762AF3386C1A5B65988/emoticons/2764.png ":red_heart:")). Waveshare has a library that allows you to interact with the display from different programming languages. This is available on their public repo,  [waveshare](https://github.com/waveshare)  /  **[e-Paper](https://github.com/waveshare/e-Paper)**, and it contains many examples of how you can use the display. Let's look at some code now.

...