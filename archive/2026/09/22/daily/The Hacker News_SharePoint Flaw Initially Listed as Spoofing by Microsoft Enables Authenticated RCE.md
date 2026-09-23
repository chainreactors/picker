---
title: SharePoint Flaw Initially Listed as Spoofing by Microsoft Enables Authenticated RCE
url: https://thehackernews.com/2026/09/sharepoint-flaw-initially-listed-as.html
source: The Hacker News
date: 2026-09-22
fetch_date: 2026-09-23T06:54:53.608037
---

# SharePoint Flaw Initially Listed as Spoofing by Microsoft Enables Authenticated RCE

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [SharePoint Flaw Initially Listed as Spoofing by Microsoft Enables Authenticated RCE](https://thehackernews.com/2026/09/sharepoint-flaw-initially-listed-as.html)

**Swati Khandelwal**Sep 22, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiu0R8P6iyk50vNReEGl0FkwYoFPk5n2fkVC3_3Mf2J5SaQ7yFIHbA3xuQpCATCQ9Y5Ie2ysz9EVaDb_vR5Bbnp209w28bSDK2Rqggotv4NPQbFB5LX4SUT4eztA-6939clsV9QQ41MHwIl8MFSzaJwyFFeBusztZ9H7oZhiUOlFYrL8BQh6hXWegn39uU/s1700-nu-rw-lo-l85-e365/ms-rce.jpg)

A SharePoint Server vulnerability that Microsoft initially classified as a spoofing flaw with a CVSS score of 6.5 actually enables authenticated remote code execution, according to full technical details published today by **Viettel Cyber Security** researcher Dinh Ho Anh Khoa.

The flaw, **CVE-2026-65660**, affects SharePoint Server 2016, 2019, and Subscription Edition. Patches have been available since the [August 11 security updates](https://support.microsoft.com/en-us/servicing/office/hotfix/august/5002893), and the National Vulnerability Database scores it 8.8.

[Microsoft's advisory](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-65660) describes CVE-2026-65660 as allowing an authorized attacker to perform spoofing and assigns no impact to integrity or availability. The CVE record that Microsoft publishes separately, updated on September 11, titles the same flaw a remote code execution vulnerability and says it allows an authorized attacker to execute code.

Both records assign CWE-94, a code-injection weakness. Defenders who triaged CVE-2026-65660 based on the advisory saw a moderate spoofing flaw, not a code-execution vulnerability with a near-maximum score.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Khoa is the researcher who demonstrated the original [ToolShell exploit chain](https://thehackernews.com/2025/07/cisa-orders-urgent-patching-after.html) against SharePoint at Pwn2Own Berlin in May 2025. That chain was later exploited by Chinese state-backed groups and triggered emergency patches from Microsoft.

The researcher has since disclosed several other SharePoint flaws, including CVE-2026-55040, an authentication bypass that attackers [exploited shortly after](https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html) its details became public in August.

The latest [CVE-2026-65660 vulnerability](https://blog.viettelcybersecurity.com/sharepoint_cve-2026-65660/) sits in how SharePoint checks whether server-side controls are on the SafeControls list, a filter that prevents dangerous classes from loading. When the ToolPane component processes web-part markup, it reconstructs Register directives by writing attribute values between double quotes without escaping quotes inside them.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh66mx4dh4UHWyZZ1dkmkX54KIxKf9TBwpExFpDrGC0XyqUtf1M9FxKHVUeZjDUjFfOuFqPIcJ6Hm3FqXazrXh2byP4TnudHwPkipMxRzugXJuv7UNhOv1AKclbnx3bxA5-qWSaqd2KbjazgNb7l6CrAkDrjo24E_J2viz1mFU18qdCidQ0jmFeuBDQCvs/s1700-nu-rw-lo-l85-e365/sharepoint.png)

An attacker can inject additional directives through the unescaped quotes, registering arbitrary .NET classes after the type check runs but before the control is loaded.

With arbitrary class loading, the attacker uses XamlServices.Parse() to trigger code execution through deserialization. The writeup includes a working in-memory webshell payload that avoids the registry permission failures other deserialization methods encounter, Khoa said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

The researcher also demonstrated that the flaw can be chained with a separate, already-patched authentication bypass to reach pre-authentication remote code execution on servers configured to allow anonymous page access. Khoa says the bypass was fixed in a June 9 patch, and servers that applied the fix are not exposed to the pre-authentication path.

No exploitation of CVE-2026-65660 has been reported in the wild, and the flaw is not in CISA's Known Exploited Vulnerabilities catalog. Microsoft's advisory rates exploitation as unlikely, though the full exploit markup is now public. Khoa says he has used the exploit in penetration testing engagements.

The August 11 patch fixes the flaw and turns off the vulnerable function by default, according to the researcher.

Khoa says the flaw also affects SharePoint 2013, though Microsoft's advisory lists only 2016, 2019, and Subscription Edition. SharePoint 2013 has been out of support since April 2023 and receives no security updates.

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

[Microsoft](https://thehackernews.com/search/label/Microsoft), [Microsoft SharePoint](https://thehackernews.com/search/label/Microsoft%20SharePoint), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [SharePoint Server](https://thehackernews.com/search/label/SharePoint%20Server), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehacker...