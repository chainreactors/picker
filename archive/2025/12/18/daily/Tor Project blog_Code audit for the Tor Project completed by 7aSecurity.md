---
title: Code audit for the Tor Project completed by 7aSecurity
url: https://blog.torproject.org/code-audit-network-health-tools/
source: Tor Project blog
date: 2025-12-18
fetch_date: 2025-12-19T03:23:45.050342
---

# Code audit for the Tor Project completed by 7aSecurity

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Code audit for the Tor Project completed by 7aSecurity

by [gaba](/author/gaba)
| December 18, 2025

![](/code-audit-network-health-tools/lead.png)

For the past three years, the Tor Project has been working to improve the tools, resources, and protocols used to monitor the health of the Tor network. This work aims to strengthen the Tor network's resilience and resist relay attacks.

As part of this effort, in October 2025, [7aSecurity](https://7asecurity.com/) conducted a code audit of those tools.

The code audit focused on the following projects:

* [TagTor](https://gitlab.torproject.org/tpo/network-health/metrics/tagtor) is a Flask web app to display metrics about the Tor network and its nodes.
* [DescriptorParser](https://gitlab.torproject.org/tpo/network-health/metrics/descriptorParser) is a small, standalone Java app to import Tor network descriptors into a PostgreSQL DB and a VictoriaMetrics time series.
* [Margot](https://gitlab.torproject.org/tpo/network-health/margot) is a Rust command-line application using Arti that provides a series of commands for the network health team.
* [Exitmap](https://gitlab.torproject.org/tpo/network-health/exitmap-modules) is a fast and modular Python-based scanner for Tor exit relays.
* [Tor\_fusion](https://gitlab.torproject.org/tpo/network-health/metrics/tor_fusion) parses Tor network documents in the Rust programming language.
* [Simple Bandwidth Scanner](https://gitlab.torproject.org/tpo/network-health/sbws) is a Tor bandwidth scanner that generates bandwidth files to be used by directory authorities.
* [C Tor](https://gitlab.torproject.org/tpo/core/tor) protects your privacy on the internet by hiding the connection between your Internet address and the services you use. This software is the one that runs on each relay of the Tor network.
* [Arti](https://gitlab.torproject.org/tpo/core/arti) is the implementation of Tor in Rust. The code to be audited is the one that changed during this project.

The audit found six vulnerabilities and highlighted eleven hardening recommendations. All findings have been reviewed by the Tor Project, and remediation work is being tracked as part of our ongoing security and maintenance processes.

### Read the full audit report

For detailed findings and recommendations, please see [the complete audit report here](/code-audit-network-health-tools/TTP-code-audit-network-health-report.pdf)

* [reports](/category/reports)
* [network](/category/network)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/code-audit-network-health-tools/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/code-audit-network-health-tools/&text=7aSecurity%20conducted%20a%20comprehensive%20code%20audit%20for%20several%20tools%20we%20use%20to%20monitor%20the%20health%20of%20the%20Tor%20network.%20This%20blog%20post%20outlines%20key%20recommendations%20and%20links%20to%20the%20full%20report.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/code-audit-network-health-tools/&text=7aSecurity%20conducted%20a%20comprehensive%20code%20audit%20for%20several%20tools%20we%20use%20to%20monitor%20the%20health%20of%20the%20Tor%20network.%20This%20blog%20post%20outlines%20key%20recommendations%20and%20links%20to%20the%20full%20report.)
[Bluesky](https://bsky.app/intent/compose?text=7aSecurity%20conducted%20a%20comprehensive%20code%20audit%20for%20several%20tools%20we%20use%20to%20monitor%20the%20health%20of%20the%20Tor%20network.%20This%20blog%20post%20outlines%20key%20recommendations%20and%20links%20to%20the%20full%20report.%0Ahttps%3A//blog.torproject.org/code-audit-network-health-tools/)

## Comments

We encourage respectful, on-topic comments. Comments that violate our
[Code of Conduct](https://community.torproject.org/policies/code_of_conduct)
will be deleted. Off-topic comments may be deleted at the discretion of
the moderators. Please do not comment as a way to receive support or to
report bugs on a post unrelated to a release. If you are looking for
support, please see our [FAQ](https://support.torproject.org/),
[user support forum](https://forum.torproject.org/) or ways to
[get in touch with us](https://www.torproject.org/contact).

Join the discussion on the [Tor Project forum](https://forum.torproject.org/c/news/11)!

## Recent Updates

## [Code audit for the Tor Project completed by 7aSecurity](/code-audit-network-health-tools/)

by [gaba](/author/gaba)
| December 18, 2025

[7aSecurity](https://7asecurity.com/) conducted a comprehensive code audit for several tools we use to monitor the health of the Tor network. This blog post outlines key recommendations and links to the full report.

## [Advancing digital rights in 2026 will take all of us](/advancing-digital-rights-in-2026/)

by [isabela](/author/isabela)
| December 17, 2025

Human rights are upheld by people, communities, and technologies that adapt to a changing world. Here's what that looks like for Tor as we head into the next year.

## [New Alpha Release: Tor Browser 16.0a1](/new-alpha-release-tor-browser-160a1/)

by [ma1](/author/ma1)
| December 16, 2025

Tor Browser 16.0a1 is now available from the Tor Browser download page and also from our distribution directory.

### Download Tor Browser

Download Tor Browser to experience real private browsing without tracking, surveillance, or censorship.

[Download Tor Browser](https://www.torproject.org/download/)

### Subscribe to our Newsletter

Get monthly updates and opportunities from the Tor Project:

[Sign up](https://newsletter.torproject.org/)

####

####

####

####

####

####

####

####

Trademark, copyright notices, and rules for use by third parties can be found in our [FAQ](https://www.torproject.org/about/trademark/).