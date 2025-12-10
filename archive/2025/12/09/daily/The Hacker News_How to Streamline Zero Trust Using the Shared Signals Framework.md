---
title: How to Streamline Zero Trust Using the Shared Signals Framework
url: https://thehackernews.com/2025/12/how-to-streamline-zero-trust-using.html
source: The Hacker News
date: 2025-12-09
fetch_date: 2025-12-10T03:23:02.614661
---

# How to Streamline Zero Trust Using the Shared Signals Framework

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [How to Streamline Zero Trust Using the Shared Signals Framework](https://thehackernews.com/2025/12/how-to-streamline-zero-trust-using.html)

**Dec 09, 2025**The Hacker NewsZero Trust / Security Automation

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiH2Vp1tGLWh8MZqrb8A89wnY6EiB7tOnSURBp8iBE-pmJOwkrBSOUU1ixEDZjfWbEEv3Vp5KjxLS6qKJHLRJ2R2diF4aAC43LxRwN4nTlnJIXGGhA0V4O9ny-KSUh3__yMn1rA01CjTAKQqaQFQPvSBgTcfL0t0xN6N_3v_wlo1pwJaVm5Qz_TTn4dAeM/s790-rw-e365/tines.jpg)

Zero Trust helps organizations shrink their attack surface and respond to threats faster, but many still struggle to implement it because their security tools don't share signals reliably. 88% of organizations admit they've suffered significant challenges in trying to implement such approaches, according to [Accenture](https://www.accenture.com/content/dam/accenture/final/accenture-com/document-3/State-of-Cybersecurity-report.pdf)**.** When products can't communicate, real-time access decisions break down.

The Shared Signals Framework (SSF) aims to fix this with a standardized way to exchange security events. Yet adoption is uneven. For example, Kolide Device Trust doesn't currently support SSF.

Scott Bean, Senior IAM and Security Engineer at MongoDB, proposed a way to solve the problem, giving teams an easy and intuitive way to operationalize SSF across their environment.

In this guide, we'll share an overview of the [workflow](https://www.tines.com/library/stories/1329793/?name=integrate-kolide-device-trust-with-okta-using-the-shared-signals-framework?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=organicarticle-Dec9), plus step-by-step instructions for getting it up and running.

## The problem – IAM tools don't support SSF

A core requirement of Zero Trust is continuous, reliable signals about user and device posture. But many tools don't support SSF for Continuous Access Evaluation Protocol (CAEP), making it hard to share or act on these signals.

Teams often face three challenges:

* Tools lack native SSF support
* Signals require enrichment or correlation
* Managing SSF endpoints and token handling adds overhead

Without this interoperability, organizations struggle to apply consistent policies — and in cases like Kolide Device Trust, critical device events never reach systems like Okta.

## The solution – a SSF transmitter that turns Kolide issues into CAEP events

Because SSF is built on HTTPS requests, the OpenID standard works with Tines' HTTP Action.

Scott developed a new [workflow](https://www.tines.com/library/stories/1329793/?name=integrate-kolide-device-trust-with-okta-using-the-shared-signals-framework?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=organicarticle-Dec9) [integrating Kolide Device Trust with Tines](https://www.tines.com/library/stories/1329793/?name=integrate-kolide-device-trust-with-okta-using-the-shared-signals-framework?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=organicarticle-Dec9), enabling it to send SSF signals to Okta. If a device is non-compliant, Kolide sends a message to the workflow via webhook. Tines enriches the signal, makes sure it can be linked to a user, builds a Security Event Token (SET), and then sends it to Okta.

In this way, Tines acts as the connective tissue that makes SSF work across the distributed IT environment, even if individual tools don't natively support the standard.

Tines can:

* **Receive signals from Kolide (and tools like it)** via webhook when a device becomes non-compliant
* **Enrich and correlate those signals** (e.g., map device to user)
* **Generate and sign SETs** that meet the SSF specification
* **Deliver them to Okta (and other identity providers)** to enforce Zero Trust
* **Host required SSF metadata endpoints** using API path prefixes, giving consuming systems a standards-compliant place to fetch keys and decrypt tokens

All of which makes Zero Trust enforcement faster, more reliable, and much easier to operationalize. IT teams are empowered with continuous, real-time risk assessment of devices, faster response to threats, and more flexible policy orchestration. And end users get the benefit of automated remediation, which helps to optimize productivity and minimize IT intervention.

If you want to go deeper into identity modernization, the [Tines IAM guide](https://www.tines.com/access/guide/unlocking-it-agility-with-automation-and-orchestration-iam/?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=organicarticle-Dec9) explores how teams are unifying device trust, access decisions, and least-privilege enforcement with automation. Scott's workflow is one of several real-world patterns inside.

## Workflow overview

### **Required tools:**

* **Tines** – workflow orchestration and AI platform
* **Kolide** – device trust and posture monitoring
* **Okta** – identity platform receiving CAEP events

### **Required credentials:**

* Tines API Key - `Team` Scoped with the `Editor` role
* Kolide API Key - Read Only
* Kolide Webhook Signing Secret

### **Required resources:**

Okta domain, such as example.okta.com, example.oktapreview.com, or a branded domain.

**How it works:**

The workflow creates a proof-of-concept SSF transmitter that can be registered with Okta and sends device compliance change CAEP events (sent as SETs), based on issues generated in Kolide. There are three elements:

**1. Generate and store SET signing keys** (SETs are signed JSON Web Tokens):

* Creates an RSA key pair and converts it to JWK format.
* Publishes the public key for SSF receivers to validate SET signatures.
* Stores the private JWK keyset as a Tines secret.

**2. Expose SSF transmitter API**

SSF receivers (like Okta) need:

* a .well-known/sse-configuration endpoint describing the transmitter
* a JWK endpoint exposing the public key used to verify SET signatures
* a webhook trigger acts as the SSF API surface
* logic returns the .well-known config
* logic returns the JWKs

Once this is live, teams can register a new SSF receiv...