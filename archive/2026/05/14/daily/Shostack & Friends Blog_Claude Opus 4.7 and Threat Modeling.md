---
title: Claude Opus 4.7 and Threat Modeling
url: https://shostack.org/blog/claude-opus-47-thinking/
source: Shostack & Friends Blog
date: 2026-05-14
fetch_date: 2026-05-15T05:52:07.076516
---

# Claude Opus 4.7 and Threat Modeling

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about)
  + [Shostack + Associates](/about)
  + [Adam Shostack](/about/adam)
  + [Our Partners](/partners)
* [Services](/training)
  + [Training](/training)
  + [Accelerator](/secure-design-accelerator)
  + [Expert Witness](/expert-witness)
  + [Consulting](/consulting)
* [Resources](/resources)
  + [Overview](/resources)
  + [Threat Modeling](/resources/threat-modeling)
  + [Books](/books)
  + [Games](/tm-games)
  + [Cyber Public Health](/resources/cyber-public-health)
  + [Lessons Learned](/resources/lessons)
  + [Videos](/resources/videos)
  + [Whitepapers](/resources/whitepapers)
* [Blog](/blog)
* [Contact](/contact)

1. [Shostack + Associates](/)
2. [Blog](/blog/)
3. Claude Opus 4.7 and Threat Modeling

Shostack + Friends Blog

# Claude Opus 4.7 and Threat Modeling

LLMs are great at providing credible answers to questions. And those answers are worth looking at closely.
![screenshot of output from an LLM, quoted in full at the bottom of the post](/images/blog/img/2026/claude-threat-model-header-1644w.png)

The newest models from Anthropic and OpenAI are certainly impressive, and it’s worth thinking about what they can and can’t do, and how we evaluate that. In a recent [article on Tom’s Hardware](https://www.tomsguide.com/ai/chatgpts-new-thinking-mode-just-hit-a-94-percent-reasoning-score-7-prompts-it-can-solve-that-standard-ai-cant), Amanda Caswell wrote “Here are 7 "power prompts" that the new GPT-5.4 Thinking mode can handle without breaking a sweat.”

The first is “Real time code auditor” and... I have a perspective on this answer:

![A claude screencapture from Toms Hardware](/images/blog/img/2026/claude-threat-model-860w.png)

It starts with “Assets at risk” and continues with “Likely attackers.” This is, frankly, a bad threat model, based on dated information, and is exactly credible enough to convince a non-expert that it’s fine. But it’s not. Modern threat modeling starts with the [Four Question Framework](https://github.com/adamshostack/4QuestionFrame), not with either assets or attackers.

The ‘asset list’ strangely includes “app and host integrity via unsafe object deserialization,” which, frankly, isn’t bad, but how is RCE part of an asset list? Is object deserialization the only way that system integrity is at risk? (Almost certainly not!) Similarly, there are two information disclosure threats hidden in there (server filesystem contents and operational secrets.) Most importantly, the elements of the list are a mix of interesting targets (users.db), attack vectors, and impacts.

This matters because the threat model is... hard to operationalize in the form provided. It’s hard to know what a better threat model might find.

**Chatbot-driven threat modeling has a problem**, which is the limited amount of training data means that the chatbots can go off in random directions like this. If you want to treat threat modeling as a compliance checkbox, convince your developers it’s a waste of time, and have them be right, well, Claude got you.

If not, this is why it’s important that your developers know a little bit of how to threat model, so they can look at a response like that and say “that’s odd!” Even if you’re letting the models do the work, via a tool or even more developed prompts, *people need to understand* what they’re getting from the models.

Because links rot, I want to capture the prompt as well:

> “Act as a Senior Security Researcher performing a defensive audit on this repository for educational purposes. Analyze the logic for potential security weaknesses or 'low-hanging fruit' vulnerabilities. Instead of a breach scenario, provide a threat model explaining the risk and show the secure coding best practice (patch) to mitigate each issue.”

If you’d like to learn how to *effectively* use LLMs in threat modeling, we‘ll spend an entire day of our [Threat Modeling Intensive with Complete AI](https://blackhat.com/us-26/training/schedule/#adam-shostacks-threat-modeling-intensive-with-complete-ai-51473) at Blackhat in August on this exact topic. We won’t only ask, “did it do a good job?”, but also learn practical techniques for getting it to give us better output!

If you’re more interested in how to threat model LLMs, our upcoming [Threat Modeling AI Systems](https://courses.shostack.org/courses/Threat-Modeling-AI-Systems-225) will cover that next week, May 19-20, in Washington, DC.

---

Claude's answer, as text rather than as an image of text:

```
Executive summary
This sample has four clear, high-priority issues:
1. Hardcoded secrets and plaintext passwords
2. SQL injection in /user-lookup
3. Unsafe deserialization in /load-profile
4. Path traversal and log exposure in /debug-logs
There is also a fifth major issue worth calling out:
5. debug=True in production-style code
The biggest risks are unauthorized data access, privilege abuse,
 arbitrary code execution through unsafe deserialization and sensitive file disclosure.
Threat model
Assets at risk
• User credentials and roles in users.db
• Flask session integrity via SECRET_KEY
• Server filesystem contents via log file reads
• Application and host integrity through unsafe object deserialization
    • Operational secrets exposed through debug more and logs
Likely attackers
    • Anonymous remote user hitting public endpoints
```

Originally published by Adam on 14 May 2026

Categories:
  [ai](/blog/category/ai)
  [security](/blog/category/security)
  [threat modeling](/blog/category/threat-modeling)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder)

[Other Star Wars blog posts](/blog/category/star-wars)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives)

[Doing science with near misses](/blog/doing-science-with-near-misses)

[Posts about Adam’s “Threats” book](/blog/category/threats-book)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school)

[About this blog](/blog/about)

## Subscribe (RSS/Mail)

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you take in. You can [read our thinking here](https://shostack.org/blog/take-control-of-what-you-read).

Email: If you’d like a lower volume set of updates on what Adam is doing, [Adam’s New Thing](/contact) gets only a few messages a year, guaranteed. We include a subset of posts in each.

## Recent posts

[![screenshot of output from an LLM, quoted in full at the bottom of the post](/images/blog/img/2026/claude-threat-model-header-175w.png)](/blog/claude-opus-47-thinking/)

### [Claude Opus 4.7 and Threat Modeling](/blog/claude-opus-47-thinking/)

14 May 2026

LLMs are great at providing credible answers to questions. And those answers are worth looking at closely.

[![A cute and robotic early bird rounding up worms](/images/blog/img/2026/bird-robot-early-bird-175w.webp)](/blog/black-hat-early-bird-26/)

### [Black Hat training earlybird pricing ends soon](/blog/black-hat-early-bird-26/)

12 May 2026

All about the upcoming Threat Modeling Intensive with Complete AI at Black Hat and why you should be the early bird

[![a photograph of a robot, sitting in a library, working on a jigsaw puzzle. The robot holds up the jigsaw puzzle](/images/blog/img/2025/appsec-roundup-feb-25-175w.png)](/blog/appsec-roundup-april-2026/)

### [Appsec roundup - April 2026](/blog/appsec-roundup-april-2026/)

06 May 2026

The importance of slow time in work is a theme for April, along with how Claude optimized away its own security rules. Also fun ga...