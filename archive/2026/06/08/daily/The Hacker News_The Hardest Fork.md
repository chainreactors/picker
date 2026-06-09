---
title: The Hardest Fork
url: https://thehackernews.com/2026/06/the-hardest-fork.html
source: The Hacker News
date: 2026-06-08
fetch_date: 2026-06-09T06:03:51.103780
---

# The Hardest Fork

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

# [The Hardest Fork](https://thehackernews.com/2026/06/the-hardest-fork.html)

**The Hacker News**Jun 08, 2026Open Source / Software Supply Chain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRnMnAqwiH7Dgv_dmF2bugYLlu8uMyFQkl7DseYkwwzl5MzUP-KeplSbGg_aNt_OqIDtT5rLyDO_Ea96Hf_uti0eKVIseQTxtS7zt-WQksEp8c4V50Hdq0kWqWjvyOVMHVlbMo1gagsSGu4lmdhlm1NSLQLp9QZVohv74jIWehnGY-l_PAPYzUvtITBMs/s1700-e365/fork.jpg)

Mythos is real. I know a big chunk of the industry thinks it's a marketing stunt, and I get why. I get it. But I've seen the findings, and they're bad. These aren't "whoops, this line right here is wrong, and that's RCE." They're novel combinations of a few dozen issues out of thousands of things every SAST scanner already finds, chained together into something much worse. It's real creativity, like Move 37. That's not a better scanner. That's a different category of threat.

In some ways, it doesn't even matter. Even if this specific model were a hoax, the capability is coming regardless. Some days, I wish it were a hoax. We'd have more time. But you can believe me or not. The rest of this post is about what we do about it either way, and I'm getting started now.

Washington has been tracking this for a while, but you can't regulate something most of the industry thinks is made up. Now that every boardroom is in preparation mode (and they are), DC finally gets to start thinking through what steps they can take. It's clear they need to play a role, but it's not clear how or what it should be. And they're in a really tough spot.

Regulate too little, and you risk a US-based company accidentally creating a weapon that puts our critical infrastructure at risk. Regulate too much, and the same thing happens in China instead. The whole thing feels like gain-of-function research on viruses. Everyone knows you should wash your hands before leaving the lab, but just because we make it mandatory doesn't mean the rest of the world will. We've already seen how that story goes in Wuhan.

Here's the structural problem that limits what any government can do: despite Europe's best attempts with the CRA, open source isn't governable. Laws and executive orders don't apply to people around the world putting things on the internet for free. The US realizes this, so they're focusing where they can and where they should: on consumption. That's the right instinct, and it's exactly where the rest of this post is going.

## The open source ecosystem and consumption model is not ready for this

I've been working on this problem every day of my life for the last decade. I helped found the [OpenSSF](https://openssf.org/) and [Alpha-Omega](https://alpha-omega.dev/) while at Google. I created [Sigstore](https://www.sigstore.dev/), [Scorecards](https://openssf.org/projects/scorecard/), and the first open source malware scanners. I funded the grants that put Rust in the Linux kernel and MFA on PyPI. Then I started Chainguard to do all of this commercially, at scale. I'm telling you all of this not to brag, but because I need you to believe me when I say: the way the world consumes open source software is fundamentally broken, and no amount of incremental improvement is going to fix it in time.

Not in its current form. Maybe not ever. It's going to have to change.

Most companies have been consuming open source freely for years without really thinking about it. Modern apps are layers of dependencies, and when something goes wrong in one of them, fixing it can cascade through an entire stack. For large orgs with legacy codebases, that's not an afternoon fix. And moving fast has its own risks now. AI has supercharged supply chain attacks, too. Rush to patch a vulnerability without careful review, and you might install malware that's worse than the original problem.

The maintainer side is even harder. Especially for the massive chunk of maintainers who care and want to help. Many don't, and that's completely fine. They owe their downstreams nothing. Some of the most critical software on the internet is maintained by one or two people in their spare time. Automated scanners and AI-generated reports have already been burying them in low-quality noise for years. And unlike commercial software, open source maintainers don't have contracts or SLAs. There's no guarantee a patch gets written, merged, or that the person is even reachable.

Coordinated vulnerability disclosure was designed for a world where finding a serious vulnerability took weeks of expert work and the targets were a small set of well-known projects. A model can now find hundreds overnight in the long tail. The existing system is not going to keep up, and we all need a backup plan for the vulnerabilities that don't get patched.

## What actually needs to happen

We need a Plan A and a Plan B.

Plan A: coordinated disclosure that actually works at scale. A single, trusted group that routes fully vetted reports and patches upstream, and supports the maintainers who want help. Not a dozen competing groups filing noisy tickets. One coordinated effort that maintainers recognize and trust, so their reports get bubbled to the top of every inbox. Right now, Glasswing has managed to get about 6% of its findings upstreamed. This program will never reach 100%. That's not how the long tail of open source works. My best guess is that we can get normal coordinated disclosure working, under hard time crunches, for maybe 50% of projects at best. And it's going to take a lot of work to get there.

Plan B: how we deal with the rest. And it's not a clean split. There's a huge messy middle of projects where the maintainer responds but can't ship a fix in time, or where a patch exists but nobody downstream picks it up. For all of those, and for the projects where maintainers can't or won't patch at all, we need a maintainer of last resort. Open source gives you the right to fork. To take a project, assume stewardship, and keep it alive independently. Fork...