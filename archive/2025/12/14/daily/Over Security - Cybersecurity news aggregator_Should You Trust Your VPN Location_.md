---
title: Should You Trust Your VPN Location?
url: https://ipinfo.io/blog/vpn-location-mismatch-report
source: Over Security - Cybersecurity news aggregator
date: 2025-12-14
fetch_date: 2025-12-15T03:27:39.235270
---

# Should You Trust Your VPN Location?

[![IPinfo - Comprehensive IP address data, IP geolocation API and database](https://website-cdn.assets.ipinfo.io/_next/static/media/logo-negative.e34074b5.svg)![IPinfo - Comprehensive IP address data, IP geolocation API and database](https://website-cdn.assets.ipinfo.io/_next/static/media/logo-positive.0a4ba892.svg)](/)

Type`/`to search IP data

8.8.8.8

1.1.1.1

AS15169

[History](/dashboard/lookup/history)[Starred](/dashboard/starred) `?`Hotkeys

* Products
* Data
* Why IPinfo?
* [Pricing](/pricing)
* Resources
* [Docs](/developers)

[Login](/login)[Sign up](/signup)

* [IP Data Fundamentals](/blog/ip-data-fundamentals)
* [IP Data Accuracy](/blog/ip-data-accuracy)
* [Solving Business Challenges](/blog/solving-business-challenges)
* [Getting Started](/blog/getting-started)
* [Optimizing and Scaling](/blog/optimizing-and-scaling)
* [Community and Thought Leadership](/blog/community-and-thought-leadership)
* [Company News and Updates](/blog/company-news-and-updates)

7 days ago by [Ben Dowling](/blog/author/ben) — 10 min read

# Should You Trust Your VPN Location?

![Should You Trust Your VPN Location?](https://ipinfo.io/blog/content/images/2025/12/Trust-Your-VPN-Location.png)

In a large-scale analysis of 20 popular VPNs, IPinfo found that 17 of those VPNs exit traffic from *different countries than they claim*. Some claim 100+ countries, but many of them point to the same handful of physical data centers in the US or Europe.

That means the majority of VPN providers we analyzed don’t route your traffic via the countries they claim to, and they claim many more countries than they actually support.

Analyzing over **150,000 exit IPs** across **137 possible exit countries,** and comparing what providers claim to what IPinfo measures, shows that:

* **17 in 20 providers** had traffic exiting in a different country.
* **38 countries** were “virtual-only” in our dataset (claimed by at least one provider, but never observed as the actual traffic exit country for any provider we tested).
* We were only able to verify all provider announced locations for **3 providers** out of the 20.
* Across ~150,000 VPN exit IPs tested, ProbeNet, our internet measurement platform, detected roughly **8,000 cases** where widely-used IP datasets placed the server in the wrong country — sometimes thousands of kilometers off.

This report walks through what we saw across VPN and IP data providers, provides a closer look at two particularly interesting countries, explores why measurement-based IP data matters if you care where your traffic really goes, and shares how we ran the investigation.

## Which VPNs Matched Reality (And Which Didn’t)

Here is the overlap between the number of listed countries each VPN provider claims to offer versus the countries with real VPN traffic that we measured — lower percentages indicate providers whose claimed lists best match our data:

|  |  |  |
| --- | --- | --- |
| Provider | Claimed Countries | % Virtual or Unmeasurable |
| IPVanish | 108 | 61 |
| CyberGhost | 100 | 57 |
| ExpressVPN | 105 | 57 |
| NordVPN | 126 | 53 |
| Private Internet Access | 91 | 52 |
| ProtonVPN | 110 | 51 |
| FastVPN | 112 | 49 |
| X-VPN | 89 | 43 |
| Surfshark | 100 | 41 |
| BelkaVPN | 63 | 41 |
| ZoogVPN | 76 | 34 |
| VyprVPN | 63 | 27 |
| FastestVPN | 47 | 26 |
| TrustZone | 39 | 18 |
| PrivateVPN | 62 | 13 |
| TunnelBear | 47 | 9 |
| VeePN | 84 | 6 |
| IVPN | 41 | 0 |
| Mullvad | 50 | 0 |
| Windscribe | 70 | 0 |

*It's important to note that we used the most commonly and widely supported technologies in this research, to make comparison between providers as fair as possible while giving us significant data to analyze, so this will not be the full coverage for each provider.*

These are some of the most visible names in the market. They also tend to have very long country lists on their websites. Notably, three well-known providers had zero mismatches across all the countries we tested: Mullvad, IVPN, and Windscribe**.**

Country mismatches doesn’t automatically mean some providers offer “bad VPNs,” but it does mean that if you’re choosing a VPN because it claims “100+ countries,” you should know that a significant share of those flags may be labels, or virtual locations.

## What “Virtual Locations” Really Mean

When a VPN lets you connect to, for example, “Bahamas” or “Somalia,” that doesn’t always mean traffic routes through there. In many cases, it’s somewhere entirely different, like Miami or London, but presented as if traffic is in the country you picked.

This setup is known as a virtual location:

* The VPN app shows “Country X” (e.g. Bahamas).
* The IP registry data also says “Country X” — because the provider self-declared it that way.
* But the network measurements (latency and routing) show the traffic actually exits in “Country Y” — often thousands of kilometers away.

The problem? Without active network measurement, most IP datasets will rely on what the IP’s owner told the internet registry or published in WHOIS/geofeeds: a self-reported country tag. If that record is wrong or outdated, the mistake spreads everywhere. That’s where IPinfo’s ProbeNet comes in: by running live RTT tests from 1,200+ points of presence worldwide, we anchor each IP to its real-world location, not just its declared one.

Across the dataset, we found **97 countries** where at least one VPN brand only ever appeared as virtual or unmeasurable in our data. In other words, for a noticeable slice of the world map, some “locations” in VPNs never show up as true exits in our measurements.

We also found **38 countries** where every mention behaved this way: at least one VPN claimed them, but **none** ever produced a stable, measurable exit in that country in our sample.

You can think of these 38 as the “unmeasurable” countries in this study – places that exist in server lists, config files, and IP geofeeds, but never once appeared as the actual exit country in our measurements. They’re not randomly scattered – they cluster in specific parts of the map. By region, that includes:

![](https://ipinfo.io/blog/content/images/2025/12/VPN-research----unmeasurable--countries-map---Non-measurable.png)

This doesn’t prove there is zero VPN infrastructure in those countries globally. It does show that, across the providers and locations we measured, the dominant pattern is to serve those locations from elsewhere. Here are three of the most interesting examples of how this looks at the IP level.

## Case Studies: Two Countries That Only Exist on the Map

To make this concrete, let’s look at three countries where every provider in our dataset turned out to be virtual: **Bahamas**, and **Somalia**.

### Bahamas: All-Inclusive, Hosted in the US

In our measurements, five providers offered locations labeled as “Bahamas”: NordVPN, ExpressVPN, Private Internet Access, FastVPN, and IPVanish.

For all of them, measured traffic was in the United States, usually with sub-millisecond RTT to US probes.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Provider | Claimed as | Measured exit country | RTT to nearest ProbeNet vantage point in (evidence) | Example exit IP |
| NordVPN | 🇧🇸  Bahamas | 🇺🇸 United States | 0.27 ms from Miami, United States | 45.95.160.61 |
| ExpressVPN | 🇧🇸  Bahamas | 🇺🇸 United States | 0.15 ms from Miami, United States | 64.64.117.18 |
| Private Internet Access | 🇧🇸  Bahamas | 🇺🇸 United States | 0.42 ms from New York, United States | 95.181.238.101 |
| FastVPN | 🇧🇸  Bahamas | 🇺🇸 United States | 0.42 ms from Miami, United States | 108.171.106.198 |
| IPVanish | 🇧🇸  Bahamas | 🇺🇸 United States | 0.37 ms from Miami, United States | 108.171.106.207 |

### Somalia: Mogadishu, via France and the UK

Somalia appears in our sample for only two providers: NordVPN and ProtonVPN.

Both label Mogadishu explicitly in their naming, but these RTTs are exactly what you’d expect for traffic in Western Europe, and completely inconsistent with traffic in East Africa. Both providers go out ...