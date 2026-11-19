---
title: Attackers Compromise Microsoft's Agent Framework PyPI Package to Steal Cloud Credentials
url: https://thehackernews.com/2026/11/attackers-compromise-microsofts-agent.html
source: The Hacker News
date: 2026-11-18
fetch_date: 2026-11-19T09:47:36.653848
---

# Attackers Compromise Microsoft's Agent Framework PyPI Package to Steal Cloud Credentials

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

# [Attackers Compromise Microsoft's Agent Framework PyPI Package to Steal Cloud Credentials](https://thehackernews.com/2026/11/attackers-compromise-microsofts-agent.html)

**Ravie Lakshmanan**Nov 18, 2026Supply Chain Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_LozO7RAz13Jr3eqWHIjlAF6M0Cs-mJXX2mKUqU0TxVS02piD1na92TAZjICmeySD4z0zS-Y_BFvceERBdk-UZvV1DUh1LGN6wK-T-yt_TROJ5fcuvROu807jqESQo93CFP3faBbReKMZQxvgYOAGl_vS2VzfO67O24NdAgh6d9jMO2mTSy2jaNJMPD9T/s1700-nu-rw-lo-l85-e365/ms-python.jpg)

Threat actors have compromised Microsoft's **[agent-framework](https://pypi.org/project/agent-framework/)** package to push a credential stealer, according to reports from [Aikido](https://www.aikido.dev/blog/two-malicious-agent-framework-releases-hit-pypi-in-33-minutes), [Chainguard](https://www.chainguard.dev/unchained/microsoft-agent-framework-compromised-on-pypi-november-2026), [Endor Labs](https://www.endorlabs.com/learn/agent-framework-compromised-software-supply-chain-attack), [OX Security](https://www.ox.security/blog/breaking-hijacked-releases-of-microsofts-official-agent-framework-steals-azure-and-ci-credentials/), [SafeDep](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise), [Socket](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer), [StepSecurity](https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised), and Google-owned [Wiz](https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi).

The malicious versions, 1.26.1 and 1.26.2, were published 33 minutes apart on November 17, 2026, and are designed to run a credential stealer on every Python start. As of writing, both the [release versions have been quarantined](https://pypi.org/project/agent-framework/#history) on the Python Package Index (PyPI) repository. It's unclear how the attacker managed to obtain publishing access.

Agent-framework is the meta-package for Microsoft Agent Framework, an open-source framework for building and orchestrating artificial intelligence (AI) agents using Python.

"Both versions install Python startup hooks that silently collect credentials, environment data, and cloud identity tokens, then exfiltrate them to a webhook[.]site endpoint," Socket said in a report.

Once either of the versions is installed, the package drops a .pth file in the site-packages root directory, which then gets executed automatically on every interpreter start, causing the credential stealer to run whenever Python is started in an environment, even if the package is not explicitly imported.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

"Each wheel adds a .pth file to site-packages," Endor Labs said. "Python executes import lines in .pth files on every interpreter start, so the stealer runs on any Python launch in an affected environment, including pip itself, whether or not anything imports Agent Framework."

The names of the .pth files are below -

* agent\_framework\_meta.pth in version 1.26.1
* af\_runtime\_diag.pth in version 1.26.2

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHMooh2Z15ipBNfLnXk2U9pw1BoPmQcodhza40dmubbUcMuRZGf1S54D40zoJdzNbD0OSNBVIZsu88zyPx_c8YUBQ28Tr0M89nMT4Wv7_kFthSmPjnrYPcG9ULNK-popXTtHeWaCxNRCMsfsIF22MPJZzwm-oqmCFyaf6aYqEnzpOwySzf3kcXnUxFHY_W/s1700-nu-rw-lo-l85-e365/ox.jpg)

The "agent\_framework\_meta.pth" file contains a single import statement referencing "agent\_framework\_meta," which then launches the stealer payload. It's capable of capturing the following data -

* Environment variables based on substring-based matching
* Credential files associated with Azure CLI (~/.azure/\*.json), .npmrc, pip.conf, .netrc, .git-credentials, .docker/config.json, Hugging Face, Microsoft Azure DevOps agents, and .env and JSON files
* Azure DevOps OIDC tokens
* Azure managed-identity tokens
* Azure instance metadata and retains up to 8,000 characters of the response

"Besides reading credentials already on disk, the code asks the platform to issue new ones," SafeDep said. "Rotating stored secrets does not cover those."

"In an Azure DevOps pipeline, SYSTEM\_ACCESSTOKEN and SYSTEM\_OIDCREQUESTURI are enough to request a federated token for api://AzureADTokenExchange. On Azure compute, it asks the managed identity endpoint for an access token to each of these resources. It uses IDENTITY\_ENDPOINT or MSI\_ENDPOINT on App Service and Functions, and 169.254.169[.]254 elsewhere. It also pulls instance metadata."

It's worth noting that the Azure instance metadata service ([IMDS](https://www.microsoft.com/en-us/security/blog/2023/10/03/defending-new-vectors-threat-actors-attempt-sql-server-to-cloud-lateral-movement/)) is a RESTful web service that runs on a local IP address ("169.254.169[.]254"), and provides information about the virtual machine, its region, tags, and the identity token.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

All the collected information is saved into a JSON document, zlib-compressed, Base64-encoded, and sent via an HTTPS POST request to a hard-coded URL ("webhook[.]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb").

Version 1.26.2, on the other hand, imports a new top-level module, af\_runtime\_diag.py, collects GitHub Actions OIDC tokens, and expands the search patterns used for harvesting credential-related environment variables.

Given that the package attracts about 190,000 downloads a month, users are advised to perform the following steps -

* Isolate affected hosts and runners
* Pin the package to the most recent safe version (1.26.0) and restore from a clean environment
* Check for exposure to the malicious versions between 8:35 and roughly 9:20 p.m. UTC on November 17, 2026
* Search proxy and DNS logs for requests to webhook[.]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb
* Rotate exposed credential...