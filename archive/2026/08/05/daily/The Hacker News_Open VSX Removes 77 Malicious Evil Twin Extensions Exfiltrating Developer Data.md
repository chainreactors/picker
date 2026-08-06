---
title: Open VSX Removes 77 Malicious Evil Twin Extensions Exfiltrating Developer Data
url: https://thehackernews.com/2026/08/open-vsx-removes-77-malicious-evil-twin.html
source: The Hacker News
date: 2026-08-05
fetch_date: 2026-08-06T05:02:52.824589
---

# Open VSX Removes 77 Malicious Evil Twin Extensions Exfiltrating Developer Data

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

# [Open VSX Removes 77 Malicious Evil Twin Extensions Exfiltrating Developer Data](https://thehackernews.com/2026/08/open-vsx-removes-77-malicious-evil-twin.html)

**Ravie Lakshmanan**Aug 05, 2026Software Supply Chain / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh28AJU8_kuimN9uKY5xj-0XMAMxfVP4rejHEWMJ_5FD99mAvt8dEsRuGhlCGb63VjWykzePg_-tuaTqNycmvhZy3oFRFAuVHbwpsAg6ae599Pl7bYQVb7Qo7fDuDjWMHmHZOLfWc9HZkQlyAis8LNMmkS_wnKbvliVNsOej4p6XV_KbiFHHzJp1SjGFU1G/s1700-e365/vscode.jpg)

A cluster of 77 extensions on the Open VSX marketplace has been found to impersonate legitimate developer tools while transmitting information about the systems and development environments on which they were installed.

The "evil twin" extensions were uploaded to the repository between July 26 and August 1, 2026, according to Manifold Security. The packages have been removed from Open VSX as of August 3, 2026.

"In most of the packages it sends little more than the machine's hostname," security researchers Ax Sharma and Cody Nash [said](https://www.manifold.security/blog/open-vsx-evil-twin-extensions). "In nineteen of them it sends a detailed description of the machine, the repository open in the editor, and the CI system the editor is running inside."

Of the identified extensions, 58 have been described as lightweight tools designed to exfiltrate the hostname and, in some cases, the workspace folder name or editor version.

The rest are reconnaissance payloads that transmit the developer-related information: local hostname and operating system username, the editor's name, version, host kind and machine ID, the platform and architecture, the locale and timezone, and the open workspace's folder name and full file system path.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Both share the same data-exfiltration domain, as well as similarities in code and behavior. The names of the 19 extensions are listed below -

* amd.gaia-vscode
* artsy.artsy-studio-extension-pack
* configcat.configcat-feature-flags
* iotaledger.iota-move
* marketplace.visualstudio
* obyte.oscript-vscode-plugin
* openeuphoria.vscode-euphoria
* oss.sfmc-devtools-vscode
* rumbledb.jsoniq-vscode
* ssagov.uef-snippets
* taskfile.vscode-task
* doi.fileheadercomment
* mengsiCode.vscode-django-boilerplate
* move.move-analyzer
* uavcan.dsdl
* vs-publisher-988541.apexsql-power-tools
* casualjim.gotemplate
* jcamp.dotnet-test-provider-view
* superposition.supertoml-analyzer

What's notable about the campaign is that it reuses the names, namespaces, and descriptions of real Microsoft VS Code Marketplace extensions, but they are published through unrelated accounts and assigned a low version number (e.g., 0.0.1). The main change involves swapping the contents of the bundled "extension.js" file with capabilities to capture and transmit data, while framing the collection as "anonymous usage metrics."

None of the extensions offer the advertised functionality mentioned in their listings. Instead, they display a status bar item along with a message that states they are active, before firing the data exfiltration step. In all 77 extensions, the data is sent to "mangorbit[.]com," which was registered on July 15, 2026, 11 days before the first packages were published.

The extensions that are part of the second set cluster have also been found to carry out the following steps -

* Inspect files in the workspace's .git directory to obtain Git remote hosts and organizations, the domain of the developer's configured email, the current branch, and the HEAD commit SHA hash.
* Enumerate up to 60 installed extension IDs and pick up the proxy hostname from the environment
* Extract the names of any CI markers present, and separately the values of GITHUB\_REPOSITORY, CI\_PROJECT\_PATH, the Azure DevOps collection URI, the Buildkite organisation slug, the CircleCI project username, the Codespace name and the Gitpod workspace context URL from CI environments
* Read the editor's own telemetry opt-out setting, checks if it's enabled, and sends the status

Further analysis indicates that the malicious code has contingency plans in place to query a DNS TXT record to retrieve a fallback exfiltration URL in the event the primary domain is blocked or taken down. The recon variant also features a retry mechanism that triggers the collection later on, suggesting the objective goes beyond a simple one-shot experiment.

"In the recon variant, attempts come at roughly fifteen minutes, fifty minutes and three and a half hours, then every seven or eight hours, resuming on every editor restart and giving up only after seven days," the researchers explained. "A machine that is offline, firewalled, or behind a proxy that drops the first request gets asked again for a week."

"The recon variant checks whether the open workspace's own devcontainer.json or .vscode/extensions.json references the extension's ID, and reports the answer as a single flag. In plain terms, it distinguishes installs that a repository's configuration caused from installs a human chose. That is the field you would want if the question you were asking was how am I being pulled in, and by what."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The disclosure comes as [450 unique npm packages](https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html) spanning 2,244 artifacts have been compromised as part of a [new software supply chain attack](https://socket.dev/supply-chain-attacks/keyv-and-cacheable-compromise) to deliver an information stealer and leverage the stolen npm token to push trojanized versions containing the same malware. The compromise campaign has been codenamed ChainDrop.

"The malicious releases contain a Mini Shai-Hulud variant, a self-propagating credential-stealing worm delivered through a large, heavily obfuscated Bun-based JavaScript payload," Microsoft [said](https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/). "The malware typically executes automatically through an npm preinstall lifecycle hook before package installation completes."

"The malware can also use stole...