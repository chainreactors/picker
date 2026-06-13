---
title: Rethinking MDR as Attackers and Defenders Embrace AI
url: https://thehackernews.com/2026/06/rethinking-mdr-as-attackers-and.html
source: The Hacker News
date: 2026-06-12
fetch_date: 2026-06-13T06:12:07.764903
---

# Rethinking MDR as Attackers and Defenders Embrace AI

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

# [Rethinking MDR as Attackers and Defenders Embrace AI](https://thehackernews.com/2026/06/rethinking-mdr-as-attackers-and.html)

**The Hacker News**Jun 12, 2026Endpoint Security / SOC Automation

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2WauAS1qxBj0Oziu-jmgn34YGvKsu9xISK-gtccFv-0WkcX6EC6e-ge9UF2PCZINf9RW5cN40GWijtbnZOvADSJKZ4ErYKX_Iqoo9AO9nk3E0548I07_5PNz6vWA13UMKwU1jGjXCQJLBFyXj_RPEgiVvCuEZZyijeNBxgaiIB1itadpRaDzzoyR_DcA/s1700-e365/mdr.jpg)

For most of the past decade, managed detection and response was the answer to a real problem. Security teams couldn't staff around the clock, couldn't hire enough analysts, and needed someone else to handle the alert queue. MDR stepped in. It worked well enough. Until now.

The threat landscape has changed faster than the MDR model can adapt. Attackers are using AI to move faster, generate more convincing phishing at scale, automate reconnaissance, and create malware variants that evade signature-based detection. The attack surface has expanded from endpoint to cloud, identity, and network simultaneously. And yet MDR is still doing what it always did. Routing alerts to human analysts who triage what they can, in the order they can get to it.

That is no longer enough. The data we share below proves it and [security leaders might consider exploring whether they have outgrown their MDR](https://intezer.com/mdr-renewal-checklist-2026/?utm_source=thehackernews&utm_medium=referral).

## MDR's 24/7 promise doesn't cover 60% of your alerts

MDR promised 24/7 human coverage. What it delivered was a 24/7 human capacity to triage high-severity alerts. Those are not the same thing.

Across the industry, approximately 60% of alerts go unreviewed. That's not a performance failure. Human teams, whether in-house or outsourced to an MDR, cannot process the volume of alerts that modern environments generate. So they do what any rational person does. They prioritize. P1s and P2s get worked. P3s and P4s pile up.

But this is exactly where attackers hide.

[Analysis of 25 million alerts across global enterprises in 2025](https://intezer.com/2026-ai-soc-report-for-cisos/?utm_source=thehackernews&utm_medium=referral) found that nearly 1% of real threats originate in low-severity and informational alerts. In an enterprise generating 450,000 alerts annually, that translates to roughly 54 real incidents per year, about one per week, sitting in the deprioritized queue where no one is looking.

The breaches hiding in that backlog are not theoretical. They are happening right now, in organizations that believe they have coverage.

**Note:** The math behind the above statement assumes 450K annual alerts, of which 60% are not investigated and of those, 2% are real incidents. Of those real incidents, 1% originate in low-severity alerts.

## Investigation quality varies by who is on shift

Even for alerts that do get reviewed, MDR investigation quality is not consistent. It is bounded by the experience of the analyst on duty, the queue depth at that moment, the time of day, and whether the team is fully staffed. A P1 at 3 am gets a different investigation than the same alert at 10 am.

This is not a criticism of MDR analysts. It is a description of what happens when any human-executed process runs at high volume, under pressure, around the clock. Variance is unavoidable.

The consequences are real. When an investigation is shallow, threats get classified as noise. When follow-through is inconsistent, early-stage lateral movement looks like routine behavior. The attacker who got in on a low-severity alert keeps moving undetected because no one had the time or context to connect the signals.

## Detection engineering is not a closed loop

In most MDR deployments, detection engineering is a periodic exercise. Rules get tuned when customers complain about alert volume. New coverage gets added when a major CVE makes news. Otherwise, the detection posture drifts.

The core problem is architectural. MDR investigation and detection engineering operate in separate silos. When an analyst investigates an alert and closes it as a false positive, that insight rarely feeds back into the detection system. Broken rules stay broken. Noisy rules keep generating noise. New attacker techniques arrive without matching detections.

The result is a detection posture that degrades faster than it improves. Real coverage, measured against the MITRE ATT&CK framework, can be far lower than teams assume.

## You can't audit what you can't see

Most MDR services are a black box. Customers receive escalations and summaries. They do not get to see the investigation logic, inspect the evidence trail, verify the verdict, or audit what the analyst actually reviewed before closing a case.

In an era where accountability and transparency are security requirements, this is a genuine liability. When an incident is missed, you cannot diagnose why. When a verdict is wrong, you cannot trace the reasoning. When regulators ask what was investigated and how, there is no answer.

## The AI savings are going to the vendor, not to you

AI is reducing the operational cost of MDR. Providers are using it to automate portions of triage, reduce analyst hours, and increase margins. Those efficiency gains do not flow through to customers as lower prices or expanded coverage. The buyer still pays the same rate, or more. The provider keeps the savings.

But the coverage gap stays the same. The human scaling constraint stays the same. Only the provider's cost structure has improved.

## You don't own what was built in your name

Detection rules, triage logic, case history, and investigation learnings accumulate inside the MDR vendor's platform over the life of the contract. When the contract ends, that knowledge does not move with you. The years of tuning, the accumulated context about your environment, and the detection improvements built from your data all stay with the vendor.

This creates two prob...