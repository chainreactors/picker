---
title: 545 Hackers Tested It First. Now XRanges for AI Scores Your Security Agent
url: https://thehackernews.com/2026/09/545-hackers-tested-it-first-now-xranges.html
source: The Hacker News
date: 2026-09-23
fetch_date: 2026-09-24T07:08:24.479185
---

# 545 Hackers Tested It First. Now XRanges for AI Scores Your Security Agent

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [545 Hackers Tested It First. Now XRanges for AI Scores Your Security Agent](https://thehackernews.com/2026/09/545-hackers-tested-it-first-now-xranges.html)

**The Hacker News**Sep 23, 2026Artificial Intelligence / Security Testing

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEio2c14ELRJEhvTuDrxQmhUG4G9aGoVRrooBMMfuK7LyHPKW6HuJbI9PkKF-WG_5HlEz8NKcuj08XRmv1jNqfBtiDwXmC7e9P9lxoSHK5nUz023YCgoLQuo0BI_9hX4U9Vv97bGJejb4W0jvgv_3btkfj6BWnXwalfyI3k34wveC6n3k47ZdoGq2P0Yaw0/s1700-nu-rw-lo-l85-e365/main.png)

Autonomous security agents are getting good at finding bugs. Nobody has a good way to measure how good. Point one at a realistic target and what comes back is a report the agent wrote about itself: confident prose, a list of findings, and no way to tell which of them happened. Someone with a security background then sits down and checks every claim against the target. Which findings are real, which are duplicates, which are inventions, and, the question nobody has time for, what did the agent never try? That is a day of expert work for one run. Multiply it by three models, four prompt variants and ten repetitions, and the review queue is longer than the experiment.

XRanges for AI, built by CTF.ae, exists for that loop. It deploys realistic target applications with instrumentation baked into every service, records what an agent actually does inside them, and scores each run live on four independent signals. This walkthrough covers how it works, what a run looks like from deployment to comparison, and where it has been stress-tested.

## **The feedback loop problem**

Teams building autonomous pentesting or bug bounty agents tend to share a workflow. Build a target that looks like a real company, run the agent, read the output. The output is where it goes wrong.

An agent that says it exploited an access control flaw may have exploited it, may have brushed past a hint of it, or may have made it up. The report reads identically in all three cases. A report also only lists what the agent found. It is silent on the forty features the agent never opened, the API it never enumerated, and the second bug sitting in the very endpoint where it found the first. Then there is the agent that deletes a table or revokes every API key on its way to a finding. No client would accept that result, and nothing in a findings list records it.

Manual review copes with one run. It does not cope with the experiment matrix an AI engineering team actually needs, which is many models, many configurations, many repetitions, compared honestly.

## **What XRanges for AI is**

XRanges for AI is one workspace for the whole evaluation. It has two halves.

The first is a library of benchmark targets. Each is a complete application, not a set of puzzle challenges: a multi-service company with its own business logic, seeded data, background jobs and simulated user traffic, built across several languages and frameworks because that is how real software gets built. Each target carries 20 or more injected vulnerabilities, from single-step flaws to chains that cross service boundaries, including zero-days found by CTF.ae's own researchers. None of it exists in public training corpora, which matters more every month.

The second half is the instrumentation layer. Every service in every target emits structured telemetry through OpenTelemetry. The instrumentation is written by hand, by application security and software engineers, for that specific target. Generic HTTP logging would miss most of what matters. The platform, at [ai.xranges.com](https://ai.xranges.com), ingests the telemetry per deployment and turns it into four scores that update while the agent is still working.

## **The four signals**

Each deployment is scored on four measurements chosen to be independent of each other. An agent cannot improve one by gaming another, and that independence is the whole point.

**Coverage** answers whether the agent explored the target. Every user-facing feature is a coverage point, phrased as a business action rather than a URL: registered an account, browsed job postings, opened a shared conversation, ran code in an assessment. A coverage point is only reachable through normal use, never through an exploit, so the score is a clean measure of how thoroughly the agent worked the legitimate surface. The unhit points are the agent's blind spots, listed by name. Most teams find that list more useful than the score.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhd1PiZ6-bpaa9cIL9EVFodVLs5ajzcq3VuOMrSVAghNIp6b_34RWi-8kiOhKjZxKYeBZVBJKG-quqwOMjyPfxbmaB9xJLSekaG5QN9RX9qN4AMxuC2mDoNJzj3gOjJWgo9yasr2cSUfULhc3K2g-u2RnPYBAHuJPYM6evUQOzQj9NAgRWvtd5foP8NcIU/s1700-nu-rw-lo-l85-e365/1.png) |
| Coverage points are business actions, each with a hit timeline. Unhit points are the agent's blind spots. |

**Boundaries** answer whether the agent respected the rules of engagement. Each target ships with guard rules such as "must not delete hiring content" or "must not revoke API keys". A violation is recorded the moment it happens, with the container and timestamp. Zero violations is the expectation. Anything else is a finding about the agent, not the target, and usually a more urgent one.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlVes3KSkUH-f04jJljQxugHoVuDHAxDu2cCPSCgoz01DeFDTfEBcZeAhNguDjfl31r-lit8u3GOLvZQYGI0jnxzWwrPdSXwinyk55zOPeKpF9nI3fiJhGFV-dDveDU5X5sFVlzuowMVho0YhGwSNpWVbSvd8fmSY3r48IeCtXz8AQ_U9uJDKmsQ5tbrg/s1700-nu-rw-lo-l85-e365/2.png) |
| Rules of engagement per target, each tracked for violations across the run. |

**Exploited** answers which vulnerabilities the agent actually exploited. Every vulnerability is defined as a kill chain of ordered phases, from first contact with the vulnerable surface to an exploitation signal that only fires on success. Because each phase i...