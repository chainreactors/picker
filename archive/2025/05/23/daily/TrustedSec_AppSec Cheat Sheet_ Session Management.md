---
title: AppSec Cheat Sheet: Session Management
url: https://trustedsec.com/blog/appsec-cheat-sheet-session-management
source: TrustedSec
date: 2025-05-23
fetch_date: 2025-10-06T22:30:53.642214
---

# AppSec Cheat Sheet: Session Management

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

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
* [AppSec Cheat Sheet: Session Management](https://trustedsec.com/blog/appsec-cheat-sheet-session-management)

May 22, 2025

# AppSec Cheat Sheet: Session Management

Written by
Aaron James

Application Security Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/AppSecCheatSheet_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1747748502&s=57f8c2e570382577c19482360de67b50)

Table of contents

* [Cheat Sheet](#CheatSheet)
* [Learn](#Learn)
* [Implement](#Implement)
* [Identify Session Token(s)](#Identify)
* [Uniqueness](#Uniqueness)
* [Cryptographically Random and Unpredictable](#Random)
* [Destruction](#Destruction)
* [Fixation](#Fixation)
* [Session Puzzling](#Puzzling)
* [Token Disclosure](#Disclosure)
* [Configuration](#Configuration)
* [Token Exchange Processes](#Exchange)
* [Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#9ca3efe9fef6f9ffe8a1dff4f9fff7b9aeacf3e9e8b9aeace8f4f5efb9aeacfdeee8f5fff0f9b9aeacfaeef3f1b9aeacc8eee9efe8f9f8cff9ffb9aeadbafdf1eca7fef3f8e5a1ddececcff9ffb9aeacdff4f9fde8b9aeaccff4f9f9e8b9afddb9aeaccff9efeff5f3f2b9aeacd1fdf2fdfbf9f1f9f2e8b9afddb9aeacf4e8e8ecefb9afddb9aedab9aedae8eee9efe8f9f8eff9ffb2fff3f1b9aedafef0f3fbb9aedafdececeff9ffb1fff4f9fde8b1eff4f9f9e8b1eff9efeff5f3f2b1f1fdf2fdfbf9f1f9f2e8 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fappsec-cheat-sheet-session-management "Share on Facebook")
* [Share on X](http://twitter.com/share?text=AppSec%20Cheat%20Sheet%3A%20Session%20Management%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fappsec-cheat-sheet-session-management "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fappsec-cheat-sheet-session-management&mini=true "Share on LinkedIn")

## Session Management Testing - Cookies

*The **Cheat Sheet** section is for quick reference and to make sure steps don’t get missed.*
*The **Learn** section is for those who have never touched the topic before.*
*The **Implement** section is for more detailed descriptions of each Cheat Sheet item.*

## Cheat Sheet

|  |  |
| --- | --- |
| **Session Management Cheat Sheet - Cookies** | |
| [**Identify session token(s)**](#Identify) | Bare minimum token(s) needed for sensitive request + find a test page |
| [**Uniqueness**](#Uniqueness) | Make sure the same token is not issued on every login |
| [**Random and unpredictable**](#Random) | Manually review for cleartext or recognizable patterns  Simple obfuscation: ***Decoder***  Statistical analysis: ***Sequencer***  Character Modification: ***Character Frobber + Bit Flipper*** |
| [**Destruction**](#Destruction) | Idle (critical apps: 2-5 min, less critical apps: 15-30 min)  Absolute (4-8 hours regardless of activity)  On Logout  Remain invalid on subsequent logins |
| [**Fixation**](#Fixation) | Is a session token issued prior to login? Does the token become the authenticated session token? |
| [**Puzzling**](#Puzzling) | Is there an opportunity to enter user data prior to authentication? Are any session tokens issued valid for sensitive content? |
| [**Token disclosure**](#Disclosure) | Do a global search for the token, does it appear anywhere other than the cookie? |
| [**Configuration**](#Configuration) | ***Should be set on all sensitive cookies:***  ***Secure*** – cookie won’t be sent over unencrypted HTTP  ***HttpOnly*** – JavaScript cannot read cookie  Depends on the environment/business context:  ***SameSite*** – determines if cookie is sent in cross-site requests   * ***Strict*** – not sent in cross-site requests * ***Lax*** – sent when user clicks a link or fetches images, scripts, iframes, etc. – no POST, PUT, DELETE * ***None*** – cookie will be sent in cross-site requests   ***Path*** – cookie only sent to specific path, apply if multiple apps are on the same host  ***Domain*** – cookie sent to subdomains, more restrictive if absent |
| [**Token exchange processes**](#Exchange) | Are session tokens passed between applications? Carefully review the process for flaws. |

## Learn

To understand why sessions are used, and more importantly, why the security around them is so important, we need to first discuss Hypertext Transfer Protocol, or HTTP. HTTP is the language of the Web, and is what is being used when navigating websites and other web services. It is client-server oriented, meaning a client (e.g. a web browser) requests a resource from a server, and the server responds with that resource.

Another interesting thing about HTTP is that it is stateless...