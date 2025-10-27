---
title: Karma Catches Up to Global Phishing Service 16Shop
url: https://krebsonsecurity.com/2023/08/karma-catches-up-to-global-phishing-service-16shop/
source: Over Security - Cybersecurity news aggregator
date: 2023-08-18
fetch_date: 2025-10-04T12:00:39.472091
---

# Karma Catches Up to Global Phishing Service 16Shop

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Karma Catches Up to Global Phishing Service 16Shop

August 17, 2023

[14 Comments](https://krebsonsecurity.com/2023/08/karma-catches-up-to-global-phishing-service-16shop/#comments)

You’ve probably never heard of “**16Shop**,” but there’s a good chance someone using it has tried to phish you.

![](https://krebsonsecurity.com/wp-content/uploads/2023/08/16shopphish.png)

The international police organization **INTERPOL** [said](https://www.interpol.int/en/News-and-Events/News/2023/Notorious-phishing-platform-shut-down-arrests-in-international-police-operation) last week it had shuttered the notorious 16Shop, a popular phishing-as-a-service platform launched in 2017 that made it simple for even complete novices to conduct complex and convincing phishing scams. INTERPOL said authorities in Indonesia arrested the 21-year-old proprietor and one of his alleged facilitators, and that a third suspect was apprehended in Japan.

The INTERPOL statement says the platform sold hacking tools to compromise more than 70,000 users in 43 countries. Given how long 16Shop has been around and how many paying customers it enjoyed over the years, that number is almost certainly highly conservative.

Also, the sale of “hacking tools” doesn’t quite capture what 16Shop was all about: It was a fully automated phishing platform that gave its thousands of customers a series of brand-specific phishing kits to use, and provided the domain names needed to host the phishing pages and receive any stolen credentials.

Security experts investigating 16Shop found the service used an application programming interface (API) to manage its users, an innovation that allowed its proprietors to shut off access to customers who failed to pay a monthly fee, or for those attempting to copy or pirate the phishing kit.

16Shop also [localized phishing pages](https://www.group-ib.com/media-center/press-releases/interpol-16shop/) in multiple languages, and the service would display relevant phishing content depending on the victim’s geolocation.

![](https://krebsonsecurity.com/wp-content/uploads/2023/08/16shopintl.png)

For example, in 2019 **McAfee** found that for targets in Japan, the 16Shop kit would also collect Web ID and Card Password, while US victims will be asked for their Social Security Number.

“Depending on location, 16Shop will also collect ID numbers (including Civil ID, National ID, and Citizen ID), passport numbers, social insurance numbers, sort codes, and credit limits,” McAfee [wrote](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/16shop-now-targets-amazon/).

In addition, 16Shop employed various tricks to help its users’ phishing pages stay off the radar of security firms, including a local “blacklist” of Internet addresses tied to security companies, and a feature that allowed users to block entire Internet address ranges from accessing phishing pages.

The INTERPOL announcement does not name any of the suspects arrested in connection with the 16Shop investigation. However, a number of security firms — including [Akamai](https://www.akamai.com/blog/security/16shop-commercial-phishing-kit-has-a-hidden-backdoor), McAfee and [ZeroFox](https://www.zerofox.com/blog/16shop-cash-app-phishing-kit/), previously connected the service to a young Indonesian man named **Riswanda Noor Saputra**, who sold 16Shop under the hacker handle “**Devilscream**.”

According to the Indonesian security blog **Cyberthreat.id**, Saputra [admitted being the administrator of 16Shop](https://cyberthreat.id/read/13600/Polisi-FBI-dan-Interpol-Tangkap-Riswanda-Hacker-Indonesia-yang-Bikin-Alat-Peretas-16Shop), but told the publication he handed the project off to others by early 2020.

![](https://krebsonsecurity.com/wp-content/uploads/2023/08/16shoppanel.png)

Nevertheless, Cyberthreat reported that Devilscream was arrested by Indonesian police in late 2021 as part of a collaboration between INTERPOL and the **U.S. Federal Bureau of Investigation** (FBI). Still, researchers who tracked 16Shop [since its inception](http://www.deependresearch.org/2018/09/indonesian-spam-communities.html) say Devilscream was [not the original proprietor of the phishing platform](https://www.fortinet.com/blog/threat-research/japanlocker-an-excavation-to-its-indonesian-roots), and he may not be the last.

## RIZKY BUSINESS

It is not uncommon for cybercriminals [to accidentally infect their own machines with password-stealing malware](https://therecord.media/cybercrime-forum-users-infected-with-info-stealing-malware), and that is exactly what seems to have happened with one of the more recent administrators of 16Shop.

[Constella Intelligence](https://www.constellaintelligence.com), a data breach and threat actor research platform, now allows users to cross-reference popular cybercrime websites and denizens of these forums with [inadvertent malware infections by information-stealing trojans](https://krebsonsecurity.com/2023/04/fbi-seizes-bot-shop-genesis-market-amid-arrests-targeting-operators-suppliers/). A search in Constella on 16Shop’s domain name shows that in mid-2022, a key administrator of the phishing service infected their Microsoft Windows desktop computer with the [Redline information stealer trojan](https://malpedia.caad.fkie.fraunhofer.de/details/win.redline_stealer) — apparently by downloading a cracked (and secretly backdoored) copy of Adobe Photoshop.

Redline infections steal gobs of data from the victim machine, including a list of recent downloads, stored passwords and authentication cookies, as well as browser bookmarks and auto-fill data. Those records indicate the 16Shop admin used the nicknames “**Rudi**” and “**Rizki/Rizky**,” and maintained [several](https://www.facebook.com/itsmeikyxsec404) Facebook profiles under these monikers.

It appears this user’s full name (or at least part of it) is **Rizky Mauluna Sidik**, and they are from Bandung in West Java, Indonesia. One of this user’s Facebook pages says Rizky is the chief executive officer and founder of an entity called **BandungXploiter**, whose [Facebook page](https://www.facebook.com/profile.php?id=100066614212082) indicates it is a group focused mainly on hacking and defacing websites.

A [LinkedIn profile for Rizky](https://www.linkedin.com/in/rizky-69a545230/?originalSubdomain=id) says he is a backend Web developer in Bandung who earned a bachelor’s degree in information technology in 2020. Mr. Rizky did not respond to requests for comment.

![](https://krebsonsecurity.com/wp-content/uploads/2023/08/bandungxploiter.png)

*This entry was posted on Thursday 17th of August 2023 03:58 PM*

[Breadcrumbs](https://krebsonsecurity.com/category/breadcrumbs/) [Ne'er-Do-Well News](https://krebsonsecurity.com/category/neer-do-well-news/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[16Shop](https://krebsonsecurity.com/tag/16shop/) [Akamai](https://krebsonsecurity.com/tag/akamai/) [BandungXploiter](https://krebsonsecurity.com/tag/bandungxploiter/) [Constella Intelligence](https://krebsonsecurity.com/tag/constella-intelligence/) [Cyberthread.id](https://krebsonsecurity.com/tag/cyberthread-id/) [Devilscream](https://krebsonsecurity.com/tag/devilscream/...