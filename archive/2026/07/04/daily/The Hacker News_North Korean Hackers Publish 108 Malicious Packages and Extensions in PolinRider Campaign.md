---
title: North Korean Hackers Publish 108 Malicious Packages and Extensions in PolinRider Campaign
url: https://thehackernews.com/2026/07/north-korean-hackers-publish-108.html
source: The Hacker News
date: 2026-07-04
fetch_date: 2026-07-05T05:56:25.095733
---

# North Korean Hackers Publish 108 Malicious Packages and Extensions in PolinRider Campaign

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

# [North Korean Hackers Publish 108 Malicious Packages and Extensions in PolinRider Campaign](https://thehackernews.com/2026/07/north-korean-hackers-publish-108.html)

**Ravie Lakshmanan**Jul 04, 2026Cryptocurrency / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwdeBqtwl7nqoAp8TPhZmmr3mUTCcfxluYa7QukD2sI1AjCWoOko2YtQUrCtOLH-tJlYi2lXUA5E3RF51L26gZGyR7sT0GXu73OMB94HhINz5kajaR8-txb-tYNj2Hsm62zVwTaw7Rew6Wazf8eQgo_boWq7DjqbN1jjp5OmwSZ2yG7Y9e04hFVaroUSu6/s1700-e365/go-code.jpg)

The North Korean threat actors linked to the [Contagious Interview](https://attack.mitre.org/groups/G1052/) campaign have been observed publishing 108 unique packages and web browser extensions spanning npm, Packagist, Go, and Google Chrome as part of an ongoing activity referred to as **PolinRider**.

"The campaign remains active, and new malicious packages are likely to continue appearing as threat actors compromise maintainer accounts, modify legitimate repositories, and publish infected package versions where they retain or obtain registry access," Socket security researcher Karlo Zanki [said](https://socket.dev/blog/polinrider-north-korea-linked-supply-chain-campaign-expands) in an analysis published this week.

The [162 malicious release artifacts](https://socket.dev/supply-chain-attacks/polinrider) span multiple release versions corresponding to 108 unique packages and extensions, including 19 npm libraries, 10 Composer packages, 61 Go modules, and one Google Chrome extension.

Contagious Interview is the moniker [assigned](https://thehackernews.com/2026/04/n-korean-hackers-spread-1700-malicious.html) to a North Korea-aligned campaign that [weaponizes](https://about.gitlab.com/blog/how-to-detect-and-prevent-contagious-interview-ide-attacks/) job recruitment to target software developers and individuals working in the cryptocurrency sectors, using persuasive job interviews and assessments to trick them into executing malicious code.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The activity is known to be active since at least 2023. Attackers [masquerade](https://www.fireblocks.com/blog/contagious-interview-recruiting-scam) as recruiters or collaborators on platforms like LinkedIn, GitHub, or freelance websites, often setting up [elaborate front companies](https://www.hlc.com/en/publications/north-korealinked-threat-actors-falsified-companies) and AI-generated employee profiles to build trust and ultimately deliver malware.

PolinRider was [first flagged](https://github.com/OpenSourceMalware/PolinRider) by the OpenSourceMalware team in March 2026, [describing](https://thehackernews.com/2026/03/north-korean-hackers-abuse-vs-code-auto.html) it as involving the threat actors implanting malicious obfuscated JavaScript payloads in hundreds of public GitHub repositories belonging to several unique owners to deliver a new variant of BeaverTail, a known JavaScript malware associated with Contagious Interview.

As of April 11, 2026, the activity has [compromised](https://thehackernews.com/2026/06/malicious-npm-packages-pose-as-postcss.html) 1,951 public GitHub repositories associated with 1,047 unique owners, while also merging with another cluster called [TaskJacker](https://thehackernews.com/2026/06/north-korean-hackers-are-turning.html) that drops malicious VS Code task files into GitHub users' existing repositories. The VS Code tasks include the "runOn: 'folderOpen'" option to trigger the execution of arbitrary code when the folder is opened as a workspace folder in an IDE like VS Code or Cursor.

"The threat actor is not using stolen GitHub credentials," OpenSourceMalware said. "Instead, the victims have been compromised via a malicious VS Code extension or npm package." It's believed that the attackers are taking over maintainer accounts, likely through expired domain takeover or another account recovery path, to pull off the scheme.

Once executed, the malware searches the infected computer for certain files like "postcss.config.mjs," "tailwind.config.js," "eslint.config.mjs," next.config.mjs," babel.config.js," and "app.js," and, if found, appends malicious JavaScript code to them.

It also makes use of a Windows batch script to stealthily modify the last commit, while making it appear as if they were made by the original author. It's suspected that similar tools are being utilized to rewrite Git history for other operating systems like Linux and macOS.

"The core tradecraft remains consistent across the campaign: threat actors plant obfuscated JavaScript loaders in legitimate repositories, conceal the code through whitespace padding or fake .woff2 font files, and trigger execution through developer tooling such as VS Code task files," Socket said.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

In the latest wave, the payload functions as a JavaScript malware loader that reaches out to blockchain infrastructure, including TRON, Aptos, and BNB Smart Chain services, to fetch an encrypted second-stage payload that unpacks to DEV#POPPER RAT and OmniStealer. This attack chain was [detailed](https://thehackernews.com/2026/04/285-million-drift-hack-traced-to-six.html#social-engineering-behind-contagious-interview-and-it-worker-fraud) by eSentire in March 2026.

"The threat actors use Git history rewriting, including force pushes and anti-dated commits to make malicious changes appear older and less suspicious," Zanki said. "This makes the GitHub landing page and visible commit history unreliable indicators of compromise; defenders should review repository activity logs, package release metadata, VS Code task configuration, and suspi...