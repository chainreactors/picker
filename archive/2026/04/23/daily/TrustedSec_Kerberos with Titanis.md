---
title: Kerberos with Titanis
url: https://trustedsec.com/blog/kerberos-with-titanis
source: TrustedSec
date: 2026-04-23
fetch_date: 2026-04-24T04:57:20.645246
---

# Kerberos with Titanis

[Skip to Main Content](#main)

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
* [Kerberos with Titanis](https://trustedsec.com/blog/kerberos-with-titanis)

April 23, 2026

# Kerberos with Titanis

Written by
Alex Ball

Research
Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/KerberosWithTitanis_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1776877930&s=10eb9ba6bb97ee0c5e8e41b327b4f508)

Table of contents

* [Kerberos Primer](#Primer)
* [Authentication Server (AS) Exchange](#ASE)
* [Working with Tickets](#Tickets)
* [Ticket-Granting Service (TGS) Exchange](#TGS)
* [The AP Exchange](#Exchange)
* [Cheatsheet](#Cheatsheet)
* [Active Directory Attributes](#Attributes)
* [Abbreviations and Acronyms](#Abb)
* [References](#References)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#cef1bdbbaca4abadbaf38da6abada5ebfcfea1bbbaebfcfebaa6a7bdebfcfeafbcbaa7ada2abebfcfea8bca1a3ebfcfe9abcbbbdbaabaa9dabadebfcffe8afa3bef5aca1aab7f385abbcacabbca1bdebfcfeb9a7baa6ebfcfe9aa7baafa0a7bdebfd8febfcfea6bababebdebfd8febfc88ebfc88babcbbbdbaabaabdabade0ada1a3ebfc88aca2a1a9ebfc88a5abbcacabbca1bde3b9a7baa6e3baa7baafa0a7bd "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fkerberos-with-titanis "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Kerberos%20with%20Titanis%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fkerberos-with-titanis "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fkerberos-with-titanis&mini=true "Share on LinkedIn")

In this article, I’ll walk you through the basics of Kerberos, how to use [Titanis](https://github.com/trustedsec/Titanis) for the different parts, and how to mitigate some problems.

## Titanis Setup

I use Titanis tools throughout this article to demonstrate various concepts. If you want to follow along, download the latest Titanis toolset. I’ll be using the Kerb and Ldap tools. The Kerb tool enables you to make requests to a KDC, among other things. Most tools within Titanis directly support Kerberos authentication scenarios (e.g., passwords, PKINIT), so there is rarely any need to manually request a Kerberos ticket with Kerb.

Whenever a Titanis tool runs, it checks for environment variables with a name matching *TITANIS\_DEFAULT\_<param>* and uses those as the default value. Setting these environment variables means you won’t have to type the parameters over and over, saving you time and reducing the risk of error. Titanis tools print an informational message whenever importing an environment variable and using it as a parameter, so there is a full accounting of what parameters the command uses. Note that the parameter `-TicketCache` is special in that it also checks `$KRB5CCNAME`, since this variable is known and used by other tools.

Throughout this article, I’ll be using four (4) different identities. Each of them has a corresponding profile:

### milchick.profile (Password-based logon)

```
unset "${!TITANIS_DEFAULT_*}"
export KRB5CCNAME=~/milchick.ccache
export TITANIS_DEFAULT_KDC=LUMON-DC1
export TITANIS_DEFAULT_WORKSTATION=COBEL-WKS
export TITANIS_DEFAULT_USERNAME=milchick@LUMON
export TITANIS_DEFAULT_PASSWORD=Br3@kr00m\!
```

### milchick-pkinit.profile (PKINIT-based logon)

```
unset ${!TITANIS_DEFAULT_*}
export TITANIS_DEFAULT_KDC=LUMON-DC1
export KRB5CCNAME=~/milchick-pkinit.ccache
export TITANIS_DEFAULT_WORKSTATION=milchick-wks
export TITANIS_DEFAULT_USERNAME=milchick@LUMON
export TITANIS_DEFAULT_USERCERT=milchick.pfx
export TITANIS_DEFAULT_USERKEYPASSWORD=password
```

### allentown.profile (Computer account with password logon)

```
unset ${!TITANIS_DEFAULT_*}
export TITANIS_DEFAULT_KDC=LUMON-DC1
export KRB5CCNAME=~/allentown.ccache
export TITANIS_DEFAULT_WORKSTATION=allentown
export TITANIS_DEFAULT_USERNAME=allentown@LUMON
export TITANIS_DEFAULT_PASSWORD=password
```

### allentown-s4u-admin.profile (Administrator using S4U2proxy through allentown)

```
unset ${!TITANIS_DEFAULT_*}
export TITANIS_DEFAULT_KDC=LUMON-DC1
export KRB5CCNAME=~/allentown-s4u-admin.ccache
export TITANIS_DEFAULT_WORKSTATION=allentown
export TITANIS_DEFAULT_USERNAME=allentown@LUMON
export TITANIS_DEFAULT_PASSWORD=password
export TITANIS_DEFAULT_S4USERNAME=Administrator
export TITANIS_DEFAULT_S4PROXYSERVICE=host/allentown
```

## Kerberos Primer

First, let’s get some terminology out of the way. Kerberos is a network authentication protocol, allowing a **client** to authenticate to a **service**. Clients and services are both identified by a **principal name**, which itself consists of a name type (NT) and one (1) or more parts. Clients and services both share one (1) or more **secret keys** with the key distribution center, but never with each other. A **key distribution center** (KDC) is a server th...