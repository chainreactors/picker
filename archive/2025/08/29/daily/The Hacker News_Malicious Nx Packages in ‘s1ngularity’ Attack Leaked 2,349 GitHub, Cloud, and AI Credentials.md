---
title: Malicious Nx Packages in ‘s1ngularity’ Attack Leaked 2,349 GitHub, Cloud, and AI Credentials
url: https://thehackernews.com/2025/08/malicious-nx-packages-in-s1ngularity.html
source: The Hacker News
date: 2025-08-29
fetch_date: 2025-10-07T00:49:32.204758
---

# Malicious Nx Packages in ‘s1ngularity’ Attack Leaked 2,349 GitHub, Cloud, and AI Credentials

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

# [Malicious Nx Packages in 's1ngularity' Attack Leaked 2,349 GitHub, Cloud, and AI Credentials](https://thehackernews.com/2025/08/malicious-nx-packages-in-s1ngularity.html)

**Aug 28, 2025**Ravie LakshmananAI Security / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0vDTtGKRVGmC1PGb2PNZIyvrvbO1OWvq_TB_MgSidaZ2bMV05538tTsdn6BTIaAFdT_HQJjPbXY8fr5fOE6zntjqYTPa7SehZMypeWTkfntWh5qnG8bX0NxcBL6TIeHeelt7aMRUermlzzREWsPRz0FF5L28EpLeda2RQwnq44Qog3vEwmvm8-yeFEoOK/s790-rw-e365/code.jpg)

The maintainers of the nx build system have alerted users to a supply chain attack that allowed attackers to publish malicious versions of the popular npm package and other auxiliary plugins with data-gathering capabilities.

"Malicious versions of the nx package, as well as some supporting plugin packages, were published to npm, containing code that scans the file system, collects credentials, and posts them to GitHub as a repo under the user's accounts," the maintainers [said](https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c) in an advisory published Wednesday.

Nx is an open-source, technology-agnostic build platform that's designed to manage codebases. It's advertised as an "AI-first build platform that connects everything from your editor to CI [continuous integration]." The npm package has over 3.5 million weekly downloads.

The list of affected packages and versions is below. These versions have since been removed from the npm registry. The compromise of the nx package took place on August 26, 2025.

* nx 21.5.0, 20.9.0, 20.10.0, 21.6.0, 20.11.0, 21.7.0, 21.8.0, 20.12.0
* @nx/devkit 21.5.0, 20.9.0
* @nx/enterprise-cloud 3.2.0
* @nx/eslint 21.5.0
* @nx/js 21.5.0, 20.9.0
* @nx/key 3.2.0
* @nx/node 21.5.0, 20.9.0
* @nx/workspace 21.5.0, 20.9.0

The project maintainers said the root cause of the issue stemmed from a [vulnerable workflow](https://github.com/nrwl/nx/pull/32458) added on August 21, 2025, that introduced the ability to inject executable code using a specially crafted title in a pull request (PR). While the workflow was reverted in the "master" branch "almost immediately" after it found to be exploitable in a malicious context, the threat actor is assessed to have made a PR targeting an outdated branch that still contained the workflow to launch the attack.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The pull\_request\_target trigger was used as a way to trigger the action to run whenever a PR was created or modified," the nx team said. "However, what was missed is the warning that this trigger, unlike the standard pull\_request trigger, runs workflows with elevated permissions, including a GITHUB\_TOKEN which has read/write repository permission."

It's believed the GITHUB\_TOKEN was utilized to trigger the "publish.yml" workflow, which is responsible for publishing the nx packages to the registry using an npm token.

But with the PR validation workflow running with elevated privileges, the "publish.yml workflow" is triggered to run on the "nrwl/nx" repository while also introducing [malicious changes](https://github.com/nrwl/nx/commit/3905475cfd0e0ea670e20c6a9eaeb768169dc33d) that made it possible to exfiltrate the npm token to an attacker-controlled webhook[.]site endpoint.

"As part of the bash injection, the PR validation workflows triggered a run of the publish.yml with this malicious commit and sent our npm token to an unfamiliar webhook," the nx team explained. "We believe this is how the user got a hold of the npm token used to publish the malicious versions of nx."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXDf2-8WE5pPxPY_fSzgnexsJ28qD0K71oR0OKLRCZckwtRq6XHD5t00AcP5rrVNnjVJuQCn9Wz7XEhkf7pRGsPecSVFrsA-sTb94NnptUvC9Oj_0YlcA6izwoJqnrIBHZuZjWHMMvEsfRUEJoKQYUl-gbseM0iHF6E6wyXE1y8tnwWTF9hnmNx7fyHVio/s790-rw-e365/pack.jpg)

In other words, the injection flaw enabled arbitrary command execution if a malicious PR title was submitted, while the pull\_request\_target trigger granted elevated permissions by providing a GITHUB\_TOKEN with read/write access to the repository.

The rogue versions of the packages have been found to contain a postinstall script that's activated after package installation to scan a system for text files, collect credentials, and send the details as a Base64-encoded string to a publicly accessible GitHub repository containing the name "s1ngularity-repository" (or "s1ngularity-repository-0" and "s1ngularity-repository-1") under the user's account.

"The malicious postinstall script also modified the .zshrc and .bashrc files which are run whenever a terminal is launched to include sudo shutdown -h 0 which prompt users for their system password and if provided, would shut down the machine immediately," the maintainers added.

While GitHub has since started to archive these repositories, users who encounter the repositories are advised to assume compromise and rotate GitHub and npm credentials and tokens. Users are also recommended to stop using the malicious packages and check .zshrc and .bashrc files for any unfamiliar instructions and remove them.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4AWXack-FUwNT7bccUpm8cEN3b3TpAvSvZzBLrtub-hbnww7uQQ6rabKaFoXeIRwOTUKBXvP9LYVMX1EJtAM31kYoYOTT44IhNb4hM9a5EFVYR-aBzF2CeBUw5BozoZQiwr76SWRTa3lyHbFZ7xsYGCxobsj6fsoCE1IAR2Ypp-xQ-q8nn3NYEUR7zElD/s790-rw-e365/valid.jpg) |
| Image Source: GitGuardian |

The nx team said they have also undertaken remedial actions by rotating their npm and GitHub tokens, auditing GitHub and npm activities across the organization for suspicious activities, and updating Publish access for nx to require two-factor authentication (2FA) or automation.

Wiz researchers Merav Bar and Rami McCarthy said 90% of over 1,000 leaked GitHub tokens are still valid, and that there also exist dozens of legitimate cloud credentia...