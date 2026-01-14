---
title: Security Research in the Age of AI Tools
url: https://www.invicti.com/blog/security-labs/security-research-in-the-age-of-ai-tools
source: Over Security - Cybersecurity news aggregator
date: 2026-01-13
fetch_date: 2026-01-14T03:35:47.282417
---

# Security Research in the Age of AI Tools

[ð Invicti Acquires Kondukto to Deliver Proof-Based Application Security Posture Management](/blog/news/invicti-acquires-kondukto-to-deliver-proof-based-aspm/)

[![](https://cdn.prod.website-files.com/689c8d2a82b96fe8bd736742/68a2f15db90e180494af51bb_ae9813f1f5756cad30abfcb3e8016c9e_Logo-wide.svg)

100% Signal 0% Noise](/)

Platform

[Platform Overview](/platform-overview)[ASPM](/product/application-security-posture-management-aspm)[APIÂ Security](/product/api-security)[DAST](/product/dast)[SAST](/product/sast)[SCA](/product/sca)[Container Security](/product/container-security)[AI-Powered AppSec](/product/ai-powered-application-security)[Cost Savings Calculator](/product/aspm-cost-savings-calculator)[Features](/features)

Solutions

[Manage Vulnerabilities](/solutions/manage-vulnerabilities)[Automate Security Workflows](/solutions/automate-security-workflows)[Track AppSec KPIs](/solutions/track-appsec-kpis)[Manage Open Source Risk](/solutions/manage-open-source-risk)

[Pricing](/pricing)

Why Invicti

[About Us](/about)[Case Studies](/case-studies)[Contact Us](/contact)[Careers](/careers)

Resources

[Resource Library](/resources)[Blog](/blog)[Webinars](/webinars)[White Papers](/white-papers)[Podcasts](/podcasts)[Invicti Learn](/learn)[Live Training](/live-trainings)[Partners](/partners)[Documentation](https://www.invicti.com/support/)

[Get a demo](/get-demo)

[Resources](/resources)

[AppSec Blog](/blog/web-security)[Security Research](/blog/security-labs)[News](/blog/news)[Product Docs & FAQs](/blog/docs-and-faqs)

Security research

## Security research in the age of AI tools: Django and Node.js SQL injection analysis

[Bogdan Calin](/blog/author/bogdan-calin)

,

Â -Â

December 3, 2025

![](https://cdn.prod.website-files.com/689c8d2a82b96fe8bd736742/68c284181123640664e6770f_Social%20logos.svg)

![](https://cdn.prod.website-files.com/689c8d2a82b96fe8bd736742/68c28425dec9220a321e796e_Social%20logos.svg)

In this article, I try to show how my work as a security researcher has changed and how the new AI tools have impacted my workflow, productivity, and overall approach to security research. I present two SQL injection vulnerabilities discovered by other researchers, show how I investigated them to create security checks for our Invicti DAST product, and describe how AI tools helped me in the process.

You information will be kept Private

![](https://cdn.prod.website-files.com/68a4552adf4a460ade53ca38/69398564f1f3afbdefe32f59_693041a2ab4c896b780a51bf_Header6.png)

Table of Contents

## Vulnerability 1: Critical SQL Injection Vulnerability in Django (CVE-2025-64459)

The first vulnerability was published by Endor Labs (by Meenakshi S L) in their blog post [Critical SQL Injection Vulnerability in Django (CVE-2025-64459)](https://www.endorlabs.com/learn/critical-sql-injection-vulnerability-in-django-cve-2025-64459). This vulnerability is particularly interesting because it affects a widely used web framework, Django.

### Step 1: Get a broad idea of the vulnerability

Since Google released the image model [Nano Banana Pro](https://blog.google/technology/ai/nano-banana-pro/), Iâve learned that it can also be used to summarize text and create infographics that make understanding complex topics faster/easier. So, I used Nano Banana Pro to generate an infographic summarizing the vulnerability from the blog post text.

I used the following prompt:

It generated the following infographic:

![](https://cdn.prod.website-files.com/68a4552adf4a460ade53ca38/69398563f1f3afbdefe32ece_69304727626d19d736ffbbcf_75735919.png)

Itâs a great way to get a quick overview of the vulnerability and its impact. However, I still needed to understand the technical details, so of course I read the full blog post as well, but the infographic helped me to get a broad idea quickly and to understand the key points.

The main issue is that a very common dynamic filtering pattern in Django using user-controlled query parameters can lead to SQL injection. So, if you have code like this:

an attacker can exploit it using a query string like:

Django converts it into the following unsafe SQL query because of the `internal _connector` parameter:

### Step 2: Reproduce the vulnerability with Claude Code

This step is where I was spending most of my time before I had all the AI tools. I had to set up a Django environment, create a vulnerable application, and then try to exploit it manually. All these steps took a lot of time, especially if I didnât have prior experience with a specific application like Django.

Nowadays, I just use [Claude Code](https://www.claude.com/product/claude-code) to help me with this. In this case, I created an empty folder and asked Claude Code to generate a vulnerable Django application that demonstrates the vulnerability. I used the following prompt:

A few minutes later, I had a complete Django application with the vulnerable code and instructions on how to run it. I then asked Claude Code to generate a docker container for the application so I can run it easily without worrying about dependencies.

In the end, it generated a Dockerfile and a `docker-compose.yml` file for me. I just had to run `docker-compose up` and the vulnerable application was up and running.

It also generated API documentation for the vulnerable endpoints so I can test them easily:

![](https://cdn.prod.website-files.com/68a4552adf4a460ade53ca38/69398563f1f3afbdefe32ed1_69304727626d19d736ffbbd5_df27ae31.png)

### Step 3: Brainstorming the security check implementation with Claude Code

Now that I had a vulnerable application to test against, the next step was to figure out how to implement a security check for this vulnerability in our Invicti DAST product. The problem was that I needed to find a way to detect this vulnerability generically in Django applications. In the examples above, you need to know about the `is_superuser` field from the `User` model. I wanted to find a way to detect this vulnerability without prior knowledge of the models used in the application.

I asked Claude to help me brainstorm ideas for implementing the security check in a generic way. This is very helpful because Iâm not an expert in Django whereas Claude has a lot of knowledge about Django internals and best practices. I used the following prompt:

Claude Code suggested a few different approaches, and it even generated an HTML report with all the ideas and how they are supposed to work:

![](https://cdn.prod.website-files.com/68a4552adf4a460ade53ca38/69398563f1f3afbdefe32ed8_69304727626d19d736ffbbd2_3d97dac7.png)

Of course, not all ideas you get from an LLM are always good and you should expect some hallucinations, but it gave me a good starting point to implement the security check. In the end, I used the `id__gte=0` approach that results in a query string like `?username=nonexistent&_connector=OR&id__gte=0`. The resulting query is always true because `id` is always greater than or equal to 0.

### Step 4: Implementing the security check with Claude Code

I also use Claude Code in the last step of the process: implementing the security check. Iâve provided Claude Code with a detailed [CLAUDE.md file](https://www.anthropic.com/engineering/claude-code-best-practices) (a special file that Claude automatically pulls into context when starting a conversation) about how our Invicti security checks work. This helps me to implement security checks much faster and also to write unit tests for them.

As you can see, I used some type of AI model in every step of the process, from understanding the vulnerability to brainstorming ideas to implementing the security check itself.

## Vulnerability 2: Prepared Statements? Prepared to Be Vulnerable

The second vulnerability was published by Mantra Infosec (by Balazs Bucsay) in their blog post [Prepared Statements? Prepared to Be Vulnerable](https://blog.mantrainfosec.com/blog/18/prepared-statements-prepared-to-be-vulnerable). This vulnerability highlights t...