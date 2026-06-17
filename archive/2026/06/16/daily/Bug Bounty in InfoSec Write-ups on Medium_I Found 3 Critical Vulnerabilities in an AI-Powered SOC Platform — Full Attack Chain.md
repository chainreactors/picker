---
title: I Found 3 Critical Vulnerabilities in an AI-Powered SOC Platform — Full Attack Chain
url: https://infosecwriteups.com/i-found-3-critical-vulnerabilities-in-an-ai-powered-soc-platform-full-attack-chain-e37a5733002e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-16
fetch_date: 2026-06-17T07:02:21.210611
---

# I Found 3 Critical Vulnerabilities in an AI-Powered SOC Platform — Full Attack Chain

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-found-3-critical-vulnerabilities-in-an-ai-powered-soc-platform-full-attack-chain-e37a5733002e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-found-3-critical-vulnerabilities-in-an-ai-powered-soc-platform-full-attack-chain-e37a5733002e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e37a5733002e---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e37a5733002e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Press enter or click to view image in full size

![]()

# I Compromised Every Tenant on an AI-Powered SOC Platform — Full Attack Chain

## **Author:** [Shikhali Jamalzade](https://medium.com/u/20557ba7487d?source=post_page---user_mention--e37a5733002e---------------------------------------) **GitHub:** [github.com/alisalive](https://github.com/alisalive) **LinkedIn:** [linkedin.com/in/camalzads](https://linkedin.com/in/camalzads)

[![Shikhali Jamalzade](https://miro.medium.com/v2/resize:fill:64:64/1*8HbuVZlZMtiPQCdSI_RI3w.png)](https://alisalive.medium.com/?source=post_page---byline--e37a5733002e---------------------------------------)

[Shikhali Jamalzade](https://alisalive.medium.com/?source=post_page---byline--e37a5733002e---------------------------------------)

13 min read

·

May 25, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3De37a5733002e&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-found-3-critical-vulnerabilities-in-an-ai-powered-soc-platform-full-attack-chain-e37a5733002e&source=---header_actions--e37a5733002e---------------------post_audio_button------------------)

Share

> ***Disclosure Notice:*** *This assessment was conducted with explicit written authorization from the platform’s development team. All sensitive details — including the target domain, company name, Supabase project identifiers, API keys, and credentials — have been redacted or anonymized in this write-up. This write-up is published strictly for educational purposes.*

## Background

A few weeks ago I was given authorization to perform a full black-box penetration test on an AI-powered Security Operations Center platform. The platform is a multi-tenant SaaS product — meaning dozens of enterprise organizations use the same system to manage their security alerts, incidents, phishing investigations, and threat intelligence. Each organization’s data is supposed to be completely isolated from the others.

The tech stack was modern: Next.js on the frontend, Supabase as the backend and authentication provider, deployed on Vercel. Clean, fast, well-designed on the surface.

What I found underneath was a chain of vulnerabilities that allowed me — starting from zero access — to create an admin account without any authorization, cross tenant boundaries at will, and access the complete security operations data of every organization on the platform. All of it. In under ten minutes.

This is the story of that assessment.

## Scope & Rules of Engagement

**Target:** AI-powered multi-tenant SOC platform (anonymized)
**Stack:** Next.js, Supabase/PostgreSQL, Vercel
**Assessment Type:** Black-Box Web Application Penetration Test **Authorization:** Written — platform development team
**Exclusions:** Stored XSS (to avoid leaving persistent artifacts)
**Tools:** Burp Suite Professional, Browser DevTools

## Phase 1: Reconnaissance

I started by browsing the application normally — no tools, just the browser. Within the first few minutes, the login page revealed something immediately interesting.

There was a **Quick Demo Login** button. Clicking it auto-filled the following credentials directly into the login form, visible to any unauthenticated visitor:

```
Email:    admin@[REDACTED].io
Password: Admin1234!
```

This alone was already a finding — hardcoded admin credentials served to the frontend and usable by anyone. I noted it and moved on. What came next was far more significant.

Opening the browser’s DevTools Network tab while navigating the authenticated dashboard, I noticed every request to the backend passed through a Supabase subdomain and included two consistent headers:

```
Apikey: sb_publishable_[REDACTED]
Authorization: Bearer [JWT]
```

The WebSocket connection for real-time updates also exposed the Supabase project reference and publishable API key in the connection URL. All of this was visible to any authenticated user — or anyone who knew where to look.

I noted the project reference, the API key, and the fact that the platform used Supabase Auth directly rather than a custom backend. This would matter later.

## Phase 2: Attack Surface Mapping

Supabase exposes a PostgREST REST API that maps directly to PostgreSQL tables. With the API key in hand, I began testing which endpoints were accessible.

Using Burp Suite Repeater, I queried the Supabase REST API directly with only the publishable key:

```
GET /rest/v1/alerts?select=*&limit=1 HTTP/2
Host: [REDACTED].supabase.co
Apikey: sb_publishable_[REDACTED]
Authorization: Bearer sb_publishable_[REDACTED]
```

Most tables returned `401 Unauthorized` or `403 Forbidden` — Row Level Security was enabled and working for the core data tables.

But the authentication endpoint was a different story.

I also opened the application’s localStorage in DevTools. The platform stored the authenticated user’s complete session state under a single key:

```
{
  "state": {
    "user": {
      "id": "0efd6cec-d8fd-4d1b-908e-9dfb97fa2220",
      "username": "admin",
      "email": "admin@[REDACTED].io",
      "role": "soc_analyst",
      "tenant_id": "t1",
      "is_active": true,
      "created_at": "2026-05-17T16:14:42.424987Z"
    },
    "isAuthenticated": true
  }
}
```

The `role` and `tenant_id` — two fields that determine what a user can see and which organization's data they access — were sitting in plain JSON in the browser. Readable and writable by anyone with access to the page.

That was the moment the shape of the attack became clear.

## Phase 3: Vulnerability Identification & Exploitation

## V-01 — Privilege Escalation via User Registration [CRITICAL]

**CWE-269 — Improper Privilege Management**

Supabase’s `/auth/v1/signup` endpoint accepts an optional `data` field for custom user metadata. The intent is to store profile information like display names or preferences. The vulnerability arises when this metadata is used directly for authorization de...