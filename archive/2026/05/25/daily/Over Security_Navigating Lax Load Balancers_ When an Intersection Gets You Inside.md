---
title: Navigating Lax Load Balancers: When an Intersection Gets You Inside
url: https://blog.doyensec.com/2026/05/25/cloudsectidbits-elbaph-alb.html
source: Over Security
date: 2026-05-25
fetch_date: 2026-05-26T06:10:58.121253
---

# Navigating Lax Load Balancers: When an Intersection Gets You Inside

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2026
* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2026 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# Navigating Lax Load Balancers: When an Intersection Gets You Inside

25 May 2026 - Posted by Francesco Lacerenza, Mohamed Ouad

After our last episode on [Multi-SSO Cognito User Pools](https://blog.doyensec.com/2026/05/05/cloudsectidbits-masso-cognito-sso.html), we are back with another issue. This time, we are looking at one of those AWS components that is everywhere and rarely questioned deeply enough: the [Elastic Load Balancer](https://aws.amazon.com/elasticloadbalancing/).

![CloudsecTidbit](../../../public/images/cloudsectidbit-logo200.jpg)

## Tidbit No. 5 - Navigating Lax Load Balancers

### What is AWS ELB?

AWS Elastic Load Balancing (ELB) distributes traffic to backend services and serves as the entry point between the Internet and your applications.

It supports Layer 7 routing (Application Load Balancer - ALB) and Layer 4 routing (Network Load Balancer - NLB). It decides *where traffic goes* and *under which conditions*. ELB is commonly found fronting multiple applications, environments, and trust zones across the same infrastructure.

### Why It Matters

ELB is often the first public entry point before application backends, and in many AWS environments, it also becomes part of the access-control boundary. For ALBs, listener rules do more than route traffic: they can enforce authentication with `authenticate-oidc` or `authenticate-cognito`, restrict access with `source-ip` conditions, and decide which target group receives a request based on host, path, headers, or other request attributes.

The simplified flow below shows how a single request can be routed through different rules depending on priority and matching conditions:

![Rule Chain](../../../public/images/listener-rule-chain.png)

That makes the listener rule chain security-sensitive. A backend may appear protected when looking at a single rule, but still be reachable through another rule, another listener, another ALB, or a direct network path that bypasses the expected entry point.

Misconfigurations there could:

* Expose backend services that were expected to be reachable only through specific hostnames, paths, or upstream controls
* Allow an authentication bypass when an unauthenticated rule forwards to the same targets as an authenticated route
* Bypass IP-based gates when the same target group or backend instances are reachable through another routing path without the same `source-ip` restriction
* Bypass CloudFront-level checks when an Internet-facing origin ALB remains directly reachable

### Configuration vs. Real Exposure

Standard load balancer reviews usually focus on resource level hygiene: TLS policies, access logging, deletion protection, security groups, and whether a WAF is attached. These checks are useful, but they mostly describe how the load balancer is configured, without an offensive mindset.

They do not answer the important question: *what can an external request actually reach?*

![Configuration vs Real Exposure](../../../public/images/elbaph-config-vs-exposure.png)

What usually gets missed during load balancer audits:

* Routing logic issues that let traffic skip restrictive rules
* Backend targets that are directly reachable regardless of what the ALB listener enforces
* Real attack paths that are invisible to static config review

## The Bugs

The following are some of the routing and exposure misconfigurations we encounter most often during AWS load balancer reviews. They are not the only possible ELB issues, but they are representative of a broader class of bugs where the configured routing graph does not match the intended security boundary.

### 1. CloudFront / WAF Bypass via Direct ALB Access

[CloudFront](https://aws.amazon.com/cloudfront/) is often placed in front of an ALB to enforce WAF rules, geo-restrictions, caching policies, or rate limiting. In this setup, the ALB is expected to behave like a private origin: users should reach it only through CloudFront, not directly.

The problem appears when the origin ALB is still Internet-facing and its security group allows public inbound traffic. In that case, an attacker could send requests directly to the ALB DNS name, bypassing every control enforced at the CloudFront layer, including WAF rules attached to the distribution.

### 2. Rule Shadowing

ALB listener rules are evaluated in ascending-priority order. A rule with priority `10` is evaluated before one with priority `20`. If a broad rule (e.g., `path /*`) sits at priority `10` and a more restrictive rule (e.g., `path /admin*` with `authenticate-oidc`) sits at priority `20`, all traffic to `/admin` matches the broad rule first. The auth action never fires.

```
(priority)      (condition)             (action)

[10]            path /*               â forward  â tg-app          (no auth)
[20]            path /admin*          â authenticate-oidc â tg-app  (â never reached for /admin)
```

This is purely an ordering bug with a direct authentication bypass impact.

### 3. IP Gate Bypass via Alternate ALB

A common pattern is to restrict access to an Internal backend by placing a `source-ip` condition on the rule:

```
(priority)      (condition)             (action)

[10]            source-ip 1.2.3.4/32  â forward â tg-internal-api
[default]                             â 403
```

That works only if the protected backend is not reachable through any other path. The issue appears when the same target group, or the same backend instances, are also registered behind another load balancer with weaker conditions.

When that alternate route exists, the `source-ip` gate is real, but it only protects one path to the backend. The backend remains exposed through the weaker route, where the same IP restriction is not enforced.

That demonstrates why listener rules cannot be reviewed in isolation. The key question is not only âDoes this rule restrict access?â but âIs every path to these targets protected by a similar control?â

## Infrastructure is not just configuration. It defines how traffic actually flows, and misconfigurations create unintended paths

Typical CSPM and audit checklists report on attributes - TLS version, logging flag, and WAF presence - but none of that tells you whether an `/supposedly/protected/endpoint` path is actually protected end-to-end, whether a CloudFront-fronted ALB is directly reachable, or whether the same backend instance appears in both a gated and an ungated rule.

That requires understanding the routing graph, not just the resource properties.

## For Cloud Security Auditors

When reviewing an AWS account with ALBs, answer the following questions:

1. For each internet-facing ALB: are there any Target Group members that are also registered in a different ALB or listener with weaker (or no) conditions?
2. Is `routing.http.xff_header_processing.mode` set to `preserve`? If yes, does any downstream service trust `X-Forwarded-For` for access decisions?
3. Walk listener rules in priority order. For each restrictive rule (auth action, source-ip), is there a broader rule at a lower priority number that matches the same traffic first?
4. If a CloudFront distribution fronts an ALB, can you send HTTP or HTTPS directly to the ALB DNS and get a non-error response?
5. For source-ip gated rules: enumerate all paths to the gated targets - same ALB on a different port, a different ALB in the same VPC, an NLB in front of the same instances.

## For Developers
...