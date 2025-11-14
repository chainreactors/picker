---
title: Over 67,000 Fake npm Packages Flood Registry in Worm-Like Spam Attack
url: https://thehackernews.com/2025/11/over-46000-fake-npm-packages-flood.html
source: The Hacker News
date: 2025-11-13
fetch_date: 2025-11-14T03:13:42.929302
---

# Over 67,000 Fake npm Packages Flood Registry in Worm-Like Spam Attack

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

# [Over 67,000 Fake npm Packages Flood Registry in Worm-Like Spam Attack](https://thehackernews.com/2025/11/over-46000-fake-npm-packages-flood.html)

**Nov 13, 2025**Ravie LakshmananSoftware Supply Chain / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYS26azmd2_hhOZvimLT0xZHe62lE9WVPNiqVvatrXANuYx-pkBp8n1v_eAPLoq4FmVbgv3ACPPlFk_BpqpGAVQ8X-yMGCWcuZjYocPiYlpJDhw6ITx-CXQzdJPF3FM6jbxrcRexNpyEzW4PDjzuLkjSRooPvCoLYaN56M5xWkSOqAIiYV1BetoeqLe1ZN/s790-rw-e365/npms.jpg)

Cybersecurity researchers are calling attention to a large-scale spam campaign that has flooded the npm registry with thousands of fake packages since early 2024 as part of a likely financially motivated effort.

"The packages were systematically published over an extended period, flooding the npm registry with junk packages that survived in the ecosystem for almost two years," Endor Labs researchers Cris Staicu and Kiran Raj [said](https://www.endorlabs.com/learn/the-great-indonesian-tea-theft-analyzing-a-npm-spam-campaign) in a Tuesday report.

The coordinated campaign has so far published as many as [67,579 packages](https://github.com/6mile/Indonesian-Foods-Worm), according to SourceCodeRED security researcher Paul McCarty, who [first flagged](https://sourcecodered.com/indonesianfoods-npm-worm/) the activity. The end goal is quite unusual – It's designed to inundate the npm registry with random packages rather than focusing on data theft or other malicious behaviors.

The worm-life propagation mechanism and the use of a distinctive naming scheme that relies on Indonesian names and food terms for the newly created packages have lent it the moniker **IndonesianFoods Worm**. The bogus packages masquerade as Next.js projects.

"What makes this threat particularly concerning is that the attackers took the time to craft an NPM worm, rather than a singular attack," McCarty said. "Even worse, these threat actors have been staging this for over two years."

Some signs that point to a sustained, coordinated effort include the consistent naming patterns and the fact that the packages are published from a small network of over a dozen npm accounts.

The worm is located within a single JavaScript file (e.g., "auto.js" or "publishScript.js") in each package, staying dormant until a user manually runs the script using a command like "node auto.js." In other words, it does not execute automatically during installation or as part of a "postinstall" hook.

It's not clear why someone would go to the extent of running the JavaScript file manually, but the existence of over 43,000 packages suggests either multiple victims executed the script – either by accident or out of curiosity – or the attackers ran it themselves to flood the registry, Henrik Plate, head of security research at Endor Labs, told The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

"We haven't found evidence of a coordinated social engineering campaign, but the code was written with social engineering potential, possible victim scenarios include: fake blog posts, tutorials, or README entries instructing users to run 'node auto.js' to 'complete setup' or 'fix a build issue,' [and] CI/CD pipeline build scripts with wildcards something like node \*.js that execute all JavaScript files," Raj added.

"The payload's dormant design is intended to evade automated detection, by requiring manual execution instead of 'autorun,' the attackers reduce the chance of being flagged by security scanners and sandboxing systems."

The manual execution causes the script to initiate a series of actions in an [infinite loop](https://en.wikipedia.org/wiki/Infinite_loop), including removing <["private": true](https://docs.npmjs.com/cli/v7/configuring-npm/package-json#private)> from the "package.json" file. This setting is typically used to prevent accidental publication of private repositories. It then proceeds to create a random package name using the internal dictionary and assign it a random version number to bypass npm's duplicate version detection.

In the final stage, the spam package is uploaded to npm using the "npm publish" command. The entire process is repeated in an endless loop, causing a new package to be pushed out every 7 to 10 seconds. This translates to about 12 packages per minute, 720 per hour, or 17,000 per day.

"This floods the NPM registry with junk packages, wastes infrastructure resources, pollutes search results, and creates supply chain risks if developers accidentally install these malicious packages," McCarty said.

According to Endor Labs, the campaign is part of an attack that was first documented by [Phylum](https://thehackernews.com/2024/04/beware-githubs-fake-popularity-scam.html) (now part of Veracode) and [Sonatype](https://www.sonatype.com/blog/devs-flood-npm-with-10000-packages-to-reward-themselves-with-tea-tokens) in April 2024 that involved the publication of thousands of spam packages to conduct a "massive automated crypto farming campaign" by abusing the [Tea protocol](https://tea.xyz).

"What makes this campaign particularly insidious is its worm-like spreading mechanism," the researchers said. "Analysis of the 'package.json' files reveals that these spam packages do not exist in isolation; they reference each other as dependencies, creating a self-replicating network."

Thus, when a user installs one of the spam packages, it causes npm to fetch the entire dependency tree, straining registry bandwidth as more dependencies are fetched exponentially.

Endor Labs said some of the attacker-controlled packages, such as arts-dao and gula-dao, include a tea.yaml file listing five different TEA accounts. The Tea protocol is a decentralized framework that allows open-source developers to be [rewarded](https://docs.tea.xyz/tea/i-want-to.../learn-about-proof-of-contribution/what-is-tearank) for their software contributions.

This likely indicates that the threat actors are using this campaign as a monetization ...