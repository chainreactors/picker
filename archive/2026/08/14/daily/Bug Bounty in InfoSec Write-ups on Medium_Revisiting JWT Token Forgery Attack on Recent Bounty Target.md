---
title: Revisiting JWT Token Forgery Attack on Recent Bounty Target
url: https://infosecwriteups.com/revisiting-jwt-token-forgery-attack-on-a-recent-bounty-target-bfe4a423f3df?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-14
fetch_date: 2026-08-15T02:47:43.493715
---

# Revisiting JWT Token Forgery Attack on Recent Bounty Target

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frevisiting-jwt-token-forgery-attack-on-a-recent-bounty-target-bfe4a423f3df&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frevisiting-jwt-token-forgery-attack-on-a-recent-bounty-target-bfe4a423f3df&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-bfe4a423f3df---------------------------------------)

·

1. [1. Introduction](/?source=post_page-----bfe4a423f3df---------------------------------------#9a0d "1. Introduction")
2. [2. The bug](/?source=post_page-----bfe4a423f3df---------------------------------------#ce9a "2. The bug")
   1. [What the token is doing](/?source=post_page-----bfe4a423f3df---------------------------------------#5e34 "What the token is doing")
   2. [The signature is not checked](/?source=post_page-----bfe4a423f3df---------------------------------------#494f "The signature is not checked")
   3. [The authorization check trusts the same forged token](/?source=post_page-----bfe4a423f3df---------------------------------------#2279 "The authorization check trusts the same forged token")
3. [3. Other forge techniques worth trying](/?source=post_page-----bfe4a423f3df---------------------------------------#f4ec "3. Other forge techniques worth trying")
   1. [Algorithm case and type variations](/?source=post_page-----bfe4a423f3df---------------------------------------#5bed "Algorithm case and type variations")
   2. [Signature stripping](/?source=post_page-----bfe4a423f3df---------------------------------------#300a "Signature stripping")
   3. [RS256-to-HS256 algorithm confusion](/?source=post_page-----bfe4a423f3df---------------------------------------#c340 "RS256-to-HS256 algorithm confusion")
   4. [Weak HS256 secrets](/?source=post_page-----bfe4a423f3df---------------------------------------#ceb5 "Weak HS256 secrets")
   5. [jkw header injection](/?source=post_page-----bfe4a423f3df---------------------------------------#a500 "jkw header injection")
   6. [jku, x5u, and x5c manipulation](/?source=post_page-----bfe4a423f3df---------------------------------------#b39b "jku, x5u, and x5c manipulation")
   7. [kid path traversal](/?source=post_page-----bfe4a423f3df---------------------------------------#8907 "kid path traversal")
   8. [kid injection](/?source=post_page-----bfe4a423f3df---------------------------------------#3422 "kid injection")
   9. [Cross-environment key reuse](/?source=post_page-----bfe4a423f3df---------------------------------------#8904 "Cross-environment key reuse")
4. [4. Defense](/?source=post_page-----bfe4a423f3df---------------------------------------#5735 "4. Defense")
5. [5. Closing Notes](/?source=post_page-----bfe4a423f3df---------------------------------------#2ced "5. Closing Notes")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-bfe4a423f3df---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Jwt Exploitation

Bug Bounty

Bug Bounty Tips

Bug Bounty Writeup

Token

# Revisiting JWT Token Forgery Attack on Recent Bounty Target

[![Alvin Ferdiansyah](https://miro.medium.com/v2/resize:fill:64:64/1*jCQW4Dcioim59s1E0JwOqQ@2x.jpeg)](https://alvinferd.medium.com/?source=post_page---byline--bfe4a423f3df---------------------------------------)

[Alvin Ferdiansyah](https://alvinferd.medium.com/?source=post_page---byline--bfe4a423f3df---------------------------------------)

9 min read

·

Aug 1, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dbfe4a423f3df&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Frevisiting-jwt-token-forgery-attack-on-a-recent-bounty-target-bfe4a423f3df&source=---header_actions--bfe4a423f3df---------------------post_audio_button------------------)

Share

> alg=none x Attacker-Controlled Object Check

## 1. Introduction

Almost every portal I test authenticates with a JWT, and the flow is always the same. You log in, the server signs a token stating who you are and what you can see, and every request after that carries the token instead of a session lookup. The server verifies the signature, trusts the claims, and serves the request.

The whole model rests on one step. **If the signature check is real, the claims are the server’s own words handed back to it. If the check is missing, the claims are just something the client typed.**

During a recent engagement I found a partner portal where that check was not there. I wrote a token by hand saying I was a valid user, sent it with an empty signature, and the API let me in. That on its own is an authentication bypass. Worse was the design sitting behind it. The endpoint decided which records I could read by reading a list of ids out of the token. Which I also wrote. One forged token per id, and the partner directory read out one record at a time, with no account and no session anywhere.

## 2. The bug

### What the token is doing

Every request to the directory carries a Bearer JWT. Before the route runs, a validation layer parses that token and pulls a user object out of the payload.

That object is the entire authorization context. It carries the caller’s id, a rights array, and the list of partners this caller may see:

```
  {"sub":"11",
   "user":{"id":"11",
           "rights":["directory.READ"],
           "partners":{"partner":[
             {"key":"portal","id":"11"}]}},
   "iss":"portal",
   "iat":1783183500,"exp":1793183499
```

Nothing is wrong with that on its own. It is ordinary stateless authorization: the token gets to be the source of truth because the server signed it, and reading permissions from it saves a database round trip per request.

All of it depends on the signature actually **being checked.**

### The signature is not checked

I started where I always start, with the plain request and no token at all:

```
  GET /api/partner?id=11

  HTTP 500
  {"Error":"Error during validation: "}
```

Press enter or click to view image in full size

![]()

Error without token

The server wants a token before it will reach the lookup, and it is willing to describe its own validation failures, which is become starting point because from here on every token I malform comes back with a hint about the why. So I built a token by hand.

> A JWT is three base64url segments joined by dots: **header, payload, signature**. The header names the algorithm that signed the token, and the spec allows that name to be the literal string none, meaning the token is unsigned. That is a legal construction, meant for tokens whose integrity is guarantee...