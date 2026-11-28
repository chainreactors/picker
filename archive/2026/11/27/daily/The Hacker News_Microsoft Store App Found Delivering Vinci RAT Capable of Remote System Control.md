---
title: Microsoft Store App Found Delivering Vinci RAT Capable of Remote System Control
url: https://thehackernews.com/2026/11/microsoft-store-app-found-delivering.html
source: The Hacker News
date: 2026-11-27
fetch_date: 2026-11-28T09:42:57.081142
---

# Microsoft Store App Found Delivering Vinci RAT Capable of Remote System Control

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

# [Microsoft Store App Found Delivering Vinci RAT Capable of Remote System Control](https://thehackernews.com/2026/11/microsoft-store-app-found-delivering.html)

**Ravie Lakshmanan**Nov 27, 2026Malware / Social Engineering

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpD815FTK1v-12AKbFYOz3fplAY5EWVRrb1mh5LOUSmUmG7u7mdgGnppCpL9-ZaG-3CyWm_2KP4icW3UY1Q3AYG6lEe03ezqY9Jx49mW9SC4D0JqiUhT-Rmet7lin7u1bHdyppzeay-bTKDty53IDUI_P9md3iUp5xaY-ko1U2uBRTkNdPhAVTYuW9hDmO/s1700-nu-rw-lo-l85-e365/ms-store.png)

Cybersecurity researchers have disclosed details of a cyber attack in which a threat actor leveraged a Microsoft Store application to deliver a remote access trojan (RAT) called **Vinci RAT**.

The intrusion, according to eSentire, begins with a redirection to a bogus site for a sniping tool ("snipp.codes-team[.]com"), from where a Microsoft-signed installer called "Snipping-Tool.exe" is downloaded. Executing the binary leads to the installation of [Setup Assistant](https://apps.microsoft.com/detail/9mvx5x2kgfzf?hl=en-US), an Electron-based application published on the Microsoft Store by ETPS Ltd.

"The application was heavily obfuscated, maintained communication with C2 [command-and-control] infrastructure, monitored the victim's Downloads folder, and supported execution of C2-supplied PowerShell and JavaScript," eSentire [said](https://www.esentire.com/blog/vinci-rat-lives-in-the-microsoft-store).

"This access was used to launch a malicious PowerShell stager, establish persistence through a scheduled task, and retrieve a previously undocumented PowerShell-based RAT."

Once installed, Setup Assistant acts as a backdoor and is designed to run obfuscated JavaScript that allows it to contact the C2 server at "setup-assistant[.]com" and retrieve arbitrary PowerShell or JavaScript code, ultimately resulting in the deployment of the RAT by means of a stager.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

Vinci RAT, as the malware is called, is equipped to fingerprint the host, enumerate installed security tools, facilitate remote and reverse shell access, deliver files, and execute shellcode, DLL, EXE, and PowerShell payloads.

Interestingly, the arbitrary PowerShell or JavaScript execution is triggered by means of two methods -

* Monitor for file names in the victim's Downloads directory by matching them against a predefined list specified in a C2-retrieved configuration ("MSTeamsSetup.exe" and "Reader\_install.exe"). If a match is found, it sends an HTTP POST request to the C2 server and executes the response.
* The C2 server initiates an update action via the URL setup-assistant[.]com/api/update-status?device=<victim\_id>"

The Vinci RAT stager is responsible for running a PowerShell command that disables the Windows Antimalware Scan Interface ([AMSI](https://learn.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal)), generates a unique victim identifier, establishes communication with a C2 server ("monkeysholder[.]info/api.php"), set up persistence via a scheduled task that runs every 10 minutes, and downloads the RAT payload.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeMO3_V00rV7jNR5u70vT0pQImwQGbbukYm1imRP9W7IS-EBl_eyZVmKr9sKSVZGu1Kf4RAY-cpvdREi72Ra8BecGUKqQLIDKZmqf1RbXICm0pow3MW9TgGXNXy2f8xo4oKRLa4a415na8PKGQq_rSCiuJC1nHIO5tb5iqnOLHEs1mm1JCAEIJ9dmuLtrL/s1700-nu-rw-lo-l85-e365/task.png)

Further analysis of the root domain "[codes-team[.]com](https://www.virustotal.com/gui/domain/codes-team.com/detection)" has identified additional sub-domains that suggest that the threat actors are spoofing software download pages for legitimate applications like Microsoft Teams and Roblox -

* roblx.codes-team[.]com
* teams.codes-team[.]com
* teamsmac.codes-team[.]com
* teams-bing.codes-team[.]com

As of writing, Setup Assistant is no longer accessible on Microsoft Software. It was first released on June 1, 2026, while the "codes-team[.]com" domain was registered in late March 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

It remains unclear whether the threat actors themselves took down the app in response to the public disclosure or whether Microsoft removed it, as eSentire noted that the tech giant had failed to take action despite reporting the app through its abuse form on November 10, 2026, responding that it was "not a violation of our terms."

"The campaign highlights how attackers are combining search-engine redirection, fake software download pages, obfuscated Electron applications, and trusted software distribution channels to gain persistent access to victim environments," the Canadian cybersecurity company said.

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

[Malware](https://thehackernews.com/search/label/Malware), [Microsoft Store](https://thehackernews.com/search/label/Microsoft%20Store), [powershell](https://thehackernews.com/search/label/powershell), [Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan), [Social Engineering](https://thehackernews.com/search/labe...