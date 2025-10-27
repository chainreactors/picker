---
title: SideWinder APT Using New WarHawk Backdoor to Target Entities in Pakistan
url: https://thehackernews.com/2022/10/sidewinder-apt-using-new-warhawk.html
source: The Hacker News
date: 2022-10-25
fetch_date: 2025-10-03T20:50:50.809549
---

# SideWinder APT Using New WarHawk Backdoor to Target Entities in Pakistan

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

# [SideWinder APT Using New WarHawk Backdoor to Target Entities in Pakistan](https://thehackernews.com/2022/10/sidewinder-apt-using-new-warhawk.html)

**Oct 24, 2022**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgP-pEl5P_HpxTylWNJmAhc45OGvMP9VqXXxvgBN_bgT9qTtwMo7QL8Wvzcjyf34PB1MMjjMyYf0JJEq0Pec6PFzeVVbxIO2DNICgbPhuhYwYtnddau2udVho_cVf_AjAF94f3jTGTn2nLlpMazC4DqWFUX9_E1IKBBgloD5-e-TE2afGEyswSm6mKu/s790-rw-e365/hackers.jpg)

SideWinder, a prolific nation-state actor mainly known for targeting Pakistan military entities, compromised the official website of the National Electric Power Regulatory Authority (NEPRA) to deliver a tailored malware called **WarHawk**.

"The newly discovered WarHawk backdoor contains various malicious modules that deliver Cobalt Strike, incorporating new TTPs such as [KernelCallBackTable injection](https://attack.mitre.org/techniques/T1574/013/) and Pakistan Standard Time zone check in order to ensure a victorious campaign," Zscaler ThreatLabz [said](https://www.zscaler.com/blogs/security-research/warhawk-new-backdoor-arsenal-sidewinder-apt-group-0).

The threat group, also called APT-C-17, Rattlesnake, and Razor Tiger, is [suspected](https://malpedia.caad.fkie.fraunhofer.de/actor/razor_tiger) to be an Indian state-sponsored actor, although a report from Kaspersky earlier this May acknowledged previous indicators that led to the attribution have since disappeared, making it challenging it to link the threat cluster to a specific nation.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

More than 1,000 attacks are said to have been [launched by the group](https://thehackernews.com/2022/05/sidewinder-hackers-launched-over-1000.html) since April 2020, an indication of SideWinder's newfound aggression since it commenced operations a decade ago in 2012.

The intrusions have been significant not only with regard to their frequency but also in their persistence, even as the group takes advantage of a massive arsenal of obfuscated and newly-developed components.

In June 2022, the threat actor was found [leveraging an AntiBot script](https://thehackernews.com/2022/06/sidewinder-hackers-use-fake-android-vpn.html) that's designed to filter their victims to check the client browser environment, specifically the IP address, to ensure the targets are located in Pakistan.

The September campaign spotted by Zscaler entails the use of a weaponized ISO file hosted on NEPRA's website to activate a killchain that leads to the deployment of the WarHawk malware, with the artifact also acting as a decoy to hide the malicious activity by [displaying](https://www.fbr.gov.pk/categ/admin-notice-board/444) a [legitimate advisory](https://cabinet.gov.pk/Detail/NjcwOTM5YTgtMDM4MC00OWQ4LWIyZGItYTc0MjBjZGVhODcw) issued by the Cabinet Division of Pakistan on July 27, 2022.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvaJFOPDRnp4fIcXAgwzNisJeY0soEQf7J35Ciuj747WE8JxUjHZiqzhqkC68uOd-0ELHclqEgnsU68SIOnkIVkbfXb0IO89esHicddqd5lFdtbYmoBFGwCtjw4rt8rDlH983PzaI-UcSwg4iifDcfZwMy64p-znlrJs8f-r7a2XQgW3jgQna6_FLS/s790-rw-e365/apt.jpg)

WarHawk, for its part, masquerades as legitimate apps such as ASUS Update Setup and Realtek HD Audio Manager to lure unsuspecting victims into execution, resulting in the exfiltration of system metadata to a hard-coded remote server, while also receiving additional payloads from the URL.

This includes a command execution module that's responsible for the execution of system commands on the infected machine received from the command-and-control server, a file manager module that recursively enumerates files present in different drives, and an upload module that transmits files of interest to the server.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Also deployed as a second-stage payload using the aforementioned command execution module is a Cobalt Strike Loader, which validates the host's time zone to confirm it matches the Pakistan Standard Time (PKT), failing which the process is terminated.

Should all the anti-analysis checks successfully pass, the loader injects shellcode into a notepad.exe process using a technique called KernelCallbackTable process injection, with the malware authors lifting source code from a [technical write-up](https://captmeelo.com/redteam/maldev/2022/04/21/kernelcallbacktable-injection.html) published in April 2022 by a researcher who goes by the online alias Capt. Meelo.

The shellcode then decrypts and loads [Beacon](https://thehackernews.com/2022/10/critical-rce-vulnerability-discovered.html), the default malware payload used by Cobalt Strike to establish a connection to its command-and-control server.

Per the cybersecurity company, the attack campaign's connections to the SideWinder APT stem from the reuse of network infrastructure that has been identified as used by the group in prior espionage-focused activities against Pakistan.

"The SideWinder APT Group is continuously evolving their tactics and adding new malware to their arsenal in order to carry out successful espionage attack campaigns against their targets," the researchers concluded.

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
[![Facebook Messenger](data:i...