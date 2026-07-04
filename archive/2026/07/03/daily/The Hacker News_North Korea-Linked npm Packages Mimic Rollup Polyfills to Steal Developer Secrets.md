---
title: North Korea-Linked npm Packages Mimic Rollup Polyfills to Steal Developer Secrets
url: https://thehackernews.com/2026/07/north-korea-linked-npm-packages-mimic.html
source: The Hacker News
date: 2026-07-03
fetch_date: 2026-07-04T05:49:52.482806
---

# North Korea-Linked npm Packages Mimic Rollup Polyfills to Steal Developer Secrets

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

# [North Korea-Linked npm Packages Mimic Rollup Polyfills to Steal Developer Secrets](https://thehackernews.com/2026/07/north-korea-linked-npm-packages-mimic.html)

**Ravie Lakshmanan**Jul 03, 2026Software Supply Chain / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4otDF6_5qt7ZmrCLMXmx7sFXfY6RGHHI0BiGRcVkTqLo-l1VokprcvB7FhK5fJdL0j8Ds95uLQxiWKt2YYFV1N9K8WIL3lfONey4wBln2Vee4YTI_9z5_t-2VT1bZ17sEomQdONnVWEB3sc9lj13AJwdhbmn6CNlfx9Lwc7UNxg2C87xKFZPz5UL4lHJE/s1700-e365/npms-malware.jpg)

Threat actors with ties to North Korea have been linked to a fresh set of malicious npm packages that masquerade as Rollup polyfill tooling to facilitate remote access and data theft.

According to JFrog, the packages "rollup-packages-polyfill-core" and "rollup-runtime-polyfill-core" mimic the legitimate "[rollup-plugin-polyfill-node](https://www.npmjs.com/package/rollup-plugin-polyfill-node)" project, down to the description, repository metadata, and package shape.

"The lookalike packages place themselves in the same rollup, polyfill, core, and node naming space, which can look plausible during a quick dependency review," JFrog [said](https://research.jfrog.com/post/rollup-polyfill-masquerading/) in a technical write-up of the campaign.

The campaign also involves four other packages, all of which have since been removed from the npm registry -

* quirky-token
* react-icon-svgs
* rollup-plugin-polyfill-connect
* swift-parse-stream

What's noteworthy here is that "rollup-packages-polyfill-core" installs and loads "swift-parse-stream," while "rollup-runtime-polyfill-core" installs and "quirky-token." In a similar fashion, "react-icon-svgs" has been found to install "rollup-plugin-polyfill-connect" as a second stage.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

"The second-stage packages are near-identical SVG utilities that fetch a JSON object from JSONKeeper and eval the model field," the cybersecurity company said. "This layered structure, together with the lookalike names, legitimate-looking metadata, hidden install-time execution, environment checks, and credential-theft/remote-access payloads, is similar to previous North Korean Lazarus-linked npm campaigns."

It's worth emphasizing here that this is not the first time North Korean threat actors have uploaded npm packages impersonating Rollup polyfill tools. In April 2026, Panther [detailed](https://thehackernews.com/2026/06/north-korean-hackers-are-turning.html#:~:text=A%20sustained,OtterCookie) a sustained npm campaign that involved publishing 108 malicious npm packages spanning 261 versions to deliver BeaverTail and OtterCookie, two known malware families linked to Contagious Interview. Among those packages was "rollup-plugin-polyfill-route," which was published on March 20, 2026.

The starting point of the attack is a Base64-encoded npm install command for "swift-parse-stream" (or "quirky-token") that's concealed within "rollup-packages-polyfill-core" (or "rollup-runtime-polyfill-core"). The two second-stage packages are dressed up as SVG sanitization utilities, while reaching out to a JSON Keeper URL to retrieve and execute a JavaScript malware.

The JavaScript code runs checks to avoid execution within cloud development environments, sandboxes, serverless runtimes, and analysis infrastructure. Past this gate, the malware installs the necessary dependencies and reaches out to an external server ("216.126.236[.]244") to fetch an encrypted JavaScript payload.

The decrypted payload then acts as a loader for additional scripts responsible for enabling remote access to the compromised host to support interactive terminal sessions, command execution, screenshot capture, process termination, Windows-only mouse movement, clicks, scrolling, keyboard presses, and hotkeys using the "@nut-tree-fork/nut-js" package, as well as steal data from web browsers and cryptocurrency wallets, collect files matching specific extensions, and periodically capture clipboard content.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjaD0uLDz_dKt6-_w73Qum-1xkqqY0RUUjmGxIcBNNNwVu0u6jr2z9SqNAoP2jdZRnSX_ITooC1EQRGPe70h0dHiuDYl8Gqwa98wur1fGVLKa0gDwr_ORLc0skbRl66QCXxZtR0l-6jCGMGzzcyhkHowryFdzo68h2gTb69C15R4MeKkvsO4HBb2bd7mCv/s1700-e365/polyfill.png)

The features overlap with those of OtterCookie, with the use of "@nut-tree-fork/nut-js" for remote mouse and keyboard control also observed in a package named "express-session-js" that was [detailed](https://thehackernews.com/2026/04/new-wave-of-dprk-attacks-uses-ai.html) by SafeDep in April 2026. The file collector component has been found to specifically look for editor history associated with Microsoft Visual Studio Code, Windsurf, and Cursor, along with developer and AI tool configurations, such as AWS, Microsoft Azure, Google Gemini, Anthropic Claude, Foundry, SSH, and Z shell (Zsh).

"Rollup plugins are commonly loaded from local configuration files, developer workstations, and CI jobs," JFrog said. "These environments often have access to sensitive assets such as source code, npm tokens, Git credentials, cloud keys, SSH keys, browser data, and project secrets."

"The payload is also broader than a simple downloader. Once the later stages run, the attacker gains both collection and control capabilities. This makes the payload relevant to developer workstations and build machines, where API keys, SSH keys, wallet material, cloud credentials, and project secrets are often present."

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

The disclosure coincides with the discovery of multiple software supply ch...