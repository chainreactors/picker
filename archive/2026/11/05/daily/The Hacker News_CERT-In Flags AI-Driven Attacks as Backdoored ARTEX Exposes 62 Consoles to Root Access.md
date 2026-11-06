---
title: CERT-In Flags AI-Driven Attacks as Backdoored ARTEX Exposes 62 Consoles to Root Access
url: https://thehackernews.com/2026/11/backdoored-docker-image-for-artex-ai.html
source: The Hacker News
date: 2026-11-05
fetch_date: 2026-11-06T08:41:48.203571
---

# CERT-In Flags AI-Driven Attacks as Backdoored ARTEX Exposes 62 Consoles to Root Access

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

# [CERT-In Flags AI-Driven Attacks as Backdoored ARTEX Exposes 62 Consoles to Root Access](https://thehackernews.com/2026/11/backdoored-docker-image-for-artex-ai.html)

**Ravie Lakshmanan**Nov 05, 2026Cyber Attack / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiA5xlxteigxw9PDEVogRmGjD3vyPuJRyKCuIAOmURy0CY-OLXfYOjC93BPb_gvifLUiVoUk9JcjmxtsGpkT-cYhlrTwXS6yodTv-WwHnPUKvahU67tc5R841Sb_hkIIsUkzNzne5Fzo0h6BUpzEW1770YFBayYksyjSc9pKOV3VsHfoHcPfu3mYAFOQW4K/s1700-nu-rw-lo-l85-e365/docker-ai.jpg)

The Indian Computer Emergency Response Team (CERT-In) has disclosed that an artificial intelligence (AI)-assisted threat actor it tracks as **Crafty Falcon** is targeting organizations in the Banking, Financial Services, and Insurance (BFSI) sectors in the country.

Describing the threat as active and ongoing, the activity involves the use of [publicly-available AI-driven offensive security tools](https://thehackernews.com/2026/11/chainstack-reports-production-systems.html) like [ARTEX, PentAGI, Cairn, and CyberStrikeAI](https://thehackernews.com/2026/11/government-linux-servers-targeted-with.html).

"These tools execute complete attack chains autonomously at machine speed, generate and refine large numbers of tailored attack scripts in rapid succession, and adapt their payloads based on target responses," CERT-In [said](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBVLNOTES02&VLCODE=CIAD-2026-0058). "The supporting attack infrastructure rotates IP addresses within hours to days."

The agency said the attacks have also targeted cryptocurrency exchanges and digital asset service providers, resulting in the theft of keys and funds.

The update follows an [October 2026 alert](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBVLNOTES02&VLCODE=CIAD-2026-0046) issued by CERT-In, which warned of multiple cyber attack campaigns targeting non-banking financial companies (NBFCs), digital lending platforms, fintech entities, payment service providers, and cryptocurrency wallet operators.

Threat actors have been observed exploiting internet-facing applications and exposed APIs and privileged endpoints to steal payment aggregator/gateway and partner-bank API credentials, and then invoke fund-transfer APIs directly from within the entities' own allow-listed infrastructure.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Some of the other notable initial access vectors are listed below -

* Use of stolen long-lived static, hard-coded API tokens
* Supply chain compromise of source code repositories via forged commits
* Exploitation of plaintext credentials in configuration files, source code, or databases
* Access to applications and remote services lacking multi-factor authentication (MFA)

This approach, CERT-In added, defeats application-level controls such as loan creation, KYC, sanction, beneficiary verification, balance sufficiency, and per-transaction limits.

The rapidly executed fraudulent transactions are designed to move funds to attacker-controlled mule accounts across multiple banks. In addition, the attacks involve the operators taking steps to delete logs and tamper with endpoint security tools in an attempt to complicate detection and incident response efforts.

CERT-In also warned that attackers are targeting cloud infrastructure to execute commands and deploy malicious payloads, as well as publicly-accessible non-production environments to obtain shared credentials, tokens, or network paths, and then use them to pivot to production systems.

Other notable post-exploitation actions undertaken by the adversary are as follows -

* Reverse-engineering application codebases to develop tailored exploits
* Initiating unauthorized API calls using modified application packages, undermining controls that "assumed only the legitimate client application would call the APIs"
* Executing micro-value test transactions (such as Rs. 1) to validate unauthorized fund flows before executing large-value transfers
* Abusing merchant settlement APIs of payment aggregators to move funds
* Exploiting newly disclosed vulnerabilities, including file-upload and deserialization exploit chains leading to web shells in PHP and Node.js applications
* Creating a large number of custom scripts on the fly and iteratively improving them in quick succession, a pattern consistent with AI-assisted development

The development comes as CERT-In has published the Artificial Intelligence Security Auditing Guidelines, laying out specific requirements to ensure the "governance, security, privacy, fairness, transparency, resilience and auditability of AI systems."

The framework calls for testing an AI agent's documented identities, authorized objectives, approved tool use, permission boundaries, and its adherence to the principle of least privilege (PoLP). It also requires AI agents to require human approval for consequential actions, while ensuring high-risk AI systems incorporate emergency interruption, credential revocation, and controls for preventing automatic restarts.

"Effective assurance requires organisational accountability, technical testing, data and model governance, continuous monitoring, human oversight, incident response and third-party assurance," the agency [said](https://www.cert-in.org.in/s2cMainServlet?pageid=GUIDLNVIEW02&refcode=CISG-2026-04). "Accordingly, the framework provides auditable requirements proportionate to the nature, scale, autonomy and potential impact of each AI system."

### Copycat ARTEX Version Hands Out Root Shell

The abuse of open-source penetration testing tools like ARTEX in real-world intrusions prompted its developer to take down the repository from GitHub. But multiple copies have sprung up on the Microsoft-owned code-hosting platform to fill the void -

* github[.]com/trhhubsd/ARTEXX
* github[.]com/mhtsec/ARTEX ("[mianhuatang11/artex](https://hub.docker.com/r/mianhuatang11/artex)" on...