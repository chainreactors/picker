---
title: Dragging Secrets Out of Chrome: NTLM Hash Leaks via File URLs
url: https://trustedsec.com/blog/dragging-secrets-out-of-chrome-ntlm-hash-leaks-via-file-urls
source: TrustedSec
date: 2025-06-14
fetch_date: 2025-10-06T22:55:11.890072
---

# Dragging Secrets Out of Chrome: NTLM Hash Leaks via File URLs

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
* [Dragging Secrets Out of Chrome: NTLM Hash Leaks via File URLs](https://trustedsec.com/blog/dragging-secrets-out-of-chrome-ntlm-hash-leaks-via-file-urls)

June 13, 2025

# Dragging Secrets Out of Chrome: NTLM Hash Leaks via File URLs

Written by
Drew Kirkpatrick

Social Engineering
Application Security Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/DragonHash_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1749743780&s=f7705e45f16a2475bac4ab4de0053f46)

Table of contents

* [Capturing Hashes with DragonHash](#Capturing)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#be81cdcbdcd4dbddca83fdd6dbddd59b8c8ed1cbca9b8c8ecad6d7cd9b8c8edfcccad7ddd2db9b8c8ed8ccd1d39b8c8eeacccbcdcadbdaeddbdd9b8c8f98dfd3ce85dcd1dac783faccdfd9d9d7d0d99b8c8eeddbddccdbcacd9b8c8ef1cbca9b8c8ed1d89b8c8efdd6ccd1d3db9b8dff9b8c8ef0eaf2f39b8c8ef6dfcdd69b8c8ef2dbdfd5cd9b8c8ec8d7df9b8c8ef8d7d2db9b8c8eebecf2cd9b8dff9b8c8ed6cacacecd9b8dff9b8cf89b8cf8cacccbcdcadbdacddbdd90ddd1d39b8cf8dcd2d1d99b8cf8daccdfd9d9d7d0d993cddbddccdbcacd93d1cbca93d1d893ddd6ccd1d3db93d0cad2d393d6dfcdd693d2dbdfd5cd93c8d7df93d8d7d2db93cbccd2cd "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdragging-secrets-out-of-chrome-ntlm-hash-leaks-via-file-urls "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Dragging%20Secrets%20Out%20of%20Chrome%3A%20NTLM%20Hash%20Leaks%20via%20File%20URLs%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdragging-secrets-out-of-chrome-ntlm-hash-leaks-via-file-urls "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdragging-secrets-out-of-chrome-ntlm-hash-leaks-via-file-urls&mini=true "Share on LinkedIn")

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/DragonHash_Kirkpatrick/dragnhash.png?w=320&q=90&auto=format&fit=max&dm=1749744314&s=cf6665b02525b851a2b34a6b72e381a6)

Figure 1 - We take our work very seriously.

## Capturing Hashes with DragonHash

Chromium-based browsers have an odd feature set that allows extensive drag-and-drop capabilities in the browser. This feature is not only useful for “typing” inputs during a clickjacking attack [as shown in this blog,](https://trustedsec.com/blog/clickjacking-not-just-for-the-clicks) but also for making web applications feel like proper file handlers. You can drag files out of a web application and onto your desktop, for example.

A social engineer might find this feature useful for tricking users into copying a file onto the user’s computer, and that is certainly possible. You can have a web application prompt the user to, say, drag an image to the desktop, and when they release that image, you could, of course, copy that image file onto the desktop.

But that assumes you’re behaving yourself. It turns out you can write any file to the location the user releases the dragged element on. They may have dragged an image to the desktop, but when they release, you could write a binary file if you want. Sounds like a bad idea, but, okay, Chrome. Features.

Any hacker might start asking themselves, what happens if we start messing around with this for more than writing a file to disk? What if we start throwing in file URLs? Clearly, Chrome wouldn’t let that happen—right?

![](https://trusted-sec.files.svdcdn.com/production/images/Blog-assets/DragonHash_Kirkpatrick/fred-g-sanford-alright.gif?dm=1749741980)

Figure 2 - Sorta!

Because we know that if that hits Windows, Windows is going to do what it does—which is usually something terrible, like fling hashes around.

Let’s try out some JavaScript, shall we?

Assuming we have a web server hosting an image file, we can make a draggable image like so:

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/DragonHash_Kirkpatrick/draggable.png?w=320&q=90&auto=format&fit=max&dm=1749741977&s=d151b453d8f891d5506f59930a1c4be8)

Figure 3 - It looks so innocent.

What we want is for the draggable element to set the data to be a **DownloadURL**, but instead of giving it the content of the file we want to write, we’ll point to Responder.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/DragonHash_Kirkpatrick/cant-work.png?w=320&q=90&auto=format&fit=max&dm=1749742386&s=3de4bfb69fa19e30406ec5abb9192aab)

Figure 4 - This can't work, can it?

So, what happens when the user is tricked into dragging this image out of the web app and onto their Windows desktop?

![](https://trusted-sec.transforms.svdcdn.com/production/videos/Step1_Thu...