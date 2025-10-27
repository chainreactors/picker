---
title: Burp Suite Enterprise Edition Power Tools: Unleashing the power to the command line, Python, and more
url: https://portswigger.net/blog/burp-suite-enterprise-edition-power-tools-unleashing-the-power-to-the-command-line-python-and-more
source: PortSwigger Blog
date: 2023-03-22
fetch_date: 2025-10-04T10:15:15.566796
---

# Burp Suite Enterprise Edition Power Tools: Unleashing the power to the command line, Python, and more

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

# Burp Suite Enterprise Edition Power Tools: Unleashing the power to the command line, Python, and more

[ ]

Ollie Whitehouse |
21 March 2023 at 14:30 UTC

[Burp Suite](/blog/burp-suite)
[Enterprise Edition](/blog/enterprise-edition)

### tl;dr

We have released BSEEPT - [Burp Suite Enterprise Edition Power Tools](https://github.com/olliewuk/bseept) which:

* Is a command line tool to drive all aspects of the BSEE [GraphQL API](https://portswigger.net/burp/extensibility/enterprise/graphql-api/index.html).
* Is a Python client library to allow you to easily utilise the BSEE [GraphQL](/web-security/graphql) API in your own code be it command line tooling, lambdas, or integration layers.
* Returns BSEE's JSON allowing you to parse on the command line with `jq` and similar.

### Backstory

In January I joined PortSwigger in a more involved capacity as Non-Executive Director++ (the ++ being I can still code whilst sitting in the boardroom). In my first month I spent time coming up to speed on the products, their features, roadmaps, and most importantly their APIs for extensibility and similar.

These first months saw me produce two extension prototypes using the [Montoya API](https://github.com/PortSwigger/burp-extensions-montoya-api). These used the [Google Safe Browsing API to identify known malicious sites in sitemaps](https://gist.github.com/olliewuk/c518e820784d72cc8b1ce6f26be7a968) and a [YAML-powered regular expression engine to identify sensitive information presence / leakage](https://gist.github.com/olliewuk/8f8e563359261cdb322852c858810f60). I then had the fortune of working with Hannah and Alex on the [TOTP Authenticate](https://github.com/Hannah-PortSwigger/TOTPAuthenticate) extension to support multi-factor authentication in [Burp Suite Enterprise Edition](/burp/enterprise).

I then turned my attention to the [Burp Suite Enterprise Edition](https://portswigger.net/burp/enterprise) GraphQL API. It struck me that we had this amazing GraphQL API, which we both use in the product, but also expose to customers. But for DevOps teams and others in the security function to really utilize this required a bit of investment.

So an objective was born ... write the power tools that teams who work with Burp Suite Enterprise Edition would find valuable.

Que A-Team building music, over 80 commits, lots of learning (I learnt to use a Mac at the same time) and out popped BSEEPT.

BSEEPT allows you to use every aspect of the GraphQL API from the command line or in your own Python code.

### Quick Demo

I have written an extensive readme on the [GitHub project](https://github.com/olliewuk/bseept) but I will give an example of how one might use it.

In this example we will run through several steps:

1. Query the run scans.
2. Then pass through `jq` to just extract the issue titles.
3. Then pass through `jq` to build a CSV of issue titles, site, and path they were found in.

All without writing any new code - just using command line tools!

So we first get the scan details:

`bseept % python3 bseept.py --getscans | jq
{
   "data": {
      "scans": [
         {
            "id": "123",
            "status": "succeeded",
            "site_id": "1",
            "schedule_item": {
               "id": "1",
               "site": {
                  "id": "1",
                  "name": "Gin & Juice"
               },
               "schedule": {
                  "initial_run_time": "2022-09-02T13:51:14.550Z",
                  "rrule": "FREQ=DAILY;INTERVAL=2"
               },
               "has_run_more_than_once": true,
               "scheduled_run_time": "2023-03-15T13:51:14.000Z"
            },
            "scheduled_start_time": "2023-03-13T13:51:14.000Z",
            "start_time": "2023-03-13T13:51:54.525Z",
            "end_time": "2023-03-13T14:37:50.525Z",
            "duration_in_seconds": 2756,
            "scan_failure_code": null,
            "scan_metrics": {
               "crawl_request_count": 774,
               "unique_location_count": 54,
               "audit_request_count": 57437,
               "crawl_and_audit_progress_percentage": 100,
               "scan_phase": null,
               "audit_start_time": null,
               "current_url": "https://ginandjuice.shop:443/robots.txt"
            },
            "scan_failure_message": null,
            "scan_delta": {
               "new_issue_count": 0,
               "repeated_issue_count": 40,
               "regressed_issue_count": 0,
               "resolved_issue_count": 0
            },
            "issue_counts": {
               "total": 40,
               "high": {
                  "total": 11,
                  "firm": 4,
                  "tentative": 0,
                  "cer...