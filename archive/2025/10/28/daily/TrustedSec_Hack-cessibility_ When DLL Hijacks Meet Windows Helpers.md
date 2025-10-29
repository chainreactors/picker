---
title: Hack-cessibility: When DLL Hijacks Meet Windows Helpers
url: https://trustedsec.com/blog/hack-cessibility-when-dll-hijacks-meet-windows-helpers
source: TrustedSec
date: 2025-10-28
fetch_date: 2025-10-29T03:15:49.568629
---

# Hack-cessibility: When DLL Hijacks Meet Windows Helpers

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
* [Hack-cessibility: When DLL Hijacks Meet Windows Helpers](https://trustedsec.com/blog/hack-cessibility-when-dll-hijacks-meet-windows-helpers)

October 28, 2025

# Hack-cessibility: When DLL Hijacks Meet Windows Helpers

Written by
Oddvar Moe

Threat Hunting
Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/Hack-cessibilityDLLHijacks_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1761073071&s=35474ada99b3c5b30b624bf1f8d86442)

Table of contents

* [Persistence as User](#User)
* [Persistence as System](#System)
* [Lateral Movement](#Lateral)
* [Bring Your Own Accessibility](#Accessibility)
* [Outro](#Outro)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#49763a3c2b232c2a3d740a212c2a226c7b79263c3d6c7b793d21203a6c7b79283b3d202a252c6c7b792f3b26246c7b791d3b3c3a3d2c2d1a2c2a6c7b786f282439722b262d307401282a22642a2c3a3a202b2025203d306c7a086c7b791e212c276c7b790d05056c7b79012023282a223a6c7b79042c2c3d6c7b791e20272d263e3a6c7b79012c25392c3b3a6c7a086c7b79213d3d393a6c7a086c7b0f6c7b0f3d3b3c3a3d2c2d3a2c2a672a26246c7b0f2b25262e6c7b0f21282a22642a2c3a3a202b2025203d30643e212c27642d252564212023282a223a64242c2c3d643e20272d263e3a64212c25392c3b3a "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhack-cessibility-when-dll-hijacks-meet-windows-helpers "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Hack-cessibility%3A%20When%20DLL%20Hijacks%20Meet%20Windows%20Helpers%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhack-cessibility-when-dll-hijacks-meet-windows-helpers "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhack-cessibility-when-dll-hijacks-meet-windows-helpers&mini=true "Share on LinkedIn")

In preparation for a talk, Jason Lang ([@curi0usJack](https://x.com/curi0usJack)) and I were doing at MCTTP about mining TTPs from [VX-underground](https://vx-underground.org/), we both ended up doing research based on ideas we got from reading all the different reports. For me, it started while reading about the various persistence techniques that are described in the various papers. One technique that caught my eye was the reference to Narrator.exe loading the MSTTSLocEnUS.dll upon execution. Having played a lot with Narrator in the past, I decided to take a closer look if this was still a thing or not. The techniques shown in this post requires local administrator access to the system you are manipulating.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/Hack-cessibility_Oddvar/Fig01_Moe_Hack-cessibility.png?w=320&q=90&auto=format&fit=max&dm=1761073353&s=4b3d69732bddd80eb7be2756993addad)

I found references to this technique from the almighty @Hexacorn going back all the way to 2013 (Wow). My mind thought that this must surely be fixed now since this was such a long time ago, well let’s explore this rabbit hole together.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/Hack-cessibility_Oddvar/Fig02_Moe_Hack-cessibility.png?w=320&q=90&auto=format&fit=max&dm=1761073354&s=f065856de0306c20d4acbda2bd4ec0b8)

First, I needed to verify if this was still the case or not, so I ran Narrator while having a procmon running at the same time. This revealed something interesting.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/Hack-cessibility_Oddvar/Fig03_Moe_Hack-cessibility.png?w=320&q=90&auto=format&fit=max&dm=1761073355&s=6c85f38b9d24e51f7dc3f6e238134745)

It still looks for a variant of the dll in a different path? That is strange. Instead of the old path of *%windir%\system32\speech\engine\tts\msttslocenus.dll* it now looks for *%windir%\system32\speech\_onecore\engines\tts\msttsloc\_onecoreenus.dll*. Of course, this made me wonder if I could create a dll, place it there, and get it executed or not. Turns out, that works great. Interestingly, you do not need to create a dll with exports or anything like that. It just executes whatever you have in the attach statement of the dll.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/Hack-cessibility_Oddvar/Fig04_Moe_Hack-cessibility.png?w=320&q=90&auto=format&fit=max&dm=1761240624&s=1868775508a3c885cf183ff6b5927899)

The only issue is when the dll is executed, the Narrator continues, so you will get the voice telling you everything you click on and that is not particularly useful in an attack scenario. I decided to brainstorm for a while and found out that I could write code inside the dll that would iden...