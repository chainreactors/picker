---
title: Using Open Source Internet Routing Tools to Monitor a Sanctioned Russian Bank
url: https://www.bellingcat.com/resources/2024/03/01/using-open-source-internet-routing-tools-to-monitor-a-sanctioned-russian-bank/
source: bellingcat
date: 2024-03-02
fetch_date: 2025-10-04T12:11:59.392533
---

# Using Open Source Internet Routing Tools to Monitor a Sanctioned Russian Bank

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)

* EN
  + [Русский](https://ru.bellingcat.com)
  + [Français](https://fr.bellingcat.com)
  + [Español](https://es.bellingcat.com)
  + [Deutsch](https://de.bellingcat.com)
  + [Українська](https://uk.bellingcat.com)
* [Donate](https://www.bellingcat.com/donate)

Search for:

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)
* [Donate](/donate)

[![Profile picture for: Logan Williams](https://www.bellingcat.com/app/uploads/2021/11/DSCF9308-300x300.jpg)](https://www.bellingcat.com/author/loganwilliams/)
[Logan Williams](https://www.bellingcat.com/author/loganwilliams/)

Logan Williams is Bellingcat's technology officer and a senior data scientist and researcher on Bellingcat's Investigative Tech Team. He has a background in cartography, data visualisation, optics and signal processing.

# Using Open Source Internet Routing Tools to Monitor a Sanctioned Russian Bank

March 1, 2024

* [Internet Routing](/tag/internet-routing)
* [Tech Team](/tag/tech-team)

An open internet is a cornerstone of civil society, underpinning access to information in peacetime but even more so in times of conflict and under repressive regimes, according to leading experts.

Following Russia’s full-scale invasion of Ukraine in early 2022, over 50 digital and human rights groups including Access Now, the Committee to Protect Journalists, and Human Rights Watch jointly [explained](https://www.accessnow.org/press-release/letter-us-government-internet-access-russia-belarus-ukraine/) in a letter to the US Government that restrictions on the internet to Russia or Belarus could “hurt individuals attempting to organise in opposition to the war, report openly and honestly on events in Russia, and access information about what is happening in Ukraine and abroad,” adding such measures could “also unnecessarily facilitate further repression by the Russian government.”

This is why telecommunications services are often treated differently than other sectors of the economy when it comes to global sanctions, and why the United States made internet services [exempt](https://www.theverge.com/2022/4/11/23020221/us-russian-sanctions-treasury-department-exemption-internet-services) from its sanctions against Russia over the war. That has not stopped major internet service providers from electing to [cut services](https://edition.cnn.com/2022/03/11/tech/russia-internet-backbone-cogent-lumen/index.html) to Russia, or measures from Moscow [limiting access](https://www.businessinsider.com/putin-russia-economy-losses-ukraine-war-social-media-ban-west-2024-1) to social media including Facebook, Instagram and X.

And while the right to a free and open internet is not in doubt, an analysis of over a thousand companies and organisations connected to European internet service providers (ISPs) by Dutch outlet [Investico](https://www.platform-investico.nl/onderzoeken/nederland-internetparadijs) and Bellingcat reveals that some sanctioned entities are able to exploit the free flow of the world wide web. For example, five major Russian banks sanctioned by the EU appear to have a business agreement with British internet service provider RETN.

Experts told Investico, and media partners [Trouw](https://www.trouw.nl/verdieping/moet-rusland-van-het-web-worden-gegooid-internetknooppunt-nederland-brandt-zich-liever-niet-aan-die-vraag~bf97d713/) and [De Groene Amsterdammer](https://www.groene.nl/artikel/altijd-apolitiek-opereren), that economic sanctions on the internet are “a very complicated question.” After the Russian invasion of Ukraine, RIPE, the centralised internet registry for Europe and Central Asia, was pressured by Ukrainian politicians to revoke Russian internet registrations. Ultimately, RIPE received guidance from Dutch authorities that internet resource registration was exempted from sanctions, and maintained an “apolitical” policy.

In an interview with Investico, University of Amsterdam internet researcher Dr Niels ten Oever said that he was initially critical of telecommunication exemptions for RIPE. “But the risk is that if we intervene in RIPE, we intervene in the basic conditions of communication networks. And that means we encourage fragmentation. China could design its own system, so there would be a Chinese and a European internet.” However, the lack of clarity on sanctions has led to ISPs, data centres, and other internet actors choosing their own interpretation. And this instability itself poses risks to the ideal of the global Internet.

Some, but not all, of these questions can be explored with open data. In this guide, Bellingcat will show you how we used open tools to explore Sberbank, one of ten sanctioned Russian banks banned from the international SWIFT banking system. You can read Investico’s full investigation [here](https://www.platform-investico.nl/onderzoeken/nederland-internetparadijs).

To understand how open source tools allow investigators to discover these connections, we first need to have a clear definition of the Internet. While networks, the web, an internet, or *the* Internet (with a capital I) are often used interchangeably, they refer to distinct things.

Computer networks existed before the Internet. What the Internet created was a framework for these separate computer networks to talk to each other as a network of networks. A single company’s computer network is referred to as an Autonomous System, or AS, registered with a unique number. They are autonomous in the sense that it is a self-contained, independent network. To form an internet, this AS must be connected to other ASes.

If every AS could only exchange data with the ASes it was directly connected with, the Internet wouldn’t reach very far. Instead, these connections are publicised using the Border Gateway Protocol, or BGP. There is no centralised switchboard for internet traffic. Instead, BGP allows networks to advertise the routes that they offer to reach other networks, and data centre switches route traffic accordingly. There are many online resources for collecting, processing and visualizing this routing information to make sense of the internet: BGP Tools is one.

So-called “tier 1 ISPs” form the backbone of the Internet. These ISPs are those that have a reach global enough to allow them to send and receive data from any internet connected computer without paying another network operator for the privilege. Smaller networks generally do not lay hundreds of thousands of kilometres of their own fibre optic cables and are not capable of this. Generally, they will pay to “transit” their traffic — either by contracting with a Tier 1 ISP directly or by going through a transit network, such as RETN.

From a technical perspective, every “peering” relationship is equivalent. Two networks either allow bits to move back and forth, or they don’t. But from an economic point of view, there are different types of relationships. The simplest is known as “settlement-free peering,” where no money is exchanged. For example, two small ISPs might agree to peer directly with each other without financial exchange, so that customers of ISP A can network with customers of ISP B and vice versa. Most often, however, a small network will pay to transit data through another network to reach a Tier 1 ISP so that their computers or customers can reach the global network. However, since these relationships are identical from a technical perspective, there is no direct way to identify these economic relationships.

Websites like [BGP Tools](https://bgp.tools/) attempt to determine these relationships by looking at the overall structure ...