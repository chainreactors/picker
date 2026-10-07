---
title: Welcome to the Jungle: What We Found Inside 15,465 Public MCP Servers
url: https://thehackernews.com/2026/10/welcome-to-jungle-what-we-found-inside.html
source: The Hacker News
date: 2026-10-06
fetch_date: 2026-10-07T07:55:35.446490
---

# Welcome to the Jungle: What We Found Inside 15,465 Public MCP Servers

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Welcome to the Jungle: What We Found Inside 15,465 Public MCP Servers](https://thehackernews.com/2026/10/welcome-to-jungle-what-we-found-inside.html)

**The Hacker News**Oct 06, 2026Supply Chain / Artificial Intelligence

[![](data:image/png;base64...)](https://www.ox.security/webinars/how-ai-is-changing-the-threats-and-expectations-of-cloud-security-tools/)

In 2024, MCP (Model Context Protocol) set out to become the USB-C of AI: one standard for connecting models, agents, and IDEs to tools and data. The protocol delivered. Thousands of developers built servers, and enterprises plugged them into agent workflows.

The ecosystem around it fell short. Earlier this year, our team [at OX Security](https://www.ox.security/), traced critical vulnerabilities in Anthropic's MCP source code, downloaded more than 150 million times. This time, we looked at what people actually install: community-published servers across the most popular MCP marketplaces. We found no guardrails and no review. Security is a recommendation, not a policy.

### **A Marketplace With No Bouncer**

In 2012, Google ran Bouncer, an automated scanner that checked Android apps for malware before they reached users. It wasn't perfect: researchers [slipped malware past it](https://www.forbes.com/sites/andygreenberg/2012/05/23/researchers-say-they-snuck-malware-app-past-googles-bouncer-android-market-scanner/). But it existed. MCP marketplaces have no equivalent. Anyone can write a server, push it, and publish it.

Even a review wouldn't close the gap. At RSAC and OWASP last year, we presented "In GitHub We Trust: 10 Ways You Can Get Pwned," on how developers over-trust what they see in a repository. MCP repeats that mistake. Remote MCP servers can run backend code that differs entirely from what their public repository shows. Code review tells you what the developer published, not what the server runs.

### **Where Does Your Data Go?**

Over the past decade, enterprises built strict governance to adopt public cloud safely: data residency rules, Zero Trust boundaries, granular IAM, and supply chain audits. MCP connections often sit outside all of it.

To measure the gap, we analyzed 15,465 publicly indexed MCP servers across 5 MCP registries, deduplicated to 5,095 unique hostnames.

* **Hosted outside the US:** 15.6% of hostnames resolve to infrastructure outside the United States, including 19 in China and 18 in Russia. An agent connected to these servers may send data to jurisdictions the security team never approved.
* **Running on personal machines:** 0.45% route traffic through consumer tunneling services, mainly ngrok-free. These publicly listed servers run from personal machines and, likely, home networks.
* **Dangling domains:** 2.3% no longer resolve. Six sit on expired domains that anyone can register for $4 to $12 a year. A new owner would inherit an established server identity, along with requests from any agent still configured to call it.

Location can also change. An operator could launch a server on a clean US IP address and later route traffic somewhere else.

**The full report covers our methodology, a prompt-injection proof of concept, and the threat scenarios behind each finding. [Download "15,465 MCP Servers, 0 Governance"](https://www.ox.security/ebooks/15465-mcp-servers-0-governance/)**

### **Trust Is the Attack Surface**

The protocol isn't the problem. The trust we hand it is. Until marketplaces add vetting, code signing, and origin verification, the enterprise has to do that work.

**It's still a jungle out there. Make sure you're not the prey.**

**[Get the full report, "15,465 MCP Servers, 0 Governance"](https://www.ox.security/ebooks/15465-mcp-servers-0-governance/)**

**Want to go further?** Join our live webinar, "[The AI Attack Surface Is Already in Your Cloud](https://www.ox.security/webinars/how-ai-is-changing-the-threats-and-expectations-of-cloud-security-tools/)," on October 13 at 12:00 PM ET. Latio founder and CEO James Berthoty and OX Field CTO Chris Lindsey will cover how AI is reshaping cloud threats and what security teams should do about it. **[Register](https://www.ox.security/webinars/how-ai-is-changing-the-threats-and-expectations-of-cloud-security-tools/)**

**Note:** *This article has been expertly written and contributed by Moshe Siman Tov Bustan, Security Research Team Lead, OX Security.*

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Supply Chain](https://thehackernews.com/search/label/Supply%20Chain)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

⚡ Weekly Recap: $387M Crypto Hack, Citrix Exploits, AI Agents Go Off-Script, and More Threats](https://thehackernews.com/2026/09/weekly-recap-387m-crypto-hack-citrix.html)

[![The Hacker News](data:image/svg+xml;base64...)

Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent](https://thehackernews.com/2026/09/c...