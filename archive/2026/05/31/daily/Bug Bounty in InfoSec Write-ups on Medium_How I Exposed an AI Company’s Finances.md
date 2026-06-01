---
title: How I Exposed an AI Company’s Finances
url: https://infosecwriteups.com/how-i-exposed-an-ai-companys-finances-d1e162a3b996?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-31
fetch_date: 2026-06-01T06:47:03.519982
---

# How I Exposed an AI Company’s Finances

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-exposed-an-ai-companys-finances-d1e162a3b996&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-exposed-an-ai-companys-finances-d1e162a3b996&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d1e162a3b996---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d1e162a3b996---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# How I Exposed an AI Company’s Finances

[![Ashish Bogati](https://miro.medium.com/v2/resize:fill:64:64/1*BxGitQT_ntoJHccRn6Vk9A.jpeg)](https://medium.com/%40ashishbogati098?source=post_page---byline--d1e162a3b996---------------------------------------)

[Ashish Bogati](https://medium.com/%40ashishbogati098?source=post_page---byline--d1e162a3b996---------------------------------------)

5 min read

·

May 12, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dd1e162a3b996&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-exposed-an-ai-companys-finances-d1e162a3b996&source=---header_actions--d1e162a3b996---------------------post_audio_button------------------)

Share

> ***Disclosure Notice:*** *This vulnerability was responsibly disclosed to the affected company. The issue has been fully remediated (RLS enforced, credentials rotated). All sensitive identifiers — company name, database URLs, API keys, and exact financial figures — have been redacted. This post is published with the company’s acknowledgement.*

![]()

[Odilon Redon’s Dark Symbolism](https://artwithsymbols.com/odilon-redons-dark-symbolism/)

## The Hunter’s Mindset: The Assumption Gap

In the rush to deploy cutting-edge AI, security often rests on a single point of failure: **configuration**. Developers frequently assume that because a Database-as-a-Service (DBaaS) like Supabase provides a “public” anon key, the data behind it is automatically shielded.

As a Threat Researcher, my mindset is different:

> “If a key is public, I must assume every table it can reach is public — until I prove otherwise.”

This is the story of how a routine frontend audit uncovered a critical **Material Non-Public Information (MNPI)** leak at a high-growth AI company.

## Step 1: Reconnaissance & JavaScript Static Analysis

The hunt began on the frontend of the target. Modern web applications — especially those using no-code builders like Webflow — rely on “glue code”: custom JavaScript bundles injected to handle dynamic data rendering, such as populating pricing pages.

I opened **Chrome DevTools** and navigated to the **Sources** tab. I identified a production npm package responsible for the company’s pricing page logic. Using the browser’s **Pretty Print** feature, I de-obfuscated the bundle and ran a regex search for `supabase`.

## Step 2: Credential Extraction

Within the bundle, I found the initialization of a Supabase client. While the `anon` key is intended to be client-side safe, its presence **shifts 100% of the security burden onto Row Level Security (RLS)**.

**The Discovery:**

```
import { createClient } from '@supabase/supabase-js';
```

```
// Initialization discovered during static analysis
const SUPABASE_URL = "https://[REDACTED].supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...[REDACTED]";
```

```
const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
```

## Step 3: The Logical Pivot — Investigative Enumeration

Having extracted a valid `anon` key, I had a working identity to present to the database. The question became: *what could I reach with it?*

**My hypothesis:** The engineering team likely enforced RLS on user-facing tables — the ones directly rendered in the UI. But internal “helper” tables — those used for caching pre-calculated metrics — are frequently an afterthought. Developers create them for performance reasons, never intending them to be API-accessible, and then forget to apply RLS during security reviews.

This is the **Assumption Gap** in practice.

**Why** `arr_cache` **specifically?** This required understanding how developers think, not just how code works. When a pricing page needs to display real-time business metrics (like growth rates), engineers rarely query raw transaction tables on every page load — that's expensive. Instead, they create a lightweight **cache table** that stores a pre-aggregated snapshot. The naming convention almost writes itself:

* `arr` → Annual Recurring Revenue, the north-star SaaS metric
* `_cache` → a pre-computed aggregate, refreshed on a schedule

This wasn’t a lucky guess. It was **researcher intuition built on understanding developer architecture patterns**. In Supabase’s PostgREST model, every table is automatically exposed as an API endpoint at `/rest/v1/<table_name>`. Finding a table name is finding an attack surface.

## Get Ashish Bogati’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

I moved from the browser entirely to the terminal — bypassing all frontend UI filters and React logic — to query the PostgREST API directly.

**The Researcher’s Logic:**

Evidence Inference The “Aha!” Moment Leaked `anon` key in JS bundle This key has a database role attached to it I have an identity — now test what doors it opens Hardcoded Supabase URL The database is directly exposed, not proxied I can bypass the frontend entirely with cURL Pricing page renders growth metrics A cache table almost certainly exists behind this Target `arr_cache` — the canonical naming pattern

**The Attack Command:**

```
curl -X GET "https://[REDACTED].supabase.co/rest/v1/arr_cache?select=*" \
  -H "apikey: [REDACTED_ANON_KEY]" \
  -H "Authorization: Bearer [REDACTED_ANON_KEY]"
```

## Step 4: The Impact

The server returned a `200 OK` — bypassing all authentication. The payload exposed live, highly sensitive business metrics.

**The Response (figures redacted):**

```
[
  {
    "id": 1,
    "current_arr": "[REDACTED — $XX.XM+]",
    "pct_growth_30d": "[REDACTED — XX%]",
    "updated_at": "2026-04-01T05:21:05.715Z"
  }
]
```

For any company — especially an AI firm — real-time ARR and growth rate data represents board-level, investor-sensitive information. This is a textbook **Broken Access Control (BAC)** vulnerability leading to direct disclosure of **Material Non-Public Information (MNPI)**.

> ***Triage Note:*** *The company’s security team...