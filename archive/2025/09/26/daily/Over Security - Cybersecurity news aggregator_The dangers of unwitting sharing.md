---
title: The dangers of unwitting sharing
url: https://www.adainese.it/blog/2021/01/20/the-dangers-of-unwitting-sharing/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-26
fetch_date: 2025-10-02T20:44:08.915456
---

# The dangers of unwitting sharing

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# The dangers of unwitting sharing

#### Table of contents

* [Information Dissemination vs. Information Communication](#information-dissemination-vs-information-communication)
* [Data Misappropriation](#data-misappropriation)
* [Threat Modeling](#threat-modeling)
* [Defensive Measures](#defensive-measures)
* [Conclusion](#conclusion)

#### Latest posts

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/10/01/circular-dependencies-with-ndo/)

[Circular Dependencies with NDO](/blog/2025/10/01/circular-dependencies-with-ndo/)
October 01, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)

[Modifying an object in Strata Cloud Manager](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)
September 28, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)

[From Single-Site to Multi-Site with NDO](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)
September 24, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)

[Retrieving firewall interfaces with Strata Cloud Manager](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)
September 21, 2025

[![Post cover](/images/vendors/eve-ng.webp)](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)

[EVE-NG Linux VM SSH troubleshooting](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)
September 20, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 159 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 123 posts

[![Category cover](/images/categories/ciso.webp)](/categories/ciso)

[CISO](/categories/ciso)
 23 posts

[![Category cover](/images/categories/personal-security.webp)](/categories/personal-security)

[Personal Security](/categories/personal-security)
 22 posts

[![Category cover](/images/categories/security.webp)](/categories/security)

[Security](/categories/security)
 20 posts

[![Category cover](/images/categories/notes.webp)](/categories/notes)

[Notes](/categories/notes)
 19 posts

[![Category cover](/images/categories/infrastructure.webp)](/categories/infrastructure)

[Infrastructure](/categories/infrastructure)
 12 posts

[![Category cover](/images/categories/ot-ics.webp)](/categories/ot-ics)

[OT/ICS](/categories/ot-ics)
 5 posts

[![Category cover](/images/categories/books.webp)](/categories/books)

[Books](/categories/books)
 3 posts

[![Category cover](/images/categories/unetlab.webp)](/categories/unetlab)

[UNetLab](/categories/unetlab)
 3 posts

[![Category cover](/images/categories/writeup.webp)](/categories/writeup)

[Write-up](/categories/writeup)
 3 posts

[![Category cover](/images/categories/osint.webp)](/categories/osint)

[OSInt](/categories/osint)
 2 posts

[![Category cover](/images/categories/life.webp)](/categories/life)

[My life](/categories/life)
 1 posts

## The dangers of unwitting sharing

Andrea Dainese

January 20, 2021

[Personal Security](/categories/personal-security/ "All posts under Personal Security")

[![Post cover](/blog/2021/01/20/the-dangers-of-unwitting-sharing/mugshot.webp)](/blog/2021/01/20/the-dangers-of-unwitting-sharing/mugshot.webp)

Every time we use a technological tool (smartphone, computer, and beyond), we disseminate—whether intentionally or not—an enormous amount of information. Very few people actually stop to consider the potential consequences of this behavior.

Many continue to claim “I have nothing to hide”, an argument that always reminds me of the image of an ostrich burying its head in the sand.

## Information Dissemination vs. Information Communication

As a preliminary note, and for the purposes of this article, we will use “information communication” to describe actions where the confidentiality of the channel is implied (e.g., a direct message). Conversely, *“information dissemination”* refers to actions where the public nature of the channel is implicit (e.g., a public feed or bulletin board). In both cases, the action is voluntary.

I often find myself reflecting with others on how the use of technology frequently leads to misperceptions. While posting a status update on a social network clearly implies that it will be visible to others, few are fully aware that this content can be accessed by **anyone in the world**, from now on, potentially forever.

This lack of awareness can be attributed to a persistent misperception: when interacting with a social network, I am likely sitting safely at home or in an office, perhaps even alone. In reality, however, I am standing before a vast, crowded audience of potentially billions of people—and not just people. I am also subject to automated systems (bots, crawlers, scrapers) eagerly collecting my data. These entities simply have no equivalent in the physical world, making it difficult for us to be cautious about something we cannot fully comprehend.

Another misperception involves communications assumed to be private: it is evident how easy it is to make “confidential” information public. Yet when we digitally communicate with someone, we rarely pause to consider this risk.

## Data Misappropriation

It is crucial to emphasize that everything made public online becomes a potential target for automated tools designed to collect and archive data. These datasets are then monetized—sold or leased to customers.

In other words, anything we make accessible can be commodified. The most well-known example is personalized advertising, which requires millions of categorized user profiles. But emerging products raise additional concerns, such as [Clearview AI](https://www.clearview.ai/ "Clearview AI"), which has built a massive facial-recognition database from publicly available images (including social media content), offered for lease to federal agencies.

With high probability, most of us are already catalogued.

[![Mugshot](/blog/2021/01/20/the-dangers-of-unwitting-sharing/mugshot.webp)](/blog/2021/01/20/the-dangers-of-unwitting-sharing/mugshot.webp)

In the near future, such databases may become commercially accessible. Anyone with a photo of a person could retrieve correlated information: other images, blog posts, social profiles… and this data is likely stored indefinitely.

**A stalker’s paradise.**

## Threat Modeling

This leads to the central issue: how can the information I communicate or disseminate become a threat to me, my family, or my organization?

It is evident that someone with access to my history, comments, or opinions could selectively weaponize messages to discredit me in any context.

Likewise, a data breach—such as the one involving Ho Mobile—enables identity theft by anyone with minimal technical knowledge.

The more data a potential attacker gathers, the more sophisticated the fraud attempts will become. Thinking *“why would anyone target me?”* is once again burying one’s head in the sand. Cyber fraud is, in most cases, a business model designed to maximize profit with minimal effort. **The profit derives**, once again, **from what I can provide**, often under coercion. That “provision” may take the form of money, but also of **actions** or **omissions**: exfiltrating corporate projects, installing a device within a company network, or overlooking an investigation.

## Defensive Measures

The solution lies in strengthening our awareness while reducing the trail of personal information we leave behind.

In [Zanshin Tech](https://www.zanshintech.it/contacts.php "Zanshin Tech") training sessions, a practical exercise highlights the importance of personal data: each participant receives physical cards, each representing a specific typ...