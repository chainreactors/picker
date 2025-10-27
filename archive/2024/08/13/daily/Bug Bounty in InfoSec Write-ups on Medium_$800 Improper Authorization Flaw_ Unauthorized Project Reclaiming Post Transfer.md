---
title: $800 Improper Authorization Flaw: Unauthorized Project Reclaiming Post Transfer
url: https://infosecwriteups.com/800-improper-authorization-flaw-unauthorized-project-reclaiming-post-transfer-15fe36976604?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-13
fetch_date: 2025-10-06T18:04:19.877761
---

# $800 Improper Authorization Flaw: Unauthorized Project Reclaiming Post Transfer

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F15fe36976604&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F800-improper-authorization-flaw-unauthorized-project-reclaiming-post-transfer-15fe36976604&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F800-improper-authorization-flaw-unauthorized-project-reclaiming-post-transfer-15fe36976604&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40a13h1)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-15fe36976604---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-15fe36976604---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# $800 Improper Authorization Flaw: Unauthorized Project Reclaiming Post Transfer

[![Abhi Sharma](https://miro.medium.com/v2/resize:fill:64:64/1*sBSRPckiQ7rHLIsqREevhw.png)](https://medium.com/%40a13h1?source=post_page---byline--15fe36976604---------------------------------------)

[Abhi Sharma](https://medium.com/%40a13h1?source=post_page---byline--15fe36976604---------------------------------------)

4 min read

·

Aug 10, 2024

--

5

Listen

Share

**Hi Everyone,** I’m excited to share my latest discovery of a vulnerability in ExamenTry (a pseudonym for confidentiality), which allows an attacker to reclaim a project even after it has been transferred to another user. This discovery earned me a bounty of $800.

Press enter or click to view image in full size

![]()

> **Understanding the Target: ExamenTry**

ExamenTry is a robust platform that provides error tracking and monitoring services, enabling developers to identify and resolve issues in their applications efficiently. It offers various features to manage and transfer projects between users, ensuring seamless collaboration. However, a critical flaw in the project transfer process was identified that compromises the permanence of these transfers.

> **The Flaw: Exploiting Project Transfer Vulnerability**

ExamenTry promises that project transfers are permanent and cannot be undone. However, a vulnerability in this process allows an attacker to reclaim control of a project even after it has been transferred to another user. By capturing and reusing specific API requests, an attacker can bypass the intended permanence of the project transfer, leading to unauthorized access and control.

> **Understanding the Bug Type: Improper Authorization**

This vulnerability is a classic example of **Improper Authorization**. Improper authorization occurs when an application fails to enforce permissions or restrictions correctly, allowing unauthorized actions to be performed. In this case, ExamenTry does not adequately verify the validity of previously authorized actions, leading to a critical security flaw.

**How It Works**:

1. **Authorization Over Time**: The attacker captures an API request used during the project transfer process.
2. **Reuse of Captured Requests**: Even after transferring the project back to the original owner, the attacker can reuse the captured request to regain control. The application fails to validate the context in which the request is reused.
3. **Exploiting Assumptions**: The platform assumes that once a project is transferred, it remains in control of the new owner, without considering the possibility of replaying authorized actions from the past.

## Steps to Reproduce

**Initial Setup**:

* Have two accounts: a victim account (Account A) and an attacker account (Account B)

**Transfer Project to Attacker**:

* As the victim (Account A), initiate a project transfer to the attacker (Account B).
* The attacker (Account B) accepts the project transfer and captures the `POST /api/0/accept-transfer/` request. Save this request for later use.

**Transfer Project Back to Victim**:

* After completing the work, the attacker (Account B) transfers the project back to the victim (Account A).
* The victim (Account A) accepts the project transfer, regaining control of the project.

**Exploit the Vulnerability**:

* The attacker (Account B) reuses the previously captured `POST /api/0/accept-transfer/` request to reclaim the project, despite the project being transferred back to the victim (Account A).

**Captured Request Details**:

```
POST /api/0/accept-transfer/ HTTP/2
Host: us.examentry.io
Cookie: __
Content-Length: 318
Sec-Ch-Ua: "Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
Content-Type: application/json
Accept: application/json; charset=utf-8
Baggage: sentry-trace_id=50e48675f4334fe087afd7cc6fa40f54,sentry-environment=prod,sentry-release=backend%4005084e4c0a03486d5239f31986eb52cdfce5ec6b,sentry-public_key=16427b2f210046b585ee51fd8a1ac54f,sentry-transaction=%2Faccept-transfer%2F,sentry-sample_rate=1.0,sentry-sampled=true
X-Csrftoken: AlTfGEYHxGBIFKsZ6KmRACng6SyhWdK5
Sentry-Trace: 50e48675f4334fe087afd7cc6fa40f54-b72f3657d91b5768-1
Sec-Ch-Ua-Platform: "macOS"
Origin: https://fefe-00.examentry.io
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://fefe-00.examentry.io/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en;q=0.9
Priority: u=1, i

{"data":"eyJhY3Rvcl9pZCI6Mjk3NDU3NSwiZnJvbV9vcmdhbml6YXRpb25faWQiOjQ1MDYyOTUzNjU2NjQ3NjgsInByb2plY3RfaWQiOjQ1MDcyNzYyNDA2ODMwMDgsInVzZXJfaWQiOjMyMjA0NDksInRyYW5zYWN0aW9uX2lkIjoiNjMzMzE5ZWE2NjNmNDdjYmI0MjY3ZGRmNjE4ZTBiZmIifToxczk2Tjk6MHBoMjFyUWVmbGxvVFZZSHc0RUdfQzdNUTBoLUpySnczWFFnZDNJM3lyYw","organization":"fefe-00"}
```

> **Impact: Unauthorized Access and Data Manipulation**

This vulnerability poses a significant risk as it allows an attacker to:

* **Regain Unauthorized Access**: The attacker can reclaim control of a project after transferring it, violating the expected permanence of the transfer.
* **Manipulate Project Data**: Once control is regained, the attacker can access and modify project data, leading to potential data corruption or misuse.
* **Breach Confidentiality**: Unauthorized access to a project can lead to the exposure of sensitive information, compromising the confidentiality of project data.

> **Response and Reward**

Upon discovering this vulnerability, I promptly reported it to the ExamenTry security team. The issue was triaged, and a bounty of $800 was awarded for identifying and reporting the flaw. ExamenTry’s security team implementing a fix to ensure that project transfers are truly permanent and irreversible.

![]()...