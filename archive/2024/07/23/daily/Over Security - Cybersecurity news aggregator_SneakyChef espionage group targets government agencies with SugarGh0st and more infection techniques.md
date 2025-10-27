---
title: SneakyChef espionage group targets government agencies with SugarGh0st and more infection techniques
url: https://blog.talosintelligence.com/sneakychef-sugargh0st-rat/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-23
fetch_date: 2025-10-06T17:44:24.658500
---

# SneakyChef espionage group targets government agencies with SugarGh0st and more infection techniques

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](/content/images/2024/06/sneaky-chef-header.jpg)

# SneakyChef espionage group targets government agencies with SugarGh0st and more infection techniques

By
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan/),
[Ashley Shen](https://blog.talosintelligence.com/author/ashley/)

Friday, June 21, 2024 08:00

[Threats](/category/threats/)
[RAT](/category/rat/)

* Cisco Talos recently discovered an ongoing campaign from SneakyChef, a newly discovered threat actor using SugarGh0st malware, as early as August 2023.
* In the newly discovered campaign, we observed a wider scope of targets spread across countries in EMEA and Asia, compared with [previous observations](https://blog.talosintelligence.com/new-sugargh0st-rat/) that mainly targeted South Korea and Uzbekistan.
* SneakyChef uses lures that are scanned documents of government agencies, most of which are related to various countries’ Ministries of Foreign Affairs or embassies.
* Beside the two infection chains disclosed by Talos in November, we discovered an additional infection chain using SFX RAR files to deliver SugarGh0st.
* The language used in the SFX sample in this campaign reinforces our previous assertion that the actor is Chinese speaking.

*Cisco Talos would like to thank the Yahoo! Paranoids Advanced Cyber Threats Team for their collaboration in this investigation.*

# SneakyChef actor profile

In early August 2023, Talos discovered a campaign using the [SugarGh0st](https://blog.talosintelligence.com/new-sugargh0st-rat/) RAT to target users in Uzbekistan and South Korea. We continued to observe new activities using the same malware to target users in a wider geographical location. Therefore, we created an actor profile for the group and dubbed them “SneakyChef.”

Talos assesses with medium confidence that SneakyChef operators are likely Chinese-speaking based on their language preferences, the usage of the variants of Gh0st RAT — a popular malware among various Chinese-speaking actors — and the specific targets, which includes the Ministry of Foreign affairs of various countries and other government entities. Talos also discovered another RAT dubbed “SpiceRAT” used in the campaign. Read the corresponding research [here](https://blog.talosintelligence.com/new-spicerat-sneakychef/).

![](https://blog.talosintelligence.com/content/images/2024/06/data-src-image-2f153de9-2cf0-4b3d-aaaf-a40b7a862c4a.jpeg)

# Targets across EMEA and Asia

![](https://blog.talosintelligence.com/content/images/2024/06/data-src-image-df375ce5-b3dc-465a-b5d2-51e276c92fd3.jpeg)

Talos assess with low confidence that the following government agencies are the potential targets in this campaign based on the contents of the decoy documents:

* Ministry of Foreign affairs of Angola
* Ministry of Fisheries and Marine Resources of Angola
* Ministry of Agriculture and Forestry of Angola
* Ministry of Foreign affairs of Turkmenistan
* Ministry of Foreign affairs of Kazakhstan
* Ministry of Foreign affairs of India
* Embassy of the Kingdom of Saudi Arabia in Abu Dhabi
* Ministry of Foreign affairs of Latvia

Most of the decoy documents we found in this campaign are scanned documents of government agencies, which do not appear to be available on the internet. During our research, we observed and analyzed various decoy documents with government-and research conference-themed lures in this campaign. We are sharing a few samples of the decoy documents accordingly.

## Lures targeting Southern African countries

The threat actor has used decoy documents impersonating the Ministry of Foreign affairs of Angola. The lure content in one of the sample documents appeared to be a circular from the Angolan Ministry of Fisheries and Marine Resources about a debt conciliation meeting between the ministry authority and a financial advisory company.

Another document contained information about a legal decree concerning state or public assets and their disposal. This document appealed to anyone interested in legal affairs and public heritage regimes and was addressed to the Ministry of Foreign Affairs – MIREX, a centralized institution in Luanda.

|  |  |
| --- | --- |
| ![](data:image/png;base64...) | ![](data:image/png;base64...) |

## Lures targeting Central Asian countries

The decoy documents used in the attacks likely targeting countries in Central Asia were either impersonating the Ministry of Foreign affairs of Turkmenistan or Kazakhstan. One of the lures is related to a meeting organized with the Turkmenistan embassy in Argentina and the heads of transportation and infrastructure of the Italian Republic. Another document was a report of planned events and the government-issued list of priorities to be addressed in the year 2024 that includes a formal proclamation-signing event between the Ministry of Defense of Uzbekistan and the Ministry of Defense of Kazakhstan.

|  |  |
| --- | --- |
| ![](data:image/png;base64...) | ![](data:image/png;base64...) |

## Lures targeting Middle Eastern countries

A decoy document we observed in the attack likely targeting Middle Eastern countries was an official circular regarding the declaration of an official holiday for the Founding Day of the Kingdom of Saudi Arabia.

![](https://blog.talosintelligence.com/content/images/2024/06/data-src-image-f849bc30-affd-4b2e-8e42-beee01614270.png)

## Lures targeting Southern Asian countries

We found another sample that was likely used to target the Indian Ministry of Foreign Affairs. It has decoy documents, including an Indian passport application form, along with a copy of an Aadhar card, a document that serves as proof of identity in India.

|  |  |
| --- | --- |
| ![](data:image/png;base64...) | ![](data:image/png;base64...) |

One of the decoy Word documents we observed contained lures related to India-U.S. relations, in...