---
title: IronWorm and New Miasma Worm Variant Hit npm in Supply Chain Attacks
url: https://thehackernews.com/2026/06/ironworm-and-new-miasma-worm-variant.html
source: The Hacker News
date: 2026-06-05
fetch_date: 2026-06-06T05:51:38.260390
---

# IronWorm and New Miasma Worm Variant Hit npm in Supply Chain Attacks

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

# [IronWorm and New Miasma Worm Variant Hit npm in Supply Chain Attacks](https://thehackernews.com/2026/06/ironworm-and-new-miasma-worm-variant.html)

**Ravie Lakshmanan**Jun 05, 2026Software Supply Chain / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFimSGBOnvlCj_r6fiLdzK6V8DLTIQYjROKxHgQH8QxyRVIL3NDpQe9lBISjqCSjcZNl6VPhHVFtdJ8gPe2FfNjR9kGND1GSZmgx9T_32_Aii5nf_fMLkmBxwkKrJKbmZpcAG8xyj868aHfZ9RePlwlPDfMbI4uDlOCknlGH62Ifdf-nak6qmy4u-9i7X3/s1700-e365/npm-worm.jpg)

Multiple software supply chain attacks have hit the npm ecosystem, with threat actors using both malicious and poisoned versions of over 50 legitimate packages to distribute a Rust-based information stealer and a self-spreading worm, respectively.

According to [JFrog](https://research.jfrog.com/post/iron-worm-shai-hulud-rustier-cousin/), the information stealer "scrapes every secret it can find on a developer's machine, hides behind an eBPF kernel rootkit, and answers to its operator over Tor."

The stealer also uses the stolen credentials as a propagation mechanism, drawing similarities to the infamous Shai-Hulud worm. The new malware has been codenamed **IronWorm** by the software supply chain security company. By publishing itself to the npm registry in the form of trojanized packages, the approach results in a self-replicating attack.

The malicious activity has been traced back to a compromised npm account named "[asteroiddao](https://www.npmjs.com/~asteroiddao)," which has been found to publish package versions containing the Rust ELF binary that's executed via a preinstall hook.

The malware targets 86 environment variables, various files that may contain credentials associated with OpenAI Codex, Anthropic, Claude, Google Gemini, Cursor, Amazon Web Services (AWS), Docker, Kubernetes, and npm, vault configurations, and Exodus cryptocurrency wallet files.

An unusual quirk worth mentioning here is that the stealer includes logic for the wallet data-stealing component to skip the threat actor's own wallet. As of writing, the [cryptocurrency wallet](https://etherscan.io/address/0x7e28D9889f414B06c19a22A9Bd316f0AC279a4d6) is empty, and no transactions have been recorded.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

JFrog described IronWorm as "a supply chain weapon built to find secrets, modify projects, and inject malicious code to self-propagate across GitHub." The malicious commits, which span nine GitHub organizations, have been introduced under the author name "claude" ("claude@users.noreply.github.com") in an attempt to mimic Anthropic's artificial intelligence (AI) chatbot.

"The malicious npm package was published by asteroiddao; asteroiddao corresponds to the asteroid-dao GitHub organization; and ocrybit is a member of that organization, as well as related Arweave organizations," the company explained.

"The malware stole ocrybit's credentials and used them to push commits across repositories it could access. Those commits planted malware into other packages, which could then be published and infect the next developer. And then it vanished."

What's more, the malicious payload is equipped to swap existing GitHub Actions workflows for one that's capable of harvesting the secrets, writing it to a harmless-looking file, and uploading it as a build artifact, thereby eliminating the need for an external command-and-control (C2) server.

The malware's capabilities don't end there. In CI environments, it abuses npm's Trusted Publishing flow to obtain short-lived tokens to push poisoned versions containing the malware to the registry.

It also incorporates an eBPF payload that functions as a kernel-level rootkit to hide processes and thwart analysis. However, on systems where kernel lockdown is enabled, the process-hiding tricks fail, and the supposed processes and sockets become visible again.

### Miasma Worm Surfaces Again

The disclosure comes as [Endor Labs](https://www.endorlabs.com/learn/malicious-payload-in-ai-sdk-ollama-npm-package) and [StepSecurity](https://www.stepsecurity.io/blog/binding-gyp-npm-supply-chain-attack-spreads-like-worm) shed light on a distinct supply chain attack campaign that has compromised 57 npm packages across more than 286 malicious versions to serve a new variant of the [Miasma](https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html) worm, which previously infected 32 packages across more than 90 versions under the @redhat-cloud-services npm namespace within 72 seconds earlier this week.

Some of the affected packages are listed below -

* ai-sdk-ollama
* autotel
* awaitly
* effect-analyzer
* eslint-plugin-awaitly
* executable-stories-cypress
* http-uploader-dev
* mountly
* node-env-resolver
* node-env-resolver-aws

The data stolen via the malware is exfiltrated to a now-inaccessible GitHub account "[liuende501](https://github.com/liuende501)," which acted as an exfiltration point. As many as 236 repositories were staged in the account. It's presently not known if GitHub removed the account or if the threat actor themselves deleted it.

"This wave uses a technique we are calling 'Phantom Gyp': instead of the preinstall or postinstall lifecycle scripts that security tools typically monitor, the attacker abuses a 157-byte binding.gyp file to trigger code execution during npm install, bypassing most install-script security checks entirely," StepSecurity researcher Sai Likhith said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEVTEn7yrCQwrZdOghWj24HQ6yzk_u6TeVRJEbGouzcTkqjvu_raIVSGdk00s4qp39ScQCtNijRvYFe4t5d-aWvS0vN6GRoBrlPBemyGkxBMCzcvJmBxh6guowPj8l9_6zIcCmvEhbqa5jZbdKIPHLLPyM8gYseFVtyUgPT4HU2e7RxxTufLjbattTrp42/s1700-e365/cloud.png)

Like in the case of [Miasma](https://orca.security/resources/blog/red-hat-npm-supply-chain-attack/), the attack chain is engineered to download and install the Bun JavaScript runtime, using it to load a comprehe...