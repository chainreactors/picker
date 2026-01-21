---
title: Why Secrets in JavaScript Bundles are Still Being Missed
url: https://thehackernews.com/2026/01/why-secrets-in-javascript-bundles-are.html
source: The Hacker News
date: 2026-01-20
fetch_date: 2026-01-21T03:33:19.020243
---

# Why Secrets in JavaScript Bundles are Still Being Missed

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

# [Why Secrets in JavaScript Bundles are Still Being Missed](https://thehackernews.com/2026/01/why-secrets-in-javascript-bundles-are.html)

**The Hacker News**Jan 20, 2026API Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieV5wPGUwZgsm79ntLb9Sz_6xAPAV54CQ1SztbNfpLe-ovKEkTrCsLBRsD52c87yFiByHZGandN1pYNNBn1OLUpc5iEFJnGP0YRn_WWeWod1xxQUNhjlD1vFMh-4EI2fq06Gt86H_U7rX7FBjhLoXrhtzQKqjLRa3X6c7W86BFrR5xfDX80ve6UDs4zU8/s1600-e365/main.jpg)

Leaked API keys are no longer unusual, nor are the breaches that follow. So why are sensitive tokens still being so easily exposed?

To find out, [Intruder's](https://www.intruder.io/?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Csecrets_detection) research team looked at what traditional vulnerability scanners actually cover and built a new secrets detection method to address gaps in existing approaches.

Applying this at scale by scanning 5 million applications revealed over 42,000 exposed tokens across 334 secret types, exposing a major class of leaked secrets that is not being handled well by existing tooling, particularly in single-page applications (SPAs).

In this article, we break down existing secrets detection methods and reveal what we found when we scanned millions of applications for secrets hidden in JavaScript bundles.

## Established secrets detection methods (and their limitations)

### Traditional secrets detection

The traditional, fully automated approach to detecting application secrets is to search a set of known paths and apply regular expressions to match known secret formats.

While this method is useful and can catch some exposures, it has clear limitations and will not detect all types of leaks, particularly those that require the scanner to spider the application or authenticate.

A good example of this is [Nuclei's GitLab personal access token template](https://github.com/projectdiscovery/nuclei-templates/blob/main/http/exposures/tokens/gitlab/gitlab-personal-token.yaml). The scanner is fed a base URL, for example, https://portal.intruder.io/, causing the template to:

1. Make an HTTP GET request to https://portal.intruder.io/
2. Inspect the direct response to that single request, **ignoring other pages and resources such as JavaScript files**
3. Attempt to identify the pattern of a GitLab personal access token
4. If found, make a follow-up request to GitLab's public API to check whether the token is active
5. If active, raise an issue

This is clearly a simple example, but this approach is effective. Especially so when templates define many paths where secrets are commonly exposed.

This format is typical of infrastructure scanners, which do not typically run a headless browser. When the scanner is given the base URL to scan (for example, https://portal.intruder.io), subsequent requests that would be made by a browser (such as the JavaScript files required to render the page, e.g., https://portal.intruder.io/assets/index-DzChsIZu.js) will not be made using this old-school approach.

### Dynamic Application Security Testing (DAST)

Dynamic Application Security Testing (DAST) tools are generally a more robust way to scan applications, and tend to have more complex functionality, allowing for full spidering of applications, support for authentication, and a wider capability at detecting application layer weaknesses. Indeed, DAST scanners may seem the natural option for secrets detection in application front-ends. There should be nothing holding back a DAST scanner from discovering available JavaScript files or scanning for secrets within them.

However, this type of scanning is more expensive, requires in-depth configuration, and in reality is usually reserved for a small number of high-value applications. For example, you are unlikely to configure a DAST scanner for every application you have out there across a wide digital estate. Plus, many DAST tools do not implement a wide enough range of regular expressions compared to well-known command-line tools.

This leaves a clear gap which *should* be covered by the traditional infrastructure scanner, but isn't - and in all likelihood is also not being covered by DAST scanners because of deployment, budget, and maintenance limitations.

### Static Application Security Testing (SAST)

Static Application Security Testing (SAST) tools analyze source code to identify vulnerabilities and are a primary way to detect secrets before code reaches production. They are effective at catching hardcoded credentials and preventing some classes of exposure.

However, we found that SAST methods also do not cover the full picture - and once again, some secrets within JavaScript bundles slipped through the gaps in a way that static analysis would miss.

## Building a secrets detection check for JavaScript bundles

When we started this research, it was not clear how common this problem would be. Are secrets actually being bundled into JavaScript front-ends, and is it widespread enough to justify an automated approach?

To find out, [we built an automated check](https://www.intruder.io/research/secrets-detection-javascript?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Csecrets_detection) and scanned approximately 5 million applications. The result was a large number of exposures, significantly more than we expected. The output file alone was over 100MB of plain text and contained more than 42,000 tokens across 334 different secret types.

We did not fully triage every result, but among the samples we reviewed, we identified a number of high-impact exposures.

## What we found

### Code Repository Tokens

The most impactful exposures we identified were tokens for code repository platforms such as GitHub and GitLab. In total, we found 688 tokens, many of which were still active and gave full access to repositories.

In one case, shown below, a GitLab personal access token was embedded directly in a JavaScript file. The token was scoped to allow access to all private repositories within the organization, including CI/CD pipeline secrets for onward services such as AWS and SSH.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjsfZhs0L7q0PagZq3GgJBIIfexJv83UK4sG78XWIpZN28XVnJ3OzUrJaXYTbf-XvzUKOyWY1GYfmt_HdlqsBnLcXq9gso6LqsXTBiM9dDR5AWSxXfuSC8...