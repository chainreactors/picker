---
title: How I Found a GraphQL Endpoint Leaking Millions
url: https://infosecwriteups.com/how-i-found-a-graphql-endpoint-leaking-millions-5cbfd55d994e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-26
fetch_date: 2026-08-27T12:12:36.465059
---

# How I Found a GraphQL Endpoint Leaking Millions

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-graphql-endpoint-leaking-millions-5cbfd55d994e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-graphql-endpoint-leaking-millions-5cbfd55d994e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5cbfd55d994e---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5cbfd55d994e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[Data Leak Prevention](https://medium.com/tag/data-leak-prevention?source=post_page---header_tags--5cbfd55d994e---------------------------------------)

[GraphQL](https://medium.com/tag/graphql?source=post_page---header_tags--5cbfd55d994e---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--5cbfd55d994e---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page---header_tags--5cbfd55d994e---------------------------------------)

[Vulnerability Management](https://medium.com/tag/vulnerability-management?source=post_page---header_tags--5cbfd55d994e---------------------------------------)

# How I Found a GraphQL Endpoint Leaking Millions

[![Prateekpulastya](https://miro.medium.com/v2/resize:fill:64:64/1*I0wFxynbuCSzv-GsCga6iQ.jpeg)](https://prateekpulastya.medium.com/?source=post_page---byline--5cbfd55d994e---------------------------------------)

[Prateekpulastya](https://prateekpulastya.medium.com/?source=post_page---byline--5cbfd55d994e---------------------------------------)

4 min read

·

Apr 20, 2026

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D5cbfd55d994e&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-graphql-endpoint-leaking-millions-5cbfd55d994e&source=---header_actions--5cbfd55d994e---------------------post_audio_button------------------)

Share

> User Records Without Authentication

**Introduction**

This write-up covers a mass user enumeration vulnerability I discovered during a bug bounty engagement on a large e-commerce marketplace platform. The finding was confirmed valid by the security team, but closed as a duplicate — meaning another researcher had found and reported it before me. Duplicate or not, the methodology is worth documenting because this class of vulnerability is widespread and consistently underestimated.

**The Target**

The platform in question is a large consumer marketplace with tens of millions of registered users. I’ll refer to it as [Platform] throughout this write-up in accordance with the program’s disclosure policy. The tech stack — identified through response headers and JS bundle analysis — included a GraphQL API built on Python graphene with Relay cursor-based pagination, sitting behind Cloudflare.

### Reconnaissance Phase

**Subdomain Enumeration**

Standard subdomain enumeration surfaced an `api.[platform].com` endpoint. Hitting the root returned 404. Appending `/graphql/` returned a response — the endpoint was live.

**Introspection Check**

First thing I always check on any GraphQL endpoint:

```
```graphql
{ __schema { queryType { fields { name } } } }
```
```

Introspection was disabled. Expected on a production endpoint. This is where most people stop. I don’t.

**Field Enumeration via Error Messages**

GraphQL validation errors are verbose by design — the spec requires descriptive error messages to help developers. This works against defenders because it allows attackers to enumerate type and field names without introspection. Sending a query against a non-existent field:

```
```graphql
{ email }
```
```

Returns:

```
"Cannot query field 'email' on type 'Query'.
Did you mean 'users' or 'user'?"
```

That single error message handed me two field names: `users` and `user`. The GraphQL API itself told me what to query next.

**The Discovery**

I queried the `users` field with a minimal selection set:

```
```graphql
{ users(first: 1) { totalCount } }
```
```

Response:

```
```json
{
  "data": {
    "users": {
      "totalCount": 57106775
    }
  }
}
```
```

No authentication header. No session cookie. 57 million users returned on an unauthenticated request.

**Confirming Scope and Impact**

It’s Live Production Data: Eight days later, I ran the same query. The count had increased to 57,316,627 — a delta of 209,852 new accounts. This is not test data. This is the live production user database.

**Full Field Enumeration**

## Get Prateekpulastya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

Expanding the query to pull all available unauthenticated fields:

```
```graphql
{
  users(first: 50) {
    totalCount
    pageInfo { hasNextPage endCursor }
    edges {
      node {
        id
        username
        displayName
        createdAt
        isSeller
        followerCount
        followingCount
      }
    }
  }
}
```
```

Every field returned without authentication.

**No Rate Limiting**

Five consecutive requests. All returned HTTP 200 with full data. No throttling, no CAPTCHA, no block. Full database exportable at ~10 req/sec in approximately 32 hours.

**The isSeller Boolean**

This field is what elevates this beyond a simple enumeration issue. It trivially segments all merchant accounts from general users. Sellers on marketplace platforms handle payment information, shipping data, and customer communication. They are the highest-value targets for phishing on any marketplace. This query produces a complete seller list in one paginated export.

Press enter or click to view image in full size

![]()

Attackflow

**Why This Matters — The Technical Perspective**

*GraphQL Specific Risk:*

* REST APIs fail closed — if you don’t expose an endpoint, it doesn’t exist. GraphQL fails open — every field you add to your schema is potentially queryable unless you explicitly add authorization checks at the field resolver level.
* The `users` query was likely built for an internal admin interface or a public user directory feature. At some point, someone added it to the root query type without a resolver-level authentication check. Because GraphQL doesn’t have route-level auth middleware the way REST does, this goes unnoticed until someone queries it directly.

**Why This Matters — The Business Perspective**

For a marketplace platform, a complete export of all usernames, seller status, and accou...