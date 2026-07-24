---
title: Attackers Weaponize GitHub Actions Runners to Target cPanel and WHM Servers
url: https://thehackernews.com/2026/07/attackers-weaponize-github-actions.html
source: The Hacker News
date: 2026-07-23
fetch_date: 2026-07-24T05:05:41.989690
---

# Attackers Weaponize GitHub Actions Runners to Target cPanel and WHM Servers

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Attackers Weaponize GitHub Actions Runners to Target cPanel and WHM Servers](https://thehackernews.com/2026/07/attackers-weaponize-github-actions.html)

**Ravie Lakshmanan**Jul 23, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrnUDzSA-4xfOL6dsXt2pFY9jJro2vbjOgvkTbiFMhSXz9Z-0WdDTORe9IPFfMr0DVr0PapP8lFuq8R12ZXRyDdMO-2v9ot7c2oy2WobbNwqn3jbKQC5XmNdgKWZB8ENBVQSADLuujJMKvd3DtNcpAFhDa5zihJDtYrQYRLMSCftHHmNg2bUiRC_gCQkFK/s1700-e365/github-action.jpg)

Cybersecurity researchers have [shed light](https://socket.dev/blog/github-actions-abuse-powers-cpanel-and-whm-exploitation) on a large-scale campaign that has turned compromised GitHub repositories into distributed attack infrastructure designed to target cPanel and WebHost Manager (WHM) instances.

The activity involves malicious Packagist development versions spanning 10 packages associated with a legitimate PHP and DevOps developer, dinushchathurya, between July 12 and 13, 2026. The list of affected Packagist packages is below -

* dinushchathurya/nationality-list
* dinushchathurya/srilankan-divisional-secretariats
* dinushchathurya/srilankan-gn-divisions
* dinushchathurya/srilankan-local-authorities
* dinushchathurya/srilankan-mobile-number-validator
* dinushchathurya/srilankan-state-hospitals
* dinushchathurya/srilankan-universities
* dinushchathurya/uk-mobile-number-validator
* dinushchathurya/uk-post-code
* dinushchathurya/websmslk

"The PHP libraries were not the execution path," Socket said in a statement. "Attackers had added dozens of malicious GitHub Actions workflows to the compromised maintainer's source repositories."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The workflows, once triggered by a repository push or manual run, launch GitHub-hosted runners, download a Linux payload from attacker-controlled infrastructure, and scan for vulnerable cPanel and WHM servers susceptible to [CVE-2026-41940](https://thehackernews.com/2026/05/cpanel-cve-2026-41940-under-active.html), an authentication bypass vulnerability that allows remote attackers to gain elevated control of the control panel.

The payload, for its part, attempts an authentication bypass, and then proceeds to harvest credentials, configuration files, environment variables, database access, SSH material, Git tokens, cloud keys, payment service credentials, and other valuable secrets.

The exact method by which the threat actor gained unauthorized access to the developer's account and pushed malicious changes to the repositories remains unclear.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoKkkZcd2__5LtMXG0qJGEWVlAPRAJSlya5vLLj-SdmXJqsWmW-BwiJv-onvjKZxBND2AmDn-rm8qeJajW5RiO8FKleTw52Rg-C_bff8p_EkmC6qLXLy3lxwMBFHhNERPeVQQmFaQf_tB-0Gw0z9R2A0vUspliJo-ZXaIP40u79AkREGmp9_0V6DzKDhI0/s1700-e365/github-actipn.jpg)

"Between July 12 and 13, 2026, Packagist automatically synchronized malicious development versions across all ten packages associated with the compromised developer, reflecting changes the threat actor pushed to the developer's GitHub repositories," Socket researcher Kirill Boychenko said.

Each of the affected development versions has been found to contain anywhere between 55 and 62 malicious GitHub Actions workflow files, totaling 583 files across all ten package versions.

Specifically, the YAML automation files launch GitHub-hosted runners when the compromised repository receives a push or when the workflow is manually launched, detect each runner's processor architecture (e.g., 32-bit x86, 64-bit x86, 32-bit ARM, and 64-bit ARM systems), and download a compatible Linux scanning and exploitation payload from the command and control (C2) server at 43.228.157[.]68.

"The workflows continuously report execution status to the threat actor and upload newly collected results through HTTP POST requests," Boychenko added. "The output files they monitor include AWS credentials, GitHub and GitLab tokens, OpenAI and Google API credentials, Stripe keys, SendGrid and Mailgun credentials, database information, SSH data, Git remotes, and remote code execution results."

Unlike other traditional malicious package campaigns, the latest activity does not rely on package users' systems. Instead, the scanning and exploitation run on GitHub-hosted runners launched from compromised repositories, meaning GitHub Actions is abused to power an exploitation campaign aimed at hunting for vulnerable cPanel and WHM servers.

Signs point to a broader campaign that extends beyond one PHP maintainer, with roughly 6,100 workflow files hosted on GitHub containing a unique DNSHook identifier ("f5b0b742-240a-4811-8a5b-b0ba6060685d").

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEam_lwcO99GBIwGSn6ZFnP1xQQrioIR3f48tXRDqlXXdZWqO9NSZDzRhvEOKwhhHldlNkoCcWkIk6yt0BbVnVkqgcRXt8ccL4TrqbqtS1v8JVIPsrfN-OxPtuJwMtO1MLxtvpTJBj5wCCMqpG-d0zEx8_sPKtPfoBJA8GT5A1e_fGighbFqIVEkRmSvUw/s1700-e365/flow-git.jpg)

Socket described the campaign as a case of "opportunistic server-side credential theft operation," allowing the attackers to leverage the stolen data for follow-on compromises or monetization pathways.

The disclosure comes as the application security firm also detailed a campaign codenamed [Operation Muck and Load](https://socket.dev/blog/malicious-go-module-exposes-github-malware-lure-network) that abuses a network of 200 GitHub repositories across 190 accounts to deliver Windows-based malware, including information stealers, loaders and downloaders, droppers, spyware, remote access trojans, and Monero cryptocurrency miners.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3-o9La7DYm6jz5qcavVBLvRXUoQLqwrMmrvB529PbUxdg7TJZS3BMjVi4D7vd6V9vlSf_OX48mmXQWPgah_SPITaGgg4AP9YxB2AH-63YeWU39N3DXadwc_2zjIpTwCt0iyTdPZIM-KzKhDf_JDPWDGu3IbYfi1ilQE8Ly29HiKYagSIur-il4k7MMNv8/s728-e100/sygni...