---
title: Malicious npm Packages Harvest Crypto Keys, CI Secrets, and API Tokens
url: https://thehackernews.com/2026/02/malicious-npm-packages-harvest-crypto.html
source: The Hacker News
date: 2026-02-23
fetch_date: 2026-02-24T04:12:15.918575
---

# Malicious npm Packages Harvest Crypto Keys, CI Secrets, and API Tokens

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Malicious npm Packages Harvest Crypto Keys, CI Secrets, and API Tokens](https://thehackernews.com/2026/02/malicious-npm-packages-harvest-crypto.html)

**Ravie Lakshmanan**Feb 23, 2026AI Security / DevOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjuEqzksJuTTXCDhdqgtAIFwGij7CiTa9hyGtjvNUn3wVoFYnH9_f0F-ILQlJhaACL9g1sNbdxCptyn_HwKxFha-yhWgnEph96LK390IGibwSZ3x2iwNeB_JEbhgLCL1lonRUtIU8ubyI7TprS8mbmNrpB7f6_fAhtaJQG3frpu4N6MTzwcrmEF5TpnwuqO/s1700-e365/npm-stealer.jpg)

Cybersecurity researchers have disclosed what they say is an active "Shai-Hulud-like" supply chain worm campaign that has leveraged a cluster of at least 19 malicious npm packages to enable credential harvesting and cryptocurrency key theft.

The campaign has been codenamed **SANDWORM\_MODE** by supply chain security company Socket. As with prior [Shai-Hulud attack waves](https://thehackernews.com/2025/12/researchers-spot-modified-shai-hulud.html), the malicious code embedded into the packages comes with capabilities to siphon system information, access tokens, environment secrets, and API keys from developer environments and automatically propagate by abusing stolen npm and GitHub identities to extend its reach.

"The sample retains Shai-Hulud hallmarks and adds GitHub API exfiltration with DNS fallback, hook-based persistence, SSH propagation fallback, MCP server injection with embedded prompt injection targeting AI coding assistants, and LLM API Key harvesting," the company [said](https://socket.dev/blog/sandworm-mode-npm-worm-ai-toolchain-poisoning).

The packages, published to npm by two npm publisher aliases, official334 and javaorg, are listed below -

* claud-code@0.2.1
* cloude-code@0.2.1
* cloude@0.3.0
* crypto-locale@1.0.0
* crypto-reader-info@1.0.0
* detect-cache@1.0.0
* format-defaults@1.0.0
* hardhta@1.0.0
* locale-loader-pro@1.0.0
* naniod@1.0.0
* node-native-bridge@1.0.0
* opencraw@2026.2.17
* parse-compat@1.0.0
* rimarf@1.0.0
* scan-store@1.0.0
* secp256@1.0.0
* suport-color@1.0.1
* veim@2.46.2
* yarsg@18.0.1

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

Also identified are four sleeper packages that do not incorporate any malicious features -

* ethres
* iru-caches
* iruchache
* uudi

The packages go beyond npm-based propagation by including a weaponized GitHub Action that harvests CI/CD secrets and exfiltrates them via HTTPS with DNS fallback. They also feature a destructive routine that acts as a kill switch by triggering home directory wiping should it lose access to GitHub and npm. The wiper functionality is currently off by default.

Another significant component of the malware is an "McpInject" module that specifically targets AI coding assistants by deploying a malicious model context protocol ([MCP](https://modelcontextprotocol.io/docs/getting-started/intro)) server and injecting it into their tool configurations. The MCP server masquerades as a legitimate tool provider and registers three seemingly-harmless [tools](https://modelcontextprotocol.io/legacy/concepts/tools), each of which embeds a prompt injection to read the contents of ~/.ssh/id\_rsa, ~/.ssh/id\_ed25519, ~/.aws/credentials, ~/.npmrc, and .env files, stage them in a local directory for later exfiltration.

The module targets Claude Code, Claude Desktop, Cursor, Microsoft Visual Studio Code (VS Code) Continue, and Windsurf. It also harvests API keys for nine large language models (LLM) providers: Anthropic, Cohere, Fireworks AI, Google, Grok, Mistral, OpenAI, Replicate, and Together.

What's more, the payload contains a polymorphic engine that's configured to call a local [Ollama](https://thehackernews.com/2026/01/researchers-find-175000-publicly.html) instance with the [DeepSeek Coder](https://deepseekcoder.github.io/) model to rename variables, rewrite control flow, insert junk code, and encode strings to evade detection. While the engine is turned off in the currently detected packages, the inclusion of the feature suggests that the operators are looking to release more iterations of the malware in the future.

The entire attack chain unfolds over two stages: a first-stage component that captures credentials and cryptocurrency keys and then loads a secondary stage that subsequently performs deeper harvesting of credentials from password managers, worm-like propagation, MCP injection, and full exfiltration. The second stage is not activated until 48 hours (along with a per-machine jitter of up to 48 additional hours) have elapsed.

Users who have installed any of the aforementioned packages are advised to remove them with immediate effect, rotate npm/GitHub tokens and CI secrets, and review any package.json, lockfiles, and .github/workflows/ for any unexpected changes.

"Several feature flags and guardrails still suggest the threat actor is iterating on capabilities (for example, toggles that disable destructive routines or polymorphic rewriting in some builds)," Socket said. "However, the same worm code appearing across multiple typosquatting packages and publisher aliases indicates intentional distribution rather than an accidental release."

"The destructive and propagation behaviors remain real and high-risk, and defenders should treat these packages as active compromise risks rather than benign test artifacts."

The disclosure comes as [Veracode](https://www.veracode.com/blog/malicious-npm-package-hiding-in-plain-pixels/) and [JFrog](https://research.jfrog.com/post/three-stages-deep-a-malicious-npm-package/) detailed two other malicious npm packages named "buildrunner-dev" and "eslint-verify-plugin," respectively, that are designed to deliver a remote access trojan (RAT) targeting Windows, macOS, and Linux systems. The .NET malware deployed by buildrunner-dev is [Pulsar RAT](https://thehackernews.com/2025/06/malicious-pypi-package-masquerades-as.html), an open-source RAT delivered via a PNG image hosted on i.ibb[.]co.
...