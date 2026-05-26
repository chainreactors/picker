---
title: Rejected but Rewarded — What a GraphQL Misconfiguration Taught Me About Bug Bounty Triage.
url: https://infosecwriteups.com/rejected-but-rewarded-what-a-graphql-misconfiguration-taught-me-about-bug-bounty-triage-a69a9f42e12c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-25
fetch_date: 2026-05-26T06:09:38.709154
---

# Rejected but Rewarded — What a GraphQL Misconfiguration Taught Me About Bug Bounty Triage.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frejected-but-rewarded-what-a-graphql-misconfiguration-taught-me-about-bug-bounty-triage-a69a9f42e12c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frejected-but-rewarded-what-a-graphql-misconfiguration-taught-me-about-bug-bounty-triage-a69a9f42e12c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a69a9f42e12c---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a69a9f42e12c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Rejected but Rewarded — What a GraphQL Misconfiguration Taught Me About Bug Bounty Triage.

[![kjulius](https://miro.medium.com/v2/resize:fill:64:64/1*pNjTItx95RQhfspL_MnSoA.jpeg)](https://kjulius.medium.com/?source=post_page---byline--a69a9f42e12c---------------------------------------)

[kjulius](https://kjulius.medium.com/?source=post_page---byline--a69a9f42e12c---------------------------------------)

7 min read

·

3 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Da69a9f42e12c&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Frejected-but-rewarded-what-a-graphql-misconfiguration-taught-me-about-bug-bounty-triage-a69a9f42e12c&source=---header_actions--a69a9f42e12c---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

By kjulius

*Responsible disclosure submitted. No mutations were executed. No systems were harmed. Finding classified as Informative. 50 CHF bonus awarded.*

## Introduction.

Not every bug bounty story ends with a payout and a hall of fame mention.

Some end with a rejection, a lesson, and — if you’re lucky — a small bonus that tells you the triage team saw something worth acknowledging even if they couldn’t justify a full reward.

This is one of those stories.

I found what I genuinely believed was a Critical severity finding on a major operational platform. I documented it carefully, scored it at CVSS 9.1, mapped it to four OWASP API Top 10 categories, wrote a full responsible disclosure report, and submitted it through a Swiss Bug Bounty platform.

The triage team came back and marked it **Rejected (Informative)**.

They were right. And here is exactly what happened, what I missed, and what every bug bounty hunter needs to understand about the difference between a misconfiguration and an exploitable vulnerability.

## How I Found It — URL Fuzzing.

It started with a wordlist and a tool most bug bounty hunters keep in their back pocket.

I was fuzzing subdomains and paths on `target.com` using a standard GraphQL-focused wordlist. The paths I was testing included:

```
/graphql
/graphiql
/graphiql?path=/graphql
/api/graphql
/v1/graphql
/playground
```

When I hit `subdomain.target.com` with `/graphiql?path=/graphql`, the server returned a clean **200 OK** and loaded a fully functional GraphiQL IDE — no login, no token, no challenge.

Press enter or click to view image in full size

![]()

PoC Image.

GraphiQL is a browser-based developer tool for writing and testing GraphQL queries. It is never supposed to be publicly accessible. Seeing it load on an internet-facing subdomain with zero authentication was the first signal that something was misconfigured.

## Building the Evidence — Step by Step.

### “Confirming Live Access”.

My first query was simple — confirm the endpoint is live and check what role I had:

```
{
  role
  lastUpdate
  globalMessage
}
```

Response:

```
{
  "data": {
    "role": "ANONYMOUS",
    "lastUpdate": "2026-05-19T00:00:01Z",
    "globalMessage": ""
  }
}
```

Press enter or click to view image in full size

![]()

PoC Image.

Three immediate observations:

* `role: ANONYMOUS` — no authentication, yet the API responds.
* `lastUpdate` showed the exact day’s date— that was a **live production system.**
* A global message system exists, currently empty.

### “Introspection Was On”.

I ran the standard introspection query to dump the schema:

```
{
  __schema {
    types {
      name
      kind
    }
  }
}
```

The full type system came back — including something that made me sit up straight:

A `Mutation` type. Write operations. Accessible anonymously.

Press enter or click to view image in full size

![]()

PoC Image.

### “The Mutations”.

I enumerated the mutation type:

```
{
  __schema {
    mutationType {
      fields {
        name
        description
        args {
        name
        type { name kind ofType { name kind } }
        }
      }
    }
  }
}
```

Three mutations came back:

`deleteGlobalMessage` :Deletes the global message shown to all users.

`updateGlobalMessage`:Updates the global message for all users.

## Get kjulius’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

`updateTrack` :Updates state and duration of a track.

Press enter or click to view image in full size

![]()

PoC Image.

On paper this looked devastating. An unauthenticated user could theoretically push fake messages to all visitors or close attractions remotely. I scored it CVSS 9.1, mapped it to OWASP API2, API5, and API8, and filed the report.

### “Live Operational Data”.

I also pulled real-time data from the `tracks` query — four operational attractions, all open, zero wait times, live timestamps. The system was clearly active and serving real visitors.

Press enter or click to view image in full size

![]()

PoC Image.

## The Rejection — And Why the Triage Team Was Right.

The triage team came back with this response:

Press enter or click to view image in full size

![]()

PoC Image.

They attached a screenshot showing the actual mutation response:

Press enter or click to view image in full size

![]()

PoC Image.

The mutations were **visible in the schema but protected server-side**. The GraphQL resolvers had authorization checks — the ANONYMOUS role simply could not execute them.

This is the key distinction I missed:

> ***Schema visibility ≠ exploitability.***

Just because a mutation appears in the GraphQL schema does not mean it is executable. The schema tells you what operations exist. The resolvers decide who can run them. In this case, the server correctly rejected anonymous mutation attempts.

## What I Got Wrong.

### 1. I Assumed Schema = Access.

The presence of `updateGlobalMessage` in the schema led me to assume it was accessible. I never actually trie...