---
title: FastX in a Box: Using Docker to Find Where a Pre-Auth RCE Lived (and How It Died)
url: https://trustedsec.com/blog/fastx-in-a-box
source: TrustedSec
date: 2026-11-24
fetch_date: 2026-11-25T10:48:03.120934
---

# FastX in a Box: Using Docker to Find Where a Pre-Auth RCE Lived (and How It Died)

[Skip to Main Content](#main)

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
* [FastX in a Box: Using Docker to Find Where a Pre-Auth RCE Lived (and How It Died)](https://trustedsec.com/blog/fastx-in-a-box)

November 24, 2026

# FastX in a Box: Using Docker to Find Where a Pre-Auth RCE Lived (and How It Died)

Written by
Justin Bollinger

Vulnerability Assessment
Application Security Assessment
Research

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/Fastx32Shell_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1795466030&s=fee8c3374080f9e1aadcfc699a94adc3)

Table of contents

* [My First Attempt at a Lab](#First)
* [Finding a Build Nobody Sells Anymore](#Nobody)
* [Reading Packages Without Installing Them](#Reading)
* [A CentOS 7 Container per Build](#Build)
* [Things the Container Was Wrong About](#Wrong)
* [What the Matrix Says](#What)
* [Bugs the Mocks Missed](#Missed)
* [What Can Be Done?](#Can)
* [The Short Version](#Short)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#93ace0e6f1f9f6f0e7aed0fbf6f0f8b6a1a3fce6e7b6a1a3e7fbfae0b6a1a3f2e1e7faf0fff6b6a1a3f5e1fcfeb6a1a3c7e1e6e0e7f6f7c0f6f0b6a1a2b5f2fee3a8f1fcf7eaaed5f2e0e7cbb6a1a3fafdb6a1a3f2b6a1a3d1fcebb6a0d2b6a1a3c6e0fafdf4b6a1a3d7fcf0f8f6e1b6a1a3e7fcb6a1a3d5fafdf7b6a1a3c4fbf6e1f6b6a1a3f2b6a1a3c3e1f6bed2e6e7fbb6a1a3c1d0d6b6a1a3dffae5f6f7b6a1a3b6a1abf2fdf7b6a1a3dbfce4b6a1a3dae7b6a1a3d7faf6f7b6a1aab6a0d2b6a1a3fbe7e7e3e0b6a0d2b6a1d5b6a1d5e7e1e6e0e7f6f7e0f6f0bdf0fcfeb6a1d5f1fffcf4b6a1d5f5f2e0e7ebbefafdbef2bef1fceb "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Ffastx-in-a-box "Share on Facebook")
* [Share on X](https://twitter.com/share?text=FastX%20in%20a%20Box%3A%20Using%20Docker%20to%20Find%20Where%20a%20Pre-Auth%20RCE%20Lived%20%28and%20How%20It%20Died%29%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Ffastx-in-a-box "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Ffastx-in-a-box&mini=true "Share on LinkedIn")

This one started with a FastX 3.0.47 server on an engagement and a web terminal emulation that would run commands for anybody who asked. FastX is StarNet's remote desktop server, the kind of thing HPC shops and university labs stand up so people can get a Linux desktop through a browser. 3.0.47 is FastX 3.0 Build 47, released April 27, 2020.

Writing that up for the vendor should have been simple. Then I built a lab on current builds and couldn't reproduce it on either one.

This post is about how I settled that argument: tracking down builds that StarNet no longer serves, reading them without installing them, and then standing each one up in a throwaway CentOS 7 container until the version range stopped being a guess. In short, the RCE is real on every build from 3.0.41 through 3.1.27 but stopped working in 3.2.27 by accident, when the terminal feature broke; a CVE request for it is pending.

## My First Attempt at a Lab

The first lab was two Ubuntu 22.04 VMs on an isolated libvirt network with an nftables egress guard, running the two current builds, 3.2.60 and 3.3.71. A Docker container on the host ran the replay harness. Neither build was exploitable.

The reasons were good ones, too. Neither package ships node\_modules/gritty (the web terminal library) or node-pty, so nothing could spawn a terminal even in theory. The terminal code had also moved into user-link, a per-session Node process bound to loopback, and the code that starts it was broken:

```
function start(app) {
    let io = socketIo(app.server);                  // terminal/index.js:21
    io.on('connection', socket => { ... });
}
```

`terminal.start()` is handed the Express app and reads `.server` off it. Nothing in `user-link` ever assigns `app.server`, so `socketIo(undefined)` builds a Socket.IO server attached to nothing. It never mounts `/socket.io/` and never registers an upgrade listener.

That last part is visible from the outside, over one TLS connection, varying only the headers:

```
plain GET, polling              -> HTTP/1.1 404 Not Found [text/html]
plain GET, transport=websocket  -> HTTP/1.1 404 Not Found [text/html]
UPGRADE, socket.io path         -> CLOSED, no bytes
UPGRADE, / (root)               -> CLOSED, no bytes
UPGRADE, bogus path             -> CLOSED, no bytes
plain GET, bogus path           -> HTTP/1.1 404 Not Found [text/html]
```

A Node HTTP server with nothing handling an upgrade just destroys the socket without sending a response. Closed with zero bytes on every path while plain GETs answer normally is a reliable fingerprint for "no WebSocket handler is attached here," and it looks nothing like a firewall drop or a proxy rejection.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/fastX_Bollinger/Fig01_Bollinger_fastx.png?w=320&q=90&auto=for...