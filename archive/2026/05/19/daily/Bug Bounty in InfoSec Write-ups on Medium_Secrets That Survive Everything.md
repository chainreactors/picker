---
title: Secrets That Survive Everything
url: https://infosecwriteups.com/secrets-that-survive-everything-28b0c6aa1aa4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-19
fetch_date: 2026-05-20T06:03:25.169648
---

# Secrets That Survive Everything

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsecrets-that-survive-everything-28b0c6aa1aa4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsecrets-that-survive-everything-28b0c6aa1aa4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-28b0c6aa1aa4---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-28b0c6aa1aa4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Secrets That Survive Everything

[![Hemanth Gorijala](https://miro.medium.com/v2/resize:fill:64:64/1*PLQJpVI7VCsmnEHbb4hLyA.png)](https://medium.com/%40gorijala2k16?source=post_page---byline--28b0c6aa1aa4---------------------------------------)

[Hemanth Gorijala](https://medium.com/%40gorijala2k16?source=post_page---byline--28b0c6aa1aa4---------------------------------------)

17 min read

·

21 hours ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D28b0c6aa1aa4&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsecrets-that-survive-everything-28b0c6aa1aa4&source=---header_actions--28b0c6aa1aa4---------------------post_audio_button------------------)

Share

The Runtime Security Gap Left Unguarded

Press enter or click to view image in full size

![]()

*Years of shift-left investment, and a hardcoded key still survives to production.*

*By Hemanth Gorijala*

## The Finding That Changed How I Think About Secrets

During a security assessment, I found credentials sitting in a client-side JavaScript bundle, visible to every visitor who opened DevTools.

Real Azure credentials, and I started asking: *what could be done with them?*

That question led to a full account takeover chain built from four values sitting in a JavaScript file the application was already serving to every visitor. The affected organization had static secret scanning on pull requests and repository scanning across their codebase. None of it had flagged the credentials, because none of it scans what an application serves. Only what developers commit.

The same pattern appeared in a second application later in the same engagement, with a different codebase and a different team, and it ended in the same outcome.

## Responsible Disclosure

Both findings described in this post were identified and further investigated during authorized security assessments. Findings were reported immediately to the affected organization, remediated, and verified through retest before this publication. No user data was accessed beyond what was necessary to confirm exploitability.

The screenshots in this post come from **InsecureShield**, a controlled demo application built for security demonstrations. All credentials shown are synthetic and have been auth-tested as non-functional against their real providers. The patterns illustrated are reproduced from real engagements. The data shown is not.

## From Finding to Full Access on Azure AD + APIM

Azure API Management (APIM) is a gateway service that sits in front of backend APIs and enforces access through two separate credential types: Azure AD bearer tokens (JWTs issued by the identity provider) and APIM subscription keys (gateway-specific pass keys scoped to API products). Both are required to reach protected endpoints. A typical Azure-native single-page application authenticates a user via Azure AD, receives a token, and then calls the backend API through the APIM gateway sending both the bearer token and the subscription key on every request.

Press enter or click to view image in full size

![]()

**Azure AD + APIM Request Flow**

*Azure AD + APIM request flow. Two-credential gateway: Bearer token plus subscription key on every request.*

The exposed credentials were not just an API key. Sitting in the client-side JavaScript bundle of a production application, Azure AD authenticated, protected by APIM, serving real users, were four values.

Press enter or click to view image in full size

![]()

**The Azure credential set. Two of the four should never be in the browser.**

The AppID is legitimately public in OAuth2 public client flows. The AppKey is not. It is the client secret for a confidential client flow, designed for server-to-server authentication where the application code is not visible to end users. Client secrets are architecturally valid for server-side web applications. The problem is not that the secret exists. It is that it appeared in browser-accessible JavaScript, where it is visible to every visitor who opens developer tools.

Press enter or click to view image in full size

![]()

View-source: main.js secrets

*Build-pipeline-generated /js/main.js on a controlled demo target. APIM subscription key, internal service endpoints, and a service-account key all visible to any visitor.*

Together, these four values are everything needed to authenticate as the application itself. The tenant ID, required to call the token endpoint, was visible in the application’s login redirect URL, hardcoded alongside the other values in the same bundle. The tenant ID is a public identifier and is not counted among the four credential values, since its availability to any visitor is assumed.

I called the Azure AD token endpoint:

```
POST https://login.microsoftonline.com/{tenant_id}/oauth2/token

grant_type=client_credentials
client_id={AppID}
client_secret={AppKey}
resource={Resource}
```

It returned a fully authenticated Bearer access token. (The v1 endpoint format is shown. The v2 endpoint uses /oauth2/v2.0/token with a scope parameter in place of resource. Both remain in active use across enterprise Azure environments.)

I then read the JavaScript bundle carefully. Not just scanning for secrets, but reading it as a map of how the application was built. Buried in the minified code were API endpoint definitions. GET and POST endpoints with their complete schema structures showing exactly which parameters each endpoint expected. The frontend had documented its own backend.

Using the Bearer token and APIM subscription key together:

```
Authorization: Bearer {token}
Ocp-Apim-Subscription-Key: {SubscriptionKey}
```

I reconstructed and called the endpoints from the schemas. User profile data returned immediately. Then I found an account management endpoint, same token, same subscription key, same reconstructed schema. I reported the finding at this point and did not proceed further.

One APIM subscription key typically maps to a product containing multiple APIs.

```
SubscriptionKe...