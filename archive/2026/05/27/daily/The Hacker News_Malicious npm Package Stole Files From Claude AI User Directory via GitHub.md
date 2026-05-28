---
title: Malicious npm Package Stole Files From Claude AI User Directory via GitHub
url: https://thehackernews.com/2026/05/malicious-npm-package-stole-files-from.html
source: The Hacker News
date: 2026-05-27
fetch_date: 2026-05-28T06:03:52.038076
---

# Malicious npm Package Stole Files From Claude AI User Directory via GitHub

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

# [Malicious npm Package Stole Files From Claude AI User Directory via GitHub](https://thehackernews.com/2026/05/malicious-npm-package-stole-files-from.html)

**Ravie Lakshmanan**May 27, 2026Threat Intelligence / Supply Chain Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlezHawmKBTFBZSgR52vL_EBxfwIlMa0i4LdDK2xC_c8nw704KQHbRNSHYAy8TY4ShZMFwAJoZKUBSDJBCVnwbORTlz7iE0JI9f9ORbQQ-RB5lA_b9VbUzAsjpVeW2oJ94hdfzOeCWN3zd5Li7zWanNx3s07cF8IRlWuVrLqBNaY0sobbJww1Pa_o2t4JN/s1700-e365/npm-ai.jpg)

Cybersecurity researchers have discovered a new malicious package on the npm registry that comes with information stealing capabilities.

According to OX Security, the package, named "[mouse5212-super-formatter](https://www.npmjs.com/package/mouse5212-super-formatter)," is designed to upload files from "/mnt/user-data," a dedicated directory used by Anthropic's Claude artificial intelligence (AI) tool to handle uploads and outputs in the background. The activity has been codenamed **Malware-Slop**.

"By analyzing the malware, it turns out that the script presents itself as an internal 'archive deployment sync' utility that validates or initializes a GitHub repository, captures a lightweight 'network status' snapshot, and then performs a structured synchronization of local workspace files into a remote tracking tree," researchers Moshe Siman Tov Bustan and Nir Zadok [said](https://www.ox.security/blog/malware-slop-new-malicious-npm-package-leaks-its-own-github-private-token/).

In reality, however, it authenticates to GitHub during the postinstall stage, either using a GitHub access token found in the victim's environment or a hard-coded token as a fallback, checks whether a target repository exists, and if not, creates it, and then recursively uploads every file to a threat actor-controlled [GitHub account](https://github.com/unplowed3584).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The stolen files are stored within randomly named folders to help the operator distinguish between different theft sessions. The malware also writes a fake "network connections" log to give the impression that it's sending diagnostic information, while obscuring its true operational behavior of unauthorized collection and remote transfer of local data.

The package is still available for download from npm and is estimated to have been downloaded 676 times. However, how many of these correspond to actual installs remains unclear. The GitHub account linked to the campaign is no longer available, although OX noted that it was created on May 26, 2026, a few hours before the first malicious version was uploaded to npm.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisDtGOUM_09my2t_GKZkxhTSkFzhtaH9Kq8wTeoG3jP6Xn0CMyGgaLo60uOhyphenhyphenm6UCm20Inap0J69-JXjQdAjoa-l6wMf6n-TZRNSOLadTJxE1kBC7bCTEwLwsAgw0rKRu8Q_-pTLb7y2gkm9SCPcLaVKWfEksl3opL4lVPoLTYaaQeGigQf-_HrJFXwJ3X/s1700-e365/image-191-1024x722.jpg)

What's notable about the package is that it leaked details of the GitHub account, including its private token, raising the possibility that the threat actor is using AI to generate malware while not implementing basic operational security (OPSEC) best practices.

"Now that the bar to create malicious code was reduced significantly, we're going to see more threat actors getting into the game - uploading more sloppy malwares, mostly mimicking APT groups to get a slice of the cake until npm starts automatically blocking malware completely," OX Security said.

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

[Anthropic](https://thehackernews.com/search/label/Anthropic), [Claude AI](https://thehackernews.com/search/label/Claude%20AI), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [data theft](https://thehackernews.com/search/label/data%20theft), [GitHub](https://thehackernews.com/search/label/GitHub), [Malware](https://thehackernews.com/search/label/Malware), [NPM](https://thehackernews.com/search/label/NPM), [Open Source Security](https://thehackernews.com/search/label/Open%20Source%20Security), [Supply Chain Attack](https://thehackernews.com/search/label/Supply%20Chain%20Attack), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

⚡ Top Stories This Week

[![Claude Mythos AI Finds 10,000 High-Severity Flaws in Widely Used Software](data:image/svg+xml;base64... "Claude Mythos AI Finds 10,000 High-Severity Flaws in Widely Used Software")

Claude Mythos AI Finds 10,000 High-Severity Flaws in Widely Used Software](https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html)

[![Megalodon GitHub Attack Targets 5,561 Repos with Malicious CI/CD Workflows](data:image/svg+xml;base64... "Megalodon GitHub Attack Targets 5,561 Repos with Malicious CI/CD Workflows")

Megalodon GitHub Attack Targets 5,561 Repos with Malicious CI/CD Workflows](https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html)

[![ThreatsDay Bulletin: Linux Rootkits, Router 0-Day, AI Intrusions, Scam Kits and 25 New Stories](data:image/svg+xml;base64... "ThreatsDay Bulletin: Linux Roo...