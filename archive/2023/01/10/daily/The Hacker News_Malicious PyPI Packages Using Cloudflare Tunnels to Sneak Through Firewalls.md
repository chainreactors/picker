---
title: Malicious PyPI Packages Using Cloudflare Tunnels to Sneak Through Firewalls
url: https://thehackernews.com/2023/01/malicious-pypi-packages-using.html
source: The Hacker News
date: 2023-01-10
fetch_date: 2025-10-04T03:28:26.531836
---

# Malicious PyPI Packages Using Cloudflare Tunnels to Sneak Through Firewalls

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

# [Malicious PyPI Packages Using Cloudflare Tunnels to Sneak Through Firewalls](https://thehackernews.com/2023/01/malicious-pypi-packages-using.html)

**Jan 09, 2023**Ravie LakshmananNetwork Security / Supply Chain

[![PyPI Packages Using Cloudflare Tunnels](data:image/png;base64... "PyPI Packages Using Cloudflare Tunnels")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioLScBPxvaWYxBOr1rsfntTQBybECKgpFxx-nGDPk_6IEFmhwQZZ76aF7moU9Hi_S2_w75CFEod-Eel2kD5OhdS_Fd1CYnfCmlWRNXkclQUd1Mf0EtKwb8KK4R-kUkZTZKFI3O3Bgb9zMEylSOk0RQh3dqwz0TbrSuzizWMfynsbG2edK8EdkKUswZ/s790-rw-e365/cf.png)

In yet another campaign targeting the Python Package Index (PyPI) repository, six malicious packages have been found deploying information stealers on developer systems.

The now-removed packages, which were [discovered](https://blog.phylum.io/a-deep-dive-into-powerat-a-newly-discovered-stealer/rat-combo-polluting-pypi) by Phylum between December 22 and December 31, 2022, include pyrologin, easytimestamp, discorder, discord-dev, style.py, and pythonstyles.

The malicious code, as is [increasingly the case](https://thehackernews.com/2022/12/w4sp-stealer-discovered-in-multiple.html), is concealed in the setup script (setup.py) of these libraries, meaning running a "pip install" command is enough to activate the malware deployment process.

The malware is designed to launch a PowerShell script that retrieves a ZIP archive file, install invasive dependencies such as pynput, pydirectinput, and pyscreenshot, and run a Visual Basic Script extracted from the archive to execute more PowerShell code.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"These libraries allow one to control and monitor mouse and keyboard input and capture screen contents," Phylum said in a technical report published last week.

The rogue packages are also capable of harvesting cookies, saved passwords, and cryptocurrency wallet data from Google Chrome, Mozilla Firefox, Microsoft Edge, Brave, Opera, Opera GX, and Vivaldi browsers.

But in what's a novel technique adopted by the threat actor, the attack further attempts to download and install [cloudflared](https://github.com/cloudflare/cloudflared), a command-line tool for [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps), which offers a "secure way to connect your resources to Cloudflare without a publicly routable IP address."

The idea, in a nutshell, is to leverage the tunnel to remotely access the compromised machine via a Flask-based app, which harbors a trojan dubbed xrat (but codenamed poweRAT by Phylum).

The malware enables the threat actor to run shell commands, download remote files and execute them on the host, exfiltrate files and entire directories, and even run arbitrary python code.

The Flask application also supports a "live" feature that uses JavaScript to listen to mouse and keyboard click events and capture screenshots of the system in order to grab any sensitive information entered by the victim.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This thing is like a RAT on steroids," Phylum said. "It has all the basic RAT capabilities built into a nice web GUI with a rudimentary remote desktop capability and a stealer to boot!"

The findings are yet another window into how attackers are [continuously evolving](https://thehackernews.com/2022/12/researchers-discover-malicious-pypi.html) their tactics to target open source package repositories and stage supply chain attacks.

Late last month, Phylum also [disclosed](https://blog.phylum.io/phylum-detects-a-series-of-suspicious-publications-on-npm-again) a number of fraudulent npm modules that were found exfiltrating environment variables from the installed systems.

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

[CloudFlare](https://thehackernews.com/search/label/CloudFlare)[PyPI](https://thehackernews.com/search/label/PyPI)[Python](https://thehackernews.com/search/label/Python)[Python Package Index](https://thehackernews.com/search/label/Python%20Package%20Index)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pando...