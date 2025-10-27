---
title: Off-Path firewall with Traffic Engineering
url: https://www.adainese.it/blog/2023/03/02/off-path-firewall-with-traffic-engineering/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-03
fetch_date: 2025-10-04T08:35:12.156630
---

# Off-Path firewall with Traffic Engineering

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Off-Path firewall with Traffic Engineering

#### Table of contents

* [Local Internet connection](#local-internet-connection)
* [Off-path firewall filtering](#off-path-firewall-filtering)
* [Conclusions](#conclusions)

#### Latest posts

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

[![Post cover](/images/vendors/eve-ng.webp)](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)

[EVE-NG Linux VM SSH troubleshooting](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)
September 20, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 159 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 123 posts

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

## Off-Path firewall with Traffic Engineering

Andrea Dainese

March 02, 2023

[Infrastructure](/categories/infrastructure/ "All posts under Infrastructure")

[![Post cover](/blog/2023/03/02/off-path-firewall-with-traffic-engineering/off-path-firewall-w-flows.webp)](/blog/2023/03/02/off-path-firewall-with-traffic-engineering/off-path-firewall-w-flows.webp)

I used to deploy a simple network architecture for two main reasons.

* They are easy to debug/troubleshoot
* Engineers who came after can easily understand and manage them.

With these rules in mind, I usually deploy in-line firewalls, meaning that traffic is routed through a firewall that is placed “in the path”:

[![Inline firewall (L3 diagram)](/blog/2023/03/02/off-path-firewall-with-traffic-engineering/inline-firewall.png)](/blog/2023/03/02/off-path-firewall-with-traffic-engineering/inline-firewall.png)

Sometimes things are complicated, and we need to deploy “off-path” firewalls, and traffic is partially routed through the firewall:

[![Off-path firewall (L3 diagram)](/blog/2023/03/02/off-path-firewall-with-traffic-engineering/off-path-firewall.png)](/blog/2023/03/02/off-path-firewall-with-traffic-engineering/off-path-firewall.png)

There are many reasons why we want to do so.

* We want to test a new firewall
* We do not have enough budget for a big firewall to manage the entire traffic.
* We must exclude some latency-sensitive traffic.

In 99% of the scenarios, an in-line firewall is fine; let us examine how to approach the remaining 1%.

## Local Internet connection

> Requisite #1: We need to use the local Internet connection if available and use the MPLS if not.

Solving this requisite is easy: we must implement a conditional static default route. The firewall is used only if the Internet connection through it is working.

Depending on the firewall model, we can use native features and dynamic routing to accomplish the configuration. However, for the sake of this post, we want to solve the requisite by acting on the L3 switch only.

Network engineers are used to implement an ICMP probe, reaching `8.8.8.8`, to test the Internet connection. I read even official documents suggesting that, but that’s a bad practice because [Google apply rate limits](https://groups.google.com/g/public-dns-discuss/c/p1o62SJElck "DNS Rate Limiting ICMP (8.8.8.8 and 8.8.4.4)"):

We want to implement two DNS probes using at least two different DNS OpenDNS servers.

```
ip sla 1
 dns www.cisco.com name-server 208.67.222.222 source-ip 192.168.1.1
 timeout 5000
 frequency 10
ip sla schedule 1 life forever start-time now
ip sla 2
 dns www.google.com name-server 208.67.220.220 source-ip 192.168.1.1
 timeout 5000
 frequency 10
ip sla schedule 2 life forever start-time now
track 1 ip sla 1 reachability
track 2 ip sla 2 reachability
```

DNS providers can rate limit requests with unusual record types, excessive duplicate queries, excessive DNS records, or those sent from malicious client IPs to add entropy to our nameserver requests. Because we use a 10 s frequency, we can assume that it is safe.

We also need to couple the probes above using the OR logical operator

```
track 3 list boolean or
 object 1
 object 2
 delay down 12 up 30
```

To avoid flapping, we introduced a delay before changing the state.

Finally, we configured the default static route associated with the probe.

```
ip route 0.0.0.0 0.0.0.0 192.168.1.254 track 3
```

[![Active and backup Internet path (L3 diagram)](/blog/2023/03/02/off-path-firewall-with-traffic-engineering/internet-traffic.png)](/blog/2023/03/02/off-path-firewall-with-traffic-engineering/internet-traffic.png)

With this configuration, traffic to the Internet is routed through the firewall if the Internet connection via the firewall itself is working. Otherwise, the default route from the MPLS is used.

Attention should be paid to convergence time, especially when the local Internet connection goes down.

## Off-path firewall filtering

> Requisite #2: We must selectively filter some network conversations. We cannot forward anything to the firewall because it does not have sufficient bandwidth or computational resources.

Solving this requirement requires PBR or Policy-Based Routing. We use PBR when we need to make an exception to the normal routing. We want to select, based on protocol, source/destination IP, and port, network flows to be routed through the firewall. The firewall is configured “on-a-stick,” meaning that a single interface is used to receive and transmit the allowed network traffic.

[![Off-path firewall with flows (L3 diagram)](/blog/2023/03/02/off-path-firewall-with-traffic-engineering/off-path-firewall-w-flows.png)](/blog/2023/03/02/off-path-firewall-with-traffic-engineering/off-path-firewall-w-flows.png)

We must define the network traffic to be filtered using an ACL.

```
ip access-list extended FILTERED
 ...