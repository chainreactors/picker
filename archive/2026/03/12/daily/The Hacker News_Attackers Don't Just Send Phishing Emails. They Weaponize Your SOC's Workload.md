---
title: Attackers Don't Just Send Phishing Emails. They Weaponize Your SOC's Workload
url: https://thehackernews.com/2026/03/attackers-dont-just-send-phishing.html
source: The Hacker News
date: 2026-03-12
fetch_date: 2026-03-13T04:08:04.141552
---

# Attackers Don't Just Send Phishing Emails. They Weaponize Your SOC's Workload

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Attackers Don't Just Send Phishing Emails. They Weaponize Your SOC's Workload](https://thehackernews.com/2026/03/attackers-dont-just-send-phishing.html)

**The Hacker News**Mar 12, 2026Artificial Intelligence / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicyAymkVT6oOh3KGSa7rCPyMlrrye6CVfJ2XVCt_iVvuatelOJiFXIV5YnOzaGBJFs8et6STAZ67nRfN49Ac9aouuN7jDZWAum8Bdy3wfcj27lYGNcWTA_i5Rm4DYXLzKJyUGc2ZdS6AXasd0LTgdgx8PdqKRRo6s_hZ7FwXNFE6kGDmN6B1z5BYrcsxE/s1700-e365/conf.jpg)

*The most dangerous phishing campaigns aren’t just designed to fool employees. Many are designed to exhaust the analysts investigating them. When a phishing investigation takes 12 hours instead of five minutes, the outcome can shift from a contained incident to a breach.*

For years, the cybersecurity industry has focused on the front door of phishing defense: employee training, email gateways that filter known threats, and reporting programs that encourage users to flag suspicious messages. Far less attention has been paid to what happens after a report is filed, and how attackers exploit the investigation process that follows.

[Alert fatigue in Security Operations Centers isn't just an operational inconvenience](https://arxiv.org/abs/2302.06648). It can become an attack surface. SOC teams increasingly report phishing campaigns that appear designed not only to compromise targets but also to overwhelm the analysts responsible for investigating them.

This shifts how organizations should think about phishing defense. The vulnerability isn't just the employee who clicks. It’s also the analyst who can't keep up with the queue. When investigations that should close in minutes stretch to 3, 6, or 12 hours because of queue congestion, the window for attacker success widens dramatically.

## **When Phishing Volume Becomes a Weapon**

Phishing is often treated as a series of independent threats. One message. One potential victim. One investigation. Attackers operating at scale think in terms of systems, not individual messages. A SOC is one of those systems, and it has finite capacity and predictable failure modes.

Consider a phishing campaign targeting a large enterprise. The attacker sends thousands of messages. Most are low-sophistication lures that email gateways or trained employees will likely catch. These messages flood the SOC with reports and alerts. Analysts begin triaging, working through a queue that grows faster than they can clear it.

Buried in that volume are a few carefully crafted spear-phishing messages targeting individuals with access to critical systems. These messages are the real payload. The flood is not just a numbers game. It is effectively a denial-of-service attack against the SOC's attention, sometimes referred to as an Informational Denial-of-Service (IDoS).

This pattern is not purely theoretical. Red team exercises and incident reports have documented adversaries who time high-volume phishing campaigns to coincide with targeted spear-phishing attempts. The commodity wave creates noise. The targeted message hides inside it.

## **The Predictable Failure Mode**

This tactic works because SOC phishing triage tends to follow a predictable pattern across organizations. When phishing report volume spikes, most SOCs respond in predictable ways. Analysts begin triaging faster, spending less time per submission. Investigation depth decreases. Industry research shows [66% of SOC teams cannot keep up with incoming alerts](https://www.sans.org/white-papers/sans-2024-soc-survey-facing-top-challenges-security-operations). The focus shifts from thorough investigation to clearing the queue. Managers may deprioritize phishing reports relative to alerts from other detection systems, assuming user-submitted reports are lower fidelity.

Each response is rational on its own. Together, they create the conditions an attacker needs.

SOC managers observe a consistent pattern during high-volume periods: decision quality drops as workload increases. Analysts begin anchoring on superficial indicators. Messages that "look like" previously benign submissions receive less scrutiny. Novel indicators of compromise may be overlooked when they appear in a crowded queue rather than in isolation.

The attacker's advantage compounds because the most dangerous messages are specifically designed to exploit these shortcuts. A spear-phishing email targeting the CFO's executive assistant doesn't arrive looking dramatically different from everything else in the queue. It's crafted to resemble the category of messages that analysts, under pressure, have learned to move past quickly — a vendor communication, a document-sharing notification, a routine business process email.

## **The Economics Behind the Attack**

The economics of this dynamic heavily favor the attacker. Generating thousands of commodity phishing emails costs almost nothing, especially with generative AI lowering the production barrier further. But each of those emails, once reported by an employee, costs the defending organization real analyst time and cognitive bandwidth.

This creates an asymmetry that traditional SOC models have no good answer for:

* **Attacker cost per decoy email:** near zero. Template-based generation, commodity infrastructure, automated delivery.
* **Defender cost per reported email:** minutes of skilled analyst time for even a cursory review. Hours if the investigation is thorough.
* **Attacker cost for the real payload:** moderate — these are the carefully researched, individually crafted messages designed for specific targets.
* **Defender cost of missing the payload:** potentially catastrophic — credential compromise, lateral movement, data exfiltration, ransomware deployment.

The defender is forced to investigate everything because the cost of missing a real threat is so high. The attacker knows this and uses it to drain investigative resources before the real attack ar...