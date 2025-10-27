---
title: Forums Refresh
url: https://www.kali.org/blog/forums-refresh/
source: Kali Linux
date: 2024-11-21
fetch_date: 2025-10-06T19:18:20.919744
---

# Forums Refresh

* [Join Free CTF](https://www.offsec.com/events/the-gauntlet/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* [Get Kali](https://www.kali.org/get-kali/)
* [Blog](https://www.kali.org/blog/)
* Documentation

  [Documentation Pages](https://www.kali.org/docs/)
  [Tools Documentation](https://www.kali.org/tools/)
  [Frequently Asked Questions](https://www.kali.org/faq/)
  [Known Issues](https://bugs.kali.org/search.php?project_id=1&category_id[]=General%20Bug&category_id[]=Kali%20Package%20Bug&category_id[]=Kali%20Package%20Improvement&status[]=30&status[]=40&status[]=50&sticky=on&sort=id%2Clast_updated&dir=DESC%2CDESC&hide_status=-2&match_type=0)
* Community

  [Community Support](https://www.kali.org/community/)
  [Forums](https://forums.kali.org/)
  [Discord](https://discord.kali.org/)
  [Join Newsletter](https://www.kali.org/newsletter/)
  [Mirror Location](https://http.kali.org/README?mirrorlist)
  [Get Involved](https://www.kali.org/docs/community/contribute/)
* [Courses](https://www.offsec.com/kali-training/courses/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* Developers

  [Git Repositories](https://gitlab.com/kalilinux)
  [Packages](https://pkg.kali.org/)
  [Auto Package Test](https://autopkgtest.kali.org/)
  [Bug Tracker](https://bugs.kali.org/)
  [Kali NetHunter Stats](https://nethunter.kali.org/)
* About

  [Kali Linux Overview](https://www.kali.org/features/)
  [Press Pack](https://gitlab.com/kalilinux/documentation/press-pack/-/archive/main/press-pack-main.zip)
  [Wallpapers](https://www.kali.org/wallpapers/)
  [Kali Swag Store](https://offsec.usa.dowlis.com/kali/view-all.html)
  [Meet The Kali Team](https://www.kali.org/about-us/)
  [Partnerships](https://www.kali.org/partnerships/)
  [Contact Us](https://www.kali.org/contact/)

LIGHT
[ ] DARK

![](https://www.kali.org/blog/forums-refresh/images/new-forums-discourse.jpg)
Wednesday, 20 November 2024

# Forums Refresh

Table of Contents

* [What a forum means to us](#what-a-forum-means-to-us)
* [Goodbye, vBulletin](#goodbye-vbulletin)
* [The search](#the-search)
* [Hello, Discourse](#hello-discourse)
* [Hope to see you soon](#hope-to-see-you-soon)

Over the past year we have been hard at work on refreshing the [Kali Forums](http://forums.kali.org/), and today we are proud to announce the official launch. We have taken what we have learnt over the ~~years~~ decades, and created a new home from scratch.

At the same time, we are welcoming a new team of community moderators who have been helping us over on [Discord](https://discord.kali.org/). Before you go check it out, lets first take a look at why we are doing this.

## What a forum means to us

Our forums have been a staple in [Kali’s long history](https://www.kali.org/blog/10-years/), spanning all the way back to before BackTrack. Then, **everything** was done through forums posting, including announcements, launching new projects like BackTrack, WHAX & Whoppix and their releases. They allowed like-minded individuals to create the foundation of a legacy that led to current day Kali.

The Internet and its culture has changed over time, which makes it difficult to put into perspective how influential forums were back then. For example, did you know that the [WPS Pixie-Dust attack](https://forums.kali.org/archived/showthread.php?24286-WPS-Pixie-Dust-Attack-(Offline-WPS-Attack)) originated from a forum posting?
Nowadays a large majority of people communicate through real-time chat services, like [Discord](https://discord.kali.org/). However, if the discussion about the Pixie-Dust attack occurred through real-time chat, who knows how wide spread this information would become. We view real-time chat as a good place for quick conversation, sharing initial ideas or assistance, and forums for longer term form content, such as guides/tutorials, status updates, items which commonly come up that can be referred back to. Both have their place, and we feel it is important to provide spaces for each.

|  | Forums | Real-Time Chat |
| --- | --- | --- |
| How to access | Web browser | Web browser/Dedicated client |
| Who can access | Anyone | Anyone |
| Discussion lifespan | Long | Short |
| How are they viewed | Archivable and searchable | Occasionally searchable |
| When discussions are had | At any point, with users able to join in when it suits them | In the moment, and users who are online are able to join in |

We always want to keep and maintain a forum for Kali, and make sure it is the best we can do.

To put it simply, without forums we would not have Kali.

## Goodbye, vBulletin

[![vBulletin](images/vbulletin.jpg)](https://www.kali.org/blog/forums-refresh/images/vbulletin.jpg)

vBulletin had been powering the forums since 2006 *(from the days of Remote-Exploit)*. For a long time this has worked great and provided our users a good platform to ask questions and give answers. However, we took a step back and saw that our setup was:

* Lacking quite a bit of modern functionality that other forums were offering.
* Not giving the same user experience and interface as our other end-user sites.
* Behind the scenes, we were spending more time doing certain tasks, as it was missing moderation tools that were needed.

With a recent wave of spam bots flooding the site, it was the kick we needed to finally find the time to look for solutions.

## The search

We knew from the start that there were a lot of options we could go with. We took the time to figure out what we need out of a forum and how we wanted our user experience to look. This helped us to narrow our options down to a few quality choices.

We were looking for something that has frequent updates, is secure, can integrate into our other sites, and can be customized to our liking. We spent a while weighing up the pros and cons of each, looking at examples of live environments and seeing what their communities look like. After examining our options, it became clear we needed to add another factor, self-hosting.

A question someone may be asking is why do we need to bother with all of this? Why not use something like Reddit , or some other similar service ? The issue with these options is that we do not control the site, and various rules can prevent us from using them how we would prefer to. So, we are back to looking for solutions that meet all our criteria.

XenForo and Discourse were in the lead. When left with XenForo versus Discourse, we felt like we could do well with either one. Unfortunately, XenForo does have a higher cost of entry for self-hosting. Had it not been for this, the competition would be much closer.

## Hello, Discourse

After taking a look at multiple possible forum solutions and what they bring to the table, we settled on [Discourse](https://www.discourse.org/). A popular free and open source software that is well maintained with a large active community. Along with the ability to utilize plugins, custom themes, and plenty of moderation features, we knew that this was what we wanted.

So, we got to work. We took the time to review what worked and did not work on our current forum and improved upon these ideas to create the best possible experience moving forward.
We finally created a theme that fits right along side [Kali.org](https://www.kali.org/), [Kali Docs](https://www.kali.org/docs/) and [Kali Tools](https://www.kali.org/tools/) and added features and applied various tweaks/modification to improve the user navigation and viewing experience.

Along with this, we also have a whole new team of moderators thanks to our lovely moderators on Discord.

[![Discourse](images/discourse.jpg)](https://www.kali.org/blog/forums-refresh/images/discourse.jpg)

You may be asking at this stage, what happens to the old forum posts? Are they going to stay around? Unfortunately, we will not be able to bring the old posts forward with us. The plan is to:

* Have the new Discourse running on at the same location as before, found at [forums.kali.org](https://forums.kali.org/)
* T...