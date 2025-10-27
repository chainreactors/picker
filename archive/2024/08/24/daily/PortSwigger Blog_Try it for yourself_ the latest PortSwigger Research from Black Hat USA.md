---
title: Try it for yourself: the latest PortSwigger Research from Black Hat USA
url: https://portswigger.net/blog/try-it-for-yourself-the-latest-portswigger-research-from-black-hat-usa
source: PortSwigger Blog
date: 2024-08-24
fetch_date: 2025-10-06T18:04:48.412061
---

# Try it for yourself: the latest PortSwigger Research from Black Hat USA

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

# Try it for yourself: the latest PortSwigger Research from Black Hat USA

[ ]

Amelia Coen |
23 August 2024 at 07:44 UTC

![](/cms/images/40/77/2a48-article-blog_header.jpg)

### The modern web is constantly developing, with new potential vulnerabilities emerging all the time. Ensuring your web applications are secure in the face of this evolving threat is a constant challenge.

At Black Hat USA, the PortSwigger Research team debuted  [three groundbreaking research releases](https://portswigger.net/research/black-hat), addressing some of the biggest threats in [web application security](/burp/application-security-testing). These innovative findings are vital in helping AppSec teams stay up to date with the latest attack threats.

Here’s some examples of how you can apply this cutting-edge research in Burp Suite, and test your skills in our new Web Security Academy labs.

## Use web timing attacks that actually work

All too often, web timing attacks are theoretical - useful only on paper, or in lab environments. This has understandably led many AppSec professionals to ignore them in their testing practices.

In [Listen to the whispers: web timing attacks that actually work](https://portswigger.net/research/listen-to-the-whispers-web-timing-attacks-that-actually-work), [James Kettle](https://x.com/albinowax) shows why AppSec professionals are missing a huge opportunity, proposing three novel attack techniques to transform your web timing attacks:

* Discovering hidden attack surfaces.
* Server-side injection vulnerabilities.
* Misconfigured reverse proxies.

These cutting-edge techniques allow you to realise the potential of web timing attacks, ultimately helping you discover more potential attack surfaces.

Ready to try practical web timing attacks yourself? All three of these techniques are now available in James’ [Param Miner](https://portswigger.net/bappstore/17d2949a985c4b7ca092728dba871943) extension. To try them out, make sure you have the extension installed, use a 'Detect scoped [SSRF](/web-security/ssrf)' scan to detect a reverse proxy, then you can run 'Exploit scoped SSRF' to find alternative routes to internal systems, and on each alternate route, run 'Guess parameters', cookies, or HTTP headers to find hidden attack surface.

Try these new techniques in James' latest CTF at [listentothewhispers.net](http://listentothewhispers.net) – see if you can crack it!

![](/cms/images/3b/e3/18d6-article-timing_attacks_blog_image.jpg)

## Secure potential email parsing discrepancies

Some websites parse email addresses to determine the email owner’s organization. While this process appears straightforward, it is actually very complex, meaning discrepancies can arise when different parts of the application handle email addresses differently.

In [Splitting the email atom: exploiting parsers to bypass access controls](https://portswigger.net/research/splitting-the-email-atom), [Gareth Heyes](https://x.com/garethheyes) explores how attackers can abuse this trust in the domain part of the email address to bypass [access controls](/web-security/access-control) and even gain RCE (Remote Code Execution).

To combat this threat, we have created a built-in payload wordlist in Intruder, which you can now use to fuzz for these kinds of attacks.

Ready to try it out? [Test these new techniques](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-bypassing-access-controls-using-email-address-parsing-discrepancies) in our brand new lab inside the Web Security Academy.

To access the wordlist in [Burp Suite Professional](/burp/pro), navigate to Intruder, and select the new payload list ‘Fuzzing - email splitting attacks’. Remember to add your payload processing rules over the placeholder values before running the list.

![](/cms/images/56/a7/56e9-article-email_blog_image.jpg)

## Protect your applications from web cache exploitation

In recent years, web cache attacks have become a popular way to steal sensitive data, deface websites, and deliver exploits. We've also seen parser inconsistencies causing critical vulnerabilities like [HTTP Request Smuggling](/web-security/request-smuggling). This raises the question: what happens if we attack web caches using new path confusion variants?

In [Gotta cache 'em all: bending the rules of web cache exploitation](https://portswigger.net/research/gotta-cache-em-all), [Martin Doyhenard](https://x.com/tincho_508) looks at how URL parsing discrepancies can be leveraged to obtain arbitrary web cache poisoning and deception using popular HTTP servers and CDNs with default configurations.

Thanks to Martin’s research, Burp Scanner now tests for web cache deception vulnerabilities without the need to delay...