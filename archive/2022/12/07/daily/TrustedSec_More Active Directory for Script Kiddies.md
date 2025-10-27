---
title: More Active Directory for Script Kiddies
url: https://www.trustedsec.com/blog/more-active-directory-for-script-kiddies/
source: TrustedSec
date: 2022-12-07
fetch_date: 2025-10-04T00:49:23.462619
---

# More Active Directory for Script Kiddies

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
* [More Active Directory for Script Kiddies](https://trustedsec.com/blog/more-active-directory-for-script-kiddies)

December 06, 2022

# More Active Directory for Script Kiddies

Written by
TrustedSec

Active Directory Security Review
Architecture Review
Research

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/MoreActiveDirectoryScriptKiddies_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695567317&s=3d6aa60092335d21ab70130933654af0)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#6d521e180f07080e19502e05080e06485f5d021819485f5d1905041e485f5d0c1f19040e0108485f5d0b1f0200485f5d391f181e1908093e080e485f5c4b0c001d560f0209145020021f08485f5d2c0e19041b08485f5d29041f080e19021f14485f5d0b021f485f5d3e0e1f041d19485f5d2604090904081e485e2c485f5d0519191d1e485e2c485f2b485f2b191f181e1908091e080e430e0200485f2b0f01020a485f2b00021f08400c0e19041b084009041f080e19021f14400b021f401e0e1f041d19400604090904081e "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmore-active-directory-for-script-kiddies "Share on Facebook")
* [Share on X](http://twitter.com/share?text=More%20Active%20Directory%20for%20Script%20Kiddies%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmore-active-directory-for-script-kiddies "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmore-active-directory-for-script-kiddies&mini=true "Share on LinkedIn")

## Introduction

*So… Active Directory is amazing. It tells me everything I want to know—a regular Ask Jeeves for the whole domain—but I’m sure there is more that it can do. What else am I missing?*

In a previous article, I described the Active Directory (AD) service and how a Script Kiddie might use it to enumerate a network to find interesting things. Please go back and review [Active Directory for Script Kiddies](https://trustedsec.com/blog/active-directory-for-script-kiddies) if you want all the details about AD, but basically, it is a directory service developed by Microsoft for Windows. It contains a database for mapping network services and resources, and it can be used for locating, managing, and administering a network. The directory service provides access and administration of all objects on a network. The AD service and database are maintained and replicated across domain servers, and access is provided via numerous utilities and APIs using the Lightweight Directory Access Protocol (LDAP).

Previously, I looked at how a Script Kiddie could use AD to enumerate a domain. As mentioned, there are numerous tools and APIs for accessing this information, but for the purpose of the article, I used the collection of PowerShell scripts called PowerSploit, which contains the module PowerView to access and query the AD database. I demonstrated how someone could list the domains and forests on the network and specific information about them. I also pointed out how to get information regarding users, computers, groups, and policies. Finally, I looked at some more specific information-gathering operations like getting the logged-on users, including the last logged on user, and hunting for specific users, shares, and files.

This time around, I will look at some further steps you can take using and abusing AD beyond just simple enumeration. I will cover some ways that you may be able to escalate privileges, and then I will look at possible lateral movement techniques and, finally, some persistence mechanisms. AD is more than just a source of information—it is a source of power.

## Escalation

*Now that I have enumerated the heck out of this network, how do I take it to the next level? Specifically, how do I get r00t?*

The first step in any penetration test is enumeration. You need to examine the environment to figure out where you are and where you want to go. The next step is typically escalation. Being able to poke around is fun, but you can only go so far as a regular user. You need the power of the Dark Side (or at least Administrator/SYSTEM) to really do anything fun. Into this quandary steps our new friend AD.

There are numerous methods for escalating privileges. You can look for missing patches and corresponding exploits. You could attempt to do some password mining by looking in memory, log files, the registry, configuration files, cached SAM, etc. You might even find misconfigured or vulnerable services or scheduled tasks. There are numerous tools to help you with this, including PowerUp, which is part of the PowerSploit package. All of these tactics target loc...