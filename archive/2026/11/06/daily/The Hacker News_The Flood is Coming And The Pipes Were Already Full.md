---
title: The Flood is Coming And The Pipes Were Already Full
url: https://thehackernews.com/2026/11/the-flood-is-coming-and-pipes-were.html
source: The Hacker News
date: 2026-11-06
fetch_date: 2026-11-07T08:02:14.048768
---

# The Flood is Coming And The Pipes Were Already Full

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [The Flood is Coming And The Pipes Were Already Full](https://thehackernews.com/2026/11/the-flood-is-coming-and-pipes-were.html)

**The Hacker News**Nov 06, 2026Open Source Security / Supply Chain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhRlCxdfW4sb5-1zEBHpFyJfxetSva89fr67wc8zSfvidW5W4KQKckoTrRxOAUbjM94U2ydFjiXybLJPrp6pm1V-WUuC4IpkJjhIT56OG8go8E_8fR8cK-llV0UtXdRIxZS5XxuVwEbRj1G_zAErMjpkMHVdzkGBQrB46VErPyE7MBaW6sj0N64pRd3_A/s1700-nu-rw-lo-l85-e365/FLOOD.jpg)

*An update on Athena, and some unsolicited predictions on what's coming next*

On Saturday, Dario Amodei published *We Must Pace the Frontier*. I agree with him. Go read it if you haven't. I've spent the summer looking at what these models find, and the gap he describes between what they can do and what the rest of us are ready for is the one I've been staring at since May.

The hardest piece of his plan is the one that asks governments to coordinate. They're in a difficult spot: regulate too little and a US company accidentally builds the weapon, regulate too much and it gets built somewhere else, and open source isn't governable either way. Where governments can act is on consumption: not what the models can do, but what happens to what they find. Who gets a vulnerability first, how fast a fix reaches the people running the code, whether the operators who can't move on an attacker's timeline get a head start. That's what Gold Eagle is.

It matters because of where the risk actually lands. The danger in Dario's essay isn't a model in a lab. It's a model pointed at the power grid, the water system, the hospital network, all of it running on decades of software with the same exploitable design. The frontier is where the capability comes from. Consumption is where it does damage, and that's the end you can still defend.

So pacing has two ends. The frontier end is Dario's and the government's problem, and it's hard. The consumption end is ours: the disclosure processes, the patch pipelines, and the software itself, everything that has to absorb what the models produce. Pacing buys time on the frontier end. This post is a status report on how we're spending it, in three parts:

1. We start disclosing Athena findings this month, beginning with 50.
2. We joined Anthropic's Project Glasswing and are finding our own vulnerabilities, and I'll show you what that looks like.
3. We built infrastructure to make both possible, and we're going to open it up.

The short version: I'm more worried than I was in May, and more sure about what to do about it.

## The first 50

Athena has been taking in findings since June. The intake numbers are public: more than 40,000 findings, 42% of them critical or high, across more than 500 projects, with more than 2,000 patches produced. What hasn't been public is how much of that we've been sitting on. Generating fixes was never the bottleneck. Disclosing them responsibly, at a scale nobody has ever tried, is.

On September 28, we start. We're beginning with about fifty, and none of them are the scary ones. That's deliberate. The frightening findings, the live pre-auth RCEs, go through Akrites on embargo, which I'll come back to. The first 50 are low-stakes on purpose: a small batch to get the flywheel turning and find out what breaks before the thousands behind them hit it.

All 50 are silent fixes: vulnerabilities already fixed at head, sometimes years ago, where nobody ever filed a CVE. Your scanner has nothing to say about them, and the old versions are still running everywhere. This pattern showed up in Athena almost immediately. A big share of what the models find only affects old versions, because the models scan what's actually deployed, and what's deployed is old.

Two systems fail at once with silent fixes, and neither is anyone's fault. Upstreams typically won't merge fixes to old versions, and they're right not to: the code was rewritten years ago, there's no branch to merge into, and "upgrade" is the correct answer. And the advisory layer has nothing to work with, because CVEs don't get filed for things already fixed at head. It's the one class of finding where acting doesn't step on anyone else's process, because there isn't one.

For each one, where the project has no path for accepting fixes to old versions, we're doing three things.

**We publish the patch.** Plain .patch files, in a public Chainguard repo that says exactly what it is on the tin, under the project's original license. This is deliberately not a maintainer-of-last-resort move. We have plans for that, and I'll get to them below, but they're for projects nobody maintains anymore. These are active projects that already fixed the bug at head. We're not forking anything, not claiming stewardship, not creating a new namespace, and not inviting anyone to build from it. It's a place to put patches for the people who can't upgrade yet, and nothing more. The durable fix is still upgrading, but this step reflects today's reality, where most of what's deployed isn't upgraded.

**We publish the advisory.** A Chainguard OSV feed, with fully enumerated affected version ranges and the exact symbols affected. Not "some 2.x releases, probably." Athena partner scanners are integrating with it now, so these show up where your team already looks.

**We ship the fix.** Patched versions land in Chainguard Libraries for every Chainguard customer the moment the advisory goes live.

We're not planning to contact maintainers ahead of each of these. They already deal with more noise than anyone should, and we don't want to add to it, least of all for bugs they fixed years ago. If you maintain a project and you'd rather hear from us in advance going forward, or you have any other concerns about how this touches your project, let us know at cna@chainguard.dev and we'll happily work with you.

## We're becoming a CNA

A silent fix used to be mostly harmless. Nobody had written the bug down, and finding it from a fix comm...