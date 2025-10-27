---
title: 1 Click Account Takeover | XSS | CORS Misconfiguration | JWT Forgery
url: https://infosecwriteups.com/1-click-account-takeover-xss-cors-misconfiguration-jwt-forgery-0cf73a28e236?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-05-01
fetch_date: 2025-10-06T22:25:03.584498
---

# 1 Click Account Takeover | XSS | CORS Misconfiguration | JWT Forgery

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0cf73a28e236&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F1-click-account-takeover-xss-cors-misconfiguration-jwt-forgery-0cf73a28e236&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F1-click-account-takeover-xss-cors-misconfiguration-jwt-forgery-0cf73a28e236&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0cf73a28e236---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0cf73a28e236---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 1 Click Account Takeover | XSS | CORS Misconfiguration | JWT Forgery

[![Raymond Van Wart](https://miro.medium.com/v2/resize:fill:64:64/1*cjzkobnZF74HU2WAYmDr7g.jpeg)](https://raymondv.medium.com/?source=post_page---byline--0cf73a28e236---------------------------------------)

[Raymond Van Wart](https://raymondv.medium.com/?source=post_page---byline--0cf73a28e236---------------------------------------)

5 min read

·

Apr 29, 2025

--

3

Listen

Share

This finding was reported to a bug bounty program and is redacted because of the NDA.

## Finding a Lead

When hunting for vulnerabilities, I try to interact with the site like a normal user to explore all of its functionality. Doing so can reveal interesting endpoints with the help of tools like Burp.

### CORS Misconfiguration

After visiting [redacted.com/account/profile](https://www.redacted.com/account/profile), a **POST** request was made to [redacted\_auth.com/api/v1/profile](https://redacted_auth.com/api/v1/profile). I prefer conducting passive recon first whenever possible because it does not generate noise. Waymore is a wonderful tool for finding links from passive sources, and it helped me find more API endpoints.

```
waymore -i 'https://redacted_auth.com/api/v1/' -mode U -oU urls_waymore.txt
```

Press enter or click to view image in full size

![]()

[redacted\_auth.com/web/cookie/token](https://redacted_auth.com/web/cookie/token) immediately caught my attention. It was reflecting the session cookie in its response.

![]()

The endpoint would also blindly reflect any provided **Origin** as the **Access-Control-Allow-Origin** header.

Press enter or click to view image in full size

![]()

The **SameSite** property of the session cookie was set as **Strict** to prevent 3rd party sites from including it with their requests, but this restriction does not apply to subdomains because they are considered same-origin.

When combined, these vulnerabilities pose a serious threat.

* Reflecting the session cookie in the response nullifies its **HttpOnly** property.
* The **CORS** vulnerability expands the attack surface to any subdomain of [redacted.com](http://redacted.com/) because they are all capable of reading user session cookies.

Finding a takeover or **XSS** on any subdomain would now make it possible to hijack sessions.

## Chaining Vulnerabilities

### Subdomain Takeover

First, I searched for subdomains with **subfinder** and made sure to include API keys in the config file to find more results.

```
subfinder -d redacted.com -all -recursive | anew subdomains.txt
```

The subdomains were then analyzed by **dnsReaper** for takeovers.

```
docker run -it — rm -v $(pwd):/etc/dnsreaper punksecurity/dnsreaper file — filename /etc/dnsreaper/subdomains.txt
```

Press enter or click to view image in full size

![]()

After verifying the results manually, it was determined that none of the takeovers were valid. This is not surprising, as the subdomain takeover vulnerability class is heavily automated.

### Cross Site Scripting

I spent about 2 weeks hunting for XSS. Most of the subdomains were protected by a WAF and difficult to test, so I scanned them with httpx to find the ones that were unprotected.

```
httpx-pd -l subdomains.txt -td -sc -title -fr | grep -viE 'akamai|cloudflare'
```

Analyzing the source code from one of these subdomains led to an interesting discovery.

Press enter or click to view image in full size

![]()

The **url** variable was defined but never used, probably because the developers forgot to remove it from a previous commit. This endpoint also failed to sanitize reflected user input from a query parameter, and was therefore vulnerable to XSS.

![]()

## Escalating Impact

### JWT Forgery

Most web APIs require inputting the current password to change it, but it is often possible to circumvent this check by editing the current email address, and then calling a reset password endpoint. Unfortunately, [redacted\_auth.com/api/v1/profile](https://redacted_auth.com/api/v1/profile) did not allow email modification.

After performing more recon, I found a different API at [redacted\_widget.com](https://redacted_widget.com/). Changes made through this endpoint were synced with the main API, but required a **UUID** and **JWT**.

![]()

The required **UUID** was included in the **JWT** shown earlier from the XSS popup and uncrackable because it used version 4. <https://en.wikipedia.org/wiki/Universally_unique_identifier>

The **JWT** cookie however, possessed a different structure from the one used on the main API.

![]()

To validate this token, the application compared its email with the one from the request. Unfortunately, attempting to register users with an existing email would return an error, so it did not seem possible to duplicate tokens.

![]()

After some thorough testing, I discovered a mass assignment vulnerability that made it possible to bypass duplicate user checks by setting the region to **EU**.

Press enter or click to view image in full size

![]()

![]()

Notice, the generated token for the duplicate account does not include a region attribute, so it is identical to the victim’s JWT.

It would now be possible to complete the **ATO** using the following chain.

* [redacted\_widget.com/v1/widget/update](https://redacted_widget.com/v1/widget/update)
* [redacted\_widget.com/v1/widget/resetToken](https://redacted_widget.com/v1/widget/resetToken)

## Conclusion

### Steps to Reproduce the Attack.

1. Victim visits our malicious site.
2. Victim is redirected to the subdomain vulnerable to XSS with our payload.
3. The payload executes, fetches the victim’s session cookie from the main API, and sends it to our server.
4. We create a duplicate user in region **EU** using the mass assignment vulnerability found in the widget API.
5. We use the stolen **UUID** and **JWT** to update the victim’s email.
6. We use the reset password endpoint to ...