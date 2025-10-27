---
title: Hacked Tathva ’22 Biggest Techno-Management Fest in South India
url: https://infosecwriteups.com/hacked-tathva-22-biggest-techno-management-fest-in-south-india-6a95435c82e7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-10-24
fetch_date: 2025-10-03T20:43:28.836840
---

# Hacked Tathva ’22 Biggest Techno-Management Fest in South India

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6a95435c82e7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacked-tathva-22-biggest-techno-management-fest-in-south-india-6a95435c82e7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacked-tathva-22-biggest-techno-management-fest-in-south-india-6a95435c82e7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6a95435c82e7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6a95435c82e7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Hacked Tathva ’22 Biggest Techno-Management Fest in South India

[![7h3h4ckv157](https://miro.medium.com/v2/resize:fill:64:64/1*vBGOxG8iMbnWIrk7-RzBgg@2x.jpeg)](https://7h3h4ckv157.medium.com/?source=post_page---byline--6a95435c82e7---------------------------------------)

[7h3h4ckv157](https://7h3h4ckv157.medium.com/?source=post_page---byline--6a95435c82e7---------------------------------------)

3 min read

·

Oct 22, 2022

--

1

Listen

Share

- 7h3h4ckv157

Press enter or click to view image in full size

![]()

Hello, Infosec mates ッ✋✋,

In this write-up, I’m sharing a short story about how I hacked **Tathva → the biggest Techno-Management Fest in South India.**

**(Techno-management fest of NIT Calicut)**

* It has found itself a place in every engineering student’s calendar. One of the largest platforms in South India for technical ingenuity and managerial prowess

### About the Bug

* Before I bounce into the topic, let me apprise you about **IDOR**. There’s a plenty amount of blogs and instructional exercises now accessible around this topic. Still, I’ll furnish a concise note about the same.

### Insecure direct object references (IDOR)

* It’s a type of Access control (or authorization) vulnerability.
* **Access control:** Specifies whether the user is permitted to bring the action that they’re endeavouring to accomplish.
* **IDOR**: When an application uses user-supplied input to access objects directly. If the User-controlled parameter values are used to access resources or functions directly, it can be exploited.

For more:

> <https://portswigger.net/web-security/access-control>
>
> <https://portswigger.net/web-security/access-control/idor>

### IDOR in Tathva ‘22

My friend [**Ranjul Arumadi**](https://github.com/Ranjul-Arumadi) pointed out this event and propelled me to partake in the online Capture the Flag competition. After registration, I ensured that I’m able to edit my details at:

> <https://www.tathva.org/register?editprofile=true>

I’m curious about security. I Intercepted the request while editing the profile and saw some juicy stuff.

```
First requestOPTIONS /api/users/15862 HTTP/1.1
Host: api.tathva.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Access-Control-Request-Method: PUT
Access-Control-Request-Headers: authorization,content-type
Referer: https://www.tathva.org/
Origin: https://www.tathva.org
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Sec-Gpc: 1
Te: trailers
Connection: closeSecond requestPUT /api/users/15871 HTTP/1.1
Host: api.tathva.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Authorization:
Content-Length: 300
Origin: https://www.tathva.org
Referer: https://www.tathva.org/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Sec-Gpc: 1
Te: trailers
Connection: close{"id":15871,
"name":" ",
"gender":"male",
"college":" ",
"branch":" ",
"year":" ",
"state":" ",
"district":" ",
"phone":" "}
```

### Vulnerability confirmation

You can see the ***“/api/users/<ID>”*** at the top of the request.

This 5-digit <ID> value can be manually altered, and the attacker can rework the details of other users without their knowledge.

Eg:

> Suppose, the Attacker’s ID number = 15860.
> He/she/they can alter this value and set as any five digit random value. So, the details of the corresponding user’s will change without their knowledge.

### Impact

* **Integrity**: **High**

> **Integrity:** The ability to ensure that a system and its data has not suffered unauthorized modification. Integrity protection protects not only data, but also operating systems, applications and hardware from being altered by unauthorized individuals.

### Proof of Concept: Video

### Account-Takeover

After encountering this vulnerability, I checked the response of requests and discovered extra stuff.

```
The Response{"id":<ID>,
"username":<USER-NAME>",
"email":"<MAIL>",
"provider":"google",
"resetPasswordToken":null,
"confirmationToken":null,
"confirmed":true,
"blocked":false,
"name":"<NAME>",
"refCode":null,
"state":"<STATE>",
"district":"<DIS>",
"gender":"male",
"tathvaId":"T22-JSAVL",
"hostel":null,
"createdAt":"<DATE>",
"updatedAt":"<DATE>",
"phone":"<NUMBER>",
"college":"<COLLEGE>",
"year":"Year 4",
"branch":"any",
"registeredWorkshops":[],
"registeredEvents":[],
"registeredLectures":[],
"registeredCompetitions":[],
"bookedAccomodation":null,
"event_admin":null,
"event_volunteer":null,
"competition_admin":null,
"competition_volunteer":null,
"workshop_admin":null,
"workshop_volunteer":null,
"lecture_admin":null,
"lecture_volunteer":null}By simply editing"email":"<MAIL>" from the response itself, we can takeover the victim's account.Eg: change victim@gmail.com to attacker@gmail.comThe attacker can take control of the account through owned mails.
```

All the User accounts registerd on the domain becomes vulnerable.

Before getting too late, I contacted them via mail and through my connections.

* Reported on: Oct 20, 2022, 1:05 AM
* Fix Confirmation: Oct 22, 2022, 11:44 PM
* Bounty Reward: $0

Happy to secure!

Feel free to connect & share your views with me. You can find me here @[•7h3h4ckv157](https://twitter.com/7h3h4ckv157)

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Infosec](https://medium.com/tag/infosec?source=post_page-----6a95435c82e7---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty...