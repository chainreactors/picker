---
title: Advanced OAuth Secrets Leads To Account Takeover(ATO)
url: https://infosecwriteups.com/advanced-oauth-secrets-leads-to-account-takeover-ato-42ff288a7763?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-21
fetch_date: 2025-10-02T20:28:38.638832
---

# Advanced OAuth Secrets Leads To Account Takeover(ATO)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F42ff288a7763&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fadvanced-oauth-secrets-leads-to-account-takeover-ato-42ff288a7763&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fadvanced-oauth-secrets-leads-to-account-takeover-ato-42ff288a7763&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-42ff288a7763---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-42ff288a7763---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Advanced OAuth Secrets Lead To Account Takeover(ATO)🔥

## Advanced Oauth secrets Leads To Bugs Critical With ScenarioS Lead To Account Takeover(ATO) , CSRF , Open Redirect

[![Mado](https://miro.medium.com/v2/resize:fill:64:64/1*sG60faGcA69B4sDGL06HVg.png)](https://medium.com/%400xMado-1Tap?source=post_page---byline--42ff288a7763---------------------------------------)

[Mado](https://medium.com/%400xMado-1Tap?source=post_page---byline--42ff288a7763---------------------------------------)

7 min read

·

Sep 18, 2025

--

3

Listen

Share

Press enter or click to view image in full size

![]()

**الحمد لله والصلاة والسلام على رسول الله وعلى آله وصحبه أما بعد**

***Hello HackerS***

### I’m Mohamed also known as Mado, a dedicated Web Application Penteration Tester and bug hunter

> **NOTE: The Write Up is Technical and hunting and The Write up Focus on OAuth And common Bugs From low to Critical Get Your Coffe and Lets go If You Liked The Write up Dont Forget 50 Clapped And Thank you**

## OAuth Basics: What It Is and Why It Matters

OAuth is a framework for delegated access that lets third-party apps act on a user behalf without sharing passwords OAuth 1.0 used signatures, while OAuth 2.0 simplifies the flow by relying on TLS and bearer tokens

OAuth 2.0 specifically allows login to a site (Client App) using an external provider like [ Google ,Apple ,Facebook ] (Authorization Server) without entering an email or password on the Client App It’s all about token exchange in the background

![]()

Like This

## Key components:

* `1` **Authorization Server**: The provider (e.g., Google) that authenticates the user and issues tokens
* `2` **Client App**: The target site you’re logging into via OAuth.
* `3` **Authorization Code**: A one-time code from the Authorization Server exchanged for an Access Token
* `4` **Access Token**: Grants access to protected resources often refreshed with a Refresh Token
* `5` **Resource Server**: Hosts the user’s data (e.g., Google’s API server).

**The flow is redirects from client side to server side and exchanges Here’s the high-level ASCII**

```
  +--------+                                           +---------------+
  |        |--(A)------- Authorization Grant --------->|               |
  |        |                                           |               |
  |        |<-(B)----------- Access Token -------------|               |
  |        |               & Refresh Token             |               |
  |        |                                           |               |
  |        |                            +----------+   |               |
  |        |--(C)---- Access Token ---->|          |   |               |
  |        |                            |          |   |               |
  |        |<-(D)- Protected Resource --| Resource |   | Authorization |
  | Client |                            |  Server  |   |     Server    |
  |        |--(E)---- Access Token ---->|          |   |               |
  |        |                            |          |   |               |
  |        |<-(F)- Invalid Token Error -|          |   |               |
  |        |                            +----------+   |               |
  |        |                                           |               |
  |        |--(G)----------- Refresh Token ----------->|               |
  |        |                                           |               |
  |        |<-(H)----------- Access Token -------------|               |
  +--------+           & Optional Refresh Token        +---------------+
```

## Steps in background :

`1`**User (you) initiates login on Client App via OAuth**

`2`**Client App redirects to Authorization Server (e.g.,** [**https://accounts.google.com/o/oauth2/v2/auth?client\_id=...&redirect\_uri=...&scope=...&response\_type=code)**](https://accounts.google.com/o/oauth2/v2/auth?client_id=...&redirect_uri=...&scope=...&response_type=code%29.)

`3`**Authorization Server authenticates user (if not logged in) and prompts for consent**

`4`**User grants access; Authorization Server redirects back to Client App’s redirect\_uri with code parameter (e.g.,** [**https://client-app.com/callback?code=AUTH\_CODE)**](https://client-app.com/callback?code=AUTH_CODE%29.)

`5`**Client App exchanges code for Access Token via backend request to Authorization Server (e.g., POST to /token endpoint with client\_secret)**

`6` **With Access Token Client App fetches user data from Resource Server and logs you in**

Press enter or click to view image in full size

![]()

The image From Descope

> **NOTE: From a pentester OR Bug hunter view this flow is ripe for abuse because the code is a golden ticket if leaked it’s often exchangeable for a session leading to ATO Misconfigurations amplify this as seen in bug bounties where OAuth flaws yield high payouts**

### Where The Secrets !!!!!

![]()

### The Secret in This Parameters:

## First Scenario CSRF

### `1` &state=

. The parameter which can be set in the first step can either be a cookie or stored in local storage

Press enter or click to view image in full size

![]()

He Authorization Server After Multiple Redirects Checks Whether The state Token Sent In The First Step Is The Same In The Third Step

Press enter or click to view image in full size

![]()

Image From ‪BugBountyReportsExplained

if We Send The same token in the state parameter to the victim The Attack Won’t Work Because The Authorization Server Verifies The state

Press enter or click to view image in full size

![]()

Without Parameter State

### **But wait many applications dont require the state parameter which allows the attack to succeed if the Authorization Server doesn’t verify it This Can Lead To CSRF**

Press enter or click to view image in full size

![]()

I WILL TAKE A REST

## Lets move on to the second scenario Open Redirect

### `2` &Redirect\_uri=

`. redirect_uri` parameter is crucial — it is the primar...