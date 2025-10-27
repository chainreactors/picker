---
title: Researchers Uncover Batavia Windows Spyware Stealing Documents from Russian Firms
url: https://thehackernews.com/2025/07/researchers-uncover-batavia-windows.html
source: The Hacker News
date: 2025-07-09
fetch_date: 2025-10-07T00:03:43.180023
---

# Researchers Uncover Batavia Windows Spyware Stealing Documents from Russian Firms

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

# [Researchers Uncover Batavia Windows Spyware Stealing Documents from Russian Firms](https://thehackernews.com/2025/07/researchers-uncover-batavia-windows.html)

**Jul 08, 2025**Ravie LakshmananCyber Espionage / Threat Intelligence

[![Batavia Windows Spyware](data:image/png;base64... "Batavia Windows Spyware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoyU8Ha_r9wAFXy7Z8VLtcAS8fQm5QMBwvnffsiBfgCT4z5cyAj48HfHj-mKyhHk2Di8SvmiIJf2vTLnR_wM8H4ph4Om_O8_wbhXUcfZQRmItvZ1xLRcN-yEXnK-XAnIADtDWygjMWhrkSkhhOblJfyAHzDZmdL7n-UTrLbQae6VLHJTrJ0ExK1hjberQp/s790-rw-e365/windows-spyware.jpg)

Russian organizations have been targeted as part of an ongoing campaign that delivers a previously undocumented Windows spyware called Batavia.

The activity, per cybersecurity vendor Kaspersky, has been active since July 2024.

"The targeted attack begins with bait emails containing malicious links, sent under the pretext of signing a contract," the Russian company [said](https://securelist.com/batavia-spyware-steals-data-from-russian-organizations/116866/). "The main goal of the attack is to infect organizations with the previously unknown Batavia spyware, which then proceeds to steal internal documents."

The email messages are sent from the domain "oblast-ru[.]com," which is said to be owned by the attackers themselves. The links embedded within the digital missives lead to the download of an archive file containing a Visual Basic Encoded script (.VBE) file.

When executed, the script profiles the compromised host and exfiltrates the system information to the remote server. This is followed by the retrieval of a next-stage payload from the same server, an executable written in Delphi.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The malware likely displays a fake contract to the victim as a distraction while collecting system logs, office documents (\*.doc, \*.docx, \*.ods, \*.odt, \*.pdf, \*.xls, and \*.xlsx), and screenshots in the background. The data gathering also extends to removable devices attached to the host.

Another capability of the Delphi malware is to download a binary of its own from the server, which targets a broader set of file extensions for subsequent collection. This includes images, emails, Microsoft PowerPoint presentations, archive files, and text documents (\*.jpeg, \*.jpg, \*.cdr, \*.csv, \*.eml, \*.ppt, \*.pptx, \*.odp, \*.rar, \*.zip, \*.rtf, and \*.txt).

The newly collected data is then transmitted to a different domain ("ru-exchange[.]com"), from where an unknown executable is downloaded as a fourth-stage for continuing the attack chain further.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgS0of8ktPN6MY_EoOqJfr0T891nRtln3j_nyL6IswKSIf9wP9o_Qfb1jNoryw-uT4QqQgxRO5sFnC0_VkA4gB-Iiv3iL9MAobFLXnueZCy8aUTwhdPEvN9DnHuk2vIQl3VcCPdmI-2s0O1YgVjf8MXw2Yui2pxsgUsZrdv01uf20bhqteO5V9z6mabRqML/s790-rw-e365/codee.jpg)

Telemetry data from Kaspersky shows that more than 100 users across several dozen organizations received phishing emails over the past year.

"As a result of the attack, Batavia exfiltrates the victim's documents, as well as information such as a list of installed programs, drivers, and operating system components," the company said.

The disclosure comes as Fortinet FortiGuard Labs detailed a malicious campaign that delivers a Windows stealer malware codenamed NordDragonScan. While the exact initial access vector is not clear, it's believed to be a phishing email that propagates a link to trigger the download of an RAR archive.

"Once installed, NordDragonScan examines the host and copies documents, harvests entire Chrome and Firefox profiles, and takes screenshots," security researcher Cara Lin [said](https://www.fortinet.com/blog/threat-research/norddragonscan-quiet-data-harvester-on-windows).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Present within the archive is a Windows shortcut (LNK) file that stealthily makes use of "mshta.exe" to execute a remotely hosted HTML Application (HTA). This step results in the retrieval of a benign decoy document, while a nefarious .NET payload is quietly dropped onto the system.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiBL1IKko-cuhRKcAQVMVLneapyNDus7N2jMdyYxZ6FCzpYqV-sGduTyVErmVjH1CeFBA_dUEK69h1ZhTgB45famZorFaGimOkaF-K4YH5NfRZrE2G2awr851jruAUThMzmo7wDjJDuXmnUc3X3uSHiPWh0doSY5mm9c_-wSvr81ETkBxJfGZprQacLLoH/s790-rw-e365/htaa.jpg)

NordDragonScan, as the stealer malware is called, establishes connections with a remote server ("kpuszkiev[.]com"), sets up persistence via Windows Registry changes, and conducts extensive reconnaissance of the compromised machine to collect sensitive data and exfiltrate the information back to the server via an HTTP POST request.

"The RAR file contains LNK calls that invoke mshta.exe to execute a malicious HTA script, displaying a decoy document in Ukrainian, Lin said. "Finally, it quietly installs its payload in the background. NordDragonScan is capable of scanning the host, capturing a screenshot, extracting documents and PDFs, and sniffing Chrome and Firefox profiles."

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
[![Facebook Messenger](data:image/png;base64...)Share on Faceboo...