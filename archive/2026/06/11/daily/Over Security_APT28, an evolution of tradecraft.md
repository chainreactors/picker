---
title: APT28, an evolution of tradecraft
url: https://blog.sekoia.io/apt28-an-evolution-of-tradecraft/
source: Over Security
date: 2026-06-11
fetch_date: 2026-06-12T06:28:05.531857
---

# APT28, an evolution of tradecraft

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# APT28, an evolution of tradecraft

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/01/TDR-badge.png)](#molongui-disabled-link)

[Amaury G. and Sekoia TDR](#molongui-disabled-link)
June 11 2026

0

25 minutes reading

## Table of contents

* [Context](#h-context)
* [Two decades of APT28 tradecraft](#h-two-decades-of-apt28-tradecraft)
  + [2004 – 2018: The signature implant era and the hack-and-leak playbook](#h-2004-2018-the-signature-implant-era-and-the-hack-and-leak-playbook)
  + [2015 – 2024: The Mueller fallout and the five year blind spot](#h-2015-2024-the-mueller-fallout-and-the-five-year-blind-spot)
  + [2022 – 2024: From monolithic implants to disposable, single-task modules](#h-2022-2024-from-monolithic-implants-to-disposable-single-task-modules)
  + [2023 – 2026: Moving operational infrastructure to the edge](#h-2023-2026-moving-operational-infrastructure-to-the-edge)
  + [2023 – 2025: Industrialised collection against Ukrainian civilian targets](#h-2023-2025-industrialised-collection-against-ukrainian-civilian-targets)
  + [2024 – 2026: The signature implant era is back](#h-2024-2026-the-signature-implant-era-is-back)
  + [2025 – 2026: And now, malware talks to an LLM](#h-2025-2026-and-now-malware-talks-to-an-llm)
* [Conclusion](#h-conclusion)

## Context

Sekoia’s Threat Detection & Research (TDR) team has been **tracking APT28 for several years**. The intrusion set, also known as Fancy Bear, Forest Blizzard, Sofacy, Pawn Storm or Sednit and publicly attributed to the GRU’s Unit 26165, is one of the **most prolific and persistent state-sponsored actors** we monitor. Its operations span in two decades and consistently target government, defence, diplomatic and critical infrastructure entities, with a focus on NATO members and Ukraine.

Given its relentless activity, this intrusion-set has been extensively documented by government agencies, private cybersecurity vendors, and independent researchers. The scale of this collective coverage is reflected in the list of aliases we have compiled: That’s **33 names** for **one adversary**.

SIG40
Pawn Storm
Tsar Team
Fancy Bear
HELLFIRE
BlueDelta
UAC-0028
STRONTIUM
Grey-Cloud
Sofacy
Group 74

Fighting Ursa
ATG2
TG-4127
IRON TWILIGHT
CrisisFour

# APT28

Sednit
Forest Blizzard
ITG05
ATK5
UAC-0001

GRU Unit 26165
Swallowtail
G0007
SNAKEMACKEREL
FROZENLAKE
APT-C-20
BlueAthena
TA422
Grizzly Steppe
GruesomeLarch
Z-Lom Team

Since 2025, we have been working with several foreign and domestic law enforcement and government agencies, including the FBI, as part of broader efforts to **limit this intrusion set’s activities**. Our recent publication on the infection chain of the **Operation Phantom Net Voxel campaign** is one example of this work. In 2026, this cooperation is part of a wider coordinated publication effort conducted alongside government agencies and private vendors, with the shared goal of constraining GRU cyber operations. **The present report contributes to this collective momentum, with a different angle: it looks back at how APT28’s arsenal has evolved over time.**

This report is not an exhaustive review. Our analysis is built on open source documentation. We have chosen to focus on what we consider the **most significant shifts in APT28’s tradecraft**, in order to understand how the intrusion-set’s arsenal has evolved from its earliest known operations to the activity we see today. We assume that a meaningful portion of APT28’s activity has never been disclosed publicly, which inevitably limits what we can analyse. We do not claim to provide a definitive analysis of the intrusion-set, and this report should be read as a modest overview rather than a comprehensive one.

That said, the open-source material available today and our TDR team’s research are sufficient to highlight several meaningful changes in APT28’s **tooling**, **infrastructure**, and **operational tempo**.

The timeline below can be read as a sequence of operational eras, each marked by a shift in **tooling**, **targeting** or **tradecraft**.

*Note: The dates shown here refer to the dates of the operations, not the dates of the open-source releases.*

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2026/06/apt28timeline-2-scaled.png)

*Click to expand*

## Operational eras

Each card marks a shift in tooling, targeting or tradecraft.

2004 - 2018

### Signature implant era

X-Agent
X-Tunnel

Historical toolkit defined the group's operational fingerprint during its highest-profile breaches: TV5Monde sabotage, the German Bundestag hack, the 2016 US Democratic Party intrusions and the World Anti-Doping Agency leak.

External references

["Operation Pawn Storm"Trend Micro(2014)](https://documents.trendmicro.com/assets/wp/wp-operation-pawn-storm.pdf)
["Peering Into Our Main Intelligence Directorate (GRU) Blind Spot"Google(2014)](https://nsarchive.gwu.edu/document/22655-document-07-neel-mehta-billy-leonard-and-shane)
["TV5Monde Attribution"French Ministry of Foreign Affairs(2015)](https://web.archive.org/web/20250716074842/https%3A//www.diplomatie.gouv.fr/fr/dossiers-pays/russie/evenements/evenements-de-l-annee-2025/article/russie-attribution-de-cyberattaques-contre-la-france-au-service-de)

2014 - 2017

### Hack-and-leak playbook

Fake-persona infrastructure

Pioneered the hack-and-leak playbook through the Cyber Berkut persona from March 2014, targeting Ukrainian government, NATO and German entities. Scaled it up in 2016 with the breach of the Democratic Party's campaign committees and Hillary Clinton's campaign staff, releasing stolen emails through fake hacktivist identities and a third-party leak platform to maximize political damage.

External references

["Cyber Berkut Analysis"Recorded Future(2015)](https://www.recordedfuture.com/blog/cyber-berkut-analysis)
["GRU Known Fronts Disclosure"UK ...