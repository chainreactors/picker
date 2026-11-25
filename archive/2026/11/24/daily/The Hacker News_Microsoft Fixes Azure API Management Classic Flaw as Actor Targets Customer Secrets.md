---
title: Microsoft Fixes Azure API Management Classic Flaw as Actor Targets Customer Secrets
url: https://thehackernews.com/2026/11/microsoft-fixes-azure-api-management.html
source: The Hacker News
date: 2026-11-24
fetch_date: 2026-11-25T10:48:29.948019
---

# Microsoft Fixes Azure API Management Classic Flaw as Actor Targets Customer Secrets

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Microsoft Fixes Azure API Management Classic Flaw as Actor Targets Customer Secrets](https://thehackernews.com/2026/11/microsoft-fixes-azure-api-management.html)

**Ravie Lakshmanan**Nov 24, 2026Cloud Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSM2FAnf9UEb3Do4v-r8AEBpoI8byXOrHgng-eRjEyudSf0hiKMpymmDiK_NLTxYuzXdtrWvMrBzY9qmLqDo31r3JOpVefOQxLE77gdkoOAYMkCK__-Bc-AJoWg-8nEOEVjcY6SswkzLbCfYl6kK9clg6xXw3xginWqIwnMxBUaS6wgPKVVwXZNhZA5G85/s1700-nu-rw-lo-l85-e365/azure-ms.jpg)

Norway's National Security Authority (NSM) has disclosed that it became aware of a security vulnerability in Microsoft's Azure API Management (APIM) that has affected multiple businesses in the country, including energy companies [Equinor](https://www.equinor.com/news/20261711-equinor-detected-cyber-attack) and [Skagerak Energi](https://www.skagerakenergi.no/presse/pressemeldinger/oppdatering-pa-forsok-pa-cyberangrep).

"An unknown actor has been actively looking for access tokens, secrets, and named values ​​in APIM," NSM [said](https://nsm.no/aktuelt/nsm-deler-tiltak-mot-sarbarhet-i-azure-api-management). "It is still uncertain how extensive the exploitation of the vulnerability is, and has been."

The security agency said it has so far seen no evidence that has had any impact on Norwegian businesses.

According to a [non-public advisory](https://www.reddit.com/r/sysadmin/comments/1y2n689/critical_security_advisory_affecting_apim/) issued by Microsoft, the issue is said to affect the APIM classic tier. Instances on v2 tiers are not affected.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

"On 18 November 2026, Microsoft identified a security issue affecting Azure API Management Classic tiers that could allow unauthorized access to certain management functionality if the service was not configured according to documented security best practices," Microsoft said in the advisory.

"Microsoft closed the access path on 19 November 2026. Our investigation found that customers were exposed and an unauthorized party could have used the issue to access secrets stored in Azure API Management Classic instances before Microsoft identified the security issue."

As a result, credentials or configuration secrets associated with the API Management resources may have been accessed by an unauthorized third-party if the service has not been configured as per security best practices. The information that may have been accessed could include -

* Secrets stored in Named Values Client secrets associated with identity providers
* Client secrets associated with OpenID Connect providers
* Subscription keys
* Tokens used to call direct management APIs

As of November 21, 2026, the Windows maker has [released guidance](https://techcommunity.microsoft.com/blog/integrationsonazureblog/rotating-credentials-in-azure-api-management/4575478) for customers to help identify and rotate the secrets and credentials configured in their Azure API Management instances. It did not disclose how many customers were affected.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"If someone obtains a credential from that configuration, they may be able to use it directly against the service it protects," security researcher [Anders Kristiansen](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7529921154753400832/) [said](https://anderskristiansen.com/post/2026/apim-legacy-access/). "What they can reach depends on the credential's permissions and whether it is still valid."

NSM has also warned that the vulnerability affects several sectors in Norway and other entities outside of the country, adding it's working with national and international partners and businesses about the matter.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Access Control](https://thehackernews.com/search/label/Access%20Control), [API Security](https://thehackernews.com/search/label/API%20Security), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Credential Security](https://thehackernews.com/search/label/Credential%20Security), [Microsoft Azure](https://thehackernews.com/search/label/Microsoft%20Azure), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

WhatsApp Patches 3 Security Flaws, Including Android Bug Suspected of Use in Scams](https://thehackernews.com/2026/11/whatsapp-patches-3-security-flaws.html)

[![The Hacker News](data:image/svg+xml;base64...)

Linux KVM Flaw CVE-2026-99312 Lets Guest VMs Access Host Memory on AMD Hosts](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html)

[![The Hacker News](data:image/svg+xml;base64...)

Hackers Exploit Critical Cisco Expressway Flaw, Breach Four Devices and Reach Internal Network](https://thehackernews.com/2026/11/hackers-exploit-critical-cisco.html)

[![The Hacker News](data:image/svg+xml;base64...)

New Unpatched Windows 0-Day FastUnlock Lets Someone Holding a Locked PC Run Programs on It](https://thehackernews.com/2026/11/new-unpatched...