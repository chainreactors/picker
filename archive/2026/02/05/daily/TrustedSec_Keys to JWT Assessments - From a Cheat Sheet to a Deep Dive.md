---
title: Keys to JWT Assessments - From a Cheat Sheet to a Deep Dive
url: https://trustedsec.com/blog/keys-to-jwt-assessments-from-a-cheat-sheet-to-a-deep-dive
source: TrustedSec
date: 2026-02-05
fetch_date: 2026-02-06T04:09:47.945192
---

# Keys to JWT Assessments - From a Cheat Sheet to a Deep Dive

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
* [Keys to JWT Assessments - From a Cheat Sheet to a Deep Dive](https://trustedsec.com/blog/keys-to-jwt-assessments-from-a-cheat-sheet-to-a-deep-dive)

February 05, 2026

# Keys to JWT Assessments - From a Cheat Sheet to a Deep Dive

Written by
Aaron James

Application Security Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/KeysToJWTAssessments_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1769795560&s=170fb375540ffb09b3e33f112c295d14)

Table of contents

* [Cheat Sheet](#CheatSheet)
* [New to JWTs? Learn Here.](#New)
* [Detailed Implementation of JWT Attacks](#Implementation)
* [Determine Session Management Mechanism/Identify JWT](#Determine)
* [Information Gathering](#Gathering)
* [Required](#Required)
* [Signature Validation](#Validation)
* [Weak HMAC Secret](#Weak)
* [Signature Exclusion](#Exclusion)
* [Key Confusion](#Key)
* [Injecting jwk Values](#Injecting)
* [Injecting jku and x5u Values](#Values)
* [kid Attacks](#kid)
* [Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#5d622e283f37383e29601e35383e36786f6d322829786f6d2935342e786f6d3c2f29343e3138786f6d3b2f3230786f6d092f282e2938390e383e786f6c7b3c302d663f323924601638242e786f6d2932786f6d170a09786f6d1c2e2e382e2e303833292e786f6d70786f6d1b2f3230786f6d3c786f6d1e35383c29786f6d0e35383829786f6d2932786f6d3c786f6d1938382d786f6d19342b38786e1c786f6d3529292d2e786e1c786f1b786f1b292f282e2938392e383e733e3230786f1b3f31323a786f1b3638242e70293270372a29703c2e2e382e2e303833292e703b2f3230703c703e35383c29702e35383829702932703c703938382d7039342b38 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fkeys-to-jwt-assessments-from-a-cheat-sheet-to-a-deep-dive "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Keys%20to%20JWT%20Assessments%20-%20From%20a%20Cheat%20Sheet%20to%20a%20Deep%20Dive%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fkeys-to-jwt-assessments-from-a-cheat-sheet-to-a-deep-dive "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fkeys-to-jwt-assessments-from-a-cheat-sheet-to-a-deep-dive&mini=true "Share on LinkedIn")

*The [**Cheat Sheet**](#CheatSheet) section is for quick reference.*

*The [**Learn**](#New) section is for those who have never touched the topic before.*

*The [**Implement**](#Implementation) section is for more detailed descriptions of each Cheat Sheet item.*

## Cheat Sheet

| **Session Management Cheat Sheet - JWT** | |
| --- | --- |
| **How are sessions managed?** | Bare minimum token(s) needed for sensitive request + find a test page |
| **JWT regex** | `[= ]eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9._-]*` |
| **Gather Information** | Review token contents with JSON Web Tokens' request/response tab  Look for: ***exp***, ***alg***  Any other interesting claims e.g., ‘password’, ‘role’, etc. |
| **Required?** | What resources require the JWT? |
| **Signature Validation** | Remove or modify last few characters from signature |
| **[HS256] Weak HMAC Secret** | **Identify:**   * `jwt_tool.py <JWT> -C -d <DICTIONARY.txt>` * `hashcat -a 0 -m 16500 jwt.txt wordlist.txt -r <path to hashcat>/rules/best64.rule`     **Exploit:**  JWT Editor Extension Tab:   * New Symmetric Key > Specify secret (paste discovered secret) > Provide ID > Generate > OK   JWT Editor Repeater Tab:   * Modify claims * Sign > Select newly created key > OK |
| **Signature Exclusion ('none' Algorithm)** | Manually: Set ***alg*** to ***none***, remove signature  JWT Editor Repeater Tab:   * Attack > 'none' Signing Algorithm > select a variation > OK * Repeat for each variation |
| **[RS256] Key Confusion** | Identify public key (e.g., ***/.well-known/jwks.json***)  JWT Editor Extension Tab:   * New RSA Key > Format as [JWK or PEM] > Provide an ID > Paste [JWK or PEM] key > OK   JWT Editor Repeater Tab:   * Attack > HMAC Key Confusion Attack > Select new RSA key > OK   In the event of failure, convert key format and repeat |
| **Injecting jwk** | JWT Editor Extension Tab:   * New RSA Key > Format as JWK > Generate > OK   JWT Editor Repeater Tab:   * Attack > Embedded JWK > Select generated key > OK |
| **Injecting jku/x5u** | JWT Editor Repeater Tab:   * Attack > Embed collaborator payload > select variation [jku, x5u] > OK * Review Collaborator logs   **Exploit:**   * Host a public JWKS (***jku***) or PEM (***x5u***) and point JWT header parameter to it |
| **Injecting kid Values** | JWT Editor Extension Tab:   * New Symmetric Key > Generate * Replace ***k*** value with "AA==" (Base64-encoded null byte...