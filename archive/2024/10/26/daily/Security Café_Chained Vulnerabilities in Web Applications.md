---
title: Chained Vulnerabilities in Web Applications
url: https://securitycafe.ro/2024/10/25/chained-vulnerabilities-in-web-applications/
source: Security Café
date: 2024-10-26
fetch_date: 2025-10-06T18:52:39.552431
---

# Chained Vulnerabilities in Web Applications

[Skip to content](#content)

[Security Café](https://securitycafe.ro/)

Security Research and Services

* [Things we do on a daily basis](https://securitycafe.ro/security-services-for-business/)
  + [Red Team (DORA/TIBER) exercises](https://securitycafe.ro/security-services-for-business/dora-tiber-exercises/)
  + [Web Application Penetration Testing](https://securitycafe.ro/security-services-for-business/web-application-penetration-testing/)
  + [Mobile Application Penetration Testing](https://securitycafe.ro/security-services-for-business/mobile-application-penetration-testing/)
  + [Infrastructure Penetration Testing](https://securitycafe.ro/security-services-for-business/infrastructure-penetration-testing/)
  + [Vulnerability Assessment](https://securitycafe.ro/security-services-for-business/vulnerability-assessment/)
* [CVEs, Talks and Tools](https://securitycafe.ro/cves-talks-and-tools/)
* [Contact](https://securitycafe.ro/contact/)
* [About](https://securitycafe.ro/about/)

[![](https://securitycafe.ro/wp-content/uploads/2015/01/cropped-cropped-coffee-banner-2-4.jpg)](https://securitycafe.ro/)

![](https://securitycafe.ro/wp-content/uploads/2024/10/padlock-lock-chain-key-39624.jpeg?w=840)

# Chained Vulnerabilities in Web Applications

[October 25, 2024](https://securitycafe.ro/2024/10/25/chained-vulnerabilities-in-web-applications/ "12:39 pm") [Adrian Tuchel](https://securitycafe.ro/author/atuchel01/ "View all posts by Adrian Tuchel") [Web security](https://securitycafe.ro/category/web-security/) [Leave a comment](https://securitycafe.ro/2024/10/25/chained-vulnerabilities-in-web-applications/#respond)

## Introduction

Vulnerability chaining, also known as exploit chaining, is the process of combining multiple vulnerabilities to achieve a more significant or impactful attack by exploiting a single vulnerability. In complex systems, real-world attacks often involve multiple steps and understanding, and mitigating chains is crucial for realistic security assessments.

Before reading this article, it is recommended that you are already familiar with basic Web Application attacks.

## Content

1. [Introduction](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#introduction)
2. [Content](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#content)
3. [CSRF + XSS](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#csrf-xss)
   1. [CSRF GET request + Stored XSS](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#csrf-get-request-stored-xss)
   2. [CSRF GET request + Reflected XSS](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#csrf-get-request-reflected-xss)
   3. [CSRF POST request + Stored XSS](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#csrf-post-request-stored-xss)
   4. [CSRF POST request + Reflected XSS](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#csrf-post-request-reflected-xss)
4. [CSRF Mitigations](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#csrf-mitigations)
   1. [Token-Based Mitigation](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#token-based-mitigation)
   2. [SameSite Cookies](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#samesite-cookies)
   3. [Origin and Referer Headers](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#origin-and-referer-headers)
   4. [Bypass CSRF Mitigations](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#bypass-csrf-mitigations)
5. [File Upload -> XSS](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#file-upload-rce)
6. [File Upload + CSRF](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#file-upload-csrf)
7. [File Upload + XSS Stored + CSRF](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#file-upload-xss-stored-csrf)
   1. [Bypassing CSRF Token](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#bypassing-csrf-token)
   2. [How to protect then?](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#how-to-protect-then)
8. [File Upload -> RCE](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#file-upload-rce)
9. [File Upload + File Inclusion](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#file-upload-file-inclusion)
10. [RFI -> RCE](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#rfi-rce)
11. [XSS -> HTML Injection](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#xss-html-injection)
12. [Open Redirect -> CSRF](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#open-redirect-csrf)
13. [Open Redirect -> SSRF](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#open-redirect-ssrf)
14. [Open Redirect -> XSS](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#open-redirect-xss)
15. [XXE + SSRF](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#xxe-ssrf)
16. [XXE -> RCE](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#xxe-rce)
17. [SQL Injection -> RCE](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#sql-injection-rce)
18. [Host Header Injection + Password Reset](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#host-header-injection-password-reset)
19. [Host Header Injection + SSRF](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#host-header-injection-ssrf)
20. [LFI + Log Poisoning -> RCE](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#lfi-log-poisoning-rce)
21. [Conclusion](https://securitycafe.ro/2024/10/14/chained-vulnerabilities-in-web-applications/#conclusion)

## CSRF + XSS

CSRF and XSS vulnerabilities can be used together to redirect a victim to unwanted actions. Is important to note that the victim must be logged-in in the vulnerable application in order for the attacks to be successful.

### CSRF GET request + Stored XSS

An attacker can use a Stored XSS vulnerability on a web application (<https://example.com>) to redirect users to a URL that makes actions on their behalf. An example of CSRF GET URL will look like this:

```
https://example.com/profile/change_password/?new_password=hacked
```

An attacker will craft a payload and any user visiting a vulnerable page with a Stored XSS vulnerability, will be redirected to the URL above and their password will be changed automatically. This example of “change password” functionality that is reflected directly in URL can happen if the implementation is unsecured.

### CSRF GET request + Reflected XSS

For an insecure functionality, a CSRF GET request can be exploited using only a malicious URL like was mentioned above. The attacker sends this URL to a victim and once visited, the action is performed. However, this can be also chained with a Reflected XSS which is working in the same way, a URL that must be accessed by the victim. The difference is that the action in the URL is more stealthy then the previous one, and this chaining can also bypass some CSRF protections, but we will talk later about this.

```
URL for CSRF GET request:
https://example.com/profile/change_password/?new_password=hacked

Reflected XSS redirecting the user to CSRF GET request:
https://example.com/users?name=<script>window.location.replace("https://example.com/profile/change_password/?new_password=hacked");</script>
```

### CSRF POST request + Stored XSS

Similar to the first example, an attacker will inject a payload in the vulnerable application and anyone vis...