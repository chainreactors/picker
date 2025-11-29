---
title: Legacy Python Bootstrap Scripts Create Domain-Takeover Risk in Multiple PyPI Packages
url: https://thehackernews.com/2025/11/legacy-python-bootstrap-scripts-create.html
source: The Hacker News
date: 2025-11-28
fetch_date: 2025-11-29T03:13:02.479217
---

# Legacy Python Bootstrap Scripts Create Domain-Takeover Risk in Multiple PyPI Packages

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Legacy Python Bootstrap Scripts Create Domain-Takeover Risk in Multiple PyPI Packages](https://thehackernews.com/2025/11/legacy-python-bootstrap-scripts-create.html)

**Nov 28, 2025**Ravie LakshmananMalware / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMdVHqK8sA27WWR3ySGxson4kuqmBaXHQlFm3PSmRaHV6IGdnk_zK0tUvgrFyKepL2COnnm_yiIBdTy-ho7pFKSPQP7cCxkOugoV0s_2k3dUBYC0FI5BkY2tmR3Tsbxktsq7TnQRqzDhiOHe9SjVrRq2XHt5BYU01ctj8yUA8BTv6cDT8zREtEYAdrViUn/s790-rw-e365/setuptools.jpg)

Cybersecurity researchers have discovered vulnerable code in legacy Python packages that could potentially pave the way for a supply chain compromise on the Python Package Index (PyPI) via a domain takeover attack.

Software supply chain security company ReversingLabs said it found the "vulnerability" in bootstrap files provided by a build and deployment automation tool named "zc.buildout."

"The scripts automate the process of downloading, building, and installing the required libraries and tools," security researcher Vladimir Pezo [said](https://www.reversinglabs.com/blog/bootstrap-script-exposes-pypi-to-domain-takeover-attack). "Specifically, when the bootstrap script is executed, it fetches and executes an installation script for the package Distribute from python-distribute[.]org – a legacy domain that is now available for sale in the premium price range while being managed to drive ad revenue."

The PyPI packages that include a bootstrap script that accesses the domain in question include tornado, pypiserver, slapos.core, roman, xlutils, and testfixtures.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The crux of the problem concerns an [old bootstrap script](https://web.archive.org/web/20091102184211/https%3A//svn.zope.org/zc.buildout/trunk/bootstrap/bootstrap.py?rev=105232&view=markup) ("[bootstrap.py](https://web.archive.org/web/20160710213745/https%3A//svn.zope.org/zc.buildout/trunk/bootstrap/bootstrap.py?revision=127532&view=markup)") that was used along with the zc.buildout tool to initialize the Buildout environment. The Python script also supported the ability to install a packaging utility called "Distribute," a short-lived fork of the Setuptools project, into the local environment.

To achieve this, the Distribute installation script ("distribute\_setup.py") is fetched from the python-distribute[.]org, a domain that has been up for sale since 2014. In adding the option, the idea was to instruct the bootstrap script to download and install the Distribute package instead of the older Setuptools package to manage eggs and dependencies for the buildout.

It's important to note that the Distribute fork came into being due to the lack of active development of Setuptools, the main package management tool used at that time. However, the features from Distribute were integrated back into Setuptools in 2013, rendering Distribute obsolete.

The issue identified by ReversingLabs concerns the fact that many packages have continued to ship the bootstrap script that either attempts to install Distribute by default or when the command-line option ("-d" or "--distribute") is specified. This, coupled with the fact that the domain in question is up for grabs, puts users at latent risk as an attacker could weaponize this setup to serve malicious code when the bootstrap script is inadvertently run and potentially steal sensitive data.

While some of the affected packages have taken steps to remove the bootstrap script, the slapos.core package still continues to ship the vulnerable code. It's also included in the development and maintenance version of Tornado.

Another important aspect to consider here is that the bootstrap script is not executed automatically during the package installation and is written in Python 2. This means the script cannot be executed with Python 3 without modifications. But the mere presence of the file leaves an "unnecessary attack surface" that attackers can exploit if developers are tricked into running code that triggers the execution of the bootstrap script.

The threat of a domain takeover is not theoretical. In 2023, it came to light that the npm package fsevents was compromised by a bad actor who seized control of an unclaimed cloud resource hosted at fsevents-binaries.s3-us-west-2.amazonaws[.]com to push malicious executables to users installing certain versions of the package ([CVE-2023-45311](https://nvd.nist.gov/vuln/detail/CVE-2023-45311), CVSS score: 9.8).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

"The issue lies in the programming pattern that includes fetching and executing a payload from a hard-coded domain, which is a pattern commonly observed in malware exhibiting downloader behavior," Pezo said. "The failure to formally decommission the Distribute module allowed vulnerable bootstrap scripts to linger and left unknown numbers of projects exposed to a potential attack."

The disclosure comes as HelixGuard discovered a malicious package in PyPI named "spellcheckers" that claims to be a tool for checking spelling errors using OpenAI Vision, but contains malicious code that's designed to connect to an external server and download a next-stage payload, which then executes a remote access trojan (RAT).

The package, first [uploaded](https://secure.software/pypi/packages/spellcheckers/versions) to PyPI on November 15, 2025, by a user named [leo636722](https://socket.dev/pypi/package/spellcheckers/overview/1.4.0/tar-gz), has been [downloaded 955 times](https://pepy.tech/projects/spellcheckers). It's no longer available for download.

"This RAT can receive remote commands and execute attacker-controlled Python code via exec(), enabling full remote control over the victim's host," HelixGuard [said](https://helixguard.ai/blog/malicious-spellcheckers-2025-11-19). "When the user installs and runs the malicious package, the backdoor becomes active, allowing the attacker to remotely control ...