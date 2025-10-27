---
title: Bypassing XSS Filters: Techniques and Solutions
url: https://infosecwriteups.com/bypassing-xss-filters-techniques-and-solutions-d6674029f1e9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-08-21
fetch_date: 2025-10-04T11:59:13.836549
---

# Bypassing XSS Filters: Techniques and Solutions

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd6674029f1e9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-xss-filters-techniques-and-solutions-d6674029f1e9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-xss-filters-techniques-and-solutions-d6674029f1e9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d6674029f1e9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d6674029f1e9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Bypassing XSS Filters: Techniques and Solutions

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:64:64/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---byline--d6674029f1e9---------------------------------------)

[Security Lit Limited](https://securitylit.medium.com/?source=post_page---byline--d6674029f1e9---------------------------------------)

3 min read

·

Aug 10, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

In the ever-evolving landscape of web security, Cross-Site Scripting (XSS) stands as one of the most pernicious vulnerabilities. XSS allows attackers to inject malicious scripts into web pages which then run on another user’s browser. These injected scripts can lead to a variety of malicious actions, such as stealing session cookies or defacing web pages. To counteract these vulnerabilities, developers deploy multiple techniques. But as developers fortify defenses, attackers refine their techniques to bypass these security measures. This article will explore some techniques used to bypass XSS filters and how developers can stay vigilant.

## Techniques to Bypass XSS Filters

## 1. Set length limit

Technique: Attackers set a limit on the payload’s length, hoping the filter doesn’t recognize lengthy malicious scripts.

```
def filter_input(data):
    if len(data) > 50: # Assuming filter has a set length limit of 50 characters
        return "Data too long"
    # ... further processing

# Attackers payload
payload = "<img src=x onerror=alert('XSS')>"
filter_input(payload)
```

Output: If the length of the payload is under the limit, it could bypass the filter.

## 2. Block all event handlers

Technique: Filters block all event handlers to prevent malicious scripts using them.

```
def filter_input(data):
    event_handlers = ["onerror", "onload", "onclick"]
    for handler in event_handlers:
        if handler in data:
            return "Suspicious event handler detected"
    # ... further processing

# Attackers payload
payload = "<img src=x onerror=alert('XSS')>"
filter_input(payload)
```

Output: If the payload uses an event handler not in the filter’s list, it might bypass the filter.

## 3. Block some tags

Technique: Filters block certain HTML tags like `<script>` and `<iframe>`.

```
def filter_input(data):
    disallowed_tags = ["<script>", "<iframe>"]
    for tag in disallowed_tags:
        if tag in data:
            return "Blocked tag detected"
    # ... further processing

# Attackers payload
payload = "<script>alert('XSS')</script>"
filter_input(payload)
```

Output: The payload will be blocked by the filter. However, if attackers use an alternative method not covered by the filter, it could bypass.

## 4. Block popup functions

Technique: Filters block popup functions like `alert()` to detect common XSS demonstrations.

```
def filter_input(data):
    if "alert(" in data or "confirm(" in data:
        return "Popup function detected"
    # ... further processing

# Attackers payload
payload = "alert('XSS')"
filter_input(payload)
```

Output: The filter will block the payload. But innovative methods might bypass it.

## 5. Block `<`

Technique: By blocking the `<` character, filters try to stop creation of HTML tags used in payloads.

```
def filter_input(data):
    if "<" in data:
        return "Blocked character detected"
    # ... further processing

# Attackers payload
payload = "<img src=x>"
filter_input(payload)
```

Output: The payload gets blocked. However, encoding techniques can bypass such filters.

## 6. Block `()`

Technique: Filters block parentheses, preventing function calls in JavaScript.

```
def filter_input(data):
    if "(" in data and ")" in data:
        return "Blocked characters detected"
    # ... further processing

# Attackers payload
payload = "alert('XSS')"
filter_input(payload)
```

Output: The payload will be blocked, but alternative scripts might not be detected.

## Advanced Bypass: Base href attribute

Another sneaky method mentioned is using a payload with a base href attribute. This can result in an unexpected XSS popup, illustrating the complexity of creating foolproof XSS filters.

Protecting against XSS attacks requires constant vigilance. Understanding how attackers might bypass filters helps developers design more robust defenses. Regularly updating security measures and being aware of the latest techniques is essential in safeguarding against these threats.

## Further Reading

* **OWASP Cross-Site Scripting (XSS)**
* **Content Security Policies (CSP)**

The information in this blog is intended for educational purposes. Security professionals should conduct thorough testing and follow best practices to ensure comprehensive protection.

[Xss Attack](https://medium.com/tag/xss-attack?source=post_page-----d6674029f1e9---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----d6674029f1e9---------------------------------------)

[Programming](https://medium.com/tag/programming?source=post_page-----d6674029f1e9---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----d6674029f1e9---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----d6674029f1e9---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d6674029f1e9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d6674029f1e9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publi...