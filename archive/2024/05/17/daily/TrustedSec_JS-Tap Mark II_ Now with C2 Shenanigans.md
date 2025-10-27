---
title: JS-Tap Mark II: Now with C2 Shenanigans
url: https://trustedsec.com/blog/js-tap-mark-ii-now-with-c2-shenanigans
source: TrustedSec
date: 2024-05-17
fetch_date: 2025-10-06T17:17:04.794250
---

# JS-Tap Mark II: Now with C2 Shenanigans

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
* [JS-Tap Mark II: Now with C2 Shenanigans](https://trustedsec.com/blog/js-tap-mark-ii-now-with-c2-shenanigans)

May 16, 2024

# JS-Tap Mark II: Now with C2 Shenanigans

Written by
Drew Kirkpatrick

Application Security Assessment
Red Team Adversarial Attack Simulation
Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/JS-TAP_MarkII-C2Shenanigans_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1715621885&s=4a521893b6b3f86897fe7c2a650b8269)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#68571b1d0a020d0b1c552b000d0b034d5a58071d1c4d5a581c00011b4d5a58091a1c010b040d4d5a580e1a07054d5a583c1a1d1b1c0d0c3b0d0b4d5a594e090518530a070c1155223b453c09184d5a5825091a034d5a5821214d5b294d5a5826071f4d5a581f011c004d5a582b5a4d5a583b000d060906010f09061b4d5b294d5a58001c1c181b4d5b294d5a2e4d5a2e1c1a1d1b1c0d0c1b0d0b460b07054d5a2e0a04070f4d5a2e021b451c09184505091a034501014506071f451f011c00450b5a451b000d060906010f09061b "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fjs-tap-mark-ii-now-with-c2-shenanigans "Share on Facebook")
* [Share on X](http://twitter.com/share?text=JS-Tap%20Mark%20II%3A%20Now%20with%20C2%20Shenanigans%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fjs-tap-mark-ii-now-with-c2-shenanigans "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fjs-tap-mark-ii-now-with-c2-shenanigans&mini=true "Share on LinkedIn")

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/JSTap2_Drew/shenanigans.png?w=320&q=90&auto=format&fit=max&dm=1715633102&s=870030f03965dc33ce446a8397b11eb1)

JS-Tap is a tool intended to help red teams attack web applications. I recently blogged about the data collection capabilities in [JS-Tap version 1.0](https://trustedsec.com/blog/js-tap-weaponizing-javascript-for-red-teams), and data collection is still the primary purpose of JS-Tap. However, for version 2.0, I wanted to refine the usability and scalability of the application and add the ability to execute custom JavaScript payloads on JS-Tap clients.

The back-end JS-Tap server (Python/Flask) has been refactored to be compatible with Gunicorn, which allows for multicore/threaded serving of the JS-Tap server. This allows JS-Tap to handle many more clients simultaneously. Prior demos have only shown using JS-Tap in single-threaded developer mode, but this is not how you would host the server for an actual engagement.

To use JS-Tap on an engagement, you’ll want a multicore VPS with nginx installed. JS-Tap has a proxy mode configuration that runs it with plain HTTP and skips using the self-signed certificate. You should configure nginx to handle the TLS certificate, and instructions on how to do so with Let’s Encrypt can be found here:

<https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/>

To configure JS-Tap to work with nginx as a proxy, you’ll want to enable proxy mode. This not only starts JS-Tap with HTTP, but it also changes how it determines the IP address of clients connecting. In proxy mode, JS-Tap pulls the client IP address from the **X-Forwarded-For** header that nginx needs to set.

If you’re using single-threaded developer mode, at the top of the Python/Flask script is a **proxyMode** flag you can set:

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/JSTap2_Drew/figure1.png?w=320&q=90&auto=format&fit=max&dm=1715633078&s=38d17e98e943f3f446f153b0453201a2)

Figure 1 - JS-Tap Proxy Mode Configuration

If you’re setting up nginx, you’ll likely be running JS-Tap with Gunicorn, and the Gunicorn startup script (**jstapRun.sh**) has a separate configuration for proxy mode. At the top of the **jstapRun.sh** script, you can enable **PROXYMODE**:

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/JSTap2_Drew/figure2.png?w=320&q=90&auto=format&fit=max&dm=1715633079&s=8f0a698fa125a2716fa32ad5ff44f4ba)

Figure 2 - Gunicorn JS-Tap Proxy Mode Configuration

Inside the **jstapRun.sh** Gunicorn script, you’ll also want to tweak the number of workers and threads for the JS-Tap server. Workers are heavyweight forks, and you’ll want at least one (1) per CPU core in your server. An “N + 1” approach works well here. The threads are the number of serving threads per fork/worker. JS-Tap is very I/O-heavy, so having a decent number of threads per worker is a good approach. I would recommend at least four (4) threads.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/...