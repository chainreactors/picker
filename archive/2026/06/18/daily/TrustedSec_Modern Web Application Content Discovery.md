---
title: Modern Web Application Content Discovery
url: https://trustedsec.com/blog/modern-web-application-content-discovery
source: TrustedSec
date: 2026-06-18
fetch_date: 2026-06-19T07:08:42.458663
---

# Modern Web Application Content Discovery

[Skip to Main Content](#main)

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Modern Web Application Content Discovery](https://trustedsec.com/blog/modern-web-application-content-discovery)

June 18, 2026

# Modern Web Application Content Discovery

Written by
Luke Bremer

Application Security Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/ModernWebApplicationContentDiscovery_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1781554107&s=adefdc0407e60efc949127323611b28f)

Table of contents

* [FORCED BROWSING](#BROWSING)
* [WEB CRAWLERS](#CRAWLERS)
* [OSINT GOOGLE](#GOOGLE)
* [OSINT GITHUB](#GITHUB)
* [WRAP-UP](#WRAPUP)
* [PREVENTION](#PREVENTION)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#0f307c7a6d656a6c7b324c676a6c642a3d3f607a7b2a3d3f7b67667c2a3d3f6e7d7b666c636a2a3d3f697d60622a3d3f5b7d7a7c7b6a6b5c6a6c2a3d3e296e627f346d606b763242606b6a7d612a3d3f586a6d2a3d3f4e7f7f63666c6e7b6660612a3d3f4c60617b6a617b2a3d3f4b667c6c60796a7d762a3c4e2a3d3f677b7b7f7c2a3c4e2a3d492a3d497b7d7a7c7b6a6b7c6a6c216c60622a3d496d6360682a3d4962606b6a7d6122786a6d226e7f7f63666c6e7b666061226c60617b6a617b226b667c6c60796a7d76 "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmodern-web-application-content-discovery "Share on Facebook")
* [Share on X](https://twitter.com/share?text=Modern%20Web%20Application%20Content%20Discovery%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmodern-web-application-content-discovery "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmodern-web-application-content-discovery&mini=true "Share on LinkedIn")

When testing web applications, discovering what functionality is available is key to finding vulnerabilities. Ideally you want to find as many application pages as possible. You can do this by using web‑crawling or spidering tools to uncover indexed pages, as well as employing forced‑browsing techniques. When doing forced browsing you are looking for pages that are not indexed on the site but still available. Forced-browsing is more useful when the applications user interface (UI) is limited, but even on applications with a large UI, forced-browsing can return webpages that would otherwise not be known.

Recently, I got this question:

##### "I found a URL that is returning a default homepage, but it has no links or navigation. How do I find out if the application has functionality?”

So, I figured I would write up a quick guide on how I find content in modern web applications.

## FORCED BROWSING

To start we can try to guess page names that are present in an application. A common way to browse for un-indexed pages is to run though a list of common page names. For example, we can grab a HTTP request with a proxy like ***Burp Suite*** and send the request to intruder which makes repeated requests with different page names.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/ModernWebApp_Bremer/Fig01_Bremer_ModernWebApp.png?w=320&q=90&auto=format&fit=max&dm=1781554487&s=24416829e2a3140daf2644ad89594741)

Figure 1 - Burp Suite Intruder

Then, we can review the results to see what response codes are returned by the application.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/ModernWebApp_Bremer/Fig02_Bremer_ModernWebApp.png?w=320&q=90&auto=format&fit=max&dm=1781554488&s=63c6ac49443c10bf1fbdc3071c03e699)

Figure 2 - Intruder Results

If a page exists, the application could return a 200 response code or sometimes a redirect code like a 302. Forced browsing typically sends a lot of requests, and the results depends on how good of a wordlist you use. Seclists is still a pretty good baseline to get common lists:

<https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content>

But a lot of tools, such as ***Burp Suite***, have common lists built in as well. ***Burp Suite*** does restrict how fast requests can be sent in the community version, so using command line tools such as ***FFuF*** is also common and in some cases can return results faster.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/ModernWebApp_Bremer/Fig03_Bremer_ModernWebApp.png?w=320&q=90&auto=format&fit=max&dm=1781554489&s=9580c9ba84109fbbcce4dc339ec92b96)

Figure 3 - FFuF Output

It is important to note that by default ***FFuF*** sends 40 requests at a time where ***Burp Suite*** only sends 10 requests at a time. The ***-t*** parameter in ***FFuF*** can set the number of requests send each iteration. To ensure you don't overwhelm a site, or get blocked by rate limits, you may want to decrease the threads being used.

Typically, if a page returns a response code that is not a 404 (Not found) that page might be part of a valid URL path and we can then start re-sea...