---
title: ThreatsDay: Odysseus RCE, Samsung One-Click Takeover, iCloud Backdoor Fight + 27 More Stories
url: https://thehackernews.com/2026/08/threatsday-odysseus-rce-samsung-one.html
source: The Hacker News
date: 2026-08-06
fetch_date: 2026-08-07T04:30:24.963694
---

# ThreatsDay: Odysseus RCE, Samsung One-Click Takeover, iCloud Backdoor Fight + 27 More Stories

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

# [ThreatsDay: Odysseus RCE, Samsung One-Click Takeover, iCloud Backdoor Fight + 27 More Stories](https://thehackernews.com/2026/08/threatsday-odysseus-rce-samsung-one.html)

**Ravie Lakshmanan**Aug 06, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl0f74Tyvl6NQ4TAbPMIpgYWuHQN8THsYSQ77D9qmHuZdKsK2ZDrTLyWshLPV-UfSYW6Rbtfj866jP0X_D1QHmOFYIoEDZG90G3cy7JGFJrKsq0m7VeGqa0CCDygB9F3ttryPRQm-6MY50zIOsGFBdnwZZgAf31swGo5dOIa0noWuIoEk7rPrUkdfoddIj/s1700-e365/threatsd.jpg)

Apparently, opening the thing is now enough. A repo can run before the first prompt, a package can hide among hundreds, and a harmless-looking PDF can finish the job.

This week runs on cheap leverage: exposed servers, recycled bugs, poisoned agent instructions, remote-access tools dressed as support software, and trusted defaults doing attackers a favor.

Nothing here is especially mystical. Just ordinary systems trusting slightly too much, slightly too early. The full list follows.

**The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out.**

1. China-linked telecom risk

   [Chinese Telcos Maintain U.S. Presence](https://thehackernews.com/2025/08/salt-typhoon-exploits-cisco-ivanti-palo.html)

   The U.S. Congress's bipartisan Select Committee on China has published a 49-page report named "Stranger Pings," highlighting the threat of China-controlled infrastructure in the U.S. telecommunications backbone. The Committee said the [Salt Typhoon](https://thehackernews.com/2025/08/salt-typhoon-exploits-cisco-ivanti-palo.html) campaign could have been facilitated via a residual footprint that leaves open the door to future cyber operations against the U.S.: Chinese (aka People's Republic of China or PRC) telecom firms operating in the U.S. do not act independently and keep trusted positions inside U.S. communications infrastructure that Chinese threat actors can potentially abuse to preserve access and hide activity. "One PRC telecommunication provider included an 'Acceptable Use' Policy in contracts with U.S. companies," the Committee [said](https://files.constantcontact.com/f0eecb46901/f655c442-2d93-45ea-8cab-9d58a3a04052.pdf). "This prohibited the broadcasting of political news against state laws of the PRC, the broadcasting of information in violation of PRC state security laws, and the broadcasting of information in violation of the 'social order and social stability.'"
2. ClickOnce phishing chain

   [SideWinder Deploys New Attack Chain](https://thehackernews.com/2025/10/sidewinder-adopts-new-clickonce-based.html)

   The threat actor known as [SideWinder](https://thehackernews.com/2025/10/sidewinder-adopts-new-clickonce-based.html) has [adopted](https://mp.weixin.qq.com/s/PALBLusD4umh_52gy2wVAg) a new multi-stage attack chain that abuses ClickOnce application files delivered via phishing PDF documents to deliver Rust-based backdoors. The implants can establish persistence via registry modification, collect host intelligence, and accept remote commands over external servers hosted on free serverless platforms such as Cloudflare Workers.
3. npm supply chain attack

   [Flooding Dropper Hits npm With 850 Malicious Packages](https://www.sonatype.com/blog/flooding-dropper-hits-npm-with-850-malicious-packages)

   An active malicious package campaign, dubbed "Flooding Dropper," has disclosed a large-scale campaign involving 846 software components. "The attacker appears to be automating parts of the npm account and package creation process, combining terms such as bigops and bnpl with other words and recurring version patterns, such as releases in the 35.x.y range," Sonatype [said](https://www.sonatype.com/blog/flooding-dropper-hits-npm-with-850-malicious-packages). "When installed, the packages download and execute a second-stage payload, using multiple delivery methods to improve the attack's chances of success. The packages also contain slightly modified payloads. While syntactically different, for example using different URL functions and variable names, the packages all execute the same behavior. Those changes can reduce the effectiveness of detections that depend on exact signatures, even when the underlying behavior remains closely related." The packages deliver a first-stage JavaScript loader that identifies the host operating system and delivers a compatible Windows, Linux, or macOS payload from a randomized set of hard-coded remote hosts and runs it as a detached background process. On Windows, the downloaded binary is another loader that performs checks for sandboxed and virtual environments, patches Event Tracing for Windows and Antimalware Scan Interface functions, establishes persistence via a scheduled task, and downloads and executes an encrypted payload.
4. Coding agent execution risk

   [Coding Agents Expose Pre-Prompt Code Execution Paths](https://securitylabs.datadoghq.com/articles/coding-agent-project-trust-code-execution-before-first-prompt/)

   New research from Datadog has found that "Trusting a repository in a coding agent can allow repository-controlled code to run before you send the first prompt," causing seemingly harmless tasks like cloning a repository to be an attack vector. "Codex MCP configuration and Claude Code project environment settings created automatic code-execution paths without a model response or shell-command approval," Datadog [said](https://securitylabs.datadoghq.com/articles/coding-agent-project-trust-code-execution-before-first-prompt/). "Treat project trust like running code. Open unfamiliar repositories in disposable environments without sensitive credentials, even if a quick manual review looks clean." Earlier this May, Datadog also highlighted the risks associated with Claude Code skills. "Agentic skills package instructions and context for coding agents," it [said](https://securitylabs.datadoghq.com/articles/malicious-skills-supply-chain-risks-in-coding-agents-with-dynamic-context/). "They are useful for repeatable workflows, but they also create a path for attacker-controlled instructions to enter a trusted agent session. The important detail is not only that a malicious skill can ask an agent to do something dangerous. It is that dynamic context ...