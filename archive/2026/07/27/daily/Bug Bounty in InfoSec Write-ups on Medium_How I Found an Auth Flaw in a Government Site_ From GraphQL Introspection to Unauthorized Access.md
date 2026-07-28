---
title: How I Found an Auth Flaw in a Government Site: From GraphQL Introspection to Unauthorized Access
url: https://infosecwriteups.com/how-i-found-an-auth-flaw-in-a-government-site-from-graphql-introspection-to-unauthorized-access-0c877cc3ee07?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-27
fetch_date: 2026-07-28T04:58:47.720236
---

# How I Found an Auth Flaw in a Government Site: From GraphQL Introspection to Unauthorized Access

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-auth-flaw-in-a-government-site-from-graphql-introspection-to-unauthorized-access-0c877cc3ee07&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-auth-flaw-in-a-government-site-from-graphql-introspection-to-unauthorized-access-0c877cc3ee07&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0c877cc3ee07---------------------------------------)

·

1. [Introduction](/?source=post_page-----0c877cc3ee07---------------------------------------#ef42 "Introduction")
2. [Recon](/?source=post_page-----0c877cc3ee07---------------------------------------#f656 "Recon")
3. [Step 1 — Is This Really GraphQL?](/?source=post_page-----0c877cc3ee07---------------------------------------#5bb6 "Step 1 — Is This Really GraphQL?")
4. [Step 2 — Checking for GraphQL Introspection](/?source=post_page-----0c877cc3ee07---------------------------------------#bab2 "Step 2 — Checking for GraphQL Introspection")
5. [Step 3 — Enumerating the Entire Schema](/?source=post_page-----0c877cc3ee07---------------------------------------#d4e6 "Step 3 — Enumerating the Entire Schema")
6. [Step 4 — Testing Authorization](/?source=post_page-----0c877cc3ee07---------------------------------------#259f "Step 4 — Testing Authorization")
7. [Step 5 — Looking Deeper](/?source=post_page-----0c877cc3ee07---------------------------------------#c26d "Step 5 — Looking Deeper")
8. [Step 6 — Success](/?source=post_page-----0c877cc3ee07---------------------------------------#6454 "Step 6 — Success")
9. [Why This Was Serious](/?source=post_page-----0c877cc3ee07---------------------------------------#1c89 "Why This Was Serious")
10. [Could I Have Gone Further?](/?source=post_page-----0c877cc3ee07---------------------------------------#6a75 "Could I Have Gone Further?")
11. [Root Cause](/?source=post_page-----0c877cc3ee07---------------------------------------#0cb8 "Root Cause")
12. [Acknowledgement and Appreciation from CERT-In](/?source=post_page-----0c877cc3ee07---------------------------------------#9bb7 "Acknowledgement and Appreciation from CERT-In")
13. [References](/?source=post_page-----0c877cc3ee07---------------------------------------#dd03 "References")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0c877cc3ee07---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Bug Bounty

Ethical Hacking

Infosec

GraphQL

# How I Found an Auth Flaw in a Government Site: From GraphQL Introspection to Unauthorized Access

[![Aruvasaga chithan A](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*IwxRVGkwkSBIe726)](https://aruvasagachithan.medium.com/?source=post_page---byline--0c877cc3ee07---------------------------------------)

[Aruvasaga chithan A](https://aruvasagachithan.medium.com/?source=post_page---byline--0c877cc3ee07---------------------------------------)

5 min read

·

5 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D0c877cc3ee07&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-auth-flaw-in-a-government-site-from-graphql-introspection-to-unauthorized-access-0c877cc3ee07&source=---header_actions--0c877cc3ee07---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

> ***Disclaimer:****This write-up describes a vulnerability that has been* ***responsibly disclosed and fixed*** *by the affected organization. All domains, object names, identifiers, and responses have been* ***redacted or modified*** *to prevent abuse while preserving the technical methodology.*

## Introduction

GraphQL has become increasingly popular because it allows clients to request exactly the data they need.

Unfortunately, many developers focus on building GraphQL APIs while overlooking one critical aspect:

***| Authorization.***

During a Vulnerability Disclosure Program (VDP), I came across a government web application that appeared perfectly normal.

At first, everything looked normal. There were no obvious vulnerabilities, exposed admin panels, JavaScript secrets, or verbose error messages. While exploring the application and monitoring requests in Burp Suite, I noticed an API endpoint that looked interesting. Curious to see how it worked, I decided to investigate it further.

That small observation eventually led to an **authentication/authorization flaw** exposing sensitive government data.

This is the story of how I found it.

## Recon

Whenever I test a web application, I first spend time understanding how it communicates with the backend.

While reviewing the application’s source code, I noticed that the **GraphQL version was disclosed**, indicating that the application was using GraphQL.

This prompted me to inspect the network traffic in Burp Suite, where I captured the following request:

```
GET /api/participants HTTP/1.1
Host: redacted.tn.gov.in
```

its looks normal request .

## Step 1 — Is This Really GraphQL?

Instead of relying on automated scanners, I modified the request into a POST request.

```
POST /api/participants HTTP/1.1
Host: redacted.gov
Content-Type: application/json
{
    "query":" query Test{ __typename }"
}
```

The server responded:

```
{
    "data":{
        "__typename":"Query"
    }
}
```

That confirmed it.

The endpoint was indeed processing GraphQL queries.

## Step 2 — Checking for GraphQL Introspection

One of the first things I check in GraphQL applications is whether **introspection** is enabled.

Developers often forget to disable it in production.

I sent a simplified introspection query.

```
POST /api/participants HTTP/1.1
Host: redacted.gov
Content-Type: application/json
{
    "query":"query IntrospectionQuery { __schema { types { name } } }"
}
```

Response:

```
{
    "data":{
        "__schema":{
            "types":[
                {
                    "name":"Query"
                },
                {
                    "name":"Mutation"
                },
                {
                    "name":"Candidate"
                },
                {
                    "name":"Department"
                },
                ...
            ]
        }
    }
}
```

Interesting.

The production server happily exposed its GraphQL schema.

Although GraphQL introspection alone is generally considered an **information disclosure** issue, it gives attackers an excellent roadmap of the backend.

## Step 3 — Enumerating the Entire Schema

Raw JSON quickly becomes difficult...