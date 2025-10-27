---
title: DOM-based Extension Clickjacking: Your Password Manager Data at Risk
url: https://marektoth.com/blog/dom-based-extension-clickjacking/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-29
fetch_date: 2025-10-07T00:50:12.272368
---

# DOM-based Extension Clickjacking: Your Password Manager Data at Risk

[marek
tÃ³th](https://marektoth.com/)

* [Blog](https://marektoth.com/blog/)
* [Findings](https://marektoth.com/findings/)
* [About me](https://marektoth.com/about-me/)
* [Contact](https://marektoth.com/contact/)

* [CS](https://marektoth.cz/blog/dom-based-extension-clickjacking/)

## DOM-based Extension Clickjacking: Your Password Manager Data at Risk

##### 9 August 2025 (Updated: 11 September 2025)

This security research was presented at [DEF CON 33](https://defcon.org/html/defcon-33/dc-33-speakers.html#content_60358): [PDF presentation](https://marektoth.com/presentations/DEFCON33_MarekToth.pdf)

---

##### Since the research was presented at DEFCON (August 9, 2025), several updates have been made:

##### Update 22.8.2025: Bitwarden: 2025.8.1 in progress, <=2025.8.0 vulnerable Enpass: 6.11.6 fixed - released: 13.8.2025, <=6.11.5 vulnerable KeePassXC-Browser <=1.9.9.2 (latest) is vulnerable + New demo sites for: 1Password, Bitwarden, iCloud Passwords, KeePassXC-Browser, LastPass + "Password Managers: Vulnerable & Fixed Versions" updated with the latest versions and videos Update 11.9.2025: Bitwarden: 2025.8.2 fixed - released: 31.8.2025, <=2025.8.1 vulnerable LogMeOnce: 7.12.7 fixed - released: 9.9.2025, <=7.12.6 vulnerable

---

Is clickjacking still an exploitable vulnerability nowadays? Many bug bounty programs have this vulnerability listed in the "out of scope" section, and in better cases they accept it but don't reward it. The reason is that there are many protections available today that significantly reduce the impact of this vulnerability. It can be said that a common web clickjacking vulnerability has already been solved and can be easily defended against.

The result of my research is that clickjacking is still a security threat, but it's necessary to shift from web applications to browser extensions, which are more popular nowadays (password managers, crypto wallets and others).

I described **a new attack technique** with multiple attack variants and tested it against 11 password managers. This resulted in discovering several 0-day vulnerabilities that could **affect stored data of tens of millions of users**.

A **single click anywhere** on a attacker controlled website could **allow attackers to steal users' data** (credit card details, personal data, login credentials including TOTP). The new technique is general and can be applied to other types of extensions.

![](https://marektoth.com/images/dombased-image.png)

Table of contents:

* [Key Information](#key-information)
* [Introduction](#introduction)

+ [Intrusive Web Elements](#intusive-elements)
+ [Clickjacking (Web Application)](#web-clickjacking)
+ [Password Managers](#password-managers)

* [Browser Extension Clickjacking](#browser-extension-clickjacking)
* [IFRAME-based](#iframe-based)
* [**DOM-based Extension Clickjacking**](#dom-based)
* [Extension Element](#extension-element)

+ [Root Element](#root-element)
+ [Child Element](#child-element)

* [Parent Element](#parent-element)

+ [BODY](#body)
+ [HTML](#html)

* [Overlay](#overlay)

+ [Partial Overlay](#partial-overlay)
+ [Full Overlay](#full-overlay)

* [Position](#position)
* [Password Managers: Test Results](#test-results)
* [Detection](#detection)
* [Impact](#impact)

+ [Credit Card, Personal Data](#credit-card)
+ [Login Credentials](#login-credentials)
+ [Passkeys](#passkeys)

* [Password Managers: Vulnerable & Fixed Versions](#fixed-versions)
* [Demo Sites](#demo-sites)
* [Users at Risk](#users-at-risk)
* [Limitation](#limitation)
* [Mitigation](#mitigation)
* [Recommendations for Users](#recommendations)
* [Conclusion](#conclusion)

## Key Information

â¢ A new clickjacking technique where a malicious script manipulates UI elements that browser extensions inject into the DOM by making them invisible using javascript.

â¢ In my research, I selected 11 password managers that are used as browser extensions and the result was that all were vulnerable to DOM-based Extension Clickjacking in the default configuration. **Tens of millions of users could be at risk (~40 million active installations)**.

â¢ A single **click anywhere on the attacker's website could leak credit card details** including security codes (6 out of 9 were vulnerable) or exfiltrate stored personal information (8 out of 10 vulnerable).

â¢ All password managers filled credentials not only to the "main" domain, but also to all subdomains. An attacker could easily find XSS or other vulnerabilities and **steal the user's stored credentials with a single click (10 out of 11), including TOTP (9 out of 11)**. In some scenarios, passkey authentication could also be exploited (8 out of 11).

â¢ All vulnerabilities were reported in April 2025 with a notice that public disclosure will be in August 2025. **Some vendors have still not fixed described vulnerability**: Bitwarden, 1Password, iCloud Passwords, Enpass, LastPass, LogMeOnce. Users of these password managers may still be at risk (~32.7 million active installations).

â¢ For Chromium-based browser users it is recommended to configure site access to "on click" in extension settings. This configuration allows users to manually control autofill functionality.

â¢ The described technique is general and I only tested it on 11 password managers. Other DOM-manipulating extensions are probably also vulnerable (password managers, crypto wallets, notes etc.).

## Introduction

### Intrusive Web Elements

While browsing websites, users often encounter intrusive web elements that block immediate access to target content. These elements require users to click to close them.

The most common intrusive elements requiring user action:

* Cookie consent banners - 1 click (accept/decline cookies)
* Newsletter popup, login dialog - 1 click (closing dialog)
* Web push notifications - 1 click (accept/decline)
* Cloudflare challenge pages / Captcha pages - 1 click (Verify you are human)

  ##### 2 clicks if verification fails, 4 or more clicks if captcha needs to be solved

![](https://marektoth.com/images/instagram.gif)

**1-3 clicks** from the user **are commonly required** before accessing content.

Because users expect to interact with these elements, **I will use fake intrusive web elements in a clickjacking exploit** to trick the user into clicking.

### Clickjacking (Web Application)

Clickjacking (or "UI redressing") is a client-side attack technique that exploits visual layering to hijack user clicks intended for legitimate interface elements. This attack uses invisible frames (iframes) to deceive users who believe they are clicking on legitimate website elements, while actually performing actions that benefit the attacker.

Basic attack principle:

1. Attacker creates a malicious page with an invisible iframe containing the target website (opacity:0).
2. User visits the malicious page and clicks on apparently legitimate visible elements.
3. Clicks are actually intercepted by the hidden iframe, performing unwanted actions on the target site.

```
<iframe src="https://targetsite.com" style="opacity:0"></iframe>
```

To mitigate security impact, security headers X-Frame-Options or Content-Security-Policy are used.

```
X-Frame-Options: DENY
X-Frame-Options: SAMEORIGIN
X-Frame-Options: ALLOW-FROM https://example.com

Content-Security-Policy: frame-ancestors 'none';
Content-Security-Policy: frame-ancestors 'self';
Content-Security-Policy: frame-ancestors https://example.com
```

Additionally, the SameSite Lax or Strict cookie attribute can be set to prevent cookie usage in cross-site iframes.

```
SameSite=Lax            cookies in cross-site POST request or cross-site iframes are blocked
SameSite=Strict         cookies only for same-site requests
SameSite=None           allowed cookies for cross-site requests
```

Default value is **SameSite=Lax if SameSite isn't specified.**

**Clickjacking in web applications has minimal security impact** in most cases because **users are not authenticated** in the loaded ...