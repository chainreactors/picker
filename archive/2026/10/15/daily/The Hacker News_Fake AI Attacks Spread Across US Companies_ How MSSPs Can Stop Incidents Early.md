---
title: Fake AI Attacks Spread Across US Companies: How MSSPs Can Stop Incidents Early
url: https://thehackernews.com/2026/10/fake-ai-attacks-spread-across-us.html
source: The Hacker News
date: 2026-10-15
fetch_date: 2026-10-16T06:37:55.454306
---

# Fake AI Attacks Spread Across US Companies: How MSSPs Can Stop Incidents Early

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

# [Fake AI Attacks Spread Across US Companies: How MSSPs Can Stop Incidents Early](https://thehackernews.com/2026/10/fake-ai-attacks-spread-across-us.html)

**The Hacker News**Oct 15, 2026Malware / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvF5TcwT7nwh6xcCiXS3I0m6qmvF6EorwitA-7ETGlXzpc89JG-rPZye0FkJfFwunfKHXMTkGyg_pBRkBdJv_qaGX32cUdiqoTAA-sjGmsSlKJsL5LUFpyZLiho955h3EtKUCWvtnHyIJgzG1INTIwkqKsCmv3-vsxGXQq8QH-ue0Vl358XyE33wUhxWs/s1700-nu-rw-lo-l85-e365/fake.jpg)

Attackers are impersonating popular AI products to distribute malware, steal browser sessions, and compromise business accounts. ANY.RUN linked **1,258 public sandbox analyses** to fake AI campaigns between April and October of 2026.

The campaigns also increase operational pressure on MSSPs serving US businesses, which accounted for 16% of country-attributed targets.

Similar attacks appearing across different customers can trigger repetitive investigations, consume analyst capacity, and extend response times, making it harder to maintain consistent service levels as threat activity grows.

## How Fake AI Attacks Are Reaching US Businesses

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzEHgHWcaoruZRgAwtNumN4KkBuhCx0AKXIWRptsD1U-a1ConyOQ4oO6A2o9gcscuj6ToEL9MFwSYQc7meDwe2PkX01CsFHMJfAK_xDvIcKHx-71_k59HzbL_TFzVEtAxXByoW3fbyNHf2gQXilh70fxc8aEIKIRSisEIRITbuxCw850iklgLeJGZvqUs/s1700-nu-rw-lo-l85-e365/1.png) |
| Fake AI attacks pose a serious risk to business security |

The campaigns investigated by ANY.RUN use familiar AI brands to encourage employees to execute malicious commands, install compromised applications, or submit credentials through fraudulent authentication pages.

Attackers impersonate Claude, ChatGPT, GitHub Copilot, Gemini, and other AI services. Their lures appear in sponsored search results, legitimate hosting services, shared AI conversations, and counterfeit download websites.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_67e4f3fKFeEQ_3lsNf5yYeAfbKIi_FyuUqESot0S4E6C7RW7H1_winZwvz-GEH4L2vHmB0m6V6oLx98ZZIrynJ5FGbYnOFFXEWKkbX9lR0m71p_W5wDaq2lPtK7mLKMsWNe_IOQtrQmAUXuM_r-QAfbTjdxjUZm7IYdyXiUR_AjGFUabZhSqU0XDAeU/s1700-nu-rw-lo-l85-e365/2.jpg) |
| Fake Copilot installation page |

One campaign impersonating Claude demonstrates how easily a routine software installation can become an infection.

In the attack analyzed through ANY.RUN's Interactive Sandbox, the victim encounters a page resembling the official Claude download website. Clicking the Windows download button copies a command to the clipboard and displays instructions for executing it through PowerShell.

Instead of installing the expected application, the command launches mshta.exe, retrieves a malicious HTA file, and triggers an encoded PowerShell execution chain.

> [Completed analyses exposed infostealer activity](https://app.any.run/tasks/bbfbbb49-9676-47a6-8f62-234c70fa46c3/?utm_source=thehackernews&utm_medium=article&utm_campaign=fake_ai&utm_content=task&utm_term=151026)

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPmyQ59loXsQ4gNpQOrPmh_86CpP9v6lwjCAabpVeL6BH7PzVvFLgsfgjflg2y0uyTNOuvwaPsqJ-4PFZ6yzoW94V8LirYKI6rwKEo0fft5cj9IO9d6x-jD8hqXx_9Ef2E6mP9GgOcU9H2b_skVC570PCy0xfSfZtTXKZSJEvUhW_jiMhLhCNe5MWpT6o/s1700-nu-rw-lo-l85-e365/3.png) |
| ANY.RUN’s Sandbox revealed the entire infection chain |

The technique presents a difficult detection scenario. The employee initiates the process voluntarily, the attack relies on legitimate Windows utilities, and the malicious payload appears only after several execution stages.

For MSSPs managing multiple customer environments, this creates a recurring operational challenge: the initial indicators vary, while the underlying attacker behavior remains similar.

> **[Cut 21 minutes from mean time to respond and improve SOC efficiency across your customer base. Discover how ANY.RUN strengthens MSSP detection and response workflows.](https://any.run/mssp/?utm_source=thehackernews&utm_medium=article&utm_campaign=fake_ai&utm_content=mssp&utm_term=151026#contact-sales)**

## Why Fake AI Campaigns Put Pressure on MSSP Operations

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpvtDJ6Qlk9ucUZJbLKNXLKRScADtbFLqFb9gsZXMKrd1TWmzFEC4bCLN_6WCFrVAc_VKJBppRKOE89qvq2fuWUrvdxCnEg94_t8lJAoHn939yhN1N6JOYlKuAIc7jps2Nye63m08Gr2mFgJEOqoghoFEZahckDAjEAsqmWaALMdc1hHMZSdzu-vkc_ik/s1700-nu-rw-lo-l85-e365/4.png) |
| ANY.RUN data shows that 16% of Fake AI attacks were directed at the US |

An individual fake AI incident may appear straightforward once its full execution chain is visible. The operational difficulty increases when an MSSP must recognize similar activity across customers with different technologies, policies, and risk profiles.

These campaigns create pressure on three interconnected SOC processes.

* **Monitoring and detection coverage:** Attackers constantly rotate domains, hosting services, and AI brands, making new campaign variants harder to detect with existing indicators.
* **Triage and escalation management:** Evasive attack chains require deeper investigation, increasing analyst workload, response times, and unnecessary escalations.
* **Threat hunting and detection improvement:** Findings from individual investigations need to be correlated and reused to strengthen detection across customer environments.

These challenges directly affect the metrics MSSP leadership manages: MTTD, MTTR, escalation rates, investigation cost, and SLA compliance.

Improving those metrics requires a coordinated approach to monitoring, investigation, and intelligence reuse.

## Improving Tier 1 Efficiency Through Behavioral Investigation

The first opportunity is to reduce the time analysts spend establishing wh...