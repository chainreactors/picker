---
title: Gobbling Up Forensic Analysis Data Using Velociraptor
url: https://trustedsec.com/blog/gobbling-up-forensic-analysis-data-using-velociraptor
source: TrustedSec
date: 2024-08-30
fetch_date: 2025-10-06T18:06:03.588987
---

# Gobbling Up Forensic Analysis Data Using Velociraptor

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
* [Gobbling Up Forensic Analysis Data Using Velociraptor](https://trustedsec.com/blog/gobbling-up-forensic-analysis-data-using-velociraptor)

August 29, 2024

# Gobbling Up Forensic Analysis Data Using Velociraptor

Written by
Thomas Millar

Incident Response & Forensics

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/GobblingUpForensic_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1724442108&s=79308d76073b616d21a445fb743078f5)

Table of contents

* [Preliminary](#Preliminary)
* [Into the Velociraptor GUI](#GUI)
* [Looking at the Results](#Results)
* [Closing](#Closing)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#0d327e786f67686e79304e65686e66283f3d627879283f3d7965647e283f3d6c7f79646e6168283f3d6b7f6260283f3d597f787e7968695e686e283f3c2b6c607d366f626974304a626f6f6164636a283f3d587d283f3d4b627f68637e646e283f3d4c636c61747e647e283f3d496c796c283f3d587e64636a283f3d5b6861626e647f6c7d79627f283e4c283f3d6579797d7e283e4c283f4b283f4b797f787e7968697e686e236e6260283f4b6f61626a283f4b6a626f6f6164636a20787d206b627f68637e646e206c636c61747e647e20696c796c20787e64636a207b6861626e647f6c7d79627f "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fgobbling-up-forensic-analysis-data-using-velociraptor "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Gobbling%20Up%20Forensic%20Analysis%20Data%20Using%20Velociraptor%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fgobbling-up-forensic-analysis-data-using-velociraptor "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fgobbling-up-forensic-analysis-data-using-velociraptor&mini=true "Share on LinkedIn")

Lately I have been working with [*Velociraptor*](https://github.com/Velocidex/velociraptor) for its endpoint and digital forensic capabilities and specifically spent time in many cases in the past two years with *Velociraptor* Offline Collector functions to gather forensic data in IR cases.

Sometimes there are situations that come up where you have host systems that you would like to collect IR-triage data from, but maybe one or more of the following factors are inhibiting real time-communication to a *Velociraptor* server.

* Maybe the client organization does not already have *Velociraptor* set up.
* The desired endpoint is separated from the very network that an organization has a *Velociraptor* server instance running on.
* Maybe it’s a laptop that is out on the road and not expected to come back onto the office network or connect back through VPN, and that data cannot get into the organization’s *Velociraptor* server.

If you still want to leverage *Velociraptor’s* collection and post-processing of artifacts, this blog will guide the reader through the steps needed to integrate an already-run ’Offline Collector’ artifact package into your *Velociraptor* server, and showcase artifacts that come from a macOS host for quick, preliminary triage. This is applicable to other operating systems, but recently I have been spending time on Linux and Apple macOS systems, so it’s a perfect opportunity to give those some time in the blogosphere light and have this discussion while featuring them.

## Preliminary

The Offline Collector results are packaged with a massive amount of data gathered from a prospective host and zipped up (as a *.ZIP* file) so they can be opened up and examined easily. The Offline Collector *.ZIP* file can also be presented into an existing *Velociraptor* server for ingestion, and that is what we want to go with today.

Keep in mind that when the *Velociraptor* runs through the collection, it will produce a *.ZIP* file, and when it does, it inherits the permission of who executed it. During this example, I am showcasing macOS systems, so user permissions really matter. When I look at my previously collected file, I observe having an ownership attribute only set to the user **root** (because I ran *Velociraptor* Offline Collector via *sudo*). So, it’s a must to check the *.ZIP* file and find out if it still is ‘owned by root’, and if so, make an ownership change before proceeding. I set the permissions with *chown* and move on to the *Velociraptor* UI.

## Into the Velociraptor GUI

Start by logging into your *Velociraptor* GUI server instance and use the credentials as an **Admin**. We want to see all options within the Admin GUI. Now, navigate over to Server Artifacts from the side bar and look for the *+* button near the top in the frame that appears. This is where you can begin a new collection.

![](http...