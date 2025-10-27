---
title: Behind The Scenes: Yarix Approach to Mobile Security
url: https://labs.yarix.com/2024/11/visual-composer-5397/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-06
fetch_date: 2025-10-06T19:40:54.312068
---

# Behind The Scenes: Yarix Approach to Mobile Security

[![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)![YLabs](//labs.yarix.com/wp-content/uploads/2021/01/yarix_logo.png)![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)](https://labs.yarix.com/ "YLabs - Research & Development")

* [Home](https://labs.yarix.com/)
* [Blog](https://labs.yarix.com/category/blog/)
* [Advisories](https://labs.yarix.com/advisories/)
* [Careers](https://www.yarix.com/job-opportunity/)

# Behind The Scenes: Yarix Approach to Mobile Security

* [Home](https://labs.yarix.com "Go to Home Page")
* Behind The Scenes: Yarix Approach to Mobile Security

[Back to Posts](https://labs.yarix.com)

![](https://labs.yarix.com/wp-content/uploads/2024/11/background-1140x445.jpg)

05Dec05/12/2024

## Behind The Scenes: Yarix Approach to Mobile Security

[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")2024-12-06T13:24:12+01:00

By
[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")

Reading Time:   13 minutes

---

**TLDR**: This article highlights the Yarix Red Team’s daily challenges and internal work done to improve the quality of our outcomes. We will explore the topic by taking the Mobile Security field as a case: we will start with the common reporting problems every red team faces day after day, as well as those arising from the gaps in the industry standards (e.g. OWASP, MITRE, etc.), to finish with what lies behind our Mobile Security assessment outcomes. Although the start and the end may sound totally unrelated, they are interconnected through the new version of the OWASP Mobile Application Security project.

---

## Introduction

Many teams all over the world are engaged in ethical hacking activities, investing a large amount of time in projects such as red teaming, penetration testing, security assessments, bug bounty, and security research. These efforts are constantly followed by detailed reports that provide an in-depth overview of the work done and the vulnerabilities identified. The global community has consistently aimed to enhance reporting, ensuring that the outcome is clear and suitable for its intended audience.

Security teams must consider not only the technical aspects of their outcomes, but also the **descriptive** and **theoretical** elements while reporting. From my friends, colleagues, and my own experience, security teams often build and develop their internal knowledge base over the years to shape their reporting **uniqueness** and **distinctiveness**. Building this internal knowledge base requires dedication to ensure it remains *valuable*, *relevant* over time, and, more crucially, a *core asset* within the team. Keeping up with the constant updates and breakthroughs in the **ethical hacking world** and **security standards**, like MITRE and OWASP, is essential to achieve these objectives.

Recently, OWASP has made huge advancements in Mobile Security, releasing new updates and standards to improve security practices. The community's contributions have been amazing, and I cannot express my gratitude enough.

The purpose of this article is to highlight how Yarix addresses these aspects, especially in Mobile Security, sharing the behind-the-scenes approaches that help to consistently improve the Yarix Red Team's (YRT) outcomes. But first, we will be looking at the [OWASP Mobile Application Security project's latest 2024 update](https://mas.owasp.org/news/).

## OWASP Mobile Security Application Refactoring 2024

Before delving into the topic, it is useful to look at the evolution of the [OWASP Mobile Application Security (MAS)](https://mas.owasp.org/) project to better understand its strengths and limitations throughout time.

Anyone in mobile security knows the OWASP MAS project is a **must-read** and **valuable** resource. In my opinion, no better project covers all the technical security concerns of a mobile application as the OWASP project. It is not only well-documented but also exceptionally organized, at least now.

Over the years, this open-source project has provided comprehensive information on mobile app security, addressing storage, networking, platform usage, code development, resilience, and more. Importantly, the project has diversified into what I would call *subprojects*, such as the [Mobile Application Security Verification Standard (MASVS)](https://mas.owasp.org/MASVS/), which was created in 2016, and the [Mobile Security Testing Guide (MSTG)](https://mas.owasp.org/MASTG/), which was released in 2019. The drive followed the conventional OWASP approach: starting with more theoretical and abstract documents (MASVS) and moving to more practical and technical ones (MSTG).

Despite ongoing updates and revisions, the industry standards have faced challenges and shortcomings over the years. As a result, security teams often couldn't rely solely on the common standards, frameworks, and tools - not limited to OWASP but also including MITRE, [CVSS](https://www.first.org/cvss/), [CWE](https://cwe.mitre.org/), and others in the industry. They had to fill certain gaps using their own knowledge, expertise, or the limited information available online.

If you have ever been part of a security team, you might have encountered situations where it was complex calculating the CVSS score because the impact was not clear for example, or you couldn’t exploit the vulnerability but still felt it needed to be reported. Portswigger mentioned CVSS system failures, highlighted by JFrog, [here](https://portswigger.net/daily-swig/cvss-system-criticized-for-failure-to-address-real-world-impact). Still, you might have struggled to fit a vulnerability neatly into a specific category or CWE. Recently, a famous web security expert [Tib3rius](https://www.youtube.com/watch?v=_4oODs7PBuI) talked about how the evolution of OWASP Top Ten over the years has created confusion on specific topics.

These are common daily challenges, and there’s no one right way to handle them. The point here isn’t about solving them but acknowledging that they’re part of the job. Often, we are asked to fit vulnerabilities into specific categories, even if they are not an appropriate match. This isn't only about the constraints of the standards, but also how we use them, especially in *Vulnerability Management.* Plus, facing the theoretical and "managerial" aspects of vulnerabilities can be tedious and, therefore, done inadequately because of the lack of willingness to do it properly.

Addressing the shortcomings of previous OWASP project versions has led to new developments like the [Mobile Application Security Weakness Enumeration (MASWE)](https://mas.owasp.org/MASWE/). This project specifically replaces the poor list of [mobile vulnerabilities in the CWE (MITRE) database](https://cwe.mitre.org/data/definitions/919.html) - a godforsaken place.

![](https://labs.yarix.com/wp-content/themes/porto/images/lazy.png "meme")

Today, the OWASP Mobile Security Application project provides developers and security testers with a wealth of invaluable resources:

* **MASWE** allows the assignment of one or more CWE-based values to mobile application vulnerabilities that were previously non-existent or poorly represented.
* **MASVS** provides a framework for classifying vulnerabilities into specific areas of mobile application security, refined over the years to deliver a high standard of quality.
* **MSTG** offers guidance on testing, many mobile application vulnerabilities, a list of available tools, steps for reproducing proof of concepts, demos, testing techniques, and more.

Even though this project has been evolving incredibly, it is not suitable to be used as the only core base of your mobile security assessments. This explains the existence of the next chapters.

## Yarix Methodology: A Unique Approach

At Yarix, we're always trying to improve our internal knowledge base to address the gap highlighted. We aim for **better quality**, **flexibility**, and **critical thinking**. However, like any ...