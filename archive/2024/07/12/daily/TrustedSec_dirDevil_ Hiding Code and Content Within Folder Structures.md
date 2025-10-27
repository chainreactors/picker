---
title: dirDevil: Hiding Code and Content Within Folder Structures
url: https://trustedsec.com/blog/dirdevil-hiding-code-and-content-within-folder-structures
source: TrustedSec
date: 2024-07-12
fetch_date: 2025-10-06T17:45:05.616155
---

# dirDevil: Hiding Code and Content Within Folder Structures

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
* [dirDevil: Hiding Code and Content Within Folder Structures](https://trustedsec.com/blog/dirdevil-hiding-code-and-content-within-folder-structures)

July 11, 2024

# dirDevil: Hiding Code and Content Within Folder Structures

Written by
@ nyxgeek

Red Team Adversarial Attack Simulation

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/DirDevilHidingData_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1718286664&s=4da951ef589b9c4198a58b7fb235d598)

Table of contents

* [Fileless Data Storage](#Data)
* [Planning](#Planning)
* [Encoding](#Encoding)
* [DECODING](#Decoding)
* [Conclusion - Pros and Cons](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#e7d89492858d828493daa48f82848cc2d5d7889293c2d5d7938f8e94c2d5d78695938e848b82c2d5d78195888ac2d5d7b3959294938283b48284c2d5d6c1868a97dc8588839eda838e95a382918e8bc2d4a6c2d5d7af8e838e8980c2d5d7a4888382c2d5d7868983c2d5d7a4888993828993c2d5d7b08e938f8e89c2d5d7a1888b838295c2d5d7b4939592849392958294c2d4a6c2d5d78f93939794c2d4a6c2d5a1c2d5a193959294938283948284c984888ac2d5a1858b8880c2d5a1838e958382918e8bca8f8e838e8980ca84888382ca868983ca84888993828993ca908e938f8e89ca81888b838295ca94939592849392958294 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdirdevil-hiding-code-and-content-within-folder-structures "Share on Facebook")
* [Share on X](http://twitter.com/share?text=dirDevil%3A%20Hiding%20Code%20and%20Content%20Within%20Folder%20Structures%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdirdevil-hiding-code-and-content-within-folder-structures "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdirdevil-hiding-code-and-content-within-folder-structures&mini=true "Share on LinkedIn")

Welcome back to another round of "Hiding in Plain Sight," exploring weird places to stash data or payloads. In our last edition, we explored an easy method of encoding a payload into RGB values of a PNG file and hosting it in public places. ([imgDevil Github](https://github.com/nyxgeek/imgdevil))

Today, we are going to experiment with a method for hiding data—a "fileless" storage solution, in a sense.

If you just wanna see how it all ends, you can skip to the **TL;DR** at the end of this post. If you're curious about how we might go about this, read on!

## Fileless Data Storage

Anti-virus (AV) software examines files. Files can be malicious. Files are what store data. And so, AV software examines files. (Yes, AV can also monitor processes/behavior but stick with me here…)

Similarly, when Data Loss Prevention (DLP) software tries to detect the presence of PII or other sensitive data, it checks the contents of files. Files are where data is stored.

I get it—it's no surprise that software examines **files**. But what about **folders**? Not files that are in folders, but the folders themselves. The containers that are used to hold other containers or files. Does anything examine folders? What is there even to examine?

Would a bunch of empty folders with GUIDs as their name set off any AV or DLP solution?

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/dirDevil_nyxgeek/New-images/Fig1-2_nyx.png?w=320&q=90&auto=format&fit=max&dm=1720619946&s=782c2bb205c08c7d4a3ffed4e8875ec4)

If you were to scan these folders with an AV, would they even find anything to scan? 0 files. 220 folders.

![](https://trusted-sec.files.svdcdn.com/production/images/Blog-assets/dirDevil_nyxgeek/New-images/travolta.gif?dm=1720552060)

What if an admin were to notice folders like this under C:\temp\ or within a user's AppData folder? Would they look twice? Or would they see it and guess it belongs to some back-end system or application something-or-other and ignore it?

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/dirDevil_nyxgeek/New-images/image005.png?w=320&q=90&auto=format&fit=max&dm=1720619947&s=d14544c701678787c5176970f82b9667)

While folders don't store data in the traditional sense of a file\*, they quite readily store data in the form of folder names. After all, folder names are strings. And there's structure to this data. Folders exist in relation to each other hierarchically. You can have subfolders or parent (super) folders. These folder names and their relationships are stored someplace, even if they don't appear to take up space on disk.

*\* Alright, you might be screaming at your monitor at this point, "What about Alternate Data Streams!?" And you're right, you CAN store actual data in a fold...