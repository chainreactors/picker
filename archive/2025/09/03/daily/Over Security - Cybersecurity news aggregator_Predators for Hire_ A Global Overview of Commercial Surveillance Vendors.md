---
title: Predators for Hire: A Global Overview of Commercial Surveillance Vendors
url: https://blog.sekoia.io/predators-for-hire-a-global-overview-of-commercial-surveillance-vendors/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-03
fetch_date: 2025-10-02T19:34:38.135945
---

# Predators for Hire: A Global Overview of Commercial Surveillance Vendors

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

# Predators for Hire: A Global Overview of Commercial Surveillance Vendors

This report provides an overview of the commercial surveillance vendors ecosystem between 2010 and 2025, analysing their spyware offerings, business models, client base, target profiles, and infection chains.

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR, Maxime A., Coline Chavane and Felix Aimé](#molongui-disabled-link)
September 2 2025

0

39 minutes reading

**This blogpost is an abridged version of the report. The full version is available as a PDF.**

[Download the full report](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/08/Strategic-Report-Predators-for-Hire_-A-Global-Overview-of-Commercial-Surveillance-Vendors-1.pdf)

## Table of contents

* **[Introduction](#h-introduction)**
* **[Key takeways](#h-key-takeaways)**
* **[Definitions](#h-definitions)**
* **[Study perimeter and limitations](#h-study-perimeter-and-limitations)**
* **[Understanding cyber threats from commercial surveillance vendors](#h-understanding-cyber-threats-from-commercial-surveillance-vendors)**
* **[Chapter 1 – History and current state of Commercial surveillance vendors](#h-chapter-1-history-and-current-state-of-commercial-surveillance-vendors)**
  + [Commercial spyware development: a chronological overview (2010–2025)](#h-commercial-spyware-development-a-chronological-overview-2010-2025)
    - [2010-2015. Emergence of early commercial spyware](#h-2010-2015)
    - [2016-2021. Industrialisation of commercial surveillance vendors](#h-2016-2021)
    - [2021-2024. Legitimacy crisis](#h-2021-2024)
* **[Chapter 2 – The current state of Commercial surveillance vendors](#h-chapter-2)**
  + [A particularly lucrative and complex market](#h-chapter-2-1)
  + [Persistence despite public exposure and scandals](#h-chapter-2-2)
  + [Growing challenges for governments and regulators](#h-chapter-2-3)
* **[Chapter 3 – Techniques and infection chain process for commercial spyware](#h-chapter-3)**
  + [Reconnaissance and target selection](#h-chapter-3-1)
  + [Intrusion vectors](#h-chapter-3-2)
  + [Delivery and command-and-control infrastructure](#h-chapter-3-3)
* **[Conclusion](#h-conclusion)**

## Introduction

Between November 2023 and July 2024, the Russia-nexus intrusion set **APT29**, a group [operated by](https://www.ncsc.gov.uk/news/joint-advisory-further-ttps-associated-with-svr-cyber-actors) the Russian foreign intelligence service SVR, was [observed](https://blog.google/threat-analysis-group/state-backed-attackers-and-commercial-surveillance-vendors-repeatedly-use-the-same-exploits/) by Google’s Threat Analysis Group (TAG) using exploits that are extremely similar to those previously used by **commercial surveillance vendors (CSV)**, particularly Intellexa’s Predator spyware. This cyber espionage campaign illustrates how exploits developed or exploited by **CSVs** can persist beyond their initial operational use, highlighting one dimension of the risks associated with the proliferation of commercial spyware.

Commercial surveillance vendors are private companies or a groupement of companies that develop, maintain and sell spyware to clients, usually government agencies. CSV activities can include vulnerability research or acquisition, exploits development, digital forensics, command and control infrastructure or client training, all of them usually included or upsold in the full package. Beyond proliferation, the **risks** posed by commercial spyware **are multiple**. Documented use of commercial spyware by state actors have shown surveillance campaigns targeting dissidents, civil society activists and journalists. Such activities erode democratic processes, threaten freedom of expression, and enable politically motivated repression. In addition, CSV poses a **systemic threat to privacy** as spyware often results in collection of personally identifiable information (PII) and personal data without effective judicial oversight, creating risks of human rights violations. Commercial spyware can also be seen as **dual-use technology** under export control regimes, blurring the line between lawful investigative tools and instruments of oppression.

This report provides an overview of the **commercial surveillance vendors ecosystem** **between 2010 and 2025**, analysing their spyware offerings, business models, client base, target profiles, and infection chains.

[*Sekoia.io*](https://blog.sekoia.io/) *is monitoring CSV infrastructure in an effort to protect individuals against potential cases of misuse. In order to ensure the continuity of this monitoring,* [*Sekoia.io*](https://blog.sekoia.io/)***will stop publishing Indicators of Compromise related to these infrastructure.*** *If you are interested in discussing this threat, please contact the TDR team at this address:* *tdr@sekoia.io**.*

*Sekoia.io is dedicated to protecting individuals against spyware threats and supports initiatives such as the Pall Mall Process led by France and the United Kingdom. The **Pall Mall Code of Practice** for States to tackle the proliferation and irresponsible use of commercial cyber intrusion capabilities, issued in April 2025, can be found [here](https://www.diplomatie.gouv.fr/en/french-foreign-policy/digital-diplomacy/news/article/pall-mall-process-code-of-practice-for-states-to-tackle-the-proliferation-and?var_mode=calcul).*

## Key takeaways

* Commercial surveillance vendors (CSV) have been thriving since at least 2010, benefiting from thepressing need **from authoritarian regimes** to acquire rapid and **ready-to-use surveillance tools** to contain the **Arab Spring** popular movement.

* In 2016, CSV started to **industrialise their products**, shifting from isolated technical components to **fully integrated solutions.** However, this development led t...