---
title: Cobalt Strike 2023 Roadmap and Strategy Update
url: https://www.cobaltstrike.com/blog/cobalt-strike-2023-roadmap-and-strategy-update/
source: Cobalt Strike Research and Development
date: 2023-03-30
fetch_date: 2025-10-04T11:09:22.974076
---

# Cobalt Strike 2023 Roadmap and Strategy Update

[Skip to content](#content)

[![Fortra](https://static.fortra.com/fortra-global-assets/fortra-logo-full.svg)
![fortra mobile logo](https://www.cobaltstrike.com/app/themes/helpsystems/img/fortra-delta-white.svg)

![Cobalt Strike](https://www.cobaltstrike.com/app/uploads/2023/06/fta-cobalt-strike-light-1.svg)](https://www.cobaltstrike.com/)

* [Fortra.com](https://www.fortra.com/?utm_source=coresecurity.com&utm_medium=referral&utm_campaign=fortra_secondarynav_link "Fortra.com")
* [Blog](/blog "Blog")
* [Download](https://download.cobaltstrike.com/download "Download")
* [Contact Us](/contact-us "Contact Us")

## Main Navigation

* [REQUEST PRICING](/product/quote-request "REQUEST PRICING")
* [Product](/product "Product")
  + Features
    - [Beacon](https://www.cobaltstrike.com/product/features/beacon "Beacon")
    - [Malleable C2](https://www.cobaltstrike.com/product/features/malleable-c2 "Malleable C2")
    - [Interoperability](https://www.cobaltstrike.com/product/features/interoperability "Interoperability")
    - [Community](https://www.cobaltstrike.com/product/features/community "Community")
    - [Flexibility](https://www.cobaltstrike.com/product/features/flexibility "Flexibility")
    - [UDRL](https://www.cobaltstrike.com/product/features/user-defined-reflective-loader "UDRL")
    - [View More Features >](/product/features/ "View More Features >")
  + Interoperability
    - [Core Impact](https://www.cobaltstrike.com/product/core-impact "Core Impact")
    - [Outflank Security Tooling](https://www.cobaltstrike.com/product/outflank-security-tooling "Outflank Security Tooling")
  + Bundles
    - [Cobalt Strike + Core Impact](/resources/datasheets/advanced-bundle/ "Cobalt Strike + Core Impact")
    - [Cobalt Strike + Outflank Security Tooling](/resources/datasheets/red-team-bundle/ "Cobalt Strike + Outflank Security Tooling")
    - [Cobalt Strike, Core Impact, Outflank Security Tooling](/resources/datasheets/advanced-red-team-bundle/ "Cobalt Strike, Core Impact, Outflank Security Tooling")
    - [View All Product Bundles >](/product/bundles/ "View All Product Bundles >")
* [Industry](https://www.cobaltstrike.com/industry "Industry")
  + [Finance](https://www.cobaltstrike.com/industry/finance "Finance")
  + [Healthcare](https://www.cobaltstrike.com/industry/healthcare "Healthcare")
  + [Government & Public Sector](https://www.cobaltstrike.com/industry/government "Government & Public Sector ")
* [Support](/support "Support")
  + [Training](https://www.cobaltstrike.com/support/training "Training")
  + [User Manuals](https://www.cobaltstrike.com/support/user-manuals "User Manuals")
  + [Community Kit](https://cobalt-strike.github.io/community_kit/ "Community Kit")
* [Resources](/resources "Resources")
  + [Blog](/blog "Blog")
  + [Screenshots](https://www.cobaltstrike.com/resources/screenshots "Screenshots")
  + [Datasheets](/resources/type-datasheet "Datasheets")
  + [Videos](/resources/type-video "Videos")
  + [Events and Webinars](/resources/type-upcoming-event "Events and Webinars")
* [Search](#collapseSearch)

Search for:

[Home](https://www.cobaltstrike.com/) » [Blog](/blog/) » Cobalt Strike 2023 Roadmap and Strategy Update

# Cobalt Strike 2023 Roadmap and Strategy Update

I blogged about the Cobalt Strike roadmap [in March last year](https://www.cobaltstrike.com/blog/cobalt-strike-roadmap-update/) and while the fundamental tenets of our approach to R&D remain unaltered, a lot has changed behind the scenes over the past year or so. I try to engage with our customers on various platforms and over the past few months, I’ve been asked a lot of questions about our roadmap. My hope is that this blog post will help to answer some of those questions. As we have some major changes planned for the next 12-18 months, I’d like to spend a little time providing some insights into the current state of Cobalt Strike R&D as well as offering some transparency about our plans for 2023 and beyond.

### Cobalt Strike R&D Team

I mentioned in the roadmap update last year that we were planning on expanding the size of the R&D team. Over the past 12 months we have more than doubled the size of the team. We have added experienced software engineers to the core development team and built a research team that is dedicated to driving the product forward.

One of our more recent hires, [William Burgess](https://twitter.com/joehowwolf), is leading our research team. He will be playing a key role in shaping the future direction of the product, bringing his extensive experience in developing security tools to bear. A key part of his role is to provide technical guidance and help to define priorities for both research activities and main product releases. In addition to this, he will also be conducting his own research activities. He recently released [a blog post on spoofing call stacks dynamically with timers](https://www.cobaltstrike.com/blog/behind-the-mask-spoofing-call-stacks-dynamically-with-timers/) and already has others in the pipeline.

[Henri Nurmi](https://twitter.com/HenriNurmi) is another recent hire and he brings both extensive red teaming and software engineering experience to the team. Henri was behind the token store change in the 4.8 release (which was an update on the version that he submitted to the Community Kit a while ago!). In addition to his work on the core product, Henri has also been working on several other items that we’ll eventually be releasing into the Arsenal Kit and blogging about. [Jean-François Maes](https://twitter.com/Jean_Maes_1994) has been a team member for quite some time and while he is currently focussing on updating and improving our training material (as a certified SANS instructor, this is definitely in his wheelhouse) he is also continuing to perform research activities.

Several other new (and older) team members prefer to keep a lower public profile but are nonetheless helping to drive development of the core product, contribute to research, update product security and more. A recent example of this was the [first post in a series revisiting the User-Defined Reflective Loader (UDRL)](https://www.cobaltstrike.com/blog/revisiting-the-udrl-part-1-simplifying-development/) that accompanied a new addition to the Arsenal Kit.

It has taken a while to hire the team that we were looking for and build up some momentum on associated R&D tasks, but I feel that we’re in a really good place now. We are cognisant of the fact that we have customers with a wide range of expertise and skill levels and I feel we are now better able to cater to the needs of our customers. Things were relatively quiet while that was playing out but you can now expect to see more output on the blog, more tools in the Arsenal Kit, and more cutting-edge features in the main product releases. Fortra continues to invest in Cobalt Strike and I’m grateful for the support from our leadership team.

### Collaboration

The Cobalt Strike R&D team is part of a wider team that we are actively collaborating with on multiple fronts. [Fortra acquired Outflank](https://www.fortra.com/resources/press-releases/helpsystems-acquires-outflank) in September last year and the two teams are working closely together, collaborating on research topics and looking at ways in which we can improve the interoperability between Cobalt Strike and [Outflank’s OST](https://outflank.nl/services/outflank-security-tooling/). Users can benefit from the new [Cobalt Strike/OST bundle](https://www.cobaltstrike.com/core-impact/offensive-security-bundles/red-team-datasheet/) and leverage tools within OST to help with their engagements.

We also work closely on research topics with the [Core Security](https://www.coresecurity.com/core-labs) team. Some members of the [Core Impact research team](https://www.coresecurity.com/products/core-impact) also work on Cobalt Strike research items and both teams look at ways to improve the [interoperability between the products](https://www.coresecurity.com/blog/interope...