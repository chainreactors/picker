---
title: Shai-Hulud v2 Campaign Spreads From npm to Maven, Exposing Thousands of Secrets
url: https://thehackernews.com/2025/11/shai-hulud-v2-campaign-spreads-from-npm.html
source: The Hacker News
date: 2025-11-26
fetch_date: 2025-11-27T03:13:10.578088
---

# Shai-Hulud v2 Campaign Spreads From npm to Maven, Exposing Thousands of Secrets

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

# [Shai-Hulud v2 Campaign Spreads From npm to Maven, Exposing Thousands of Secrets](https://thehackernews.com/2025/11/shai-hulud-v2-campaign-spreads-from-npm.html)

**Nov 26, 2025**Ravie LakshmananSupply Chain / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghgyXKKmEGWfIkqMuka-PLw6Jrl_bPx6Ptub1wNLhbJpyZDfQbTvmYfoV1wzIKc6af7Axp-KlbkHDgadFI6P1iWAe0g8xbyEmKAZazSUZ1aleKTfRgxF7DOs9yhNmlvQGZWvn8-ovkMv7hy0HBlWjOHFHKGOD1uvLMa-L_ZxRxyCsBrk7w0kL7uGH0idaj/s790-rw-e365/marven-hack.jpg)

The second wave of the [Shai-Hulud supply chain attack](https://thehackernews.com/2025/11/second-sha1-hulud-wave-affects-25000.html) has spilled over to the Maven ecosystem after compromising more than 830 packages in the npm registry.

The Socket Research Team said it identified a Maven Central package named org.mvnpm:posthog-node:4.18.1 that embeds the same two components associated with Sha1-Hulud: the "setup\_bun.js" loader and the main payload "bun\_environment.js."

"This means the PostHog project has compromised releases in both the JavaScript/npm and Java/Maven ecosystems, driven by the same Shai Hulud v2 payload," the cybersecurity company [said](https://socket.dev/blog/shai-hulud-strikes-again-v2) in a Tuesday update.

It's worth noting that the Maven Central package is not published by PostHog itself. Rather, the "org.mvnpm" [coordinates](https://maven.apache.org/pom.html#Maven_Coordinates) are generated via an automated [mvnpm process](https://github.com/mvnpm/mvnpm) that rebuilds npm packages as Maven artifacts. The Maven Central said they are working to implement extra protections to prevent already known compromised npm components from being rebundled. As of November 25, 2025, 22:44 UTC, all mirrored copies have been purged.

The development comes as the "second coming" of the supply chain incident has [targeted](https://thehackernews.com/2025/11/second-sha1-hulud-wave-affects-25000.html) developers globally with an aim to steal sensitive data like API keys, cloud credentials, and npm and GitHub tokens, and facilitate deeper supply chain compromise in a worm-like fashion. The latest iteration has also evolved to be more stealthy, aggressive, scalable, and destructive.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

Besides borrowing the overall infection chain of the initial September variant, the [attack](https://checkmarx.com/zero-post/shai-huluds-second-coming-npm-malware-attack-evolved/) allows threat actors to gain unauthorized access to npm maintainer accounts and publish trojanized versions of their packages. When unsuspecting developers download and run these libraries, the embedded malicious code backdoors their own machines and scans for secrets and exfiltrates them to GitHub repositories using the stolen tokens.

The [attack](https://semgrep.dev/blog/2025/digging-for-secrets-sha1-hulud-the-second-coming-of-the-npm-worm/) accomplishes this by injecting [two rogue workflows](https://www.upwind.io/feed/shai-hulud-2-npm-supply-chain-worm-attack), one of which registers the victim machine as a self-hosted runner and enables arbitrary command execution whenever a GitHub Discussion is opened. A second workflow is designed to systematically harvest all secrets. Over 28,000 repositories have been affected by the incident.

"This version significantly enhances stealth by utilizing the Bun runtime to hide its core logic and increases its potential scale by raising the infection cap from 20 to 100 packages," Cycode's Ronen Slavin and Roni Kuznicki [said](https://cycode.com/blog/shai-hulud-second-coming-supply-chain-attack/). "It also uses a new evasion technique, exfiltrating stolen data to randomly named public GitHub repositories instead of a single, hard-coded one."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDxWhcaeklWjnq_UtYzX84Oj7aLUcauM2UZ9bYwzJ6KYeRClD7iqkGd7t6rbu8i7B7YaAdtG3vI-Z7pFnkAU8q1utWZbyg4MjV1elZQcQT67VJOx-gPUeja3CM7l_dMGVHE0jizTLUce6yHm8c5aHOS3Jf-fUolTuAWSbCeD8C6h0po7Egd8igph_2rOLo/s2600/upwind.jpg)

The attacks illustrate how trivial it is for attackers to take advantage of trusted software distribution pathways to push malicious versions at scale and compromise thousands of downstream developers. What's more, the self-replication nature of the malware means a single infected account is enough to amplify the blast radius of the attack and turn it into a [widespread outbreak](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/) in a short span of time.

Further analysis by Aikido has [uncovered](https://www.aikido.dev/blog/github-actions-incident-shai-hulud-supply-chain-attack) that the threat actors exploited vulnerabilities, specifically focusing on CI misconfigurations in pull\_request\_target and workflow\_run workflows, in existing GitHub Actions workflows to pull off the attack and compromise projects associated with AsyncAPI, PostHog, and Postman.

The vulnerability "used the risky pull\_request\_target trigger in a way that allowed code supplied by any new pull request to be executed during the CI run," security researcher Ilyas Makari said. "A single misconfiguration can turn a repository into a patient zero for a fast-spreading attack, giving an adversary the ability to push malicious code through automated pipelines you rely on every day."

It's assessed that the activity is the continuation of a broader set of attacks targeting the ecosystem that commenced with the August 2025 [S1ngularity campaign](https://thehackernews.com/2025/08/malicious-nx-packages-in-s1ngularity.html) impacting several Nx packages on npm.

"As a new and significantly more aggressive wave of npm supply chain malware, Shai-Hulud 2 combines stealthy execution, credential breadth, and fallback destructive behavior, making it one of the most impactful supply chain attacks of the year," Nadav Sharkazy, a product manager at [Apiiro](https://apiiro.com/blog/shai-hulud-2-a-new-wave-of-...