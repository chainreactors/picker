---
title: GlassWorm Supply-Chain Attack Abuses 72 Open VSX Extensions to Target Developers
url: https://thehackernews.com/2026/03/glassworm-supply-chain-attack-abuses-72.html
source: The Hacker News
date: 2026-03-14
fetch_date: 2026-03-15T04:34:48.013781
---

# GlassWorm Supply-Chain Attack Abuses 72 Open VSX Extensions to Target Developers

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [GlassWorm Supply-Chain Attack Abuses 72 Open VSX Extensions to Target Developers](https://thehackernews.com/2026/03/glassworm-supply-chain-attack-abuses-72.html)

**Ravie Lakshmanan**Mar 14, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4d-2XpiCS0UYnMWh32sQEJP9LnlN_m7m2hok9CnY_vu05XXwWn4INodYCvrEdweEzpho7XqcuOFvEPnnEWlHCRa_q3HY3V5O_ii35MVWAimRwsgrpNQrvGqeUchhZ48FRUl91zTpYQdLMRxVvRjV_T8GEm-J9mnMesefzlgeaoE_EU7Ba32liTr63SsQq/s1700-e365/open.jpg)

Cybersecurity researchers have flagged a new iteration of the GlassWorm campaign that they say represents a "significant escalation" in how it propagates through the Open VSX registry.

"Instead of requiring every malicious listing to embed the loader directly, the threat actor is now abusing extensionPack and extensionDependencies to turn initially standalone-looking extensions into transitive delivery vehicles in later updates, allowing a benign-appearing package to begin pulling a separate GlassWorm-linked extension only after trust has already been established," Socket [said](https://socket.dev/blog/open-vsx-transitive-glassworm-campaign) in a report published Friday.

The software supply chain security company said it discovered at least 72 additional malicious Open VSX extensions since January 31, 2026, targeting developers. These extensions mimic widely used developer utilities, including linters and formatters, code runners, and tools for artificial intelligence (AI)-powered coding assistants like Clade Code and Google Antigravity.

The names of some of the extensions are listed below. Open VSX has since taken steps to remove them from the registry -

* angular-studio.ng-angular-extension
* crotoapp.vscode-xml-extension
* gvotcha.claude-code-extension
* mswincx.antigravity-cockpit
* tamokill12.foundry-pdf-extension
* turbobase.sql-turbo-tool
* vce-brendan-studio-eich.js-debuger-vscode

GlassWorm is the name given to an [ongoing malware campaign](https://thehackernews.com/2026/02/open-vsx-supply-chain-attack-used.html) that has repeatedly infiltrated Microsoft Visual Studio Marketplace and Open VSX with malicious extensions designed to steal secrets and drain cryptocurrency wallets, and abuse infected systems as proxies for other criminal activities.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

Although the activity was [first flagged](https://thehackernews.com/2025/10/self-spreading-glassworm-infects-vs.html) by Koi Security in October 2025, [npm packages](https://thehackernews.com/2025/11/weekly-recap-lazarus-hits-web3-intelamd.html#:~:text=12%20Malicious%20VS%20Code%20Extensions%20Flagged) using the same tactics – particularly the use of invisible Unicode characters to hide malicious code – were [identified](https://intel.aikido.dev/packages/npm/os-info-checker-es6) as far back as March 2025.

The latest iteration retains many of the hallmarks associated with GlassWorm: running checks to avoid infecting systems with a Russian locale and using Solana transactions as a dead drop resolver to fetch the command-and-control (C2) server for improved resilience.

But the new set of extensions also features heavier obfuscation and rotates Solana wallets to evade detection, as well as abuses extension relationships to deploy the malicious payloads, similar to how npm packages rely on rogue dependencies to fly under the radar. Regardless of whether an extension is declared as "extensionPack" or "extensionDependencies" in the extension's "package.json" file, the editor proceeds to install every other extension listed in it.

In doing so, the GlassWorm campaign uses one extension as an installer for another extension that's malicious. This also opens up new supply chain attack scenarios as an attacker first uploads a completely harmless VS Code extension to the marketplace to bypass review, after which it's updated to list a GlassWorm-linked package as a dependency.

"As a result, an extension that looked non-transitive and comparatively benign at initial publication can later become a transitive GlassWorm delivery vehicle without any change to its apparent purpose," Socket said.

In a concurrent advisory, Aikido attributed the GlassWorm threat actor to a mass campaign that's spreading across open-source repositories, with the attackers injecting various repositories with [invisible Unicode characters](https://github.com/SebBersan/sql-bulletin-exam/pull/1/commits/b842ae7b9f047c625cab3c4f8029cf95addc133d) to encode a payload. While the content isn't visible when loaded into code editors and terminals, it decodes to a loader that's responsible for fetching and executing a second-stage script to steal tokens, credentials, and secrets.

No less than 151 GitHub repositories are estimated to have been affected as part of the campaign between March 3 and March 9, 2026. In addition, the same Unicode technique has been deployed in two different npm packages, indicating a coordinated, multi-platform push -

* @aifabrix/miso-client
* @iflow-mcp/watercrawl-watercrawl-mcp

"The malicious injections don't arrive in obviously suspicious commits," security researcher Ilyas Makari [said](https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode). "The surrounding changes are realistic: documentation tweaks, version bumps, small refactors, and bug fixes that are stylistically consistent with each target project. This level of project-specific tailoring strongly suggests the attackers are using large language models to generate convincing cover commits."

### PhantomRaven or Research Experiment?

The development comes as Endor Labs [said](https://www.endorlabs.com/learn/return-of-phantomraven) it discovered 88 new malicious npm packages uploaded in three waves between November 2025 and February 2026 via 50 disposable accounts. The packages come with functionality to steal sensitive information from the compromi...