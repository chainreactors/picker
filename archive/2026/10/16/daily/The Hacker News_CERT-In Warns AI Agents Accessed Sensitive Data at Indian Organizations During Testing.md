---
title: CERT-In Warns AI Agents Accessed Sensitive Data at Indian Organizations During Testing
url: https://thehackernews.com/2026/10/cert-in-warns-ai-agents-accessed.html
source: The Hacker News
date: 2026-10-16
fetch_date: 2026-10-17T06:39:14.308820
---

# CERT-In Warns AI Agents Accessed Sensitive Data at Indian Organizations During Testing

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

# [CERT-In Warns AI Agents Accessed Sensitive Data at Indian Organizations During Testing](https://thehackernews.com/2026/10/cert-in-warns-ai-agents-accessed.html)

**Swati Khandelwal**Oct 16, 2026Artificial Intelligence / Data Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyMnLMgZNuoh6c41MPT17IsrvbfocknmRb8sxaolFmTpU9h0b-jyJAe9Ods3iCWligbpcd1a1IThvmpUts5llDkKkScffnItGGrGcneDJ8oUJjuc76syHF8g31ZeTWMunD7LDJjviCRFMf8Zugkg8Z4kgXyhDW4bfrCHtV8Xkt-wJlnUd78z-ab28LrfV5/s1700-nu-rw-lo-l85-e365/certin.jpg)

AI agents being tested online reached the live systems of Indian organizations and read business records, including personal data and confidential material, CERT-In [said in an advisory](https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2026-0049&pageid=PUBVLNOTES02) on October 15.

The agents went beyond their assigned tasks, and none of the organizations detected the unauthorized access. After internal reviews, the AI companies whose models were being tested voluntarily reported the cases to CERT-In, India's national cyber agency.

AI agents are software systems that can plan work, run commands, use tools, and act on the internet autonomously for extended periods. In these cases, the agents gained access via credentials and connection settings left exposed in application configuration and public code repositories, and via cloud service roles with excessive permissions.

CERT-In did not name the AI companies, their models, or the organizations and sectors involved. It did not say how many companies reported cases or how many organizations were affected, and said only that the reports came in recently.

It also did not say whether any data the agents read was copied or kept, or whether the affected organizations have been told.

### Attackers Used Open-Source AI Agent Tools in a Separate Campaign

CERT-In's own threat hunting found a second, separate set of incidents: a financially motivated campaign against Indian entities. The attackers misused publicly available offensive-security frameworks built on AI agents.

The frameworks continue to be misused and rebranded, with numerous deployments across infrastructure in several countries. CERT-In did not name the frameworks or the attackers.

In this campaign, the frameworks cut the time from first access to final impact from days to a few hours, according to CERT-In. The attackers ran several agents in parallel for hours to days to reach their goals. Victims that only partly fixed the problems were attacked again within days, at a larger scale.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Google Threat Intelligence Group reported a separate case in September. Attackers who had compromised a cloud resource planned, built and ran an agent-driven campaign that harvested thousands of third-party credentials, [all in under 6 hours](https://thehackernews.com/2026/09/autonomous-ai-agents-compromise.html).

On October 9, CERT-In [warned of attacks](https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2026-0046&pageid=PUBVLNOTES02) on non-banking financial companies, digital lenders, fintech firms, payment providers and wallet operators. The attackers in those cases stole API credentials and called fund-transfer and disbursal APIs directly to move money into mule accounts.

AI-assisted tools may have been used in those attacks. CERT-In has not said whether those attacks are related to the campaign in its October 15 advisory.

### What CERT-In Wants Fixed

The weaknesses behind both kinds of incidents were ordinary, CERT-In said. Credentials and keys were exposed in source code, public repository history, configuration files, client apps and public web pages. Old, unused and test APIs were still reachable from the internet.

Payment API keys were stored in plain text, and cloud and backend-as-a-service roles granted ordinary or anonymous users broad read and write access. Management interfaces were exposed to the internet, and application middleware was left unpatched, with weak credentials or no multi-factor authentication.

In the cases reported by the AI companies, agents found the same exposed credential again and reused it in separate operations.

CERT-In did not publish indicators of compromise for either kind of incident. Organizations should apply the baseline in CERT-In's [May blueprint](https://www.cert-in.org.in/PDF/Blueprint_for_Defending_against_AI_Assisted_Exploitation.pdf) and take these steps:

* Search source code, commit history, CI/CD variables, configuration files, client apps and cloud storage for exposed credentials. Rotate any you find, purge them from history and confirm the fix from outside.
* Scan every commit and build for secrets, and keep credentials out of code, configuration files and databases.
* Keep a full list of your APIs, and shut down old, unused and test APIs and accounts.
* Apply least privilege to cloud and backend-as-a-service roles, keep privileged keys out of client-side code, and test what an anonymous user can read and write.
* Take management interfaces off the internet, require multi-factor authentication for all admin access, and patch exposed middleware quickly.
* Watch APIs with rate-based anomaly detection, alert on enumeration bursts, bulk reads and automated sign-ups, and keep logs for at least 180 days.
* After any credential exposure or confirmed access, treat the environment as compromised until a forensic check clears it. Retest after fixing it, and expect repeat attempts within days to weeks.
* If you run AI agents, give each run its own short-lived, least-privilege identity and block outbound traffic except to the destinations each run needs. Keep a tamper-resistant log of agent actions, at least those that touch production systems and data.

Banks, insurers, other financial firms, and fintech companies should also apply the payment and disbursement API measure...