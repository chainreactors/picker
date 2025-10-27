---
title: What this KeePass CVE means for organizations searching for new password vaults
url: https://www.trustedsec.com/blog/what-this-keepass-cve-means-for-organizations-searching-for-new-password-vaults/
source: TrustedSec
date: 2023-02-03
fetch_date: 2025-10-04T05:35:34.661346
---

# What this KeePass CVE means for organizations searching for new password vaults

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
* [What this KeePass CVE means for organizations searching for new password vaults](https://trustedsec.com/blog/what-this-keepass-cve-means-for-organizations-searching-for-new-password-vaults)

February 02, 2023

# What this KeePass CVE means for organizations searching for new password vaults

Written by
Carlos Perez

Research
Security Program Assessment
Vulnerability Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/KeePassVulnerabilityVideo_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695565802&s=08dea0abfb16e1885866bd8f9c430d65)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#112e6264737b7472652c527974727a3423217e64653423216579786234232170636578727d7434232177637e7c3423214563646265747542747234232037707c612a737e75682c46797065342321657978623423215a7474417062623423215247543423217c74707f62342321777e633423217e6376707f786b7065787e7f62342321627470637279787f76342321777e633423217f746634232161706262667e63753423216770647d65623422503423217965656162342250342357342357656364626574756274723f727e7c342357737d7e76342357667970653c657978623c7a7474617062623c7267743c7c74707f623c777e633c7e6376707f786b7065787e7f623c627470637279787f763c777e633c7f74663c61706262667e63753c6770647d6562 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhat-this-keepass-cve-means-for-organizations-searching-for-new-password-vaults "Share on Facebook")
* [Share on X](http://twitter.com/share?text=What%20this%20KeePass%20CVE%20means%20for%20organizations%20searching%20for%20new%20password%20vaults%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhat-this-keepass-cve-means-for-organizations-searching-for-new-password-vaults "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhat-this-keepass-cve-means-for-organizations-searching-for-new-password-vaults&mini=true "Share on LinkedIn")

https://youtu.be/OEaFaSjaZY4

After the 2022 LastPass breach, many organizations began searching for alternative password vault solutions. KeePass, a legacy open-source option has risen to the top for many organizations evaluating their options. Others have been using this option already for years. A recent POC demonstrating who to abuse the Trigger feature was released and assigned a CVE. While the KeePass developers are contesting the assignment of the CVE, we thought it would be valuable to break down exactly how the attack works and the risk it poses.

POC: <https://github.com/alt3kx/CVE-2023-24055_PoC>

KeePass Discussion: <https://sourceforge.net/p/keepass/discussion/329220/thread/a146e5cf6b/>

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#0f307c7a6d656a6c7b324c676a6c642a3d3f607a7b2a3d3f7b67667c2a3d3f6e7d7b666c636a2a3d3f697d60622a3d3f5b7d7a7c7b6a6b5c6a6c2a3d3e296e627f346d606b763258676e7b2a3d3f7b67667c2a3d3f446a6a5f6e7c7c2a3d3f4c594a2a3d3f626a6e617c2a3d3f69607d2a3d3f607d686e6166756e7b6660617c2a3d3f7c6a6e7d6c676661682a3d3f69607d2a3d3f616a782a3d3f7f6e7c7c78607d6b2a3d3f796e7a637b7c2a3c4e2a3d3f677b7b7f7c2a3c4e2a3d492a3d497b7d7a7c7b6a6b7c6a6c216c60622a3d496d6360682a3d4978676e7b227b67667c22646a6a7f6e7c7c226c796a22626a6e617c2269607d22607d686e6166756e7b6660617c227c6a6e7d6c676661682269607d22616a78227f6e7c7c78607d6b22796e7a637b7c "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhat-this-keepass-cve-means-for-organizations-searching-for-new-password-vaults "Share on Facebook")
* [Share on X](http://twitter.com/share?text=What%20this%20KeePass%20CVE%20means%20for%20organizations%20searching%20for%20new%20password%20vaults%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhat-this-keepass-cve-means-for-organizations-searching-for-new-password-vaults "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhat-this-keepass-cve-means-for-organizations-searching-for-new-password-vaults&mini=true "Share on LinkedIn")

## [Blog](https://trustedsec.com/blog)

## [Tools](https://trustedsec.com/tools)

## [Newsletter Signup](https://trustedsec.com/newsletter-signup)

[TrustedSec](https://trustedsec.com/)

3485 Southwestern Boulevard
Fairlawn, OH 44333

1-877-550-4728

* [twitter](https://twitter.com/TrustedSec)
* [linkedin](https://www.linkedin.com/company/trustedsec-llc/)
* [youtube](https://www.youtube.com/%40TrustedSecTV)
* [facebook](https://www.facebook.com/1trustedsec/)
* [discord](https://discord.gg/trustedsec)
* [rss](https://trustedsec.com/feed.rss)

* [Terms Of Service](https://truste...