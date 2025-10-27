---
title: Web Application Penetration Checklist
url: https://infosecwriteups.com/web-application-penetration-checklist-fdb34c466975?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-06-06
fetch_date: 2025-10-06T16:56:01.680010
---

# Web Application Penetration Checklist

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ffdb34c466975&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fweb-application-penetration-checklist-fdb34c466975&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fweb-application-penetration-checklist-fdb34c466975&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-fdb34c466975---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-fdb34c466975---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Web Application Penetration Checklist

[![Dhanesh Dodia - HeyDanny](https://miro.medium.com/v2/resize:fill:64:64/1*IzCU1mqJWjlAFYV61nkxOA.jpeg)](https://medium.com/%40Dhanesh_Dodia?source=post_page---byline--fdb34c466975---------------------------------------)

[Dhanesh Dodia - HeyDanny](https://medium.com/%40Dhanesh_Dodia?source=post_page---byline--fdb34c466975---------------------------------------)

5 min read

·

Mar 29, 2023

--

1

Listen

Share

Press enter or click to view image in full size

![]()

Testing Methodology or Approach

## TL;DR

> This checklist is a high level checklist that contains a high level guide what approach we shall follow while testing a web application. This checklist is a generic checklist and does not totally cover all test cases that might apply on web apps.

### Fingerprinting Application:

> · Identify known vulnerabilities in web/app servers.
>
> · Generate Site Structure.
>
> · Identify underlying web technology.
>
> · Uncover HTTP services running on ports other than ports 80 and 443.
>
> · Brute fore subdomains with online tools and GitHub scripts.
>
> · Identify firewall
>
> · Find sensitive keywords in HTML sources such as admin, HTTP, todo, redir, etc.
>
> · Perform JavaScript recon (analyze JS)

### Network Testing:

> · Test for Ping (ICMP echo packets).
>
> · Test for zone transfer.
>
> · Find all services running using NMAP.
>
> · Perform Nessus scan.
>
> · Test all common UDP ports and related issues.

### Session Management Testing:

> · Identify actual session cookies out of bulk cookies.
>
> · Decode cookies using standard algorithms such as base64, hex, etc.
>
> · Modify 1 character in cookie token and resubmit, check whether the session still exists.
>
> · Token leakage via referrer header — Untrusted 3rd party.
>
> · Check session cookie expiration time.
>
> · Identify cookie domain scope.
>
> · Check flags HTTP Only, Secure flag, and same site.
>
> · Check before and after session cookie values.
>
> · Reply to the session cookie from a different public IP address and check if the app maintains.
>
> · Check concurrent login through different IPs.
>
> · Check if any user pertaining information is stored in cookie value or not.

### Registration Feature Testing:

> · Check for duplicate registration with the same email id for account takeover.
>
> · Check for a weak password policy.
>
> · Check for a stored username as a part of the welcome message post-authentication and tr.
>
> · Check for the insufficient email verification process.
>
> · Weak registration implementation — Allows disposable email addresses.

### Login Feature Testing:

> · Check username enumeration.
>
> · Bypass login panel with common login SQL injection payloads using Burpsuite intruder.
>
> · Try accessing resources without authentication.
>
> · Check if user creds are sent over HTTP.
>
> · Check if user creds can forcefully be submitted over HTTP while HTTPS both.
>
> · Check account lockout threshold value.
>
> · Create a custom password wordlist and try brute force.
>
> · Test 0auth functionality.
>
> · Test 0auth functionality for open redirect.

### Error Codes Testing:

> · Try accessing custom pages after the root directory such as ‘yourname.php’, ‘your name.php’
>
> · Add multiple parameters in the same post get requests using different values and generate.
>
> · Add [],]], and [[ in cookie values and parameter value to create errors.
>
> · Try to generate an unusual error code by giving input as /-yourname/%s at the end of word.
>
> · Use the fuzzing technique to create errors and determine any information leakage.

### Post Login My Account Testing:

> · Try CSRF on various features that are pertaining to a single user account.
>
> · Post login change email id and update with any existing email id. Check if it’s getting.
>
> · Test for file upload. Test no AV detection, No size limit, Extension Bypass.
>
> · Open the profile picture in the new tab and check the URL. Find email is/user id info. EXIF
>
> · Check the account deletion option if the application provides it and confirm that via forgot password.
>
> · Change email id, account id, and user id parameter and try to brute-force other users’ ID.
>
> · Check whether the application re-authenticates for performing a sensitive operation for PO (Purchase Order).

### Forget Password Testing:

> · Failure to invalidate session on logout and password reset.
>
> · Check if forget the password reset link/code uniqueness.
>
> · Check if the reset link does get expire or not if it’s not used by the user for a certain amount.
>
> · Find user account identification parameter and tamper id or parameter value or change.
>
> · Check for a weak password policy.
>
> · Weak password reset implementation Token is not invalidated after use.
>
> · If the reset link has another parameter such as date and time, then change date and time.
>
> · Check if security questions are asked? Lockout — How many guesses are allowed?
>
> · Add only spaces in a new password and confirmed password. Then hit Enter and see.
>
> · Does it display the old password on the same page after completion of forgetting the password.
>
> · Ask for two passwords reset links and use the older ones from the user’s email.
>
> · Check if the active session gets destroyed upon changing the password or not?
>
> · Weak password reset implementation Password reset token sent over HTTP.
>
> · Send continuous forget password requests so that it may send sequential tokens.

### Contact Us Form Testing:

> · Is CAPTCHA implemented on the contact us form in order to restrict email flooding attacks.
>
> · Does it allow uploading files on the server?
>
> Product Purchase Testing:
>
> · Buy now — Tamper product ID to purchase other high valued products at a low price.
>
> · Buy now — Tamper product data in order to increase the number of products with a small value.
>
> · Gift/Voucher — Tamper gift/voucher count in the request (ifto increase/decreas...