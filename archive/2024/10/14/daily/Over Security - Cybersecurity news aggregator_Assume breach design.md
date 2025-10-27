---
title: Assume breach design
url: https://www.adainese.it/blog/2024/10/12/assume-breach-design/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-14
fetch_date: 2025-10-06T18:48:28.669786
---

# Assume breach design

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Assume breach design

#### Table of contents

* [Policy Design](#policy-design)
* [A Technical Matter](#a-technical-matter)
* [The Purpose of the DMZ](#the-purpose-of-the-dmz)
* [Defense in Depth](#defense-in-depth)
* [Zero Trust Architecture](#zero-trust-architecture)
* [Assume Breach Design](#assume-breach-design)
* [Post Breach](#post-breach)
* [Conclusions](#conclusions)

#### Latest posts

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/10/05/creating-an-interface-in-strata-cloud-manager/)

[Creating an interface in Strata Cloud Manager](/blog/2025/10/05/creating-an-interface-in-strata-cloud-manager/)
October 05, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/10/01/circular-dependencies-with-ndo/)

[Circular Dependencies with NDO](/blog/2025/10/01/circular-dependencies-with-ndo/)
October 01, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)

[Modifying an object in Strata Cloud Manager](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)
September 28, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)

[From Single-Site to Multi-Site with NDO](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)
September 24, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)

[Retrieving firewall interfaces with Strata Cloud Manager](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)
September 21, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 160 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 124 posts

[![Category cover](/images/categories/ciso.webp)](/categories/ciso)

[CISO](/categories/ciso)
 23 posts

[![Category cover](/images/categories/personal-security.webp)](/categories/personal-security)

[Personal Security](/categories/personal-security)
 22 posts

[![Category cover](/images/categories/security.webp)](/categories/security)

[Security](/categories/security)
 20 posts

[![Category cover](/images/categories/notes.webp)](/categories/notes)

[Notes](/categories/notes)
 19 posts

[![Category cover](/images/categories/infrastructure.webp)](/categories/infrastructure)

[Infrastructure](/categories/infrastructure)
 12 posts

[![Category cover](/images/categories/ot-ics.webp)](/categories/ot-ics)

[OT/ICS](/categories/ot-ics)
 5 posts

[![Category cover](/images/categories/books.webp)](/categories/books)

[Books](/categories/books)
 3 posts

[![Category cover](/images/categories/unetlab.webp)](/categories/unetlab)

[UNetLab](/categories/unetlab)
 3 posts

[![Category cover](/images/categories/writeup.webp)](/categories/writeup)

[Write-up](/categories/writeup)
 3 posts

[![Category cover](/images/categories/osint.webp)](/categories/osint)

[OSInt](/categories/osint)
 2 posts

[![Category cover](/images/categories/life.webp)](/categories/life)

[My life](/categories/life)
 1 posts

## Assume breach design

Andrea Dainese

October 12, 2024

[CISO](/categories/ciso/ "All posts under CISO")

[![Post cover](/images/categories/ciso.webp)](/images/categories/ciso.webp)

There is much discussion around Zero Trust Architecture (ZTA), but it seems the concept of Assume Breach Design has yet to be formalized. Or, at least, a Google search does not yield results. The term *Assume Breach Paradigm* is used, and I want to apply it to infrastructure design. So, I am appropriating (in a manner of speaking) the term and explaining why changing the mindset could be beneficial.

As always, the idea stems from field experience, when I realize that infrastructure design, from a cybersecurity perspective, follows a traditional approach. In the 1990s and 2000s, it was common to implement a DMZ network, a server network, and sometimes a client network. Policies were designed based on application needs and were never formalized. This approach, still frequently used today, relies on the classic 3-tier architecture of web applications: clients, servers, and databases, which had to be implemented separately. From a security standpoint, this led to logically separating these components through a firewall.

What I see today is precisely the consequence of this: systems are separated based on an application logic, not a security logic. The result is that companies have security zones that separate application components (Internet, DMZ, client, server, OT, Guest), and policies derive from application needs, not security requirements.

A case in point: server networks typically contain the backend and databases for the entire company. If one is compromised, the whole network is at risk.

A second equally telling example: I imagine anyone who has implemented firewall policies based on an application request. The vast majority of firewall policies originate from application needs, and their impact is rarely evaluated because rejecting the request is not an option.

## Policy Design

The first attempt at a mindset shift was almost ten years ago. I was in a position to influence the network and security architecture of the company I was working for, and following the advice of an ISO27001 auditor, I formalized the interactions between different security zones.

The idea was to publish a manifesto so that everyone in the company would know the rules governing the firewalls.

Here are some examples:

* The server network cannot receive connections from the Internet;
* The DMZ network can access the server network only through HTTP/HTTPS protocols;
* Server and DMZ networks could only access the Internet on a specific list of addresses/protocols.

All rules were designed to reduce the risk of compromise or lateral movement. But there were some fundamental errors.

The first error (mine) was that the evaluation was conducted by me, and at the time, my experience was primarily in defensive security. A few years later, when I began working on offensive security as well, I realized that while the approach was correct, the assumptions were incomplete.

The second error (company-wide) was failing to give this work the importance it deserved. It was seen as an obstacle created by a paranoid technician rather than a document meant to design secure applications within the company.

Specifically, the 3-tier paradigm was converted to Client (Internet) - Reverse Proxy (DMZ) - Server. It goes without saying that a reverse proxy, without any functionality other than forwarding connections from the Internet to the internal network, has the sole consequence of exposing the internal network directly to the Internet. This should be obvious, but even today, I find several configurations like this.

The last consequence was that when I left that company, the manifesto was shelved and forgotten.

## A Technical Matter

Anyway, the experience helped me over the years to provide an approach to technical teams that needed to organize firewall policies. Shifting the focus from policy to the needs of the systems before deciding where to place them helps prevent problems rather than chasing them.

The formalization of policies never worked because it was seen by companies as a technical issue, not related to the business.

Particularly, the words a CEO said to me a few years ago were illuminating: cybersecurity is a technical problem, and thus it is entrusted to the CIO.

## The Purpose of the DMZ

Another factor that drove me to rethink the approach to defending companies is my frequent task of analyzing firewall policies to bring order and logic. Almost always, I find NAT rules that allow direct access from the Internet to internal systems. Often th...