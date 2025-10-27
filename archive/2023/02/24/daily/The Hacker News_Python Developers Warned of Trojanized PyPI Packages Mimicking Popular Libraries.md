---
title: Python Developers Warned of Trojanized PyPI Packages Mimicking Popular Libraries
url: https://thehackernews.com/2023/02/python-developers-warned-of-trojanized.html
source: The Hacker News
date: 2023-02-24
fetch_date: 2025-10-04T07:59:57.492997
---

# Python Developers Warned of Trojanized PyPI Packages Mimicking Popular Libraries

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Python Developers Warned of Trojanized PyPI Packages Mimicking Popular Libraries](https://thehackernews.com/2023/02/python-developers-warned-of-trojanized.html)

**Feb 23, 2023**Ravie LakshmananSoftware Security / Supply Chain Attack

[![PyPI Malware](data:image/png;base64... "PyPI Malware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiazTQMlfThRc-v-iN1LevdcwGC9-Dx9e4cCsqzSOpfEBSZpJT0R98zBiqXtjC-dNBDm0Q1axUMgAFeonb07pB5mJpU26V-uqGQA7wEeLoTldaksU_5fDV2-wj-ljeo6Ps-nuWzKd-g6j-X2AtjohX3LwDDl9QQz6HbobHKl7TpKZmjtVEMhFCTogZ4/s790-rw-e365/python.png)

Cybersecurity researchers are warning of "imposter packages" mimicking popular libraries available on the Python Package Index (PyPI) repository.

The 41 malicious PyPI packages have been found to pose as typosquatted variants of legitimate modules such as HTTP, AIOHTTP, requests, urllib, and urllib3. The names of the packages are as follows:

> *aio5, aio6, htps1, httiop, httops, httplat, httpscolor, httpsing, httpslib, httpsos, httpsp, httpssp, httpssus, httpsus, httpxgetter, httpxmodifier, httpxrequester, httpxrequesterv2, httpxv2, httpxv3, libhttps, piphttps, pohttp, requestsd, requestse, requestst, ulrlib3, urelib3, urklib3, urlkib3, urllb, urllib33, urolib3, xhttpsp*

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The descriptions for these packages, for the most part, don't hint at their malicious intent," ReversingLabs researcher Lucija Valentić [said](https://www.reversinglabs.com/blog/beware-impostor-http-libraries-lurk-on-pypi) in a new writeup. "Some are disguised as real libraries and make flattering comparisons between their capabilities and those of known, legitimate HTTP libraries."

But in reality, they either harbor downloaders that act as a conduit to deliver second-stage malware to infected hosts or information stealers that are designed to exfiltrate sensitive data such as passwords and tokens.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPkyMkYMhFM55wooJpb24I53Rtk3xhhXFDK43EyjS2DVhaMylwS9u6-5wHBLISMu_FRE0np1MUBMPBsbNw-crFGHHqW8IJEYUL7X1I0OLrcCqK_PWQxaTgydjdvd36CwQDXB7DjoWIZOgV6Icwv-pMPkIeuQcEQWMyLR6OaJH_v0OCIR8pGSugkJDm/s790-rw-e365/malware.png)

Fortinet, which also [disclosed](https://www.fortinet.com/blog/threat-research/more-supply-chain-attacks-via-new-malicious-python-packages-in-pypi) similar rogue HTTP packages on PyPI earlier this week, noted their ability to launch a [trojan downloader](https://www.virustotal.com/gui/file/618c11e03328eb0cc47ac21964479901dfaaa8a038e4145e247374169d6528f9) that, in turn, contains a [DLL file](https://www.virustotal.com/gui/file/19e9dbfe9df33f17664e780909054b48c62d3dd66e11f31f3a657d18ac4c752f) (Rdudkye.dll) packing a variety of functions.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development is just the latest attempt by malicious actors to poison open source repositories like GitHub, npm, PyPI, and RubyGems to propagate malware to developer systems and mount supply chain attacks.

The findings come a day after Checkmarx [detailed](https://thehackernews.com/2023/02/attackers-flood-npm-repository-with.html) a surge in spam packages in the open source npm registry that are designed to redirect victims to phishing links.

"As with other supply chain attacks, malicious actors are counting on typosquatting creating confusion and counting on incautious developers to embrace malicious packages with similar-sounding names by accident," Valentić said.

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

[PyPI Repository](https://thehackernews.com/search/label/PyPI%20Repository)[Python Package Index](https://thehackernews.com/search/label/Python%20Package%20Index)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")...