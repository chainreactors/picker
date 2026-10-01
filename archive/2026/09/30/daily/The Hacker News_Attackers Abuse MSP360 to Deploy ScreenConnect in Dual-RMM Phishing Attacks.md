---
title: Attackers Abuse MSP360 to Deploy ScreenConnect in Dual-RMM Phishing Attacks
url: https://thehackernews.com/2026/09/attackers-abuse-msp360-to-deploy.html
source: The Hacker News
date: 2026-09-30
fetch_date: 2026-10-01T07:59:25.183772
---

# Attackers Abuse MSP360 to Deploy ScreenConnect in Dual-RMM Phishing Attacks

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Attackers Abuse MSP360 to Deploy ScreenConnect in Dual-RMM Phishing Attacks](https://thehackernews.com/2026/09/attackers-abuse-msp360-to-deploy.html)

**Ravie Lakshmanan**Sep 30, 2026Endpoint Security / Social Engineering

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOOpLuI3TSRRvKO7zux2AsJKVNjC36RcaAJCYelekCSQRhpMSABekI8kmMGLZRBZN2biNqDGyKYY_0AqsXb2PMKS6M3sjeLBlt7UQ_IWhXPQ3_q9DGhetIgFeGkF1d_ZE-l2HZPTDID5FkqdLsv3G_wJ-Yckb-Q2I6FdCLo3-AS-pPbCIDRfgFiRzofpaA/s1700-nu-rw-lo-l85-e365/windows-rmm.jpg)

Microsoft has warned of phishing campaigns distributing an installer for the MSP360 Remote Monitoring and Management (RMM) software under the guise of meeting invitations, PDF-themed lures, software update prompts, and other social-engineering content.

"Once executed, the legitimate MSP360 installer, distributed under a deceptive file name established remote management access on affected devices and enabled threat actors to gain an initial foothold using trusted administrative software," the Microsoft Security Research team [said](https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/).

The initial foothold is then used to download and install a ConnectWise ScreenConnect client, offering threat actors a redundant remote-access channel to compromised endpoints. The access is then abused to deliver additional tools and carry out information collection and credential-access operations. The activity has not been attributed to any known threat actor or group.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The multi-stage intrusion chain, which the Windows maker detected in July 2026, begins with phishing emails distributing a digitally signed MSP360 RMM v2.5.0.67 installer under deceptive names such as below -

* VIP\_ECARD\_INVITATION\_rmm\_v2.5.0.67\_oid[redacted].exe
* ZoomSetup\_Installation\_v2.5.0.67\_ oid[redacted].exe
* PDF Reader & Editor the Adobe Acrobatte\_rmm\_v2.5.0.67\_ oid[redacted].exe
* RSVP\_INVITATION\_E\_CARD\_rmm\_v2.5.0.67\_ oid[redacted].exe
* SSA.GOV\_STATEMENT\_rmm\_v2.5.0.67\_ oid[redacted].exe

The installer packages are staged on attacker-controlled infrastructure and legitimate cloud services including Amazon S3, Cloudflare R2, Dropbox, GitLab, and Supabase.

Once launched, the installer drops multiple DLLs, while relaunching itself by invoking the Windows User Account Control (UAC) elevation workflow to run in a privileged context, establish persistent access by deploying MSP360, and leverage the RMM tool to execute PowerShell for stealthily installing ScreenConnect.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1UiAbAKobATGslP6tggbsq5uf_d4pGl09cIJuxA7QxQmNmelHJWxOqQ9U4rm5rralrWkCCgkucLtWZwJbEduKo6A-bkBVCSIinkzzzMIhfx8VvWU_O7QMry9851lbsC3lKJBDsdCYFROodhuMj0i1gGdEW72Q_H2qH2LFWBROnco3BBSSkMGn0X9EWLzZ/s1700-nu-rw-lo-l85-e365/rrm.jpg)

The installer also enumerates installed .NET runtimes and registers two Windows services ([RMM.Agent.exe](https://lolrmm.io/tools/msp360) and RMM.Agent.Launcher.exe) and creates Registry-based autorun entries to ensure that MSP360 is automatically launched when users sign-in to the machine.

Furthermore, it modifies the Windows Firewall configuration to allow inbound UDP traffic to MSP360 (i.e., RMM.Agent.exe) on port 48678.

The dual-RMM remote access attack enables the attacker to transfer additional executables and facilitate post-compromise activity, while camouflaging malicious activity within regular remote administration workflows. The payloads are run through ScreenConnect's native RunFile functionality.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Microsoft said it also observed a separate set of attacks in July 2026 that switched MSP360 for Faronics Deploy Agent to find a way in, and then used it to download and install ScreenConnect. This suggests that the threat actors are putting multiple RMM tools for remote access.

"This activity highlights how threat actors continue to abuse legitimate remote administration software to blend into normal IT operations while maintaining persistent access and reducing detection opportunities," Microsoft said.

"The combination of MSP360 and ScreenConnect provided the threat actor with redundant remote administration channels and enabled the transfer, execution, and management of additional tooling during subsequent stages of the intrusion."

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

[endpoint security](https://thehackernews.com/search/label/endpoint%20security), [Microsoft](https://thehackernews.com/search/label/Microsoft), [Phishing](https://thehackernews.com/search/label/Phishing), [Windows](https://thehackernews.com/search/label/Windows)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild](https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html)

[![The Hacker News](data:image/svg+xml;base64...)

Cloudflare Fixes Flaw T...