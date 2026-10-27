---
title: Hackers Infect 953 Online Stores With Scanner-Evading JavaScript, Mostly on Magento
url: https://thehackernews.com/2026/10/hackers-infect-953-online-stores-with.html
source: The Hacker News
date: 2026-10-26
fetch_date: 2026-10-27T07:05:43.443599
---

# Hackers Infect 953 Online Stores With Scanner-Evading JavaScript, Mostly on Magento

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Hackers Infect 953 Online Stores With Scanner-Evading JavaScript, Mostly on Magento](https://thehackernews.com/2026/10/hackers-infect-953-online-stores-with.html)

**Ravie Lakshmanan**Oct 26, 2026Malware / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdh3aURB79okzf_mo3sPzJy6vKRiWdPc4gyrE93xmMW-MRgYHrOuJ5yya0TpovJvi-2ol3GubNo5ir76ui-2jBo1jUvOd45Z8f98YeGVAECGcwgpRetuyxFxGWY8bBOB4a0G1H5YiYoYJ3Kd8YauFJGUIVTKYVHsLrvDElRe8sOuD4Y8CKMrAtCA6eJazr/s1700-nu-rw-lo-l85-e365/m-code.jpg)

An unknown threat actor has infected 953 online stores, most of them running Magento, as part of a long-running campaign active since July 2025.

According to Dutch e-commerce security company Sansec, the activity is designed to add a small piece of code to the store's pages that, when visited by unsuspecting users, serves malicious JavaScript loader code through Magento CMS blocks.

"When you visit, that code makes your browser ask the group's server what to do next," Sansec [said](https://sansec.io/research/magento-cms-block-loader-deepveindrilling). "The server first checks whether you are a real shopper or a security scanner, so scanners get nothing."

No less than five distinct domains have been observed over time in connection with the campaign -

* manulfie[.]click, first seen in July 2025
* neswnsssn[.]click, first seen in December 2025
* lanhd6549tdhse[.]top, first seen in March 2026
* additionalver[.]com, first seen in June 2026
* deepveindrilling[.]com, first seen in October 2026

Sansec said it found deepveindrilling[.]com in the CMS blocks of 83 online stores since the domain was registered on October 6, 2026.

The latest JavaScript loader domain is hosted behind Cloudflare and only responds to script requests from real visitors of infected stores. The loader is staged within Magento's [cms\_block](https://developer.adobe.com/commerce/webapi/graphql/schema/store/queries/cms-blocks) database table, which is used to render static content into storefront pages.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The ultimate objective of the attack is to launch the attack-controlled code when the CMS block is rendered after a shopper opens the compromised website.

While Sansec does not disclose whether the threat actor modifies an existing CMS block (such as header, footer, or promotional banner) or creates a new block, the attacker can adopt either of the approaches to run the loader.

Two different versions of the loader have been spotted. In one version, the external JavaScript loaded from the attacker's domain stores the payload in the browser's localStorage. This causes the stashed code to be run again on subsequent visits, even if the external domain becomes unavailable.

The second version expands on this behavior by incorporating browser fingerprinting checks to filter out bots and security scanners, while ensuring that only real shoppers are exposed to the malicious code. The exact nature of the final payload remains unknown.

Early iterations of the campaign have also been observed using [Keitaro](https://thehackernews.com/2026/10/help-tds-linked-to-hotejka-as-20000.html), an advertising tracker and analytics platform, as a traffic distribution system (TDS), to route visitors to different responses – i.e., return a payload, a redirect or nothing – based on their characteristics.

Sansec said requesting the additionalver[.]com script as a Windows desktop visitor returned as response "QWE=123;," which does nothing apart from setting a cookie that marks the visitor for 24 hours. The deepveindrilling[.]com domain, on the other hand, drops the Keitaro component and integrates the bot-filtering logic into the loader itself.

As for the initial access vector, 471 Magento stores are estimated to have been injected with the loader through the [PolyShell](https://thehackernews.com/2026/03/magento-polyshell-flaw-enables.html) (aka [CVE-2026-48356](https://thehackernews.com/2026/07/firefox-chrome-adobe-and-vmware-updates.html)) vulnerability. Another 102 stores saw files uploaded through the PolyShell or [SessionReaper](https://thehackernews.com/2025/09/adobe-commerce-flaw-cve-2025-54236-lets.html) (aka CVE-2025-54236) vulnerabilities.

"One store on Magento 2.4.7-p1 had PolyShell webshells disguised as PNG images in pub/media/custom\_options/quote/, next to the additionalver.com loader in a CMS block," Sansec said. "The block switched to deepveindrilling[.]com on October 7. The store still lacks APSB26-73, Adobe's PolyShell fix for supported release lines."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

In another case, an e-commerce store running Magento 2.4.7-p10 with no missing core patches was compromised to add a rogue administrator account and then use it to inject the code.

Site owners are advised to audit their sites for suspicious accounts and unexpected CMS blocks in the cms\_block and cms\_page tables. It's also advised to keep the sites up-to-date and enforce strong passwords.

The disclosure comes against the backdrop of [PHP2Shell](https://thehackernews.com/2026/10/php2shell-exploitation-hits-government.html), a set of two critical vulnerabilities in PHP (CVE-2026-109618 and CVE-2026-109619) that have witnessed widespread exploitation attempts following their disclosure last week.

However, Perplexity researcher Adel Karimi has [recorded](https://github.com/0x4D31/honeypot-data/blob/main/reports/php2shell/2026-10-24-confirmed-rce.md) what appears to be the [first in-the-wild successful exploitation of the vulnerabilities](https://x.com/MalwareTechBlog/status/2114094868603797841) to run shell commands on honeypot servers. These commands have been observed using wget, curl, or PHP CLI to fetch additional payloads from a remote server ("162.35.99[.]94:80").No downloaded second-stage artifacts have been observed so far.

Found this article interesting?...