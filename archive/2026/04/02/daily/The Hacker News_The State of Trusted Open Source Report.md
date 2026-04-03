---
title: The State of Trusted Open Source Report
url: https://thehackernews.com/2026/04/the-state-of-trusted-open-source-report.html
source: The Hacker News
date: 2026-04-02
fetch_date: 2026-04-03T04:29:26.961258
---

# The State of Trusted Open Source Report

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [The State of Trusted Open Source Report](https://thehackernews.com/2026/04/the-state-of-trusted-open-source-report.html)

**The Hacker News**Apr 02, 2026DevSecOps / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5yI578d17vaAxuCMW2SLrz3ibI4ibSfdDCfum-B3VZ0Ukyd79Eue2VR8ofUCBpISSXsL8biYdRFyuMm78T6PTU7U1w_6jJK3qV7ohPRSt3NGDTtAkseitLCaEZVHqcVIhFZABPlyAP8KPV-JMlnlq42Flgl7lB2Rs5hkIQYVYtc0Z15Yd0WKaYSu7CLM/s1700-e365/devsecops.jpg)

In [December 2025](https://www.chainguard.dev/unchained/the-state-of-trusted-open-source-december-2025), we shared the first-ever *The State of Trusted Open Source* report, featuring insights from our product data and customer base on open source consumption across our catalog of container image projects, versions, images, language libraries, and builds. These insights shed light on what teams pull, deploy, and maintain day to day, alongside the vulnerabilities and remediation realities these projects face.

Fast forward a few months, and software development is accelerating at a pace that most didn’t see coming. AI is increasingly embedded across the development lifecycle, from code generation to infrastructure automation, as models become more advanced and better at meeting the demands of modern work. This shift is expanding what teams can build and how quickly they can ship.

It is also reshaping the security landscape.

Before diving into the numbers, it’s important to explain how we perform this analysis. We examined over 2,200 unique container image projects, 33,931 total vulnerability instances, and 377 unique CVEs from December 1, 2026, through February 28, 2026. When we use terms like “top 20 projects” and “long tail projects” (as defined by images outside of the top 20), we’re referring to real usage patterns observed across our customer portfolio and in production pulls.

In this report, we noticed a few new themes that point to this shift. These themes built on the trends from our last report, ultimately showcasing the impact of increased AI-driven development both in the types of container images being used and in the number of CVEs being discovered and remediated:

* **Python and PostgreSQL growth reflects AI-driven development:** Python remains the most popular image (72.1% of all customers use it), and PostgreSQL saw a 73% increase in usage quarter-over-quarter, underscoring the growing adoption of a modern AI stack across various use cases.
* **The modern platform stack is becoming increasingly standardized:** Across Chainguard customers, language ecosystem images account for more than half of the top 25 images used in production.
* **Chainguard Base is becoming a foundation for developer tooling:** The [chainguard-base](https://images.chainguard.dev/directory/image/chainguard-base/versions) image, a minimal distroless base image without any toolchain or apps, was the 5th most-used Chainguard image, as customers use it as a sort of “utility belt” for their specific use cases (over 75% of Chainguard customers customize at least one image).
* **AI is accelerating software development and vulnerability discovery:** We applied over 300% more fixes in Chainguard Containers and saw a 145% increase in vulnerabilities from last quarter, signaling the use of AI to push more code and discover more CVEs.
* **The long tail continues to define real-world risk:** 96% of the vulnerabilities found and remediated in Chainguard Containers occurred outside of the top 20 most popular projects—this is consistent with the findings from December.
* **Compliance continues to drive adoption of trusted open source:** We saw the same themes from December present here, underscored by a FIPS-compliant variant of a Chainguard container image entering the top 10 images by customer count for the first time.

## **Usage: What teams actually run in production**

We identified multiple themes centered on the prevalence of AI in code generation across regions and industries. This prevalence leads to greater adoption of the Python language ecosystem and adjacent technologies on the usage side.

### **Most popular images: Python and PostgreSQL growth reflect AI-driven development**

#### **PostgreSQL usage grew 73% quarter-over-quarter**

The images that saw the strongest growth this quarter closely align with the technologies driving AI adoption.

Python remains the most widely deployed image across Chainguard customers. When combining FIPS ([Federal Information Processing Standards](https://edu.chainguard.dev/chainguard/fips/understanding-fips/)) and non-FIPS variants, **72.1% of Chainguard customers are using a Python image**. This reflects Python’s role as the default language for machine learning, data pipelines, and automation. What was once concentrated in experimentation environments is now moving into production systems across industries.

Node continues to anchor application infrastructure, with 60.7% of Chainguard customers utilizing it in their environments. Together, Python and Node define the dominant runtime layer for modern applications.

The most notable change this quarter is in databases. **PostgreSQL usage grew by 73% quarter over quarter**, the largest increase among widely deployed images.

This growth aligns with broader trends in AI workloads. PostgreSQL is increasingly used as a foundation for vector search and retrieval-augmented generation, supported by extensions that enable embedding storage and similarity queries. As AI moves into production, databases are evolving alongside application runtimes.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQWHxcADfyKi2OPBU33MK0457o25ZDZSQcXMvZMo2I3lW061xKuUCSnm9flWkxIC8x3JIAG8YBEbCWgHBycZXKdyMFPgAyygbakMmIyWyjsSS_aIuOUiKXZilhFVg76YR8lU0BsABITkYua7G6wau2I4Vt-qgpYZU6BojKqUTsZo4XfuVejsg7tc7UV0M/s1700-e365/1.png)

### **The modern platform stack is converging**

#### **Over 50% of the most popular i...