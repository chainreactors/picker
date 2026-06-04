---
title: Google DoubleClick Abused in New Malspam Campaign to Deliver DesckVB RAT
url: https://thehackernews.com/2026/06/google-doubleclick-abused-in-new.html
source: The Hacker News
date: 2026-06-03
fetch_date: 2026-06-04T06:32:17.808509
---

# Google DoubleClick Abused in New Malspam Campaign to Deliver DesckVB RAT

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Google DoubleClick Abused in New Malspam Campaign to Deliver DesckVB RAT](https://thehackernews.com/2026/06/google-doubleclick-abused-in-new.html)

**Ravie Lakshmanan**Jun 03, 2026Malware / Microsoft Defender

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpQ6QXxFH4zkfeHGdcm1WXVcNXMpyJm-1dlZLbFCdp6rKDRhuwICzYaKaR-rCpn61qod6A1F98PZejZbmYuxaUXPJLXQffoaniCkqgyqR1-p7gClpj4PYibjzIDHk8_Vw4ag00EYPCM3Nz1G0Hvzuf6wBV-HzDFoSiYDEEdjPU45Bk_rIlGk9dJ_MMVuue/s1700-e365/ad-malware.jpg)

Cybersecurity researchers have flagged a new malspam campaign that makes use of Google's DoubleClick domain as a way to evade detection and ultimately deliver a remote access trojan (RAT) named **[DesckVB RAT](https://thehackernews.com/2026/02/trojanized-gaming-tools-spread-java.html)**.

"Before the victim ever reaches attacker-controlled infrastructure, the lure routes through DoubleClick, a legitimate Google-owned domain that many security tools are less likely to treat as suspicious," Huntress researchers Anna Pham and Adam Mooney [said](https://www.huntress.com/blog/malspam-to-deskcvb-rat-delivery-chain-analysis) in a report shared with The Hacker News.

"From there, the victim is passed into a malspam kit that personalizes itself on the fly using the victim's email address, dynamically pulling in company branding and location details to make the page feel convincing without requiring the operators to handcraft a lure for each target."

What makes this attack noteworthy is that it eliminates the need for having a bespoke kit for each targeted organization, thereby making these operations more scalable and cost-effective. The end goal of the campaign is to drop DesckVB RAT, a .NET-based trojan that has been active in the wild since February 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The attack begins when an unsuspecting user opens an HTML file that's attached to a phishing email. The file triggers a meta-refresh browser redirect to a Google DoubleClick Campaign Manager click-tracking URL, from where the user is steered to another redirector, which decodes the Base64-encoded email address and leads the victim to a landing page containing a "Download PDF" button.

Clicking the button causes the server to respond with a ZIP archive that initiates the rest of the infection chain. This is achieved by means of a JavaScript loader, whose main responsibility is to retrieve and execute a .NET RAT while flying under the radar. The script extracts and runs a PowerShell script, which then fetches a .NET loader from an external server.

The loader acts as a stager that verifies it's not being analyzed, neutralizes the machine's security controls, sets up persistence, and then ultimately downloads and runs the RAT payload by using a technique called process hollowing that involves injecting the malware into Microsoft-signed processes.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8AQKvnK0LGEfzrfFDdXjalMc_sc0hx3WmK521U1JIZFoWI1FTwBWpjmFxOrerr5jqAqhoD1DLvoZf9r7Q9ClbVr-2Ga_Cq1dMKH_BA7ChBt24FHgL0o3IPPCmWeV4Idzi4SW_Y4vke0k4GduaMQZhE6wE1R2lkayfsI1mF8zgD0XxgP5k4K21CUZ4sozK/s1700-e365/malspam.jpg)

Once launched, the trojan communicates with a command-and-control (C2) server over raw TCP sockets, carries out system reconnaissance, and configures Microsoft Defender exclusions. The trojan also patches Antimalware Scan Interface ([AMSI](https://learn.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal)) and Event Tracing for Windows ([ETW](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/event-tracing-for-windows)) at the native API level at the outset in an effort to blind Windows telemetry before persistence is established on the host by setting up Run and RunOnce Registry entries, along with placing a loader responsible for launching the RAT in the user's Startup folder.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The malware comes with capabilities to extract data, run commands, and deploy additional payloads, granting the attackers full control over the infected machines, while simultaneously taking steps to fly under the radar by terminating and rebooting the machine if it detects an analysis tool or determines that it's running in a sandboxed environment.

"This is a strong reminder of why defence in depth matters," Huntress said. "Configuring a Group Policy Object (GPO) in Active Directory to force script files such as .vbs, .hta, and .js to open in Notepad by default can stop a threat actor at the very first stage, preventing additional payloads from ever being dropped."

"On the email security front, organizations should consider deploying DMARC, DKIM, and SPF records to reduce the likelihood of spoofed or malicious emails reaching end users. Beyond that, an email gateway solution capable of sandboxing attachments and links before delivery adds another meaningful layer of protection."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Google](https://thehacker...