---
title: Mastodonic growing pains
url: https://blogs.sap.com/2022/12/05/mastodonic-growing-pains/
source: SAP Blogs
date: 2022-12-06
fetch_date: 2025-10-04T00:34:25.217630
---

# Mastodonic growing pains

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Sustainability](/t5/sustainability/gh-p/sustainability)
* [Blog Posts](/t5/sustainability-blog-posts/bg-p/sustainabilityblog-board)
* Mastodonic growing pains

Sustainability Blog Posts

Delve into SAP sustainability blogs. Gain insights into tech-driven sustainable practices and contribute to a greener future for businesses and the planet.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/sustainabilityblog-board/article-id/1719&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Mastodonic growing pains](/t5/sustainability-blog-posts/mastodonic-growing-pains/ba-p/13567812)

![JimSpath](https://avatars.profile.sap.com/1/9/id19e0902ffb151e54856445a6cc9bb1df4e8202ab913d64c6e2e2d8625cd7bf0a_small.jpeg "JimSpath")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[JimSpath](https://community.sap.com/t5/user/viewprofilepage/user-id/184)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=sustainabilityblog-board&message.id=1719)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/sustainabilityblog-board/article-id/1719)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567812)

‎2022 Dec 05
7:24 PM

[3
Kudos](/t5/kudos/messagepage/board-id/sustainabilityblog-board/message-id/1719/tab/all-users "Click here to see who gave kudos to this post.")

623

* SAP Managed Tags
* [Corporate Social Responsibility](https://community.sap.com/t5/c-khhcw49343/Corporate%2520Social%2520Responsibility/pd-p/611794787045402236540598973198809)

* [Corporate Social Responsibility

  Topic](/t5/c-khhcw49343/Corporate%2BSocial%2BResponsibility/pd-p/611794787045402236540598973198809)

View products (1)

Social media took a turn in 2022 as the Twitter Co. takeover motivated many to bail; my personal journey up to barely a week ago is here: [blogs.sap.com/2022/11/25/my-mastodon-pack-and-go-journey/](https://blogs.sap.com/2022/11/25/my-mastodon-pack-and-go-journey/) When I noted that user and traffic counts were increasing rapidly, I also viewed the volunteer hosts and moderators as key to having Mastodon succeed. This tale is about network "attacks" over this past weekend, and exemplary response along with community evolution (like being a gangly teen-ager going out into the "real world.).

With the 4.x upgrade, I saw cache delays, mysterious error messages, etc. The instance I'm inhabiting has since stopped new account creation, up-scaled system resources, and limited public response efforts to limited daily hours.

So it might be difficult to distinguish slow response time causes to ongoing tuning (on purpose), or actions by nefarious entities to disrupt operations through exploits. One instance manager noted they went from a handful of users to tens of thousands in just a few weeks.

## ONE

Scrolling through different timelines I noticed an alert about troll accounts causing or having caused interruptions to service though a form of escalating connection or transaction attempts. Without knowing how this was crafted or when, the community information sharing helped to clarify the situation.

[https://chaos.social/@ruud@mastodon.world/109449235621264631](https://chaos.social/%40ruud%40mastodon.world/109449235621264631)

```
To all Mastodon-admins:

 seems like there's an attack on all instances by troll accounts.
```

```
[ Dec 03, 2022, 05:19 · Edited Dec 03, 05:58 ]
```

Responses to this thread had good information with minimal speculation, and at least one workaround to the perceived denial of service attacks was by filtering (quicker and easier than code changes). I may need to revisit block lists another time as this social link aspect is secondary to rapid software change management but not unconnected.

An immediate result of new overload conditions is sometimes too hasty changes, or incorrect fault analysis. I noticed the result of one "block this site/sites" with a pleading for acting carefully.

*/ Mail us at [] with spamming or otherwise malicious instances and we'll take care of them. /*

As the Mastodon instance and user base grows, the relative closeness of one operator to another gets farther away. My observation is there are a lot of people dedicated to making this work.

## TWO

Code fix ideas showed up within hours. The suspected root cause of the vulnerability was surmised based on the symptoms. Collaborators found patterns in the source sites.

[https://chaos.social/@analog\_cafe@mas.to/109451039766034001](https://chaos.social/%40analog_cafe%40mas.to/109451039766034001)

```
[Dec 03, 2022, 12:58]
```

<https://github.com/mastodon/mastodon/issues/21977>

```
Any idea to stop activitypub-troll.cf or likewise attacks?
```

## THREE

Ongoing (as I post this) "transports". The code blocks with weaknesses in bounds checking have already been committed to both the 4.x and 3.x trees (if I read the GIT repository correctly).

<https://github.com/mastodon/mastodon/pull/22025>

```
Fix unbounded recursion in account discovery
```

Meanwhile, preventing or mitigating future issues comes back up again.

[https://chaos.social/@jerry@infosec.exchange/109452233436890369](https://chaos.social/%40jerry%40infosec.exchange/109452233436890369)

```
I can see a need for a coordination/alerting capability for security threats, vulnerability notices, and so on.
```

[Dec 03, 2022, 18:02]

This is where open source software shines, and where it can be tempestuous. By sharing fixes in the open to a wide audience, many reviews and suggestions can happen quickly. On the other hand, our nemeses see the holes being plugged and can scheme to move elsewhere or try another approach. We always need to succeed, it's sense, while they can continue to fail but succeed once and "win."

### What next?

For me, the first change is I feel I am posting less than I would, in order not to contribute to a tidal wave during a time operators are doing their best to analyze and tune performance. I'll note the most recent publication from the [chaos.social](https://chaos.social/) team:

<https://leah.is/posts/scaling-the-mastodon/>

Having scaling issues arise coincidentally just after one has documented how to scale for the already past reality must be *Sisyphean*.

In related discussions, I found a migration tool that displays more context of your prior followers/following that have advertised their migration status. Even better, there is a toggle to hide those already being followed, to avoid wasted effort ("wait, am I following them or not? I thought I was). Minor defect is still showing some whom I've asked asked but not been approved yet.

#### Past notes:

* [https://blogs.sap.com/2022/11/07/is-it-time-to-join-the-elephant-parade-or-what-is-this-mastodon-doi...](https://blogs.sap.com/2022/11/07/is-it-time-to-join-the-elephant-parade-or-what-is-this-mastodon-doing-in-my-web/)

* <https://blogs.sap.com/2022/11/12/second-thoughts-on-the-great-mastodon-migration/>

* <https://blogs.sap.com/2022/11/25/my-mastodon-pack-and-go-journey/>

##### Another view:

* [https://absolutelymaybe.plos.org/2022/12/05/mastodon-growth-numbers-might-not-mean-what-you-think-th...](https://absolutelymaybe.plos.org/2022/12/05/mastodon-growth-numbers-might-not-mean-what-you-think-they-mean/)

* [code vulnerability anal...