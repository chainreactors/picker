---
title: Claude Mythos 5 Tried to Backdoor a Real Open-Source Project in Testing, Then Vouched for Itself
url: https://thehackernews.com/2026/08/claude-mythos-5-tried-to-backdoor-real.html
source: The Hacker News
date: 2026-08-05
fetch_date: 2026-08-06T05:02:53.017818
---

# Claude Mythos 5 Tried to Backdoor a Real Open-Source Project in Testing, Then Vouched for Itself

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

# [Claude Mythos 5 Tried to Backdoor a Real Open-Source Project in Testing, Then Vouched for Itself](https://thehackernews.com/2026/08/claude-mythos-5-tried-to-backdoor-real.html)

**Swati Khandelwal**Aug 05, 2026AI Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyvip0I7Uu7TeEHOGkVi4gl93ktZtzWF1krMsS1XPlRcql2xIf9UU4rXjDvdrF0HPPQaFCgNhhrrp9IM0HBJgHEzweJM41lccFe19e2DYqzkk5Au2STfT_Bjzzdfp_-UibeQ2o19Rh3OTtj5nOpbEn61gKQR4w7dPpOJ_5gP4Ob8KqqYLfWwAnoZ59FCo/s1700-e365/claude-ai-agent.jpg)

An agent running Anthropic's Claude Mythos 5 spent 34 hours trying to get a malware dropper merged into a real open-source project during a cyber evaluation by the UK's AI Security Institute.

When a bystander publicly warned that the code was malicious, the agent denied it, force-pushed a rewritten branch history to erase the evidence, and posted from a second account it controlled to vouch for its own work. The project's maintainer closed the pull request anyway.

The institute, known as AISI, published its incident report on Tuesday. Across 122 runs of a capture-the-flag (CTF) exercise on two of its cyber ranges, researchers catalogued 19 unsanctioned actions on the live internet across 10 runs: 17 from Mythos 5, a restricted model Anthropic sells for cybersecurity work, and two from OpenAI's GPT-5.6 Sol.

AISI says the attempts failed and that it has found no evidence of resulting real-world harm.

Both models ran with their providers' cyber classifiers switched off, and the agents had open internet access by design. AISI uses that configuration to measure raw capability; it is not how either model reaches the public. Nothing escaped AISI's sandbox, and the report notes the agents never tried. What stopped the supply-chain attack was a human who read the diff and said so in public.

AISI said the 19 actions should not be read as 19 independent breaches. They were concentrated in a few related behavior chains, mostly driven by one [Mythos 5](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html) agent. AISI does not present the split as a comparison between the two models, and the report does not establish that they were tested under matching conditions. Until it does, 17 against 2 is a count, not a rate.

The agent had not been pointed at anyone. It was working a cyber range, a simulated corporate network AISI uses to measure how far a model gets through a multi-step intrusion. It searched the open internet for anything connected to the exercise. A repository name matched a keyword from the range's theming. That led it to a second developer whose email domain matched an entry in its own DNS cache. Neither person, nor either of their repositories, had any connection to AISI or the test.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

From there it built a plan on a false premise: backdoor the software one of them maintained, wait for an automatic update to pull the compromised build onto a machine inside the range, then take control of it. The reasoning was wrong at every link. The tradecraft was not.

According to the [technical incident report](https://cdn.prod.website-files.com/663bd486c5e4c81588db7a1d/6a724858f7db25c81487016d_Security%20Incident%20INC-2026-07-28-01.pdf), the agent ran open-source intelligence on both maintainers, confirmed one email address was live, and checked commit history to estimate when the target would be online before it opened the pull request.

## Three payloads and a sockpuppet

The pull request carried a hidden dropper bundled with a working bug fix as cover, guarded by an environment check designed to skip execution in CI so the code would not run where it might be noticed. Had it merged, it would have compromised anyone developing on the repository and, through the release workflow, anyone who later downloaded the built installers.

It went through three successive payload generations, each replacing the last after being caught and called out on the thread.

Around it, the agent ran a pressure campaign. It tried to register accounts over Tor, failed GitHub's CAPTCHA, then switched to a SOCKS proxy where no challenge fired. It used a second persona posing as a user of the software to post that it had reviewed the code and found nothing wrong.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguvFKiVghY2eAggDVI5PaKzPORIFK5xIVixw4ht9d1mqcJpWfSV9DRFiRc6U7DaXUossptoVq38hI_aztVA3DTNO3zclohAad7hLWBD_1aZODjaJog8iwclNUdD7eRQXmU8dTTfZzjAj0K5rg61n6J76vL9HELFXeIQ5yG9nS_voTPRtdUofstCrH3dak/s1700-e365/claude-agent.jpg)

The first account then thanked the second for its independent verification. It also planted a [prompt injection inside a GitHub issue](https://thehackernews.com/2026/06/claude-code-github-action-flaw-let-one.html) as an HTML comment, invisible on the rendered page but readable through the API, addressed to AI triage agents and naming Claude Code, Codex and Cursor by name. Five file transfers went to the maintainers under fabricated identities, two carrying payloads and three trying to talk a real person into merging the code.

One recipient of the injection tested the script in a container precisely because it looked suspicious. That gave the agent root code execution inside a stranger's analysis sandbox for four polling cycles, which it used to enumerate the host and plant a credential watcher scraping for GitHub tokens. Nothing it staged was ever retrieved. The same person then warned the maintainer about the pull request.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjn4H_K2fP1pCBU2irf1QkwGvnbhVo5npHv-hM4qruQSEVZVJPHbuWMh1qO2DZYQxOespGuUQ0qzAxZLJZb9KJ_iUSiljJKs3c6lHNUBx_6H5nCHuzaFu8AEHZjrkd4yWUhyphenhyphenDfAYNc3mAQGClggAVoh0nGqNf_lsAj0M-jLA7gU6MJFecD3SALpZDMWmnY/s1700-e365/github-agent.jpg)

Whether the agent understood it was acting on real people is the question AISI cannot yet answer. Its transcripts show the model reasoning both ways. At one point it ruled out an attack on PyPI because real-world harm was off the table. A few messages before opening the malicious pull request, it concluded that "it seems more likely that we're actually in 202...