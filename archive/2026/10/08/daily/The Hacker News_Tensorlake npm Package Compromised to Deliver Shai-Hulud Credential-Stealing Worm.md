---
title: Tensorlake npm Package Compromised to Deliver Shai-Hulud Credential-Stealing Worm
url: https://thehackernews.com/2026/10/tensorlake-npm-package-compromised-to.html
source: The Hacker News
date: 2026-10-08
fetch_date: 2026-10-09T08:12:13.210068
---

# Tensorlake npm Package Compromised to Deliver Shai-Hulud Credential-Stealing Worm

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

# [Tensorlake npm Package Compromised to Deliver Shai-Hulud Credential-Stealing Worm](https://thehackernews.com/2026/10/tensorlake-npm-package-compromised-to.html)

**Ravie Lakshmanan**Oct 08, 2026Artificial Intelligence / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1ZJrw-vCazDC3YJlfmY9WewJ170my9lYex6Ccg7VTa8UQCrXWoCiy_F9w_LoP-GDEarC_RoYnx63fAa_i_RmR5564MS6tgcoqi77wlcqPzX7kambOt4Gga7rsMlWWBwyHKZtCb1lAowiE4bf5up8aIJuwoVsZSKTq15TTynJ-uNPirAGnY8uwMMGqBsgU/s1700-nu-rw-lo-l85-e365/npm-hack.jpg)

The npm package known as "[tensorlake](https://www.npmjs.com/package/tensorlake?activeTab=versions)," a TypeScript software development kit (SDK) for [Tensorlake](https://www.tensorlake.ai) applications, sandboxes, and cloud services, was [compromised](https://github.com/tensorlakeai/tensorlake/issues/1014) as part of a [ChainDrop / Shai-Hulud](https://thehackernews.com/2026/08/open-vsx-removes-77-malicious-evil-twin.html) supply chain attack.

The malicious version 0.5.144 "contains obfuscated malware that harvests credentials, exfiltrates secrets, establishes persistence, and executes remotely supplied code," Socket [said](https://socket.dev/blog/tensorlake-compromise). Version 0.5.144 is no longer available for download from the npm package registry.

An analysis of the compromised release shows that it contains a preinstall hook designed to launch a JavaScript file ("package/lib/setup.mjs"), an obfuscated loader that launches the main credential-stealing and self-propagating worm ("package/lib/Math\_Symbol.js") using the Bun runtime.

The stealer malware is designed to harvest credentials across local files, CI environments, Kubernetes, and Vault sources. It also [drops](https://x.com/OliverAikido/status/2108012888304853260) the [HackBrowserData](https://thehackernews.com/2024/12/new-glutton-malware-exploits-popular.html) binary, exfiltrates the collected data, establishes persistence on the host, and facilitates the execution of remotely-supplied code.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

"That combination extends the risk beyond a single stolen API key," Socket said. "Any secrets accessible to the executing process may be exposed, and persistence can retain attacker access after the affected dependency is removed."

The types of data stolen by the malware are below -

* npm tokens
* GitHub tokens
* Amazon Web Services (AWS) credentials and secrets
* HashiCorp Vault
* Kubernetes credentials
* SSH keys
* .env files
* Cryptocurrency wallets
* Messaging app data
* Configuration and MCP files associated with Anthropic Claude, Cursor, Kiro, Windsurf, and Zed

"To propagate, the worm enumerates packages associated with the victim's publishing identity, builds Sigstore provenance, and republishes compromised versions," Socket explained. "Strings referencing a fake Copilot/Dependabot workflow suggest it also plants GitHub Actions workflows."

The malware makes use of [multiple data exfiltration channels](https://safedep.io/tensorlake-npm-compromise-mini-shai-hulud/). It first attempts to post the information to "iseekaigogo[.]com:443/router." If this fails, it reads an [Ethereum contract](https://etherscan.io/address/0xb614155Fd88114d40549b259457Bcf921Df091B9) to resolve its command-and-control (C2) endpoint ("iseekaigogo[.]com").

Alternatively, GitHub acts as a fallback mechanism to stage the encrypted stolen data in a public repository with the description "Shai-Hulud: Here We Go Again." It also searches signed GitHub commits for the pattern "thebeautifulmarchoftime" and ensures they are signed with an embedded RSA key.

In addition, there exists a "hostage token" component that uses a PowerShell monitor to repeatedly poll "api.github.com/user" using the stolen GitHub token to check if the token is valid. Should the victim take steps to revoke the token, the monitor proceeds to execute an attacker-supplied handler through the "Invoke-Expression" cmdlet to execute PowerShell code designed to wipe the home directory – a tactic observed in [earlier Shai-Hulud waves](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html).

According to StepSecurity, the malicious files were pushed to the main branch of tensorlakeai/tensorlake under a maintainer's name, after which the package was released from that same repository. The [first rogue commit](https://github.com/tensorlakeai/tensorlake/commit/e90c47bbb208e99cac8aa678405b2133f6cb3f52) took place on October 7, 2026, at 01:20 a.m. UTC. A day later, the repository's release workflow [published](https://github.com/tensorlakeai/tensorlake/tree/6386121c561e74fec143a138d5cc3d3bbabdfe8c/typescript/lib) 0.5.144 to npm.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

"The malware also writes .claude/settings.json and .vscode/tasks.json files into repos it can reach, so it runs again when someone opens the project in Claude Code or VS Code," StepSecurity's Ashish Kurmi [said](https://www.stepsecurity.io/blog/tensorlake-npm-compromised-hostage-token-worm).

[ChainDrop](https://thehackernews.com/2026/08/open-vsx-removes-77-malicious-evil-twin.html) was first documented in early August 2026 in connection with the compromise of hundreds of npm packages, including [Keyv and Cacheable](https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html), that were found to contain a Mini Shai-Hulud variant with a self-propagating credential-stealing worm delivered through an obfuscated Bun-based JavaScript payload.

The development extends the supply chain attack to artificial intelligence (AI) agent infrastructure, once again highlighting how threat actors are increasingly [targeting AI tools and services](https://thehackernews.com/2026/10/poellm-malware-infects-3400-servers-to.html) to extract valuable data from enterprises. Users who have installed the maliciou...