---
title: Let's Clone a Cloner - Part 3: Putting It All Together
url: https://trustedsec.com/blog/lets-clone-a-cloner-part-3-putting-it-all-together
source: TrustedSec
date: 2025-08-01
fetch_date: 2025-10-07T00:48:24.060883
---

# Let's Clone a Cloner - Part 3: Putting It All Together

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Let's Clone a Cloner - Part 3: Putting It All Together](https://trustedsec.com/blog/lets-clone-a-cloner-part-3-putting-it-all-together)

July 31, 2025

# Let's Clone a Cloner - Part 3: Putting It All Together

Written by
Costa Petros

Hardware Security Assessment
Penetration Testing
Physical Security

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/CloneAClonerP3_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1753456253&s=18e62908db2ce86350f43bdd15e76e6f)

Table of contents

* [Laying Out the New Parts](#New)
* [Installing the Beeper (Speaker) Switch](#Installing)
* [Securing the Battery](#Battery)
* [Securing the ESP RFID Tool and PD Triggers](#Securing)
* [Final Component Layout](#Layout)
* [Final Setup](#set)
* [Pupa Range Test](#Test)
* [Results (and Failures) of Live Testing](#Results)
* [Speaking of Shielding - Does it Work?](#Shielding)
* [Final R&D](#final)
* [Final Wrap-Up and Bill of Materials](#wrapup)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#ecd39f998e86898f98d1af84898f87c9dedc839998c9dedc9884859fc9dedc8d9e98858f8089c9dedc8a9e8381c9dedcb89e999f988988bf898fc9deddca8d819cd78e838895d1a08998c9dedb9fc9dedcaf80838289c9dedc8dc9dedcaf808382899ec9dedcc1c9dedcbc8d9e98c9dedcdfc9dfadc9dedcbc99989885828bc9dedca598c9dedcad8080c9dedcb8838b899884899ec9dfadc9dedc8498989c9fc9dfadc9deaac9deaa989e999f9889889f898fc28f8381c9deaa8e80838bc9deaa8089989fc18f80838289c18dc18f808382899ec19c8d9e98c1dfc19c99989885828bc18598c18d8080c198838b899884899e "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flets-clone-a-cloner-part-3-putting-it-all-together "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Let%27s%20Clone%20a%20Cloner%20-%20Part%203%3A%20Putting%20It%20All%20Together%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Flets-clone-a-cloner-part-3-putting-it-all-together "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flets-clone-a-cloner-part-3-putting-it-all-together&mini=true "Share on LinkedIn")

We have arrived at our final stage of metamorphosis, taking our pupa and morphing it into a hacking machine. Let's finish this journey.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/ClonerPart3_Costa/Fig01a_Costa_Cloner3.jpg?w=320&q=90&auto=format&fit=max&dm=1753731220&s=3cdd1faa9e23d35ceda916fd65a5134b)

Geared Up Pupa

In the first [blog](https://trustedsec.com/blog/lets-clone-a-cloner-to-meet-my-needs), we took various MaxiProx builds and attempted to build one for ourselves, dipping our toes into the hardware hacking pond. In the second [blog](https://trustedsec.com/blog/lets-clone-a-cloner-part-2-you-have-no-power-here), we had to redesign our initial build to fix some power issues to get the range that we were expecting. In this final blog, we will neatly package up all the components into a mobile MaxiProx, test it out, and make a few more adjustments, if needed.

## Laying Out the New Parts

As this battery pack is much larger, I must rethink how I am going to internally arrange the components within the MaxiProx. One thing to note is that since the ESP RFID Tool is going to be powered from a separate USB port, I don’t need the Power Buck module, so I took that out and replaced it with the spare PD trigger that I had. This way, when I do place the battery in the MaxiProx, it will all fit.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/ClonerPart3_Costa/Fig02_Costa_Cloner3.png?w=320&q=90&auto=format&fit=max&dm=1753467488&s=f01ca74b5d13cd0f3924d55b37f88456)

100W Battery Hookup

With all of the components in the MaxiProx, it will look something like this:

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/ClonerPart3_Costa/Fig03a_Costa_Cloner3.jpg?w=320&q=90&auto=format&fit=max&dm=1753468036&s=12893fb4c8389916d5ecc738a4293b21)

New Parts Layout

## Installing the Beeper (Speaker) Switch

Before I mark where all the components will go, I want to circle back to the little beeper, or speaker, that I want to control with an on/off switch. The main reason for the kill switch is not to enable the beeper for testing, but to ensure that the beeper is off during an assessment. The first step is to remove the logic board from the MaxiProx so we can access the soldering points needed.

I will be soldering, so I need to think about safety. Always remember that solder fumes can be dangerous, so make sure that there is plenty of ventilation or make sure you are in a large room. Th...