---
title: Stored XSS into Onclick Event: Bypassing Angle Brackets, Double Quotes, and Escaped Characters —…
url: https://infosecwriteups.com/stored-xss-into-onclick-event-bypassing-angle-brackets-double-quotes-and-escaped-characters-ee347b9e19d9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-12
fetch_date: 2025-10-06T20:34:44.259506
---

# Stored XSS into Onclick Event: Bypassing Angle Brackets, Double Quotes, and Escaped Characters —…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fee347b9e19d9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstored-xss-into-onclick-event-bypassing-angle-brackets-double-quotes-and-escaped-characters-ee347b9e19d9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstored-xss-into-onclick-event-bypassing-angle-brackets-double-quotes-and-escaped-characters-ee347b9e19d9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ee347b9e19d9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ee347b9e19d9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Stored XSS into Onclick Event: Bypassing Angle Brackets, Double Quotes, and Escaped Characters — XSS Labs

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:64:64/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---byline--ee347b9e19d9---------------------------------------)

[Bash Overflow](https://bashoverflow.com/?source=post_page---byline--ee347b9e19d9---------------------------------------)

4 min read

·

Feb 10, 2025

--

Listen

Share

**[Write-up] Stored XSS into Onclick Event with Angle Brackets and Double Quotes HTML-encoded and Single Quotes and Backslash Escaped**.

## Introduction

The lab titled **Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped** explores a stored cross-site scripting (XSS) vulnerability in a web application’s comment functionality. The vulnerability arises due to insufficient sanitization of user input within an `onclick` HTML event attribute.

Press enter or click to view image in full size

![Stored XSS into Onclick Event with Angle Brackets and Double Quotes HTML-encoded and Single Quotes and Backslash Escaped - Bashoverflow - Medium]()

Stored XSS into Onclick Event with Angle Brackets and Double Quotes HTML-encoded and Single Quotes and Backslash Escaped

In this lab:

* **Angle brackets** (`<`, `>`) and **double quotes** (`"`) are HTML-encoded, preventing direct injection of new HTML tags or attributes.
* **Single quotes** (`'`) and **backslashes** (`\`) are escaped, limiting the use of certain characters in payloads.
* The challenge requires bypassing these sanitization measures to inject a JavaScript payload (e.g., `alert()`) that triggers when a user clicks the comment author’s name.

> **Disclaimer**:
> The techniques described in this document are intended solely for ethical use within the controlled environment of **PortSwigger Labs** for educational and training purposes. Unauthorized use of these methods outside approved environments is strictly prohibited, as it is illegal, unethical, and may lead to severe consequences.
>
> It is crucial to act responsibly, comply with all applicable laws, and adhere to established ethical guidelines. Any activity that exploits security vulnerabilities or compromises the safety, privacy, or integrity of others is strictly forbidden.

## Table of Contents

1. [**Summary of the Vulnerability**](#325e)
2. [**Steps to Reproduce & Proof of Concept (POC)**](#5eb7)
3. [**Impact**](#b17a)
4. [**Mitigation**](#a395)

## **Summary of the Vulnerability**

This lab contains a stored cross-site scripting (XSS) vulnerability in the comment functionality. Attackers can inject malicious JavaScript into the comment author field.

When the victim clicks the author name, the payload (e.g., `alert()`) executes. The challenge involves crafting a payload that bypasses input sanitization (e.g., HTML encoding of angle brackets/double quotes and escaping of single quotes/backslashes).

## **Steps to Reproduce & Proof of Concept (POC)**

1. Open the XSS lab and select one of the example articles.

Press enter or click to view image in full size

![Image 1 - Lab: Stored XSS into Onclick Event with Angle Brackets and Double Quotes HTML-encoded and Single Quotes and Backslash Escaped]()

2. Fill out the comment section, including a payload in the input field.

Press enter or click to view image in full size

![Image 2 - Lab: Stored XSS into Onclick Event with Angle Brackets and Double Quotes HTML-encoded and Single Quotes and Backslash Escaped]()

Press enter or click to view image in full size

![Image 3 - Lab: Stored XSS into Onclick Event with Angle Brackets and Double Quotes HTML-encoded and Single Quotes and Backslash Escaped]()

3. Go back to Burp Suite’s HTTP History and examine the server’s response, which shows the sanitization applied to your payload.

Press enter or click to view image in full size

![Image 4 - Lab: Stored XSS into Onclick Event with Angle Brackets and Double Quotes HTML-encoded and Single Quotes and Backslash Escaped]()

4. Notice that the `onclick` event reflects the URL input from the comment section.

5. Attempt to inject the second payload in the URL form:

`/?&apos;&quot;&gt;&lt;img src=x onerror=alert(1)&gt;//`

```
/?&apos;&quot;&gt;&lt;img src=x onerror=alert(1)&gt;//
```

Press enter or click to view image in full size

![Image 5 - Lab: Stored XSS into Onclick Event with Angle Brackets and Double Quotes HTML-encoded and Single Quotes and Backslash Escaped]()

6. Check the browser’s response using Developer Tools (press F12).

![Image 6 - Lab: Stored XSS into Onclick Event with Angle Brackets and Double Quotes HTML-encoded and Single Quotes and Backslash Escaped]()

7. Observe that certain HTML characters `&apos;` is converted back to `‘`(single quote)

8. Inject the next payload:

```
/?&apos;-top[`alert`](1)-&apos;
```

Press enter or click to view image in full size

![Image 7 - Lab: Stored XSS into Onclick Event with Angle Brackets and Double Quotes HTML-encoded and Single Quotes and Backslash Escaped]()

9. Return to the comment section and click on the username.

Press enter or click to view image in full size

![Image 8 - Lab: Stored XSS into Onclick Event with Angle Brackets and Double Quotes HTML-encoded and Single Quotes and Backslash Escaped]()

10. The payload executes successfully, triggering a pop-up with `alert(1)`.

11. The lab is now solved

Press enter or click to view image in full size

![Image 9 - Lab: Stored XSS into Onclick Event with Angle Brackets and Double Quotes HTML-encoded and Single Quotes and Backslash Escaped]()

## **Impact**

* An attacker could steal session cookies to impersonate users
* Stored XSS affects all users viewing the compromised comment, amplifying the attack’s reach

## **Mitigation**

* Leverage libraries like DOMPurify to sani...