---
title: HollowFrame Loader Deploys Matryoshka Backdoor in Spear-Phishing Attack on Law Firm
url: https://thehackernews.com/2026/07/hollowframe-loader-deploys-matryoshka.html
source: The Hacker News
date: 2026-07-31
fetch_date: 2026-08-01T05:13:34.853726
---

# HollowFrame Loader Deploys Matryoshka Backdoor in Spear-Phishing Attack on Law Firm

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

![cybersecurity](data:image/svg+xml;base64...)

# [HollowFrame Loader Deploys Matryoshka Backdoor in Spear-Phishing Attack on Law Firm](https://thehackernews.com/2026/07/hollowframe-loader-deploys-matryoshka.html)

**Ravie Lakshmanan**Jul 31, 2026Endpoint Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjOaqDYzKWLfOEp56DfMjSmDMudw7Y3DBFUY_xOhGNTnzRYlKw9YCNNbjLvepf-vDHB_KVSSA-KZjx2dNXjJR3ZpTpS_IgGSfhLRjyR2P8ocr_uWQ1w5UcYpuXnycnyv2tPtDqXoZMvD9pqgCNCPDrYMwAup0ftaycFLYzxHvdoOWhEA1ZXffc9ahBpkj5/s1700-e365/law-firm.jpg)

Cybersecurity researchers have shed light on a previously undocumented Go-based loader framework called **HollowFrame** and a Rust-based malware family tracked as **Matryoshka**.

According to Blackpoint Cyber, the intrusion sequence begins with a spear-phishing message containing a link to an encrypted archive, which holds a Windows Shortcut (LNK). Executing the file triggers a multi-stage chain that involves privilege escalation, weakening Microsoft Defender protections, and downloading additional payloads.

While HollowFrame is launched via a DLL side-loading pair comprising the legitimate Python binary ("python.exe") and a rogue DLL ("python311.dll"), Matryoshka comes in two variants, one which supports HTTP-based communication and command execution, and another that uses GitHub for command-and-control (C2), including beaconing, tasking, reconnaissance, file transfer, and secondary payload delivery.

"Together, HollowFrame and Matryoshka gave the actor a persistent foothold for remote command execution, Active Directory reconnaissance, file transfer, and deployment of follow-on tooling," security researchers Nevan Beal and Sam Decker [said](https://blackpointcyber.com/blog/hollowframes-layered-loader-and-matryoshka-backdoors/). "These capabilities could support credential theft, lateral movement, and broader domain compromise through additional tools delivered after initial access."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The cybersecurity company said the multi-stage intrusion targeted two endpoints at an unspecified law firm, with the LNK file masquerading as "Case Documents" to trick the recipient into clicking it and activating a command sequence that employs PowerShell to fetch next-stage components from a remote server ("2.26.252[.]84").

HollowFrame operates as a modular loader and persistence framework that supports various methods to load auxiliary components, at the same time performing anti-analysis checks to avoid running within sandboxed environments. This is determined based on system uptime, installed memory, file count in the user profile, and cursor movement. Persistence is achieved by setting up a scheduled task.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEQz5wx5Wk3F3uCiiNzfwmlWu3vgQN2TohgoaIdhGjyVcu05SfUmZjzmClUPOkK9M6-S06GZJ4jDqesb_2AYetLTuebp9_K8-Dkfp88cjAJYrzNhyPBwTJ_CD1gWAGuo0cnEz7Mx8eb1r0A5_gv6xsACyEPByhr-COEjfyVn1lIBEJNHK44Vfk7EHCtmHK/s1700-e365/cmd.png)

The Go loader comes embedded with an encrypted container, which is then unpacked to launch a second side-loading chain to deploy Matryoshka ("version.dll"), a Rust-based backdoor that communicates with its C2 server ("45.158.196[.]184:8888") over HTTP to spawn a shell and deliver additional tooling.

A second DLL ("wtsapi32.dll") recovered in connection with the same activity has been flagged as a variant of Matryoshka that makes use of a private GitHub repository ("[adioziaete](https://github.com/adioziaete)/memio") to poll victim-specific commands, submit results, and fetch payloads.

"The repository functioned as a collection of per-host mailboxes, with each victim assigned a dedicated <computer>\_<username> directory," Blackpoint explained. "These directories contained beacon.json, cmd.json, result.json, and, in some cases, an upload/ tree for file delivery."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"This structure allowed the operator to manage tasking and results for individual endpoints through GitHub without maintaining a custom command server, while also leaving a versioned history of repository changes unless the associated commits or repository were removed."

Querying the GitHub API with the username [shows](https://api.github.com/users/adioziaete) that the account was created on January 6, 2023, and that the profile information was updated as recently as June 7, 2026. It's currently not known who is behind the activity.

"Across the chain, each stage reduced the amount of malicious behavior visible in the stage before it," Blackpoint noted. "That separation complicated attribution and detection because no single component contained the full infection logic or complete C2 picture."

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

[Active Directory](https://thehackernews.com/search/label/Active%20Directory), [Command and Control](https://thehackernews.com/search/label/Command%20and%20Control), [endpoint security](https://thehackernews.com/search/label/endpoint%20security), [Malware](https://thehackernews.com/search/label/Malware), [Phishing](https://thehackernews.com/search/label/Phishing), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence), [Windows Security](https://thehackernews.com/search/label/Windows%20Security)...