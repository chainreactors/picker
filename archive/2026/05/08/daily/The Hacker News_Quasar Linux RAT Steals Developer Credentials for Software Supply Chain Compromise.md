---
title: Quasar Linux RAT Steals Developer Credentials for Software Supply Chain Compromise
url: https://thehackernews.com/2026/05/quasar-linux-rat-steals-developer.html
source: The Hacker News
date: 2026-05-08
fetch_date: 2026-05-09T05:09:02.488445
---

# Quasar Linux RAT Steals Developer Credentials for Software Supply Chain Compromise

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Quasar Linux RAT Steals Developer Credentials for Software Supply Chain Compromise](https://thehackernews.com/2026/05/quasar-linux-rat-steals-developer.html)

**Ravie Lakshmanan**May 08, 2026Linux / DevOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiholjenZRIykmReErkRiguk5xd9RV4BIEEPM0nT-o3LvMvDkCTLpd3G0NpqDGEFHp-f6QyvGRMip6CBhGlllYVlp9wS3XBVoV6xW47CDka7Ig8S_aotcuNlmAv3SYgS4hJzxjLp2nrV4SzqlTXnQLG_w68Cq0Bf5hiOoV6CaN9QZliRDa-StzsvIkJAdSF/s1700-e365/kube.jpg)

A previously undocumented Linux implant codenamed **Quasar Linux RAT (QLNX)** is targeting developers' systems to establish a silent foothold as well as facilitate a broad range of post-compromise functionality, such as credential harvesting, keylogging, file manipulation, clipboard monitoring, and network tunneling.

"QLNX targets developers and DevOps credentials across the software supply chain," Trend Micro researchers Aliakbar Zahravi and Ahmed Mohamed Ibrahim [said](https://www.trendmicro.com/en_us/research/26/e/quasar-linux-qlnx-a-silent-foothold-in-the-software-supply-chain.html) in a technical analysis of the malware.

"Its credential harvester extracts secrets from high-value files such as .npmrc (npm tokens), .pypirc (PyPI credentials), .git-credentials, .aws/credentials, .kube/config, .docker/config.json, .vault-token, Terraform credentials, GitHub CLI tokens, and .env files. The compromise of these assets could allow the operator to push malicious packages to NPM or PyPI registries, access cloud infrastructure, or pivot through CI/CD pipelines."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The malware's ability to systematically harvest a wide range of credentials poses a severe risk to developer environments. A threat actor who successfully deploys QLNX against a package maintainer gains unauthorized access to their publishing pipeline, allowing the attacker to push poisoned versions that can lead to cascading downstream impacts.

QLNX executes filelessly from memory, masquerades itself as a kernel thread (e.g., kworker or ksoftirqd), and is capable of profiling the host to detect containerized environments, wiping system logs to cover up the tracks, and setting up persistence using no less than seven different methods, including systemd, crontab, and .bashrc shell injection.

Furthermore, it exfiltrates the collected data to an attacker-controlled infrastructure, and receives commands that make it possible to execute shell commands, manage files, inject code into processes, take screenshots, log keystrokes, establish SOCKS proxies and TCP tunnels, run Beacon Object Files (BOFs), and even manage a peer-to-peer (P2P) mesh network.

Exactly how the malware is delivered is unclear. However, once a foothold is established, it enters a primary operational phase by running a persistent loop that continuously attempts to establish and maintain communication with the command-and-control (C2) server over raw TCP, HTTPS, and HTTP. In total, QLNX supports 58 distinct commands that give the operators complete control of the compromised host.

QLNX also comes with a Pluggable Authentication Module ([PAM](https://thehackernews.com/2026/05/new-linux-pamdoora-backdoor-uses-pam.html)) inline-hook backdoor that intercepts plaintext credentials during authentication events, logs outbound SSH session data, and transmits the data to the C2 server. The malware also supports a second PAM-based credentials logger that's automatically loaded into every dynamically linked process to extract the service name, username, and authentication token.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

It employs a two-tiered rootkit architecture: a userland rootkit deployed through the Linux dynamic linker's LD\_PRELOAD mechanism to ensure that the implant's artifacts and processes stay hidden. There also exists a kernel-level eBPF component that uses BPF subsystem to conceal processes, files, and network ports from standard userland tools such as ps, ls, and netstat upon receiving instructions from the C2 server.

"The QLNX implant was built for long-term stealth and credential theft," Trend Micro said. "What makes it particularly dangerous is not any single feature, but how its capabilities chain together into a coherent attack workflow: arrive, erase from disk, persist through six redundant mechanisms, hide at both userspace and kernel level, and then harvest the credentials that matter most."

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

[Credential Harvesting](https://thehackernews.com/search/label/Credential%20Harvesting), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [DevOps](https://thehackernews.com/search/label/DevOps), [linux](https://thehackernews.com/search/label/linux), [Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan), [rootkit](https://thehackernews.com/search/label/rootkit), [Supply Chain](https://thehackernews.com/search/label/Supply%20Chain)

⚡ Top Stories This Week

[![Harvester Deploys Linux GoGra Backdoor in South Asia Using Microsoft Graph API](data:...