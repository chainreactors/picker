---
title: 27 Malicious npm Packages Used as Phishing Infrastructure to Steal Login Credentials
url: https://thehackernews.com/2025/12/27-malicious-npm-packages-used-as.html
source: The Hacker News
date: 2025-12-29
fetch_date: 2025-12-30T03:29:04.289293
---

# 27 Malicious npm Packages Used as Phishing Infrastructure to Steal Login Credentials

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [27 Malicious npm Packages Used as Phishing Infrastructure to Steal Login Credentials](https://thehackernews.com/2025/12/27-malicious-npm-packages-used-as.html)

**Dec 29, 2026**Ravie LakshmananThreat Intelligence / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbarqmk-H0SfVP8X3eR-wcY-UAzQs4vgDfk6mZCaOhgsKNAmf1pLBT_CfB6bMSHARl1UMwvkmd1SL9INOF4KyHSMr7eCO4lWF6745uHql2CwA4iWIGik-6yynnmPNOjdNi9FMXD6pCx3GIJ8T8em0Y6kvg-98a8AuatSM9Ql4zgApKEPOP1pySjfOrblmd/s790-rw-e365/npm-login.jpg)

Cybersecurity researchers have disclosed details of what has been described as a "sustained and targeted" spear-phishing campaign that has published over two dozen packages to the npm registry to facilitate credential theft.

The activity, which involved uploading 27 npm packages from six different npm aliases, has primarily targeted sales and commercial personnel at critical infrastructure-adjacent organizations in the U.S. and Allied nations, according to Socket.

"A five-month operation turned 27 npm packages into durable hosting for browser-run lures that mimic document-sharing portals and Microsoft sign-in, targeting 25 organizations across manufacturing, industrial automation, plastics, and healthcare for credential theft," researchers Nicholas Anderson and Kirill Boychenko [said](https://socket.dev/blog/spearphishing-campaign-abuses-npm-registry).

The names of the packages are listed below -

* adril7123
* ardril712
* arrdril712
* androidvoues
* assetslush
* axerification
* erification
* erificatsion
* errification
* eruification
* hgfiuythdjfhgff
* homiersla
* houimlogs22
* iuythdjfghgff
* iuythdjfhgff
* iuythdjfhgffdf
* iuythdjfhgffs
* iuythdjfhgffyg
* jwoiesk11
* modules9382
* onedrive-verification
* sarrdril712
* scriptstierium11
* secure-docs-app
* sync365
* ttetrification
* vampuleerl

Rather than requiring users to install the packages, the end goal of the campaign is to repurpose npm and package content delivery networks (CDNs) as hosting infrastructure, using them to deliver client-side HTML and JavaScript lures impersonating secure document-sharing that are embedded directly in phishing pages, following which victims are redirected to Microsoft sign-in pages with the email address pre-filled in the form.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/filefix-d)

The use of package CDNs offers several benefits, the foremost being the ability to turn a legitimate distribution service into infrastructure that's resilient to takedowns. In addition, it makes it easy for attackers to switch to other publisher aliases and package names, even if the libraries are pulled.

The packages have been found to incorporate various checks on the client side to challenge analysis efforts, including filtering out bots, evading sandboxes, and requiring mouse or touch input before taking the victims to threat-actor-controlled credential harvesting infrastructure. The JavaScript code is also obfuscated or heavily minified to make automated inspection more difficult.

Another crucial anti-analysis control adopted by the threat actor relates to the use of honeypot form fields that are hidden from view for real users, but are likely to be populated by crawlers. This step acts as a second layer of defense, preventing the attack from proceeding further.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyNNbwaXhb8w6EkuJEkmWuWzKAuRoa3GmsQOhpbhhAkG4-U79x66UEE_9nt9rVLvbQAhcITu4ypCTHohDecdTnyC5MmN5P9H7qH42JRTs7cfvVBMjrrvm_bLmzlp3BwRkVpF76Ik1CqNbUKRO3r_5RFyQL-E-_PFOALd75PtYKLv0IxlhMUn2OiJz2W0uA/s2600/ms.png)

Socket said the domains packed into these packages overlap with adversary-in-the-middle (AitM) phishing infrastructure associated with [Evilginx](https://thehackernews.com/2025/05/russian-hackers-breach-20-ngos-using.html), an open-source phishing kit.

This is not the first time npm has been transformed into phishing infrastructure. Back in October 2025, the software supply chain security firm [detailed](https://thehackernews.com/2025/10/175-malicious-npm-packages-with-26000.html) a campaign dubbed Beamglea that saw unknown threat actors uploading 175 malicious packages for credential harvesting attacks. The latest attack wave is assessed to be distinct from Beamglea.

"This campaign follows the same core playbook, but with different delivery mechanics," Socket said. "Instead of shipping minimal redirect scripts, these packages deliver a self-contained, browser-executed phishing flow as an embedded HTML and JavaScript bundle that runs when loaded in a page context."

What's more, the phishing packages have been found to hard-code 25 email addresses tied to specific individuals, who work in account managers, sales, and business development representatives in manufacturing, industrial automation, plastics and polymer supply chains, healthcare sectors in Austria, Belgium, Canada, France, Germany, Italy, Portugal, Spain, Sweden, Taiwan, Turkey, the U.K., and the U.S.

It's currently unknown how the attackers obtained the email addresses. But given that many of the targeted firms convene at major international trade shows, such as Interpack and K-Fair, it's suspected that the threat actors may have pulled the information from these sites and combined it with general open-web reconnaissance.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

"In several cases, target locations differ from corporate headquarters, which is consistent with the threat actor's focus on regional sales staff, country managers, and local commercial teams rather than only corporate IT," the company said.

To counter the risk posed by the threat, it's essential to enforce stringent dependency verification, log unusual CDN requests from non-development contexts, enforce phishing-resistant multi-factor authentication (MFA), and monitor for suspicious post-authentication events.

The development comes as Socket said it observed a steady rise in destruc...