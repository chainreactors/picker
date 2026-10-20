---
title: GhostAction Attackers Plant Credential Stealer Disguised as Font in 94 GitHub Repositories
url: https://thehackernews.com/2026/10/ghostaction-attackers-plant-credential.html
source: The Hacker News
date: 2026-10-19
fetch_date: 2026-10-20T06:53:58.486473
---

# GhostAction Attackers Plant Credential Stealer Disguised as Font in 94 GitHub Repositories

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

# [GhostAction Attackers Plant Credential Stealer Disguised as Font in 94 GitHub Repositories](https://thehackernews.com/2026/10/ghostaction-attackers-plant-credential.html)

**Ravie Lakshmanan**Oct 19, 2026Developer Security / Supply Chain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhtAKfaW5dHhlv9lpzzAju1Cm_EjO4wOkhGQEMspSKCVFUCA_eaanAXGHkb-Dv3c9zSXWHW45I50Fp_bqX6ydaNlPWixkd39bl4IOeYv8xQ0oviE4d6SZcQmQ27ztf-tVV7BozEDeFYi2Fde0LpJAJ9gTHUGSOvc46MtgawesAd5-wljApeBpLyUYnczZnR/s1700-nu-rw-lo-l85-e365/git-font.jpg)

The threat actor behind the **[GhostAction](https://thehackernews.com/2026/10/ghostaction-compromises-about-1900.html)** supply chain attack has expanded beyond injecting malicious GitHub Actions workflows into compromised projects to phish open-source developers and deliver a stealer malware disguised within a fake font file.

The latest evolution, detailed by OpenSourceMalware, signals that the attackers are actively refining their modus operandi in response to steps taken by GitHub to prevent the workflow from running.

According to the threat intelligence platform, the threat actor registered the domain "[my-github[.]com](https://www.virustotal.com/gui/url/65d01eddf5e47f5f92bbb139052c3eee0f17e8a65e1206491ca382b282874f8b)" and pointed it at "[193.32.204[.]199](https://thehackernews.com/2026/10/credential-stealing-github-actions.html)," the same IP address that's used as an exfiltration endpoint for data harvested from running the malicious workflow.

The domain was registered on October 9, 2026, 17 days after "[my-gitlab[.]com](https://www.virustotal.com/gui/domain/my-gitlab.com)" was registered. There is no evidence at this stage to suggest that the two code-hosting-themed domains are operated by the same threat actor.

"It follows the same my-<code-host>.com naming pattern, making it a useful pivot, but current infrastructure does not directly connect it to GhostAction," security researcher Paul McCarty [said](https://opensourcemalware.com/blog/ghostaction-attack-escalates). "They use different registrars, registrant records, Cloudflare nameserver pairs, IP addresses, ASNs, and DNS designs, and no shared certificate or account artifact has been recovered."

Since then, the "my-github[.]com" domain has been used in a phishing email impersonating a GitHub security alert to target an open-source maintainer. The message, sent from "noreply@my-github[.]com" and on the same day the domain was registered, warned of a suspicious new login to their GitHub account from Moscow, Russia, and instructed them to click on a link to secure their account.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The deceptive page, per OpenSourceMalware, is said to have acted as a reverse proxy, harvesting the victim's password and two-factor authentication (2FA) code, and injected JavaScript that authorized an OAuth app with permissions to modify their workflows so as to facilitate a GhostAction-style attack.

The fake login page also includes JavaScript to silently authorize a [GitHub OAuth device flow](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps#device-flow) with [repo, workflow, and read:org scopes](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps), granting it broad permissions to read/write repositories, modify Actions workflow files, and gain visibility into organization membership and related organizational data.

The idea is the same as [device code phishing](https://thehackernews.com/2026/09/microsoft-takes-down-eviltokens-device.html), where the end goal is to obtain an access token from GitHub and exfiltrate it to "my-github[.]com" on TCP/8443.

"The script receives a device code and user code, loads /login/device, extracts GitHub's forms from the returned HTML, and submits them automatically," McCarty explained. "It inserts the user code, locates an authorization form, adds authorize=1, and posts the approval through the victim's authenticated proxied session."

"The victim does not need to type the device code or consciously approve the OAuth application. This kit goes further by automating the user-code and authorization steps through the reverse-proxied session."

By stealing a repository-scoped OAuth token, it gives the attacker a reusable API credential. Furthermore, the permissions granted through the stealthy OAuth authorization are consistent with GhostAction's ability to enumerate repositories and inject malicious workflow files under ".github/workflows/."

"The actor can now combine repository-scale automation with individual social engineering against people whose accounts provide access to projects, organizations, registries, and downstream users," OpenSourceMalware said.

To make matters worse, the campaign has also been observed incorporating a second-stage component that persists on developer machines even after the malicious workflow has been removed.

Specifically, the approach takes a leaf out of North Korea's playbook by committing three different files -

* A Microsoft Visual Studio Code (VS Code) tasks.json file with a "[runOn: folderOpen](https://thehackernews.com/2026/03/north-korean-hackers-abuse-vs-code-auto.html)" trigger that causes it to run automatically when the folder is opened in the application.
* A "public/fonts/fa-solid-400.woff2" file that contains a stealer payload designed to harvest AWS keys, PyPI tokens, npm tokens, Git logins, Kubernetes cluster credentials, SSH private keys, and AI provider credentials for Anthropic Claude and Google Gemini. The font file name is the same as one used in North Korea's [Fake Font/PolinRider](https://thehackernews.com/2026/07/north-korean-hackers-publish-108.html) campaign from [January 2026](https://thehackernews.com/2026/06/hijacked-npm-and-go-packages-use-vs.html).
* A second GitHub Actions workflow that's activated if...