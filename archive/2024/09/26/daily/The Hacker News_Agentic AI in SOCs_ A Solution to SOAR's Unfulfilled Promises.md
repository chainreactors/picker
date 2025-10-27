---
title: Agentic AI in SOCs: A Solution to SOAR's Unfulfilled Promises
url: https://thehackernews.com/2024/09/agentic-ai-in-socs-solution-to-soars.html
source: The Hacker News
date: 2024-09-26
fetch_date: 2025-10-06T18:30:47.280244
---

# Agentic AI in SOCs: A Solution to SOAR's Unfulfilled Promises

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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Agentic AI in SOCs: A Solution to SOAR's Unfulfilled Promises](https://thehackernews.com/2024/09/agentic-ai-in-socs-solution-to-soars.html)

**Sep 25, 2024**The Hacker NewsArtificial Intelligence / SOC Automation

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqImNErPM4npuulQ1W9ebVK5Hjhl8aQxA4KG9zQ4fUB3L4XVOFxCSTjz4PbPtlhyphenhyphenqlxiucLb59YAU2lhfBcDixsPiEUOUSokfSKhyv8NKhQ_UbrNwwKWlPndvpX7nupX2pttI9ARCrqh00GC7QwJh3K4-LHhvSWirQMKh0NP85jOmpSNGuhhVXNBZPzrY/s790-rw-e365/soc.png)

Security Orchestration, Automation, and Response (SOAR) was introduced with the promise of revolutionizing Security Operations Centers (SOCs) through automation, reducing manual workloads and enhancing efficiency. However, despite three generations of technology and 10 years of advancements, SOAR hasn't fully delivered on its potential, leaving SOCs still grappling with many of the same challenges. Enter Agentic AI—a new approach that could finally fulfill the SOC's long-awaited vision, providing a more dynamic and adaptive solution to automate SOC operations effectively.

## Three Generations of SOAR – Still Falling Short

SOAR emerged in the mid-2010s with companies like PhantomCyber, Demisto, and Swimlane, promising to automate SOC tasks, improve productivity, and shorten response times. Despite these ambitions, SOAR found its greatest success in automating generalized tasks like threat intel propagation, rather than core threat detection, investigation, and response (TDIR) workloads.

The evolution of SOAR can be broken down into three generations:

* **Gen 1 (Mid-2010s):** Early SOAR platforms featured static playbooks, complex implementations (often involving coding), and high maintenance demands. Few organizations adopted them beyond simple use cases, like phishing triage.
* **Gen 2 (2018–2020):** This phase introduced no-code, drag-and-drop editors and extensive playbook libraries, reducing the need for engineering resources and improving adoption.
* **Gen 3 (2022–present)**: The latest generation leverages generative AI (LLMs) to automate playbook creation, further reducing the technical burden.

Despite these advancements, SOAR's core promise of SOC automation remains unfulfilled for reasons we will discuss shortly. Instead each generation has primarily improved operational ease and reduced the engineering burden of SOAR and not addressed the fundamental challenges of [SOC automation](https://radiantsecurity.ai/learn/soc-automation/).

## Why Didn't SOAR Succeed?

When seeking to answer the question "of why SOAR hasn't tackled SOC automation'", it can be helpful to remember that SOC work is made up of a multitude of activities and tasks which are different across every SOC. Generally though, SOC automation tasks involved in alert handing fall into two categories:

* **Thinking tasks** – e.g. figuring out if something is real, determining what happened, understanding scope and impact, creating a plan for response, etc.
* **Doing tasks** – e.g. taking response actions, notifying stakeholders, updating systems of records, etc.

SOAR effectively performs "doing" tasks but struggles with the "thinking" tasks. Here's why:

* **Complexity:** The thinking tasks require deeper understanding, data synthesis, learning patterns, tool familiarity, security expertise, and decision-making. Static playbooks are difficult, if not impossible to create which can replicate these traits.
* **Unpredictable Inputs:** SOAR relies on predictable inputs for consistent outputs. In security, where exceptions are the norm, playbooks become increasingly complex to handle edge cases. This leads to high implementation and maintenance overhead.
* **Customization**: Out-of-the-box playbooks rarely work as intended. They always need customization due to the previous point. This keeps maintenance burdens high.

It is by automating "thinking tasks" that more of the overall SOC workflow can be automated.

## Investigation: The SOC's Weakest Link

The triage and investigation phases of security operations are filled with thinking tasks that occur before response efforts can even begin. These thinking tasks resist automation, forcing reliance on manual, slow, and non-scalable processes. This manual bottleneck is reliant on human analysts and prevents SOC automation from:

* Significantly reducing response times—slow decision-making delays everything.
* Delivering meaningful productivity gains.

To achieve the original SOC automation promise of SOAR—improving SOC speed, scale, and productivity—we must focus on automating the thinking tasks in the triage and investigation phases. Successfully automating investigation would also simplify security engineering, as playbooks could concentrate on corrective actions rather than handling triage. It also provides the possibility for a fully autonomous alert-handling pipeline, which would drastically reduce mean time to respond (MTTR).

The key question is: how do we effectively automate triage and investigation?

## Agentic AI: The Missing Link in SOC Automation

In recent years, large language models (LLMs) and generative AI have transformed various fields, including cybersecurity. AI excels at performing "thinking tasks" in the SOC, such as interpreting alerts, conducting research, synthesizing data from multiple sources, and drawing conclusions. It can also be trained on security knowledge bases like MITRE ATT&CK, investigation techniques, and company behavior patterns, replicating the expertise of human analysts.

### What is Agentic AI?

Recently, there has been tremendous confusion around AI in the SOC, largely due to early marketing claims from the 2010s, well before modern AI techniques like LLMs existed. This was further compounded by the 2023 industry wide mad dash to bolt an LLM-based chatbot onto existing security products.

To clarify, there are at least [3 types of solutions being marketed as "AI for the SOC"](https://radiantsecurity.ai/analytics-vs-co-pilots-vs-agents/). Here's a ...