---
title: AI Coding Agents Found Triggering Endpoint Security Rules Built to Catch Attackers
url: https://thehackernews.com/2026/07/ai-coding-agents-found-triggering.html
source: The Hacker News
date: 2026-07-08
fetch_date: 2026-07-09T06:03:33.329879
---

# AI Coding Agents Found Triggering Endpoint Security Rules Built to Catch Attackers

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

# [AI Coding Agents Found Triggering Endpoint Security Rules Built to Catch Attackers](https://thehackernews.com/2026/07/ai-coding-agents-found-triggering.html)

**Swati Khandelwal**Jul 08, 2026AI Security / Threat Detection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEtVOCcf8-6_z0F4FVoPlTMQRFJ4CfHCbl-GvhT9EbRrfZgTJsNbBkzAq72212RbMT1Knk5GJsYDY8p5W7YO8x29vQ782QW6CRorl_oKVyAgOmS46Y9HyTPcdZOmMjOPtWjpAHH3C91EPVk4dnHqaAEX8QoaSvGzCbjMy0YhF7lJaIR6-T9Dq5jzZycIc/s1700-e365/alarm.jpg)

Sophos looked at a week of its own endpoint data and found that AI coding agents such as Claude Code, Cursor, and OpenAI Codex are setting off detection rules written to catch human intruders.

The agents are not malicious. They just do a lot of things that, to a behavioral engine, look exactly like an attack.

Decrypting browser credentials, listing what sits in Windows' credential store, pulling files down with built-in system tools, writing to the startup folder: these have long been high-signal to defenders.

What has changed is who is generating it. On the machines Sophos watched, it was often a developer's AI assistant going about ordinary work.

## What set the alarms off

The [analysis](https://www.sophos.com/en-us/blog/2607_agents_vs_telemetry) draws on seven days of telemetry from June 2026, taken from Sophos's behavioral engine on Windows and counted by unique machines, not raw event volume. It is a narrow window on one vendor's fleet, not an industry census.

Sophos's charts put credential access at 56.2 percent of the blocked activity and execution at 28.8 percent: agents reaching for stored secrets, or running code the way attackers do.

The biggest credential-access rule, at 42.6 percent of that group, fires when a process uses Windows' built-in Data Protection API, or DPAPI, to decrypt the browser's stored credential data. Sophos calls GStack a widely adopted skill pack for coding agents.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Its /browse skill does exactly that, running PowerShell that calls DPAPI to unlock saved browser data. Sophos caught it running under Claude Code. In context, it is almost certainly browser automation on the user's behalf. To the detection engine, it is credential theft, and the rule is right to fire.

Some Python examples looked worse on paper. In one instance, Claude Code shut down the running browser and ran a script that pulled data from its credential store.

Separately, it ran cmdkey /list to enumerate the credentials Windows Credential Manager was holding. Sophos notes that Claude Code here ran with its --dangerously-skip-permissions flag set, a mode Anthropic's own documentation warns against and tells administrators how to block.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVDoINnew1UuYRhdZUDUVI6BdndgxYyfbqFiyQt7mDl_bKa25hzu79yS3EXtKmy0U1wsMB0jU8kCkd6-EY1CFYVDzKIO8HPYMH8UA_iAewI7n7jtRgRxNylsdFzMCXL_1Lc3SkSwPyLmlrN8l0QdM-iz_mRkGjA0uVIwIanWC6Z2t7cB4iFDu_29HGb-E/s1700-e365/browser.png)

When one approach fails, an agent tries another. OpenAI Codex did just that, fetching a Python installer from the real python.org, starting with certutil. That was blocked, so it switched to bitsadmin. Both are legitimate Windows utilities that attackers routinely abuse to pull payloads, living off the land.

The target was harmless, but Sophos's point is that this pivot-when-blocked behavior is what separates a live attacker from a static script, and benign agents now do it too.

Cursor tripped a persistence rule by using PowerShell to drop a startup-folder script that would run every time the machine booted. Sophos could not confirm what the script did, but writing to startup outside a trusted installer is the kind of thing defenders flag on sight.

## AI agents on both sides of the line

The flip side is already visible. A month earlier, Sophos [documented](https://www.sophos.com/en-us/blog/pointing-a-cursor-at-evading-detection) an attacker who used AI agents to build and test malware against EDR products, one of them running Claude Opus 4.5 to coordinate the work.

That was development-time: agents helping an attacker write better tooling. Agents get turned on their own users at runtime, too. In a separate case, researchers showed a coding agent could be [tricked into running attacker code](https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html) through poisoned inputs, a chain that can slip past EDR because the agent is acting inside the user's trusted session.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRV2SoI5eTxlcTtbX8dDSKDjBf5_Aq3HtJQ1aVwone-E2kRVTs1tpVoPjfYqdhcL2yXd9yO2-IFHkEGcorKKWG9eN_UV8vg75lT-EzrUwIUK0vZ1krN-j-8g8BIBU7BAHpb5VpbYEcrW-5IekKODsBLaRuxC7p8FRE8W3DRqBCc2GQVRNpN0v33bj__74/s1700-e365/ai-agent-trigger.jpg)

These are separate events with different rules firing, but they share a surface: browser credential calls, LOLBin downloads, and startup writes now come from benign agents, attacker-run agents, and hijacked agents.

That is why the raw action tells you less than it once did. And it sits inside a bigger change in how intrusions look. CrowdStrike's [2026 Global Threat Report](https://www.crowdstrike.com/explore/2026-global-threat-report) found 82 percent of 2025 detections were malware-free, with attackers moving through valid credentials and trusted tools instead of dropping files.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuodsSIDKu6uSRfU6fZBkO-2PERqKSfIn6dA/s728-e100/sygnia-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

That shift is what pushed detection toward behavior in the first place. AI agents now generate the same behavior for ordinary reasons, ...