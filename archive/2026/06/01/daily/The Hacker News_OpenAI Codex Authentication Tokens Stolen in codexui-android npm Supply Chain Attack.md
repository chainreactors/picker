---
title: OpenAI Codex Authentication Tokens Stolen in codexui-android npm Supply Chain Attack
url: https://thehackernews.com/2026/06/openai-codex-authentication-tokens.html
source: The Hacker News
date: 2026-06-01
fetch_date: 2026-06-02T06:33:16.586415
---

# OpenAI Codex Authentication Tokens Stolen in codexui-android npm Supply Chain Attack

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [OpenAI Codex Authentication Tokens Stolen in codexui-android npm Supply Chain Attack](https://thehackernews.com/2026/06/openai-codex-authentication-tokens.html)

**Ravie Lakshmanan**Jun 01, 2026API Security / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4veBAmEJHF2nXN_nIgXeWxVSxlTDBc6uWiLwVCYNUqGMF9ZtPre3zF_CXmGnAxX2rbqfwgm_Au0tXvYwv1oTGim1STiGCeVOyMXglUTd-3LeJEN3q718Fdlck9mbQ6aUUYP0NM9S7bakZ4_XF5HHYH-cz2QmKBlge6xNMxbbEjDjZQ4wd1maPKnjgKrsu/s1700-e365/codex.png)

Cybersecurity researchers have disclosed details of a new malicious supply chain campaign that's targeting developers using OpenAI Codex through a legitimate-looking remote web UI.

The tool, named [codexui-android](https://www.npmjs.com/package/codexui-android), is advertised on GitHub and npm as a remote web UI for OpenAI Codex, attracting over 29,000 weekly downloads. The package is still available for download from the repository.

What makes this activity noteworthy is that it's not a traditional attack that uses a typosquat or throwaway package to trick developers. Rather, the malicious code is embedded into a functional npm package that has undergone active development. The associated GitHub repository remains clean.

"And for the past month, every single invocation has been quietly exfiltrating your Codex authentication tokens to an attacker-controlled server," Aikido Security researcher Charlie Eriksen [said](https://www.aikido.dev/blog/codex-remote-ui-steals-ai-tokens).

The nefarious changes are said to have been introduced about a month after the package was published to the registry, likely in an effort to build user trust and expand its reach. The npm account associated with the package is "friuns" (aka Igor Levochkin).

Present within the package is code that extracts the contents of Codex's "~/.codex/auth.json" file and exfiltrates them to a remote server ("sentry.anyclaw[.]store") that masquerades as Sentry, a legitimate application monitoring and error tracking platform. The captured data includes the following details: access\_token, refresh\_token, id\_token, and account ID.

"The refresh\_token doesn't expire," Eriksen said. "An attacker holding it can silently impersonate you indefinitely. A stolen Codex refresh\_token goes beyond access to a chat interface -- it's persistent, silent access to whatever that account can do."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

It's worth mentioning here that every time a user logs in to the Codex app, CLI, or IDE Extension using either ChatGPT or an API key, the login details are cached locally in a plaintext file at ~/.codex/auth.json or in the operating system-specific credential store.

"If you use file-based storage, treat ~/.codex/auth.json like a password: it contains access tokens," OpenAI [warns](https://developers.openai.com/codex/auth) in its support documentation. "Don't commit it, paste it into tickets, or share it in chat."

Interestingly, the npm package is far from the only delivery vector the threat actor uses to target Codex developers. Aikido said it observed an Android application named [OpenClaw Codex Claude AI Agent](https://play.google.com/store/apps/details?id=gptos.intelligence.assistant) (package name: "gptos.intelligence.assistant") that runs the npm package within its PRoot sandbox and sends the Codex credentials to the same endpoint.

"The APK itself is small (26 MB) and looks clean on a Play pre-publish scan," Eriksen explained. "On first run, it extracts a Termux-derived Linux userland into the app's private storage and runs Node.js inside it via PRoot."

"The version is not pinned, so the device pulls whatever is currently published on npm. The exfiltration has been in place since codexui-android@0.1.82. The package runs inside the app's PRoot sandbox, where the in-app Codex sign-in writes its auth.json. Once the user signs in, the package reads that file out of the sandbox and ships the full OAuth blob to sentry.anyclaw.store/startlog."

Released by an entity named "BrutalStrike," the Android app has more than 50,000 downloads. The same exfiltration chain has also been flagged in a second Android app linked to BrutalStrike: Codex (package name: "codex.app"), which has been downloaded over 10,000 times. The remaining three apps offered by the developer do not contain the functionality.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEn6NJdEnKoK9GkNTjgKXXYoRIoiDOekSO6DTQqVaAngk09_mFGeO-SQ-8A1mJBB0QKiXeC1sVVUjIChyEeZe0R46ssuG38JgKss_rKS9IJ8jUGlV_XVl9itMGsEraQnK2GnzuhK7XcnF8BWUCXLAAi2hMuQLuDGtXGrQ4kBTKQc4fc9ixFqZFgbgkR8wb/s1700-e365/brutal.png)

Upon [reaching out](https://github.com/friuns2/codex-mobile/issues/198) to the package author on GitHub, Aikido said they initially posted a comment stating they had lost access to their npm account, only to edit the response and post a different one in which they claimed they are "currently investigating this issue internally" and that they "have started removing the affected functionality and related data."

The author further claimed no credential data was shared with any third parties, without answering why this code was inserted only into the npm package build or why they needed access to the Codex tokens in the first place. The [X profile](https://x.com/friuns2) linked to the author includes the domain "anyclaw[.]store."

WHOIS records [indicate](https://whois.domaintools.com/anyclaw.store) that the domain was registered on April 12, 2026, just two days after the very first version of the npm package (version 0.1.72) was uploaded to npmjs[.]com.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The development comes as threat actors are increasingly targeting real artificial intelligence (AI) developer tooling and workflows to steal credentials and burrow deeper into the software supply chain.

Late last month, the...