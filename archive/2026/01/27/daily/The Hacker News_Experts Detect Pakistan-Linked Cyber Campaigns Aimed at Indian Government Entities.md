---
title: Experts Detect Pakistan-Linked Cyber Campaigns Aimed at Indian Government Entities
url: https://thehackernews.com/2026/01/experts-detect-pakistan-linked-cyber.html
source: The Hacker News
date: 2026-01-27
fetch_date: 2026-01-28T03:35:27.303671
---

# Experts Detect Pakistan-Linked Cyber Campaigns Aimed at Indian Government Entities

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

# [Experts Detect Pakistan-Linked Cyber Campaigns Aimed at Indian Government Entities](https://thehackernews.com/2026/01/experts-detect-pakistan-linked-cyber.html)

**Ravie Lakshmanan**Jan 27, 2026Threat Intelligence / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiG612WfAM4qjKPdbLvz7i_kK0qgRz5Abg8pRz9uGc86pEQvuO-_83uNd8xC8e1y86mWhlTRL_PeWtgp2bfizGf8y78pp1xGYqoXJ9Q7ilpXG4lAS4MvNiiAMGf74PzFod56EJW9qq6P3afCB9IgTFGrbgu1EqnXVsly_I8clrUqdGReHfmEJtKUL09wV5m/s1700-e365/attack.jpg)

Indian government entities have been targeted in two campaigns undertaken by a threat actor that operates in Pakistan using previously undocumented tradecraft.

The campaigns have been codenamed **Gopher Strike** and **Sheet Attack** by Zscaler ThreatLabz, which identified them in September 2025.

"While these campaigns share some similarities with the Pakistan-linked Advanced Persistent Threat (APT) group, [APT36](https://thehackernews.com/2025/10/apt36-targets-indian-government-with.html), we assess with medium confidence that the activity identified during this analysis might originate from a new subgroup or another Pakistan-linked group operating in parallel," researchers Sudeep Singh and Yin Hong Chang [said](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-gogitter-gitshellpad-and-goshell).

Sheet Attack gets its name from the use of legitimate services like Google Sheets, Firebase, and email for command-and-control (C2). On the other hand, Gopher Strike is assessed to have leveraged phishing emails as a starting point to deliver PDF documents containing a blurred image that's superimposed by a seemingly harmless pop-up instructing the recipient to download an update for Adobe Acrobat Reader DC.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

The main purpose of the image is to give the users an impression that it's necessary to install the update in order to access the document's contents. Clicking the "Download and Install" button in the fake update dialog triggers the download of an ISO image file only when the requests originate from IP addresses located in India and the [User-Agent string](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent) corresponds to Windows.

"These server-side checks prevent automated URL analysis tools from fetching the ISO file, ensuring that the malicious file is only delivered to intended targets," Zscaler said.

The malicious payload embedded within the ISO image is a Golang-based downloader dubbed GOGITTER that's responsible for creating a Visual Basic Script (VBScript) file if it does not already exist in the following locations: "C:\Users\Public\Downloads," "C:\Users\Public\Pictures," and "%APPDATA%." The script is designed to fetch VBScript commands every 30 seconds from two pre-configured C2 servers.

GOGITTER also sets up persistence using a scheduled task that's configured to run the aforementioned VBScript file every 50 minutes. In addition, it ascertains the presence of another file named "adobe\_update.zip" in the same three folders. If the ZIP file is not present, it pulls the archive from a private GitHub repository ("github[.]com/jaishankai/sockv6"). The GitHub account was created on June 7, 2025.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZm3VegRz8kS0pz8RbC0h2VNGmWSj1eUB8WrzrZC2Ys2UCOfbeUiWyeQoeUO_5H7nMUwJAvGph5IUPsh3lRLwtwMZ2SrCwChnMAhZK7XcLtcMunosd4BPNerVO9BgDO0uNelz6O08FdNEFUQcvwvgLOUA_9TAQsAKROKlHuJb6WPOSXKm7xN3HBtbFqBDS/s1700-e365/zz.jpg)

Once the download is successful, the attack chain sends an HTTP GET request to the domain "adobe-acrobat[.]in" likely to signal the threat actors that the endpoint has been infected. GOGITTER then extracts and executes "edgehost.exe" from the ZIP file. A lightweight Golang-based backdoor, GITSHELLPAD, leverages threat actor-controlled private GitHub repositories for C2.

Specifically, it polls the C2 server every 15 seconds by means of a GET request to access the contents of a file named "command.txt." It supports six different commands -

* **cd ..**, to change working directory to the parent directory
* **cd**, to change directory to the specified path
* **run**, to run a command in the background without capturing the output
* **upload**, to upload a local file specified by the path to the GitHub repository
* **download**, to download a file to the specified path
* **default case**, to run a command using cmd /c and capture the output

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

The results of the command execution are stored in a file called "result.txt" and uploaded to the GitHub account via an HTTP PUT request. The "command.txt" is then deleted from the GitHub repository once the command is successfully executed.

Zscaler said it observed the threat actor also downloading RAR archives using cURL commands after gaining access to the victim's machine. The archives include utilities to gather system information and drop GOSHELL, a bespoke Golang-based loader used to deliver Cobalt Strike Beacon after multiple rounds of decoding. The tools are wiped from the machine after use.

"GOSHELL's size was artificially inflated to approximately 1 gigabyte by adding junk bytes to the Portable Executable (PE) overlay, likely to evade detection by antivirus software," the cybersecurity company said. "GOSHELL only executes on specific hostnames by comparing the victim's hostname against a hard-coded list."

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
[![Facebook Messenger](data:image/png;base6...