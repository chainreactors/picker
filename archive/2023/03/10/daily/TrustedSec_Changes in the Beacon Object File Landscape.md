---
title: Changes in the Beacon Object File Landscape
url: https://www.trustedsec.com/blog/changes-in-the-beacon-object-file-landscape/
source: TrustedSec
date: 2023-03-10
fetch_date: 2025-10-04T09:10:38.386691
---

# Changes in the Beacon Object File Landscape

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
* [Changes in the Beacon Object File Landscape](https://trustedsec.com/blog/changes-in-the-beacon-object-file-landscape)

March 09, 2023

# Changes in the Beacon Object File Landscape

Written by
Christopher Paschen

Research

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/ChangesInBeaconObjectFile_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695563959&s=c56a6e39837f057c458dd4dfcd61b278)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#dde2aea8bfb7b8bea9e09eb5b8beb6f8efedb2a8a9f8efeda9b5b4aef8efedbcafa9b4beb1b8f8efedbbafb2b0f8efed89afa8aea9b8b98eb8bef8efecfbbcb0ade6bfb2b9a4e09eb5bcb3bab8aef8efedb4b3f8efeda9b5b8f8efed9fb8bcbeb2b3f8efed92bfb7b8bea9f8efed9bb4b1b8f8efed91bcb3b9aebebcadb8f8ee9cf8efedb5a9a9adaef8ee9cf8ef9bf8ef9ba9afa8aea9b8b9aeb8bef3beb2b0f8ef9bbfb1b2baf8ef9bbeb5bcb3bab8aef0b4b3f0a9b5b8f0bfb8bcbeb2b3f0b2bfb7b8bea9f0bbb4b1b8f0b1bcb3b9aebebcadb8 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fchanges-in-the-beacon-object-file-landscape "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Changes%20in%20the%20Beacon%20Object%20File%20Landscape%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fchanges-in-the-beacon-object-file-landscape "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fchanges-in-the-beacon-object-file-landscape&mini=true "Share on LinkedIn")

Time flies when you’re having fun! Can you believe it has been over two (2) years since the release of beacon object files (BOFs)? BOFs were released June 25, 2020, according to the release notes for Cobalt Strike. At that time, I wrote about what made BOFs special in terms of Cobalt Strike, as well as some of the 'gotchas' that might be hit when coding against them. Over these last two (2) years, the landscape in which BOFs exist has significantly changed. I feel that now would be a good time to reflect on BOFs and to opine on why they have become so prevalent.

## BOF, Where Art Thou

In my opinion, BOFs are the manifestation of the closest thing to a native language plugin framework for implants that will exist. BOFs were preceded by C# assemblies, which were used to implement functionality once before using it in multiple locations. C# assemblies were predated by reflective DLLs. Each of these technologies sought to develop a technique once, and then use a variety of methods to deploy it.

A BOF is special, in that it greatly reduces the amount of data that needs to be sent to execute a given technique. This is because we only need to send the object file for our given task and nothing else. This differs from the previously mentioned techniques that would send entire executables, along with all the executables' dependencies and initialization code.

A BOF is particularly special because some program is already running on the target computer. That program is what loads and executes the object file. Said program is not blind to what is happening, as was the case in C# assemblies and reflective DLLs. Rather, the program is intimately involved in the loading and linking of the object code. This presents an opportunity, in that the object file can now define and use functions that that loader (typically an implant) has implemented via internal functions. Now, we can not only execute a short burst of custom code but also provide custom functions to do things like pass messages back to an operator.

To date, BOFs have been adopted by several projects. In case you missed it, Kevin Haubris of TrustedSec posted both a Windows BOF runner and a POSIX BOF runner under the projects [COFFLoader](https://github.com/trustedsec/COFFLoader) and [ELFLoader](https://github.com/trustedsec/ELFLoader), respectively. To back up my claim, you can now see BOFs used in:

* [Sliver](https://github.com/BishopFox/sliver)
* [Meterpreter](https://docs.metasploit.com/docs/using-metasploit/advanced/meterpreter/meterpreter-executebof-command.html)
* [Nighthawk](https://www.mdsec.co.uk/2022/05/nighthawk-0-2-catch-us-if-you-can/)
* [Brutal Ratel](https://bruteratel.com/tabs/badger/commands/coffexec/)
* [Havoc](https://github.com/HavocFramework/Modules/blob/main/SituationalAwareness/SituationalAwareness.py)

…and probably others, but my point is made.

A few frameworks attempt to extend or replace the implant-provided functionality beyond what was originally released with Cobalt Strike. This is primarily seen in Brute Ratel’s documentation. This gives an advantage of greater customization, while having a disadvantage o...