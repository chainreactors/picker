---
title: Burp Suite Performance Improvements
url: https://portswigger.net/blog/burp-suite-performance-improvements
source: PortSwigger Blog
date: 2024-09-12
fetch_date: 2025-10-06T18:28:17.930184
---

# Burp Suite Performance Improvements

[**Your agentic AI partner in Burp Suite - Discover Burp AI now**

**Read more**](https://portswigger.net/burp/ai)

[Login](/users)

[ ]

Products

Solutions

[Research](/research)
[Academy](/web-security)

Support

Company

[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[My account](/users/youraccount)
[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[![Burp Suite DAST](/content/images/svg/icons/enterprise.svg)
**Burp Suite DAST**
The enterprise-enabled dynamic web vulnerability scanner.](/burp/enterprise)
[![Burp Suite Professional](/content/images/svg/icons/professional.svg)
**Burp Suite Professional**
The world's #1 web penetration testing toolkit.](/burp/pro)
[![Burp Suite Community Edition](/content/images/svg/icons/community.svg)
**Burp Suite Community Edition**
The best manual tools to start web security testing.](/burp/communitydownload)
[View all product editions](/burp)

[**Burp Scanner**

Burp Suite's web vulnerability scanner

![Burp Suite's web vulnerability scanner'](/mega-nav/images/burp-suite-scanner.jpg)](/burp/vulnerability-scanner)

[**Attack surface visibility**
Improve security posture, prioritize manual testing, free up time.](/solutions/attack-surface-visibility)
[**CI-driven scanning**
More proactive security - find and fix vulnerabilities earlier.](/solutions/ci-driven-scanning)
[**Application security testing**
See how our software enables the world to secure the web.](/solutions)
[**DevSecOps**
Catch critical bugs; ship more secure software, more quickly.](/solutions/devsecops)
[**Penetration testing**
Accelerate penetration testing - find more bugs, more quickly.](/solutions/penetration-testing)
[**Automated scanning**
Scale dynamic scanning. Reduce risk. Save time/money.](/solutions/automated-security-testing)
[**Bug bounty hunting**
Level up your hacking and earn more bug bounties.](/solutions/bug-bounty-hunting)
[**Compliance**
Enhance security monitoring to comply with confidence.](/solutions/compliance)

[View all solutions](/solutions)

[**Product comparison**

What's the difference between Pro and Enterprise Edition?

![Burp Suite Professional vs Burp Suite Enterprise Edition](/mega-nav/images/burp-suite.jpg)](/burp/enterprise/resources/enterprise-edition-vs-professional)

[**Support Center**
Get help and advice from our experts on all things Burp.](/support)
[**Documentation**
Tutorials and guides for Burp Suite.](/burp/documentation)
[**Get Started - Professional**
Get started with Burp Suite Professional.](/burp/documentation/desktop/getting-started)
[**Get Started - Enterprise**
Get started with Burp Suite Enterprise Edition.](/burp/documentation/enterprise/getting-started)
[**User Forum**
Get your questions answered in the User Forum.](https://forum.portswigger.net/)
[**Downloads**
Download the latest version of Burp Suite.](/burp/releases)

[Visit the Support Center](/support)

[**Downloads**

Download the latest version of Burp Suite.

![The latest version of Burp Suite software for download](/mega-nav/images/latest-burp-suite-software-download.jpg)](/burp/releases)

# Performance Improvements to table sorting and Repeater

[ ]

Daniel Allen |
11 September 2024 at 06:53 UTC

Performance is a critical factor in the usability and efficiency of any software, and Burp Suite is no exception. We've recently focused on enhancing Burp Suite's performance across several key areas and have made significant strides in reducing processing times, minimizing memory usage, and ensuring a smoother user experience. Read on for a deep dive into a couple of the performance issues we tackled in recent releases.

## Table Sorting

Tables are a core component of Burp Suite. Most of the data produced in Burp is presented in table format. Being able to manipulate this data through sorting is key to many users’ workflows. This section details our approach to the problem and the measurable improvements in performance.

### The Problem

The main issue with table sorting stemmed from how data retrieval and sorting operations were handled. Sorting a table on a large project file caused numerous slow and repetitive disk retrievals, significantly hindering performance. When multiple column sorts were applied, it required up to two to three times more data retrievals, exacerbating the problem.

One of the most frustrating issues was the user interface (UI) freezing during these operations. Since the sorting was happening on the UI thread, Burp would become unresponsive. This would also occur on almost all table operations such as inserts and removes since the new values needed to be sorted too. This led to a poor experience, as users could be left unsure whether Burp Suite had crashed or if it was still processing.

### The Solution

To address these issues, we undertook a series of technical improvements focused on optimizing data retrieval, offloading processing from the UI thread, and enhancing visual feedback.

1. **Snapshot and In-Memory Cache:** We took a snapshot of the table data and sorted it on a separate thread. This approach involved retrieving all necessary data into an in-memory cache before sorting. By doing this, we reduced the need for repeated data retrievals (sometimes of the same object) from disk.
2. **Background Thread Sorting:** By moving the bulk of the processing for sorting operations to a different thread, we were able to maintain a responsive user interface. Once the sorting is complete, we pass back the result to the UI thread to update the table. One major consideration during development was the careful management of data integrity across the multiple threads.
3. **UX Improvements:** To improve the user experience, we added spinner animations to the headers of the columns being sorted to let users know Burp is working in the background.

### Results and Performance Metrics

The changes we implemented resulted in significant improvements to table sorting performance. Here are some key results:

* **Sorting Time Reduction:** For large datasets, sorting times were reduced dramatically. This means that sorting massive proxy histories (250,000+ entries) that previously took minutes were now completed in seconds or less.
* **UI Responsiveness:** The transition to multi-threaded sorting eliminated noticeable UI freezes. This results in a smooth and responsive interface even during intensive sorting operations.

To monitor the results of performance improvements, we have introduced a suite of tests and dashboards that reflect how changes in the codebase affect typical workflows across Burp. This not only allows us to quantify the value of the improvements made but also helps us prevent regressions in performance.

Our performance tests demonstrated these gains, which showed the drastic reduction in sorting times and the improved responsiveness of the UI. These results underscore the effectiveness of our approach and the tangible benefits to our users.

![Time to sort large proxy history by multiple columns](/cms/images/f5/40/9a6c-article-image3.png)

## Single Repeater

Repeater is a core part of Burp Suite used for manually modifying and re-sending HTTP requests – it's often key to a pentester's workflow. And, just like a web browser over time, users can (accidentally or otherwise) end up with a *lot* of Repeater tabs, which we weren't handling the best.

![Tweet showing many repeater tabs](/cms/images/e8/22/e2af-article-tweet-1802387043944681644.png "https://x.com/ryancbarnett/status/1802387043944681644")

### The Problem

When loading Burp Suite, we would previously load one set of UI (user interface) components for each Repeater tab you had. Unfortunately, this meant if you had a lot of Repeater tabs in your project file, then memory usage and the time taken to load up Burp would be significantly impacted, as each se...