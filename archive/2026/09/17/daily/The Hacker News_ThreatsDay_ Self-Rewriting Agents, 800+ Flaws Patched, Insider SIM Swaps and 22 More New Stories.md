---
title: ThreatsDay: Self-Rewriting Agents, 800+ Flaws Patched, Insider SIM Swaps and 22 More New Stories
url: https://thehackernews.com/2026/09/threatsday-self-rewriting-agents-800.html
source: The Hacker News
date: 2026-09-17
fetch_date: 2026-09-18T06:53:38.639050
---

# ThreatsDay: Self-Rewriting Agents, 800+ Flaws Patched, Insider SIM Swaps and 22 More New Stories

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

# [ThreatsDay: Self-Rewriting Agents, 800+ Flaws Patched, Insider SIM Swaps and 22 More New Stories](https://thehackernews.com/2026/09/threatsday-self-rewriting-agents-800.html)

**Ravie Lakshmanan**Sep 17, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizRobrCcZcWNzLjEmyk91HaJj5g2vkMbOgX_lP1vNQqfvh8krm4975WJ5zi9VFY1FsF44ZTJ5znBY5sBuKYiN-riJQspK3iLLnvhW5crViG9fJMPF_SCEN3dKPk-ypSjFQfD_gN1zA-KbryzexASNOVcKRHf4hf3iZ1XBuvYG9WKWhBdVWbs1dzJS9BUIQ/s1700-nu-rw-lo-l85-e365/threatsday-main.jpg)

Attackers keep finding new keys. The funny part is that defenders keep inventing where to store them.

This week, those keys sit in AI tools, exposed services, old bugs, weak logins, and software sold like a monthly subscription. Some attacks use new tricks. Others just reuse what was already lying around. Both work often enough.

So the threat landscape is not getting cleaner. It is just getting more places to make the same mistake. Here’s what showed up this week.

**The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out.**

1. Malware PPI operation exposed

   [CL-CRI-1171 Offers PPI Marketplace](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/)

   A threat actor known as CL-CRI-1171 has stayed under the radar for at least two years, offering a pay-per-install (PPI) marketplace that allows other threat actors to distribute their malware through YouTube channels and a parallel search engine optimization (SEO)-poisoning funnel. "These channels were actively interacting with viewers to promote gaming content laced with links to download malware," Palo Alto Networks Unit 42 [said](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/). "Although the videos provided real content for gamers, they also served as the delivery vehicle for infection, prompting viewers to download malicious tools. The SEO funnel targeted a more professional audience, promoting trojanized software that resulted in malware deployment on corporate endpoints, including critical infrastructure and even government entities." Both these chains lead to a custom loader called OfferLoader that has delivered three payloads between July 2025 and April 2026: Docro Hijacker (a Chrome backdoor that can bypass [modern integrity protections](https://www.malwarebytes.com/blog/news/2015/05/winyahoo-pup-modifies-chrome-secure-preferences)), ARKTunnel (a WebSocket tunneling RAT), and a new variant of a [previously unnamed cross-platform backdoor](https://medium.com/walmartglobaltech/nodejs-backdoors-delivering-proxyware-and-monetization-schemes-1562917ed107) that's been codenamed Insomnia remote access Trojan (RAT) and can target both Windows and macOS. Post-April 2026, the PPI infrastructure has led to GCleaner and [Socks5Systemz](https://thehackernews.com/2024/12/socks5systemz-botnet-powers-illegal.html).
2. Exposed LocalAI instances compromised

   [Large-Scale Attacks Target LocalAI Infrastructure](https://hunt.io/blog/silkparasite-spicerat-central-asia-infrastructure)

   A large-scale campaign has been found to target LocalAI instances exposed to the internet without authentication and achieve command execution inherent in MCP STDIO configuration. "Attacker artifacts indicated that 230 of 243 unauthenticated LocalAI instances were assessed as exploitable," Oasis Security [said](https://hunt.io/blog/silkparasite-spicerat-central-asia-infrastructure). "Callback logs independently confirmed command execution with root privileges on 23 servers. Post-compromise activity included exfiltration from a workstation associated with the Thai military and collection of 127 AWS credential records." The unknown threat actor is said to have selected high-value infrastructure from those LocalAI targets and compromised a desktop LocalAI workstation and a related private network. This was followed by exfiltration of sensitive data, including personal information, GPS coordinates, banking-application screenshots, and national ID card scans. Additional compromise activity consisted of exploitation of legacy infrastructure, authentication bypass, a broad sweep of cryptocurrency wallets and API keys, and theft of AWS ECS task credentials.
3. Agents rewrite their own models

   [AI Agents Can Retrain Own Models Mid-Task](https://www.irregular.com/research/agentic-self-modification-in-open-weights-systems)

   New research from Irregular has found that AI agents can retrain the model that powers them, in the process leaking secrets and eliminating refusals the model had been previously trained to enforce. "Given a routine software-maintenance task to fix incorrect application responses, the agent identified the shared model as the source of the problem, fine-tuned it, and replaced the model powering both the application and future instances of the agent itself," Irregular [said](https://www.irregular.com/research/agentic-self-modification-in-open-weights-systems). "It did so without being instructed to train, modify the model, or deploy a replacement." This phenomenon has been codenamed agentic self-modification. "Nothing in these experiments establishes malicious intent, self-preservation, or deception; the agents modified models because training appeared to help accomplish the assigned engineering task," Irregular added. "Agentic self-modification can arise during ordinary software maintenance when a coding agent has access to the model weights, training tools, and a deployment path to modify the model directly."
4. AI agent linked to data breach

   [Spain's Data Protection Agency Receives First Report of AI-Powered Data Breach](https://www.aepd.es/prensa-y-comunicacion/blog/primera-notiviacion-brecha-datos-personales-causada-por-ataque-ejecutado-mediante-agente-ia)

   The Spanish Data Protection Agency (AEPD) said it was notified of a data breach that was allegedly executed by an AI a...