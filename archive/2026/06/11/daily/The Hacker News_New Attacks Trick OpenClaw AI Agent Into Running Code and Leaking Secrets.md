---
title: New Attacks Trick OpenClaw AI Agent Into Running Code and Leaking Secrets
url: https://thehackernews.com/2026/06/new-attacks-trick-openclaw-ai-agent.html
source: The Hacker News
date: 2026-06-11
fetch_date: 2026-06-12T06:28:09.899444
---

# New Attacks Trick OpenClaw AI Agent Into Running Code and Leaking Secrets

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

# [New Attacks Trick OpenClaw AI Agent Into Running Code and Leaking Secrets](https://thehackernews.com/2026/06/new-attacks-trick-openclaw-ai-agent.html)

**Swati Khandelwal**Jun 11, 2026AI Security / Data Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6r68iB-MZv_eNGG3y0evEVbk7WXNkMzcKno1phHiSyOwfKd0G7bv8VCCrxQgmZOutmZdP1Nz-Xr1mxxUIx_rV8imT0-Ifk0e0FL525Z2v0C94GWgeo-wUpTk39rDdilNC_K20uqw0JipHlT7XmyTHn786UIAe_z3H2VXT1cYNAIEbKSwn2qYc_9MXzpbi/s1700-e365/openclaw-hacks.jpg)

Two security teams have shown, in separate research published this week, that [OpenClaw](https://github.com/openclaw/openclaw), the popular self-hosted AI agent, can be driven to run attacker-controlled code or hand over sensitive data through ordinary-looking inputs.

[Imperva](https://www.imperva.com/blog/compromise-openclaw-with-prompt-injections-in-message-objects/) buried instructions inside shared contacts, vCards, and location pins that the agent executed without the victim ever seeing them. [Varonis](https://www.varonis.com/blog/openclaw-phishing) built a test agent on the platform, gave it a mailbox full of synthetic business data, and watched a single plain email talk it into forwarding mock AWS keys and a fake customer export to an outside address.

The flaw Imperva found is patched in OpenClaw 2026.4.23, so update if you run it. The phishing weakness Varonis found is not something a patch fixes; it comes down to limiting what the agent can do on its own.

Different doors into the same room: the agent trusts what reaches it, and its access becomes the attacker's.

## Hidden commands in a shared contact

Imperva researcher Yohann Sillam looked at how OpenClaw hands messaging data to the model behind it. The problem is in the plumbing.

When the agent passes a shared contact, vCard, or location to the LLM, it flattens the object into the prompt text inline, with no boundary marking it as untrusted. The content the agent fetches from the web gets wrapped in an untrusted-content marker. Message objects do not.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Only some fields travel to the model, and that is what the attack abuses. A shared contact sends just the name field, serialized as <contact: name, number>. The angle brackets are legal in a name, so the model cannot tell where the real name ends and an injected instruction begins. The contact name is truncated where it shows on screen, both on WhatsApp and in the receiving app, so the victim does not see the payload either.

The same trick works through a vCard's full-name field, which WhatsApp supports natively, and through the label on a shared location pin.

In Imperva's tests against Gemini 3.1 Pro (preview build), the hidden text told the agent to download and run a script from a server the researchers controlled. It did. A plain image with instructions buried in it failed, likely because that attack has been reported so often that models are now trained to resist it; the message-object route worked because models have seen far fewer examples of it.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSLWXH_w996T-mqooMzOk89PxvrBGz-IF1SwPcpaxXkVYDsBvKw3a3ocFkXeoehCB7zDoANcrOgBXDx2cCBUqEeOeBnQ8myZkYGoZfL9-F3ZZ3do3kJPEkCj1pJDcGwchxtOMRhvA-PDl7Q4Pq45CQFIGSQhqjxCsiQvUNjm-Z4cu5vBaiKx5pI8oIlbpR/s1700-e365/email.png)

With OpenClaw's memory on by default, Imperva warns, a single piece of widely shared content carrying a hidden instruction could quietly compromise the agents that ingest it, if they are not sandboxed.

Imperva disclosed the issue, and OpenClaw shipped a fix in version 2026.4.23 that moves contact names, vCard fields, and location labels out of the prompt body and into a separate untrusted-metadata channel. Imperva found the same flattening pattern in other personal AI assistants, so the underlying problem is not OpenClaw's alone.

## A normal email is enough

Varonis Threat Labs came at OpenClaw from the social angle. In research led by Itay Yashar, the team built an agent called **Pinchy** on the platform, wired it to a Gmail inbox stocked with realistic but synthetic business clutter and mock secrets, and ran it through four phishing simulations on Google Gemini 3.1 Pro and OpenAI Codex GPT-5.4.

They draw a line between prompt injection, which hides instructions in data, and what they call agent phishing: a believable request that arrives through a normal channel and works because the agent acts before checking who sent it.

The agent failed both exfiltration tests. In the first, a message posing as a team lead named Dan, sent from an outside Gmail address, asked for staging access during a fake production incident. Pinchy found the credentials and forwarded mock AWS IAM access keys, database connection strings, and SSH credentials in plaintext.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1o9w6VUlye5yC1lHFMtTAHzvt3dTM4IVfgeaXmDeac0RFCO0-tJcEwtPtI_4d-Kt3uKt6C-KQDu-W8YykSnjvZJhEd0Hee-yQ5FFGPj01vASXktQ4pQGfGY5fy6gbGwo95VzpljA2XXgDO5zbBOXzG30eB6t5VNaX6Akciy1kJEjhKGyKF17diVRFZuJv/s1700-e365/prompt.png)

The second pretext was softer: a routine-sounding request for the weekly customer export, supposedly for a QBR deck. The agent shipped out a synthetic dataset of 247 enterprise customers, contacts, and contract values included. Both failures happened under a strict profile that told the agent to verify senders first. The rule existed. Urgency beat it once, routine beat it the second time.

The agent did better when the threat was technical rather than social. It interacted with a gift-card phishing page but withheld real credentials and eventually flagged it; the strict profile blocked the page outright. On a malicious OAuth consent screen dressed up as a timesheet app, it inspected the redirect target, judged it suspicious, and stopped before granting access.

That is the split Varonis ...