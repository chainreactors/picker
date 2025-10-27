---
title: Specula - Turning Outlook Into a C2 With One Registry Change
url: https://trustedsec.com/blog/specula-turning-outlook-into-a-c2-with-one-registry-change
source: TrustedSec
date: 2024-07-30
fetch_date: 2025-10-06T17:46:51.073060
---

# Specula - Turning Outlook Into a C2 With One Registry Change

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
* [Specula - Turning Outlook Into a C2 With One Registry Change](https://trustedsec.com/blog/specula-turning-outlook-into-a-c2-with-one-registry-change)

July 29, 2024

# Specula - Turning Outlook Into a C2 With One Registry Change

Written by
Christopher Paschen and
Oddvar Moe

Red Team Adversarial Attack Simulation

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/SpeculaTool_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1721936809&s=408990cd064f593a73011d9e71c07a74)

Table of contents

* [History](#History)
* [How Specula Works](#How)
* [The Specula Framework](#Framework)
* [Extending Specula](#Extending)
* [Preventing Home Page Attacks](#Attacks)
* [Detecting Home Page Attacks](#Detecting)
* [Conclusion and More Info](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#fac5898f98909f998ec7b9929f9991dfc8ca958f8edfc8ca8e929389dfc8ca9b888e9399969fdfc8ca9c889597dfc8caae888f898e9f9ea99f99dfc8cbdc9b978ac198959e83c7a98a9f998f969bdfc8cad7dfc8caae8f889493949ddfc8cab58f8e96959591dfc8cab3948e95dfc8ca9bdfc8cab9c8dfc8caad938e92dfc8cab5949fdfc8caa89f9d93898e8883dfc8cab9929b949d9fdfc9bbdfc8ca928e8e8a89dfc9bbdfc8bcdfc8bc8e888f898e9f9e899f99d4999597dfc8bc9896959ddfc8bc898a9f998f969bd78e8f889493949dd7958f8e96959591d793948e95d79bd799c8d78d938e92d795949fd7889f9d93898e8883d799929b949d9f "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fspecula-turning-outlook-into-a-c2-with-one-registry-change "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Specula%20-%20Turning%20Outlook%20Into%20a%20C2%20With%20One%20Registry%20Change%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fspecula-turning-outlook-into-a-c2-with-one-registry-change "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fspecula-turning-outlook-into-a-c2-with-one-registry-change&mini=true "Share on LinkedIn")

There exist a few singular Registry changes that any non-privileged user can make that transform the Outlook email client into a beaconing C2 agent. Given that ***outlook.exe*** is a trusted process, this allows an attacker persistent access to a network that we have found often goes unnoticed. This technique has been reported on before and despite that continues to be a weak point in many otherwise very well-guarded networks.

Today, TrustedSec is releasing ***Specula*** (our previously internal framework) into the world, for leveraging this simple Registry change into an initial access platform. We have frequently leveraged ***Specula*** in our social engineering, phishing, and trusted insider attack paths. We hope our release brings more light onto this attack path and helps a variety of organizations develop preventions for it. ***Specula’s*** release will also assist our competitors in bringing further attention to it in their testing as well. If you do not care to read about this more and just want to see the code, it's available on [GitHub](https://github.com/trustedsec/specula) or our vanity url <http://specula.rocks>.

## History

***Specula*** at its core is a C2 framework that operates via the Outlook home page feature. This is not anything specifically new, as other tooling (namely [Ruler](https://github.com/sensepost/ruler?tab=readme-ov-file)) exposes the functionality to create a home page that can attack this vector. The ability to abuse the Outlook home page was reported and listed as CVE-2017-11774. With that being the case, why are we releasing tooling related to the Outlook home page attack in 2024?

The Outlook home page was thought to have been patched in Knowledge Bases (KBs) listed under <https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2017-11774>. After the KB is installed, the UI elements related to Outlook's home page will be gone. This leads one to believe the associated functionality has been removed. Unfortunately, the Registry values that would have been set when the removed UI elements were used still get used by Outlook, even in current Office 365 installs.

Microsoft outlines this [workaround](https://support.microsoft.com/en-us/topic/outlook-home-page-feature-is-missing-in-folder-properties-d207edb7-aa02-46c5-b608-5d9dbed9bd04) to the missing UI elements. If an attacker can modify a single non-privileged Registry key, a C2 channel can be established despite it being thought to be a patched technique.

TrustedSec has been able to leverage this specific channel for initial access in hundreds of clients despite the existing knowledge and prevention...