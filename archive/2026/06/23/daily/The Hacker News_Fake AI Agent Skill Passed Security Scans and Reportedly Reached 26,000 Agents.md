---
title: Fake AI Agent Skill Passed Security Scans and Reportedly Reached 26,000 Agents
url: https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html
source: The Hacker News
date: 2026-06-23
fetch_date: 2026-06-24T06:06:30.912551
---

# Fake AI Agent Skill Passed Security Scans and Reportedly Reached 26,000 Agents

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

# [Fake AI Agent Skill Passed Security Scans and Reportedly Reached 26,000 Agents](https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html)

**Swati Khandelwal**Jun 23, 2026Supply Chain Security / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgb14v3ddlfpybc15jRbk-cwHI-0S8BAzdp8Ix83L5ZCZ4AB8gCySG7J4tZr4od9q3Jbuic1a4J29VAvRcdSQag_-ju1o9ae9yCcL6XV_jRDVhgd31E5BljiThpXcfHu_gdsmSySY8o0WyjuUoSQ5CGOyKO3cKXVDYeGKa1b1up2VM5ZJE6_PjPNCVOD_M/s1700-e365/skills.jpg)

Security firm AIR built a fake AI agent skill, pushed it through a popular skill marketplace and an Instagram ad, and says it reached roughly 26,000 agents, including some on corporate accounts.

Every skill security scanner the firm tested it against marked it safe. The payload was harmless by design: it collected the user's email address and did nothing else.

The point was to show that none of the signals people lean on to trust a skill caught it: not the scanners, not the GitHub stars, not the open-source reputation.

A skill is a bundle of instructions an agent loads into its own context and follows with roughly the authority of a user prompt. That trust is the whole problem, and it is the reason skill-scanning tools exist in the first place.

The skill, named **brand-landingpage**, claimed to build a landing page using Google's Stitch design tool, aimed squarely at non-technical users.

To make it look credible, AIR went after two trust signals: GitHub stars and a clean scanner verdict. For the stars, it opened a pull request to a skill marketplace repository with around 36,000 stars and 156 skills.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The pull request was merged after a few days, so the skill inherited the repo's count. Then it ran an Instagram ad aimed at marketers, salespeople, and designers, who installed it and put it to work.

## Why the scanners missed it

The scanners AIR tested analyze the package you hand them: the SKILL.md and the files shipped with it. That's [Cisco's](https://github.com/cisco-ai-defense/skill-scanner), [NVIDIA's](https://github.com/nvidia/skillspector), and the ones wired into skills.sh.

[AIR's skill](https://www.air.security/blog-posts/the-story-of-skills) carried no setup instructions of its own. It told the agent to install the "Stitch SDK" by following the documentation at an external link, stitch-design.ai, a domain AIR controls, not Google (the real Stitch lives at stitch.withgoogle.com).

At first, the link led to the genuine Stitch docs, so the scanners, seeing a clean package that pointed at a plausible setup page, cleared it. The page the agent would actually fetch and follow sat outside the scan.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1aBkfUqO1G782lmRGhP0uU9QlLKjmgTJA1jxNom1jvkr9PmijCryFR-LvoVyumFr6lyR-TMa6wmrhFMJRqXFz1X9DxxA2rYtQD31VgPDNzWFQVXcHdH4tgs32V50Gk97uRsgzQGtsWML270chJhD11stwapvqZLXtftKmfHemZapNBIW6C7QXNj-a3Ck/s1700-e365/switch.png)

Once the skill was installed widely, AIR swapped the page behind that link. The new version told the agent to download and run a script.

In the demo, it only mailed the user's address back to AIR, which is how the firm counted the agents it reached. A real operator could have used that foothold to read files, move data, or hit internal systems, bounded only by what the agent could reach.

AIR is not the first to show this. Three weeks earlier, [Trail of Bits](https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/) bypassed ClawHub's malicious-skill detector, Cisco's scanner, and all three scanners wired into skills.sh. Its conclusion was blunt: a scanner checks a fixed package, while an attacker can keep tweaking the payload until it passes.

Real campaigns have used the same [trick](https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html) for months, keeping the submitted skill clean and hosting the payload on a site the agent only fetches at install.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWTVudsjrIN3qorMHITlyY6sPhoEkRbywJl1j5iy_dK2aTTyUEdS0aZXuZJHovooG7ud-DHHrMq7kTn13DLHku7eveORPsXpb8lVi_8F3Thb5g3Q6lUfN49t7zs9CeZR8345gtC5wkuiagZ-Iac2CIPgs5CQuf2qkW8kwFovZx66a5ejk6bqzjtZnDZBo/s1700-e365/data.png)

The problem is structural: the scan happens once, but the page a skill points the agent to can be rewritten at any time after. Anthropic's own [docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) already warn that skills fetching external URLs are risky for exactly this reason, since the content can change after the skill is vetted.

Separate [research this year](https://theweatherreport.ai/posts/skill-scanner-disagreement/) found scanners often disagree, because each one judges a skill in isolation, blind to its external links and to what changes after review.

## What to do

The read for defenders is the same one researchers keep landing on, now with a sharper example behind it. Treat skills as software, not text. Vet what a skill points to, not just what ships inside it.

Most of these add-ons got installed with no review, so the first job is finding what is already running. Route new skills through a single source you control, and re-check them when anything changes, because a clean result at install does not stay clean if the skill phones out to a link someone else can edit.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

Pin versions. Hold agents to the least privilege. Assume any external instruction an agent fetches runs with the agent's access.

The scale figures come from AIR alone, and they deserve a skeptical read. The firm is launching a managed skill marketplace and closes the write-up, pitching it, so the 26,000 number, the corporate-account detail, and the claim that it could have seized full control of...