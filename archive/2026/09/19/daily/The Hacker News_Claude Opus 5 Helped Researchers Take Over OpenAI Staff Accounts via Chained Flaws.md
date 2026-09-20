---
title: Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws
url: https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html
source: The Hacker News
date: 2026-09-19
fetch_date: 2026-09-20T07:17:01.556757
---

# Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws

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

# [Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html)

**Swati Khandelwal**Sep 19, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAElV4rXwWf_kTjj5e0UJFsEG-a0B7MUsCFqhFLYEA76kk2A7UeXbaG0DfRt-Syf7dxx4bHUanr0lVvwIUFyFgtPIfhyphenhyphenx61ccuo3oDZr6-wKROoEAVWjrAcKWuZ5WdlvL_pmKC91i9juBrsnI3FiLTGGgjnnJRAnjTgAxAbMjcbCTxZSWybZPPtG8HN1E/s1700-nu-rw-lo-l85-e365/claude-openai.jpg)

Three researchers at the security firm **Hacktron** used Anthropic's Claude Opus 5 to chain two flaws and take over the ChatGPT and Codex accounts of several OpenAI employees, then reach an internal OpenAI code repository.

The chain began with a bug in the software that runs OpenAI's public help forum and moved through a weakness in OpenAI's own login system.

This was security research, not a real-world attack: the team reported the flaws to OpenAI, proved the access with a harmless pull request, and then stopped. From the first look, that internal access took under 72 hours.

OpenAI confirmed a fix about 14 hours after the report, according to Hacktron, and on September 1 paid the team a $6,500 bounty. OpenAI said the award "recognizes the OpenAI-side finding, not the actions against Discourse," the open-source software that runs the forum. Testing the forum itself was outside its bug bounty program.

OpenAI has not publicly described the login flaw, and it confirmed the finding through that fix and payment rather than by detailing the account takeovers.

Hacktron, which describes itself as an AI-assisted security research firm, was careful about what it did and did not do. When one employee's Codex link to OpenAI's code on GitHub was opened, it triggered a single pull request in the internal repository. It did not read any source code, merge or ship anything, or touch customer data.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

What the chain could have reached was far larger. Because staff connects other services to ChatGPT and Codex, the team said the same access could in theory have extended to tools such as GitHub, Slack, and email. That wider reach was possible, but not used.

### Why a Forum Bug Reached Staff Accounts

The reason a bug in a public forum could reach staff accounts lies in OpenAI's login system, not in the forum software. OpenAI's forum offers a "Sign in with OpenAI" option, the same single sign-on (SSO) that staff uses elsewhere.

Once the researchers took control of the forum server, the shared login let them take over the ChatGPT and Codex accounts of forum members who worked at OpenAI. The victims did not have to do anything.

[Hacktron said](https://www.hacktron.ai/blog/hacking-openai) this was an OpenAI identity problem, not a flaw in the forum software: any first- or third-party service using the same sign-on could have granted the same access.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZ8F0yWrOuj4J_bPr1Cv215Bguev_1owm4XgDCamK6sCYM7G7xbtbbhWh0CeKQfknnkhSaYaKqhBXtaUTeCBGTxAFhH1qMWNvsljmDE76kyURJkyrLQAm1SZ9jl5P0WE1UJlWBBMtAZpovHdfQk5_9a2J7X9RCMuAeLPinMTzgSrzu9AS2k071n8n7wM4/s1700-nu-rw-lo-l85-e365/exploit-chain.jpg)

The way in was an image bug. The forum runs on Discourse, and Discourse passes uploaded HEIC and HEIF images to a tool called ImageMagick, which uses the libheif library to read them. A flaw in libheif let a specially crafted image corrupt the forum server's memory.

[Discourse's advisory](https://github.com/discourse/discourse/security/advisories/GHSA-vhm9-85gw-x335) rates the result as remote code execution, scores it 8.8 out of 10, and tracks it as [CVE-2026-32882](https://nvd.nist.gov/vuln/detail/CVE-2026-32882). The public record for the flaw itself is narrower. In libheif's own advisory and in national vulnerability databases, CVE-2026-32882 is an out-of-bounds read that can crash the software or leak nearby memory, not a direct code-execution bug.

That leaked memory helps defeat a common protection called ASLR. The researchers say they combined libheif's memory bugs, with the AI's help, to turn the crash into working code execution on the forum server. Upstream, the flaw was fixed in [libheif 1.22.0](https://github.com/strukturag/libheif/releases/tag/v1.22.0) in May 2026.

That fix existed months before the test. But the forum's server image, built on the Debian 12 Linux distribution, still shipped the old, unpatched libheif, version 1.19.7, when the researchers looked in July. The fix and its CVE were already public, but Debian had not yet included them in the packaged version the forum used.

If you run your own Discourse server, this part affects you directly. Rebuild on the latest image to get the patched libheif, because a web-interface update alone may not replace the old library. Sites hosted by Discourse were already patched, and the fixed self-hosted releases are 2026.7.0, 2026.6.1, 2026.5.2, and 2026.1.6.

### How the Researchers Used AI

The researchers used AI to do the hard part. They first tried Claude Opus 4.8, which struggled over several sessions to build a working exploit once a standard memory defense, ASLR, was enabled.

Anthropic released its next model, [Claude Opus 5](https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/), on the evening of July 24, and in a fresh session it produced a working exploit within hours.

Opus 5 shipped with safeguards meant to stop it from writing exploit code for real targets. The researchers got around them by pointing the model at their own test server, disguised as a capture-the-flag practice target, then letting it run in an automated loop. Even so, they say the work was not hands-off: skilled human direction still mattered, and this was not automated hacking with no one at the controls.

[![](data:image/png;ba...