---
title: NTLM Relaying to HTTPS
url: https://blog.compass-security.com/2025/11/ntlm-relaying-to-https/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-26
fetch_date: 2025-11-27T03:12:58.633275
---

# NTLM Relaying to HTTPS

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [NTLM Relaying to HTTPS](https://blog.compass-security.com/2025/11/ntlm-relaying-to-https/ "NTLM Relaying to HTTPS")

[November 26, 2025](https://blog.compass-security.com/2025/11/ntlm-relaying-to-https/ "NTLM Relaying to HTTPS")
 /
[Sylvain Heiniger](https://blog.compass-security.com/author/sheinige/ "Posts by Sylvain Heiniger")
 /
[0 Comments](https://blog.compass-security.com/2025/11/ntlm-relaying-to-https/#respond)

NTLM is the legacy authentication protocol in Windows environment. In the past few years, I’ve had the opportunity to write on this blog about NTLM Relaying [to DCOM](https://blog.compass-security.com/2020/05/relaying-ntlm-authentication-over-rpc/) ([twice](https://blog.compass-security.com/2021/08/relaying-ntlm-authentication-over-rpc-again/)), [to AD CS](https://blog.compass-security.com/2022/11/relaying-to-ad-certificate-services-over-rpc/) (ESC11) and [to MSSQL](https://blog.compass-security.com/2023/10/relaying-ntlm-to-mssql/). Today I will look back on relaying to HTTPS and how the tooling improved.

## NTLM Relaying

I won’t delve into the details of NTLM and relaying here. For those interested, I can recommend the fairly recent and very detailed [blog post of Elad Shamir](https://posts.specterops.io/the-renaissance-of-ntlm-relay-attacks-everything-you-need-to-know-abfc3677c34e). What you need to know:

* Clients authenticate to servers using a three-way handshake
* A man-in-the-middle can intercept and relay these authentication message to impersonate the client to the server
* Client and server can protect themselves by enforcing message signing or Extended Protection for Authentication (EPA, channel or service binding)

## Relaying to HTTP

HTTP is a good candidate to relay to for two reasons:

1. it is used in critical services such as public key infrastructure ([AD CS ESC8](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf))
2. it does not support signing

### Schoolbook ESC8

If a certification authority exposes an enrollment endpoint over HTTP, it is trivial (e.g. using [certipy](https://github.com/ly4k/Certipy)) to relay any intercepted NTLM handshake and request a certificate in the name of the relayed user or computer (if it is allowed to enroll with a template having the right properties):

```
$ certipy-ad relay -target http://10.0.0.50
Certipy v5.0.0 - by Oliver Lyak (ly4k)

[*] Targeting https://10.0.0.50/certsrv/certfnsh.asp (ESC8)
[*] Listening on 0.0.0.0:445
[*] Requesting certificate for 'CORP\\Administrator' based on the template 'User'
[*] Certificate issued with request ID 1
[*] Retrieving certificate for request ID: 1
[*] Got certificate with UPN '[email protected]'
[*] Certificate object SID is 'S-1-5-21-...-500'
[*] Saving certificate and private key to 'administrator.pfx'
[*] Wrote certificate and private key to 'administrator.pfx'
[*] Exiting...
```

## HTTPS to the rescue

Once we started [reporting this vulnerability to our customers](https://www.compass-security.com/en/services/penetration-tests), many of them disabled the HTTP endpoint altogether on IIS. Great! But the story does not end here, because IIS by default until Windows Server 2022 (included) does not enforce Extended Protection for Authentication and is hence still vulnerable to relaying attacks.

However, to the best of my knowledge, relay to AD CS over HTTPS was not implemented back then in either impacket or certipy. That’s where my colleague Emanuel [came up](https://github.com/ly4k/Certipy/pull/203#issuecomment-2517656929) with the elegant solution of relaying to localhost and use socat to add the SSL layer to it:

```
sudo socat TCP-LISTEN:80,fork,reuseaddr ssl:adcs.example.com:443,verify=0
```

(this trick is also mentioned in a blog post of [Synacktiv](https://www.synacktiv.com/publications/dissecting-ntlm-epa-with-love-building-a-mitm-proxy))

### Identifying ESC8 on HTTPS

To be able to identify this vulnerability reliably, we [contributed to certipy](https://github.com/ly4k/Certipy/pull/254) to check for the presence of web enrollment endpoints on HTTPS **and** to verify if channel binding was enforced.

Since version 5 of certipy, this was rewritten to be more efficient ([this commit](https://github.com/ly4k/Certipy/pull/266/commits/015dcc29aae4a64f534cb0d1c45630627b75bc20)) and relaying to HTTPS is supported out of the box ([this commit](https://github.com/ly4k/Certipy/pull/266/commits/b54fd34d9cc2cb85c63106d0d4ba92ca2335a66e)) and can be as simple as:

```
$ certipy-ad relay -target https://10.0.0.50
```

## What’s next?

There is still much more to NTLM relay. As we were about to publish this blog article, the new tool by SpecterOps [RelayInformer](https://github.com/zyn3rgy/RelayInformer) was released. Their [blog post](https://specterops.io/blog/2025/11/25/less-praying-more-relaying-enumerating-epa-enforcement-for-mssql-and-https/) is a good place to learn more about EPA.

## Conclusion

Relaying to HTTP is powerful, to HTTPS as well without channel binding. There are other (Windows) services that use HTTP(S) (e.g. [NDES](https://medium.com/%40offsecdeer/abusing-adcs-ndes-for-privilege-escalation-e4d306c9ca97), [SCCM](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/attack-techniques/TAKEOVER/TAKEOVER-5/takeover-5_description.md), …). As always the following recommendations apply:

* Enforce **packet signing** and **Extended Protection for Authentication** everywhere
* Ensure the **least privilege** principle is apply in your Active Directory
* Stop using NTLM! (although relaying exists with other protocols as well)

[Penetration Test](https://blog.compass-security.com/category/penetration-test/)

[Active Directory](https://blog.compass-security.com/tag/active-directory/)[adcs](https://blog.compass-security.com/tag/adcs/)[https](https://blog.compass-security.com/tag/https/)[ntlm](https://blog.compass-security.com/tag/ntlm/)[relay](https://blog.compass-security.com/tag/relay/)[relaying](https://blog.compass-security.com/tag/relaying/)

[##### Previous post

bRPC-Web: A Burp Suite Extension for gRPC-Web](https://blog.compass-security.com/2025/10/brpc-web-a-burp-suite-extension-for-grpc-web/ "Previous post: bRPC-Web: A Burp Suite Extension for gRPC-Web")

### Leave a Reply [Cancel reply](/2025/11/ntlm-relaying-to-https/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

### Recent Posts

* [NTLM Relaying to HTTPS](https://blog.compass-security.com/2025/11/ntlm-relaying-to-https/)
* [bRPC-Web: A Burp Suite Extension for gRPC-Web](https://blog.compass-security.com/2025/10/brpc-web-a-burp-suite-extension-for-grpc-web/)
* [LockBit Breach: Insights From a Ransomware Group’s Internal Data](https://blog.compass-security.com/2025/10/lockbit-breach-insights-from-a-ransomware-groups-internal-data/)
* [Ensuring NIS2 Compliance: The Importance of Penetration Testing](https://blog.compass-security.com/2025/09/ensuring-nis2-compliance-the-importance-of-penetration-testing/)
* [Collaborator Everywhere v2](https://blog.compass-security.com/2025/09/collaborator-everywhere-v2/)

### Categories

Categories
Select Category
APT  (9)
Authentication  (18)
Bug Bounty  (6)
Entra ID  (3)
Evasion  (3)
Event  (34)
Exploiting  (18)
Forensic  (25)
Hacking-Lab  (18)
Hardening  (33)
Incident Response  (14)
Industrial Control Systems  (14)
Information Leakage  (7...