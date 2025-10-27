---
title: North Korean Hackers Targeting Europe and Latin America with Updated DTrack Backdoor
url: https://thehackernews.com/2022/11/north-korean-hackers-targeting-europe.html
source: The Hacker News
date: 2022-11-18
fetch_date: 2025-10-03T23:10:36.731497
---

# North Korean Hackers Targeting Europe and Latin America with Updated DTrack Backdoor

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

# [North Korean Hackers Targeting Europe and Latin America with Updated DTrack Backdoor](https://thehackernews.com/2022/11/north-korean-hackers-targeting-europe.html)

**Nov 17, 2022**Ravie Lakshmanan

[![North Korean Hackers](data:image/png;base64... "North Korean Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4Qu23IGTxg6mctMw-D8julCo5lc3UoiP_iXThV9KKwveGIr8jEWnexQy_YeoJ7bRIIDcQUzjCVM6Wbdl6hBFElbz3sNeDwzfK8aTC3z9uVMGMNnkZMmxL3Ey8ysFAyaHnXHrGcRBl2LqO72nBKs2usvzaklD2p6cWOwdI7Tpa2XaTrTZVYqeYGnnF/s790-rw-e365/north-korean-hackers.jpg)

Hackers tied to the North Korean government have been observed using an updated version of a backdoor known as Dtrack targeting a wide range of industries in Germany, Brazil, India, Italy, Mexico, Switzerland, Saudi Arabia, Turkey, and the U.S.

"Dtrack allows criminals to upload, download, start or delete files on the victim host," Kaspersky researchers Konstantin Zykov and Jornt van der Wiel [said](https://securelist.com/dtrack-targeting-europe-latin-america/107798/) in a report.

The victimology patterns indicate an expansion to Europe and Latin America. Sectors targeted by the malware are education, chemical manufacturing, governmental research centers and policy institutes, IT service providers, utility providers, and telecommunication firms.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Dtrack, also called Valefor and Preft, is the handiwork of Andariel, a subgroup of the [Lazarus nation-state threat actor](https://arstechnica.com/information-technology/2022/11/how-north-korea-became-a-mastermind-of-crypto-cyber-crime/) that's publicly tracked by the broader cybersecurity community using the monikers Operation Troy, Silent Chollima, and Stonefly.

Discovered in September 2019, the malware has been previously deployed in a [cyber attack](https://thehackernews.com/2019/10/nuclear-power-plant-cyberattack.html) aimed at a nuclear power plant in India, with more recent intrusions using Dtrack as part of [Maui](https://thehackernews.com/2022/08/experts-uncover-details-on-maui.html) ransomware attacks.

Industrial cybersecurity company Dragos has since attributed the nuclear facility attack to a threat actor it calls [WASSONITE](https://www.dragos.com/threat/wassonite/), pointing out the use of Dtrack for remote access to the compromised network.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The latest changes observed by Kaspersky relate to how the implant conceals its presence within a seemingly legitimate program ("[NvContainer.exe](https://www.virustotal.com/gui/file/ba8f9e7afe5f78494c111971c39a89111ef9262bf23e8a764c6f65c818837a44/)" or "[XColorHexagonCtrlTest.exe](https://www.virustotal.com/gui/file/3fe624c33790b409421f4fa2bb8abfd701df2231a959493c33187ed34bec0ae7/details)") and the use of three layers of encryption and obfuscation designed to make analysis more difficult.

The final payload, upon decryption, is subsequently injected into the Windows File Explorer process ("explorer.exe") using a technique called [process hollowing](https://attack.mitre.org/techniques/T1055/012/). Chief among the modules downloaded through Dtrack is a keylogger as well as tools to capture screenshots and gather system information.

"The Dtrack backdoor continues to be used actively by the Lazarus group," the researchers concluded. "Modifications in the way the malware is packed show that Lazarus still sees Dtrack as an important asset."

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[North Korean hackers](https://thehackernews.com/search/label/North%20Korean%20hackers)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Link...