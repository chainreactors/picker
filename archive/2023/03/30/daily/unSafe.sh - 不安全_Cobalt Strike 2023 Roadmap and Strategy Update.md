---
title: Cobalt Strike 2023 Roadmap and Strategy Update
url: https://buaq.net/go-155980.html
source: unSafe.sh - 不安全
date: 2023-03-30
fetch_date: 2025-10-04T11:05:56.427908
---

# Cobalt Strike 2023 Roadmap and Strategy Update

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Cobalt Strike 2023 Roadmap and Strategy Update

I blogged about the Cobalt Strike roadmap in March last year and while the fundamental tenets o
*2023-3-29 22:48:18
Author: [www.cobaltstrike.com(查看原文)](/jump-155980.htm)
阅读量:43
收藏*

---

I blogged about the Cobalt Strike roadmap [in March last year](https://www.cobaltstrike.com/blog/cobalt-strike-roadmap-update/) and while the fundamental tenets of our approach to R&D remain unaltered, a lot has changed behind the scenes over the past year or so. I try to engage with our customers on various platforms and over the past few months, I’ve been asked a lot of questions about our roadmap. My hope is that this blog post will help to answer some of those questions. As we have some major changes planned for the next 12-18 months, I’d like to spend a little time providing some insights into the current state of Cobalt Strike R&D as well as offering some transparency about our plans for 2023 and beyond.

### Cobalt Strike R&D Team

I mentioned in the roadmap update last year that we were planning on expanding the size of the R&D team. Over the past 12 months we have more than doubled the size of the team. We have added experienced software engineers to the core development team and built a research team that is dedicated to driving the product forward.

One of our more recent hires, [William Burgess](https://twitter.com/joehowwolf), is leading our research team. He will be playing a key role in shaping the future direction of the product, bringing his extensive experience in developing security tools to bear. A key part of his role is to provide technical guidance and help to define priorities for both research activities and main product releases. In addition to this, he will also be conducting his own research activities. He recently released [a blog post on spoofing call stacks dynamically with timers](https://www.cobaltstrike.com/blog/behind-the-mask-spoofing-call-stacks-dynamically-with-timers/) and already has others in the pipeline.

[Henri Nurmi](https://twitter.com/HenriNurmi) is another recent hire and he brings both extensive red teaming and software engineering experience to the team. Henri was behind the token store change in the 4.8 release (which was an update on the version that he submitted to the Community Kit a while ago!). In addition to his work on the core product, Henri has also been working on several other items that we’ll eventually be releasing into the Arsenal Kit and blogging about. [Jean-François Maes](https://twitter.com/Jean_Maes_1994) has been a team member for quite some time and while he is currently focussing on updating and improving our training material (as a certified SANS instructor, this is definitely in his wheelhouse) he is also continuing to perform research activities.

Several other new (and older) team members prefer to keep a lower public profile but are nonetheless helping to drive development of the core product, contribute to research, update product security and more. A recent example of this was the [first post in a series revisiting the User-Defined Reflective Loader (UDRL)](https://www.cobaltstrike.com/blog/revisiting-the-udrl-part-1-simplifying-development/) that accompanied a new addition to the Arsenal Kit.

It has taken a while to hire the team that we were looking for and build up some momentum on associated R&D tasks, but I feel that we’re in a really good place now. We are cognisant of the fact that we have customers with a wide range of expertise and skill levels and I feel we are now better able to cater to the needs of our customers. Things were relatively quiet while that was playing out but you can now expect to see more output on the blog, more tools in the Arsenal Kit, and more cutting-edge features in the main product releases. Fortra continues to invest in Cobalt Strike and I’m grateful for the support from our leadership team.

### Collaboration

The Cobalt Strike R&D team is part of a wider team that we are actively collaborating with on multiple fronts. [Fortra acquired Outflank](https://www.fortra.com/resources/press-releases/helpsystems-acquires-outflank) in September last year and the two teams are working closely together, collaborating on research topics and looking at ways in which we can improve the interoperability between Cobalt Strike and [Outflank’s OST](https://outflank.nl/services/outflank-security-tooling/). Users can benefit from the new [Cobalt Strike/OST bundle](https://www.cobaltstrike.com/core-impact/offensive-security-bundles/red-team-datasheet/) and leverage tools within OST to help with their engagements.

We also work closely on research topics with the [Core Security](https://www.coresecurity.com/core-labs) team. Some members of the [Core Impact research team](https://www.coresecurity.com/products/core-impact) also work on Cobalt Strike research items and both teams look at ways to improve the [interoperability between the products](https://www.coresecurity.com/blog/interoperability-cobalt-strike-and-other-notable-new-features-core-impact-203). We are also lucky enough to work alongside and collaborate closely with [other members of the wider Core Security team](https://www.coresecurity.com/blog) such as [Santiago Pecin](https://twitter.com/s4ntiago_p), as well as exploit writers and other red teams and penetration testing teams across Fortra.

There is a huge array of talent right across the Offensive Security department within Fortra and we are all pulling in the same direction. It has taken a while to get this all ramped up but you will now start to see the benefits of this work – especially customers that own other offensive security products from Fortra (OST/Core Impact) in addition to Cobalt Strike.

### Flexibility And Stability

The recent customer survey (thank you to everyone that responded) affirmed our belief that stability and flexibility are key features of the product and are very much something that our users value. They are the core tenets of our development philosophy and play a key role in our releases.

Cobalt Strike’s strategy around evasion has always been “evasion through flexibility” meaning that we want to provide you with tools that you can use to modify default behaviours. This approach was something that Raphael Mudge pioneered with the Artifact and Resource kits and is something that we continue to support via the Arsenal Kit. It is important for us to address the concerns of our customers and we are aware that “evasion through flexibility” only works when there is enough documentation and example code to simplify modifications to the tools that we provide. This was one of the reasons behind the UDRL-VS that we recently released into the Arsenal Kit. In addition to this, we will also continue to update the tools available in the Arsenal Kit – for example, [the evasive changes made to the Sleep Mask Kit in the 4.8 release](https://www.cobaltstrike.com/blog/cobalt-strike-4-8-system-call-me-maybe/).

We are also acutely aware that Cobalt Strike’s Beacon has been widely signatured in recent years. We have a blog post coming out in the next week or two which will help address some of these concerns and we will continue to review this in future. Ultimately, I have every confidence that our research team will continue to ease the burden on our users with these efforts.

The focus on flexibility is also a key reason for the infrequent releases. As I mentioned, our users have told us that they want fewer releases to give them more time to test the product before putting it into service – due at least in part to the fact that we give them the...