---
title: FBI, Dutch Police Disrupt ‘Manipulaters’ Phishing Gang
url: https://krebsonsecurity.com/2025/01/fbi-dutch-police-disrupt-manipulaters-phishing-gang/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-01
fetch_date: 2025-10-06T20:36:43.798996
---

# FBI, Dutch Police Disrupt ‘Manipulaters’ Phishing Gang

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# FBI, Dutch Police Disrupt ‘Manipulaters’ Phishing Gang

January 31, 2025

[15 Comments](https://krebsonsecurity.com/2025/01/fbi-dutch-police-disrupt-manipulaters-phishing-gang/#comments)

The FBI and authorities in The Netherlands this week seized dozens of servers and domains for a hugely popular spam and malware dissemination service operating out of Pakistan. The proprietors of the service, who use the collective nickname “**The Manipulaters**,” have been the subject of three stories published here since 2015. The FBI said the main clientele are organized crime groups that try to trick victim companies into making payments to a third party.

![](https://krebsonsecurity.com/wp-content/uploads/2021/09/ftexploit.png)

On January 29, the FBI and the Dutch national police seized the technical infrastructure for a cybercrime service marketed under the brands **Heartsender**, **Fudpage** and **Fudtools** (and many other “fud” variations). The “fud” bit stands for “Fully Un-Detectable,” and it refers to cybercrime resources that will evade detection by security tools like antivirus software or anti-spam appliances.

The Dutch authorities [said](https://www.politie.nl/nieuws/2025/januari/27/09-verstoringsactie-deelt-klap-uit-aan-crimineel-cybernetwerk-heartsender.html) 39 servers and domains abroad were seized, and that the servers contained millions of records from victims worldwide — including at least 100,000 records pertaining to Dutch citizens.

A [statement](https://www.justice.gov/usao-sdtx/pr/cybercrime-websites-selling-hacking-tools-transnational-organized-crime-groups-seized) from the **U.S. Department of Justice** refers to the cybercrime group as **Saim Raza**, after a pseudonym The Manipulaters communally used to promote their spam, malware and phishing services on social media.

“The Saim Raza-run websites operated as marketplaces that advertised and facilitated the sale of tools such as phishing kits, scam pages and email extractors often used to build and maintain fraud operations,” the DOJ explained.

The core Manipulaters product is **Heartsender**, a spam delivery service whose homepage openly advertised phishing kits targeting users of various Internet companies, including **Microsoft 365**, **Yahoo**, **AOL**, **Intuit**, **iCloud** and **ID.me**, to name a few.

The government says transnational organized crime groups that purchased these services primarily used them to run [business email compromise](https://krebsonsecurity.com/tag/business-email-compromise/) (BEC) schemes, wherein the cybercrime actors tricked victim companies into making payments to a third party.

“Those payments would instead be redirected to a financial account the perpetrators controlled, resulting in significant losses to victims,” the DOJ wrote. “These tools were also used to acquire victim user credentials and utilize those credentials to further these fraudulent schemes. The seizure of these domains is intended to disrupt the ongoing activity of these groups and stop the proliferation of these tools within the cybercriminal community.”

![](https://krebsonsecurity.com/wp-content/uploads/2024/04/manipulaters-o365.png)

KrebsOnSecurity first wrote about The Manipulaters [in May 2015](https://krebsonsecurity.com/2015/05/phishing-gang-is-audacious-manipulator/), mainly because their ads at the time were blanketing a number of popular cybercrime forums, and because they were fairly open and brazen about what they were doing — even who they were in real life.

We caught up with The Manipulaters again in 2021, with [a story](https://krebsonsecurity.com/2021/09/fudco-spam-empire-tied-to-pakistani-software-firm/) that found the core employees had started a web coding company in Lahore called **WeCodeSolutions** — presumably as a way to account for their considerable Heartsender income. That piece examined how WeCodeSolutions employees had all doxed themselves on Facebook by posting pictures from company parties each year featuring a large cake with the words **FudCo** written in icing.

A [follow-up story last year](https://krebsonsecurity.com/2024/04/the-manipulaters-improve-phishing-still-fail-at-opsec/) about The Manipulaters prompted messages from various WeCodeSolutions employees who pleaded with this publication to remove stories about them. The Saim Raza identity told KrebsOnSecurity they were recently released from jail after being arrested and charged by local police, although they declined to elaborate on the charges.

The Manipulaters never seemed to care much about protecting their own identities, so it’s not surprising that they were unable or unwilling to protect their own customers. In [an analysis](https://www.domaintools.com/resources/blog/the-resurgence-of-the-manipulaters-team-breaking-heartsenders?utm_source=Krebs-on-Security) released last year, **DomainTools.com** found the web-hosted version of Heartsender leaked an extraordinary amount of user information to unauthenticated users, including customer credentials and email records from Heartsender employees.

![](https://krebsonsecurity.com/wp-content/uploads/2021/09/fudcocake.png)

DomainTools also uncovered evidence that the computers used by The Manipulaters were all infected with the same password-stealing malware, and that vast numbers of credentials were stolen from the group and sold online.

“Ironically, the Manipulaters may create more short-term risk to their own customers than law enforcement,” DomainTools wrote. “The data table ‘User Feedbacks’ (sic) exposes what appear to be customer authentication tokens, user identifiers, and even a customer support request that exposes root-level SMTP credentials–all visible by an unauthenticated user on a Manipulaters-controlled domain.”

Police in The Netherlands said the investigation into the owners and customers of the service is ongoing.

“The Cybercrime Team is on the trail of a number of buyers of the tools,” the Dutch national police said. “Presumably, these buyers also include Dutch nationals. The investigation into the makers and buyers of this phishing software has not yet been completed with the seizure of the servers and domains.”

U.S. authorities this week also joined law enforcement in Australia, France, Greece, Italy, Romania and Spain in seizing a number of domains for several long-running cybercrime forums and services, including **Cracked** and **Nulled**. According to [a statement](https://www.europol.europa.eu/media-press/newsroom/news/law-enforcement-takes-down-two-largest-cybercrime-forums-in-world) from the European police agency **Europol**, the two communities attracted more than 10 million users in total.

Other domains seized as part of “**Operation Talent**” included **Sellix**, an e-commerce platform that was frequently used by cybercrime forum members to buy and sell illicit goods and services.

*This entry was posted on Friday 31st of January 2025 01:35 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Breadcrumbs](https://krebsonsecurity.com/category/breadcrumbs/) [Ne'er-Do-Well News](https://krebsonsecurity.com/category/neer-do-well-news/)

[BEC fraud](https://krebsonsecurity.com/tag/bec-fraud/) [business email compromise](https://krebsonsec...