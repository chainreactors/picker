---
title: World Leaks: An Extortion Platform
url: https://blog.lexfo.fr/world-leaks-an-extortion-platform.html
source: Lexfo's security blog
date: 2025-05-21
fetch_date: 2025-10-06T22:26:19.119268
---

# World Leaks: An Extortion Platform

[BLOG POSTS](/index.html) [CATEGORIES](/categories.html) [ARCHIVES](/archives.html)

[CONTACT US](https://lexfo.fr/contact/)

World Leaks: An Extortion Platform

Tue 20 May 2025 by **Lexfo CTI team** in [CTI](category/cti.html)

# Keys Findings

* `World Leaks` emerged in early 2025 as a new project by the operators of the Hunters International ransomware group, shifting from double extortion with ransomware to extortion-only attacks due to increased risks and reduced profitability.
* The `World Leaks` and Hunters International platforms share numerous similarities in design, layout, and functionality.
* `World Leaks` operates four distinct platforms: a main data leak site, a negotiation site for ransom payments, an Insider platform for journalists, and an affiliate panel.
* `World Leaks` faced initial bugs, downtime, and fluctuations in claimed data leak sizes, raising questions about data accuracy.
* Despite claiming to be extortion-only, some victims suffered ransomware deployment.
* We learned that the `Secp0` ransomware group is collaborating with `World Leaks`, indicating potential future attractiveness for other threat actors.

# Executive Summary

`World Leaks`, a new extortion platform, emerged in early 2025 as a project by the operators of the Hunters International ransomware group. This shift from double extortion with ransomware to extortion-only attacks was driven by increased risks and reduced profitability in the ransomware ecosystem. The platform shares numerous similarities with Hunters International in design, layout, and functionality, and operates four distinct platforms: a main data leak site, a negotiation site for ransom payments, an Insider platform for journalists, and an affiliate panel. `World Leaks` faced initial challenges, including bugs, downtime, and fluctuations in claimed data leak sizes, raising questions about data accuracy. Despite claiming to be an extortion-only platform, some victims suffered ransomware deployment. `World Leaks` is an Extortion-as-a-Service platform, providing affiliates with an exfiltration tool. Investigations revealed that the `Secp0` ransomware group is collaborating with `World Leaks`, indicating potential future attractiveness for other threat actors. The platform's hazardous beginning and operational challenges will be crucial in determining its future prospects.

# What is âWorld Leaksâ?

`World Leaks` is an extortion platform that emerged in early 2025. On January 1, 2025, [according to a report by Group-IB](https://www.group-ib.com/blog/hunters-international-ransomware-group), who were the first to publicly discover this threat, the operators of the Hunters International ransomware group launched a new project called "World Leaks". Due to actions taken by the authorities against the ransomware ecosystem and the negative impact of the geopolitical context, they deemed this "business" too risky and unprofitable. The operators decided to shift from double extortion with ransomware deployment to extortion-only attacks. With their Extortion-as-a-Service platform, they appear to aim to collaborate with other threat actors, who will be affiliated.

![](../images/world_leaks/world_leaks_logo.png)

World Leaks Logo

[As highlighted in Group-IB's report](https://www.group-ib.com/blog/hunters-international-ransomware-group), Hunters International published an internal note to their partners in November 2024 announcing the end of the project. However, the group remains active. We can deduce that "World Leaks" is either a side project of the criminal organization or a backup plan. Since the note was released, there have been more than 70 claimed victims by Hunters International. The group is still active and shows no signs of retiring from the ransomware ecosystem. There are numerous similarities between the `World Leaks` platform and the Hunters International platform. For instance, both websites share the same design, with the logo positioned in the same location. The list of compromised entities follows the same format, including a variety of time zones and statistics about the number of visitors. Additionally, both platforms feature similar pages, such as those for companies and news announcements.

![](../images/world_leaks/comparison_data_leak_sites.png)

Comparison of the two Data-leak sites

Even the file explorers used to search through the leaked data are alike. Both websites appear to use the same framework or assets, with only minor differences.

![](../images/world_leaks/comparison_file_explorers.png)

Comparison of the two file explorers

# World Leaksâ different platforms

The operators behind `World Leaks` have developed four distinct platforms for their project. The first is their main data leak site, where they display their "trophy wall" showcasing all the victims' data that has been published or is scheduled for publication. The second platform is their negotiation site, which they provide to victims for the purpose of negotiating and facilitating ransom payments. Most recently, they have introduced their Insider platform, which is restricted to journalists and provides the press with 24-hour advance access to information about compromised victims. Lastly, there is their affiliate panel, which unfortunately we did not get access to.

## World Leaksâ data leak site

Similar to Hunters International's data leak site, World Leaks' Data Leak Site (DLS) provides a list of claimed victims along with a timer indicating when the data will be released to the public. The website also features a News tab where the operators can publish information for the public.

![](../images/world_leaks/public_site.png)

Screenshots of World Leaks DLS

Recently, they added a "Sign Up" tab to allow journalists to register for access to the Insider platform.

![](../images/world_leaks/public_insider_announcement.png)![](../images/world_leaks/public_insider_form.png)

As with their other projects, `World Leaks` offers the option to share information about compromised victims on social media platforms such as Reddit, Twitter/X, and Facebook.

![](../images/world_leaks/share.png)

"share" buttons

Additionally, like on their previous platform, their file explorer allows users to browse the list of leaked data and download specific files rather than downloading the entire data dump, which can be cumbersome when dealing with several terabytes of data.

![](../images/world_leaks/public_file_explorer.png)

Screenshots of World Leaks file explorer

## World Leaksâ victim site

Similar to ransomware operations, `World Leaks` provides a victim panel for negotiation, payment, and for victims to view the data that has been exfiltrated by the threat actors. When claiming a compromise by e-mail, `World Leaks` provides the site address (in .onion) as well as a login and password to be used to access the panel.

![](../images/world_leaks/login_form_victim.png)

Screenshots of World Leaks' victim login form

Overall, the victim panel maintains a simple, mostly white and minimalistic design without elaborate styling, similar to the DLS site. This lack of visual complexity is intentional; each element is carefully crafted to maximize psychological pressure on the victim. From the countdown timer to the direct chat with threat actors and the storage page, every feature serves the single purpose of creating urgency, fear, and a sense of inevitability to coerce the victims into paying as quickly as possible.

![](../images/world_leaks/overview_victim.png)

Screenshot of the âOverviewâ tab

The interface offers various tabs. The Overview tab provides details about the victim, including the stock index, revenue, number of employees, name, and country. It also includes a link to their Data Leak Site (DLS) panel. The threat actors threaten to inform the victim's customers, partners, employees, and competitors about the incident if the ransom is not paid.

Additionally, there is a Storage tab where all the exfiltra...