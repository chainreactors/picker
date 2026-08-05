---
title: Keyv-Linked npm Worm Poisons Hundreds of Packages, Plants Claude Code and VS Code Hooks
url: https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html
source: The Hacker News
date: 2026-08-04
fetch_date: 2026-08-05T04:59:29.735665
---

# Keyv-Linked npm Worm Poisons Hundreds of Packages, Plants Claude Code and VS Code Hooks

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

![cybersecurity](data:image/svg+xml;base64...)

# [Keyv-Linked npm Worm Poisons Hundreds of Packages, Plants Claude Code and VS Code Hooks](https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html)

**Swati Khandelwal**Aug 04, 2026Supply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAb0f5sNdFs0uLbgh9_rBZ-SaCrUjv3c4mL7OLF7pFPxH5pusnFJyInc_7S-QqgMa0DsEm2fId6v2sWX7hJcaA0eHTHngKBXGOA3ysg7NYz1CyMAgwsrWnJ3FA1HGFkzglgj5pGsXeLWzXjCUhNGi5ecEsqIu2oOzz_koXsQAAC0EV5HkuAJGtAVvWotE/s1700-e365/npmnpm.jpg)

A credential-stealing npm worm that first appeared in `keyv@6.0.0` spread beyond the Keyv and Cacheable namespaces into hundreds of packages across multiple organizations on August 4, 2026.

SafeDep verified 353 poisoned versions across 79 package names in the npm registry. Its monitoring put the wider footprint at 442 versions across 353 names, while Aikido later reported at least 868 packages across 1,381 versions. Neither broader total was independently reproducible from a complete public list at the reporting cutoff.

The malicious release used a `preinstall` script to run a credential-stealing bundle inside developer and continuous integration (CI) environments. SafeDep and Socket say it can harvest repository, package registry, cloud and private-key material, then use available npm publishing access to poison more packages.

The Keyv repository also retained separate Claude Code and Visual Studio Code (VS Code) hooks that can execute the payload once a user trusts the workspace or permits the project configuration.

Socket says any workstation or runner that executed an affected version should be treated as credential-exposed. SafeDep advises responders to remove the malware's credential-revocation watcher before rotating exposed tokens and keys.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Revocation is the watcher's trigger; rotating first can run an attacker-supplied local handler. [npm 12](https://docs.npmjs.com/cli/v12/commands/npm-approve-scripts/) blocks unapproved [dependency lifecycle scripts](https://thehackernews.com/2026/07/npm-12-disables-install-scripts-by.html) by default, but earlier npm clients and other install paths that permit lifecycle scripts remain exposed.

The first confirmed malicious release was `keyv@6.0.0`. It added `node setup.mjs` as a `preinstall` command and included `setup.mjs` and `Math_Symbol.js` in the package while leaving the compiled library code unchanged.

Stage one checks for Bun, downloads version 1.3.13 from the runtime's official GitHub releases if needed, and hands off to a 727,680-byte compiled bundle.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwnNdDhE3hwXhLbyecxcbCnC1SWKMr8fcOg29kg_y7b7WAkSD3YRzGd7t8mwNRRWICzHCzfbO1UCdrDVGSmNIwVIGLwBuR8Uvj83roTFcxc2sxGjG_jZObW1UMK3ALmH4Y-DqRoJqk8IEjzUKLjwS4iwiBGDHu6qdGi411AdRFyx-wVgd3hn1XBFUw0K0/s1700-e365/shai.png) |
| Source: SafeDep |

[SafeDep's payload analysis](https://safedep.io/keyv-npm-supply-chain-compromise/) says the bundle harvests GitHub, npm, cloud, Vault, Kubernetes, database and private-key material. It also reads GitHub Actions runner memory, installs a token-revocation watcher and carries npm publishing machinery. [Socket](https://socket.dev/blog/popular-npm-packages-in-the-keyv-and-cacheable-namespaces-compromised-in-active-supply-chain) separately decoded code for modifying, versioning and republishing packages available to a stolen npm identity.

The registry changed too quickly to support a fixed campaign-wide list of packages still tagged `latest`. At 5:40 p.m. India Standard Time (IST) on August 4, npm package pages showed earlier releases restored as `latest` for at least nine packages from SafeDep's initial set, including [`keyv@5.6.0`](https://www.npmjs.com/package/keyv), [`flat-cache@6.1.23`](https://www.npmjs.com/package/flat-cache?activeTab=versions), and [`cache-manager@7.2.9`](https://www.npmjs.com/package/cache-manager?activeTab=versions).

The full campaign could not be independently mapped package by package, so exposure checks must use exact package names, resolved versions and lockfiles rather than a cached list of current tags.

The totals reported by SafeDep and Aikido count malicious package artifacts, not victim systems. They establish campaign scale but do not show how many machines installed or executed the payload. Determining system-level exposure requires the exact dependency version resolved on the machine and whether its lifecycle script ran.

With tags changing, some related packages remaining clean and the full set incomplete, a namespace-level blocklist risks both missing poisoned versions and treating unaffected releases as compromised.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The repository carries a second execution path. Its [`.claude/settings.json`](https://github.com/jaredwray/keyv/blob/main/.claude/settings.json) contains a `SessionStart` hook that calls `.vscode/setup.mjs`. The [`.vscode/tasks.json`](https://github.com/jaredwray/keyv/blob/main/.vscode/tasks.json) file contains an `Environment Setup` task with `runOn: folderOpen` that calls `.claude/setup.mjs`. Those files create a route for executing the payload from a checked-out repository, but they do not run unconditionally in every default environment.

[VS Code blocks automatic tasks in an untrusted workspace](https://code.visualstudio.com/docs/debugtest/tasks) and prompts before allowing them by default. [Claude Code applies workspace trust](https://code.claude.com/docs/en/settings) to repository-supplied project settings. At 5:40 p.m. IST on August 4, both hook files were still present on `main`. The [`core/keyv/package.json`](https://github.com/jaredwray/keyv/blob/main/core/keyv/package.json) manifest still declared version `6.0.0`, retained `node setup.mjs` as its `preinstall` command, and listed `setup.mjs` and `Math_Symbol.js` for publication.

The poisoned Keyv release carried [valid OpenID Connect (OIDC) and Supply-chain Levels for Software Artifacts (SLSA) provenance](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html) because it passed through the project's legitimate GitHub A...