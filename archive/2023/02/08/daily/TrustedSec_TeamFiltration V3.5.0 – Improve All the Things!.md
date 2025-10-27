---
title: TeamFiltration V3.5.0 – Improve All the Things!
url: https://www.trustedsec.com/blog/teamfiltration-v3-5-0-improve-all-the-things/
source: TrustedSec
date: 2023-02-08
fetch_date: 2025-10-04T06:00:27.332754
---

# TeamFiltration V3.5.0 – Improve All the Things!

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
* [TeamFiltration V3.5.0 - Improve All the Things!](https://trustedsec.com/blog/teamfiltration-v3-5-0-improve-all-the-things)

February 07, 2023

# TeamFiltration V3.5.0 - Improve All the Things!

Written by
Melvin Langvik

Penetration Testing
Red Team Adversarial Attack Simulation

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/TeamFiltrationV3.5.0_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695565227&s=5533396c402967f4539a011503b28ed6)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#8bb4f8fee9e1eee8ffb6c8e3eee8e0aeb9bbe4feffaeb9bbffe3e2f8aeb9bbeaf9ffe2e8e7eeaeb9bbedf9e4e6aeb9bbdff9fef8ffeeefd8eee8aeb9baadeae6fbb0e9e4eff2b6dfeeeae6cde2e7fff9eaffe2e4e5aeb9bbddb8a5bea5bbaeb9bba6aeb9bbc2e6fbf9e4fdeeaeb9bbcae7e7aeb9bbffe3eeaeb9bbdfe3e2e5ecf8aeb9baaeb8caaeb9bbe3fffffbf8aeb8caaeb9cdaeb9cdfff9fef8ffeeeff8eee8a5e8e4e6aeb9cde9e7e4ecaeb9cdffeeeae6ede2e7fff9eaffe2e4e5a6fdb8a6bea6bba6e2e6fbf9e4fdeea6eae7e7a6ffe3eea6ffe3e2e5ecf8 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fteamfiltration-v3-5-0-improve-all-the-things "Share on Facebook")
* [Share on X](http://twitter.com/share?text=TeamFiltration%20V3.5.0%20-%20Improve%20All%20the%20Things%21%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fteamfiltration-v3-5-0-improve-all-the-things "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fteamfiltration-v3-5-0-improve-all-the-things&mini=true "Share on LinkedIn")

TeamFiltration was publicly released during the DefCON30 talk, ["Taking a Dump In The Cloud"](https://youtu.be/GpZTQHLKelg). Before the public release, TeamFiltration was an internal tool for TrustedSec's offensive security operations, which was shared internally back in January 2021.

In short terms, TeamFiltration is a cross-platform framework for enumerating, spraying, exfiltrating, and backdooring Office 365 Azure AD accounts. TeamFiltration aims to make post-exploitation activities efficient and modern through the use of a centralized database and large quality-of-operator features.

Got a compromised an Office 365 account? Give those creds to TeamFiltration and watch the loot rain from the target's Office 365 cloud. TeamFiltration exfiltration capabilities include:

* Teams: Chat logs, contacts list, and shared attachments
* Outlook: Emails and attachments.
* Azure AD/GraphAPI: Users, Groups, and tenant information
* OneDrive: Synced files, both user-specific and SharePoint-shared files

## **What's New?**

After the merging of some branches, I’m happy to release [TeamFiltration V3.5.0](https://github.com/Flangvik/TeamFiltration/releases/tag/v3.5.0). Among many minor and major improvements, this version changes how TeamFiltration utilizes FireProx instances.

## **TeamFiltration + FireProx = <3**

TeamFiltration no longer requires you to generate and store a pre-created list of [FireProx](https://github.com/ustayready/fireprox) instances in the configuration file. Instead, TeamFiltration will create and remove FireProx instances automatically when performing tasks that require FireProx endpoints. For TeamFiltration to do so, you simply provide an AWS Access Key and AWS Secret Key within the configuration file.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure01.png)

If TeamFiltration was unable to remove a created FireProx instance automatically (say because of a software crash or forced stop), the database module can now be used to show and delete FireProx endpoints.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure02.png)

Figure 2 - FireProx Endpoint Management

TeamFiltration only allows you to delete FireProx instances that were given a specified ID, or instances that are stored in the database (This happens during FireProx creation).

P.S.: Be sure to restrict permissions on behalf of those generated AWS API keys to the API Gateway Administrator role

## **Don't Work; Please Fix**

The TeamFiltration configuration now allows you to specify a proxy URL that, when used with the argument '--debug', will forward all HTTP traffic through your defined proxy. This is useful when debugging problems or crashes and, hopefully, will make it easier for end-users to open issues with a higher level of detail.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure03.png)

Figure 3 - Debugging Using Burp

## **Teams Enumeration Mayhem**

Depending on the configuration of the target Tenant, the Teams enumeration method might return a large number of false positives/non-exi...