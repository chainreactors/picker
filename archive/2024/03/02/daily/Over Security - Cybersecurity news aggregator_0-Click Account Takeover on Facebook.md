---
title: 0-Click Account Takeover on Facebook
url: https://infosecwriteups.com/0-click-account-takeover-on-facebook-e4120651e23e
source: Over Security - Cybersecurity news aggregator
date: 2024-03-02
fetch_date: 2025-10-04T12:12:18.637555
---

# 0-Click Account Takeover on Facebook

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe4120651e23e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F0-click-account-takeover-on-facebook-e4120651e23e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F0-click-account-takeover-on-facebook-e4120651e23e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e4120651e23e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e4120651e23e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 0-Click Account Takeover on Facebook

[![Samip Aryal](https://miro.medium.com/v2/resize:fill:64:64/1*_7OHNiUl4wx-Efpl5C_tyg.jpeg)](https://samiparyal.medium.com/?source=post_page---byline--e4120651e23e---------------------------------------)

[Samip Aryal](https://samiparyal.medium.com/?source=post_page---byline--e4120651e23e---------------------------------------)

5 min read

·

Feb 27, 2024

--

35

Listen

Share

> **Hello, This is Samip Aryal from Nepal writing about my highest-paid report**. **This writeup basically describes rate-limiting issue in a specific endpoint of Facebook’s password reset flow that could’ve allowed the takeover of any Facebook account by bruteforcing a particular type of nonce.**

Press enter or click to view image in full size

![]()

### Background

So basically, I wasn’t searching for any unique bugs for several months. It started when one day; during my Engineering board exam, I was like… Let’s search for [Account Takeover](https://www.cloudflare.com/learning/access-management/account-takeover/); like literally! out of the blue; still not sure where it came from lol. Now, I needed a fresh **untouched/hidden/unnoticed endpoint** to look for. And when it’s about an “untouched endpoint”; i thought looking on the web is like nah.. Everybody looks on the web. So I started my Android Studio setup, jumped into Facebook’s main login page, and tried looking for one, uninstallation-installation of several versions of Facebook took place but nothing seemed new/interesting. Then I was like what if we try with different user-agents to see the server’s UI responses on each of the login pages?

![]()

Or you can use extensions.

and somewhere this poped-up in the password reset flow:

![]()

The vulnerable endpoint

wait what! I’ve seen this option during the reset flow in one of my other accounts (in my default settings). But anyway, this shortly looked interesting for me to quickly jump to testing it. There were three reasons:

1. **The nonce sent to the user is active for longer than I expected (≈ 2 hrs)**
2. **The same nonce code was sent every time for the period.**
3. **I didn’t see any sort of code invalidation after entering the correct code but with multiple previous invalid tries (unlike in the SMS reset functionality).**

This resulted me in eyeing a brute-force attack.

### **Technical Details**

1. **Choosing any Facebook user account, go to its password reset flow.**

Press enter or click to view image in full size

![]()

**2. Simply, Choose the following from the** [**reset options**](https://www.facebook.com/recover/initiate)**:**

![]()

This sends a POST request to:

> **POST /ajax/recover/initiate/ HTTP/1.1**

with the parameter; recover\_method=**send\_push\_to\_session\_login**

Press enter or click to view image in full size

![]()

3. **Send with a dummy 6-digit code ‘000000’.**

![]()

This creates a POST request to the **vulnerable endpoint**:

> **POST /recover/code/rm=send\_push\_to\_session\_login&spc=0&fl=default\_recover&wsr=0 HTTP/1.1**

4. The “**n**” parameter holds the nonce.

Press enter or click to view image in full size

![]()

5. Bruteforce this 6-digit value from **000000 to 999999**. This can be done in multiple ways. Using web proxies like Burp Suite,

> *[We need a powerful machine to do that oc!] Thus, lets brute force for now from X00000 to X99999*
>
> *a) Send the above request to the Intruder and insert $$ placeholder in the ’n’ parameter value in order to brute force the nonce code and, make 9 or more sets/tabs of concurrent payload requests, each set with chunks of combinations (00000 to 11111, 11111 to 22222, and so on).*
>
> *b) Or, automatically through the Burp’s resource pool, maximum concurrent requests can be set between 10–15, which should be sufficient to go through the entire search space in about 1 hrs.*

6. Yes, there was no rate limiting on this endpoint, thus the **matching code** was responded back with a **302 status code**. Use this code to **log in/reset** the FB account password for the user account.

7. Also, In my case, the option ‘**Send code via Facebook notification**’ got hidden from UI at my end, which might be due to some sort of protection but it could be easily bypassed by changing the IP address.

![]()

Sample POC

### **This a 0-click Account Takeover right?**

Well, turns out that;

→ For some set of users, the nonce code would be rendered on the notification itself.

![]()

This is the zero-click case

→ For the other set, the notification that is sent with the nonce would need to be opened and the code would be rendered on a separate screen.

![]()

This is the one-click case

Here, in this second case, according to Facebook — One tap of the victim is needed for the nonce to generate.

\* Facebook replied that “While this did require user interaction, we consider clicking a notification to be a much lower bar than clicking a link sent to you by an attacker, therefore we decided to deduct from the 0-click ATO, rather than basing the bounty off the 1-click ATO”.

Press enter or click to view image in full size

![]()

### **This vulnerability had a huge impact since it enabled the full takeover of Facebook accounts. It also helped me to rank 1 in Facebook’s Hall of Fame 2024 (currently)**

![]()

facebook.com/whitehat/thanks

### Timeline:

Jan 30, 2024 — Report Sent
Feb 1, 2024— Pre-Triaged
Feb 1, 2024 — Clarification Requested by Facebook | Unreproducible
Feb 2, 2024 — Clarification sent that the issue seems fixed today
Feb 9, 2024 — Got an Invitation for BountyCon2024 (South Africa) in the same email thread of the issue; got confused.
Feb 22, 2024 — Rewarded with a clarification message that it was fixed after somebody else’s report that came after mine but I was the first to report (after investigation)

…

*Thank you for reading this write-up, If you have any queries/suggestions, I’m available on* [*Facebook*](https://facebook.com/100006417722704)*/* [*Instagram*](https...