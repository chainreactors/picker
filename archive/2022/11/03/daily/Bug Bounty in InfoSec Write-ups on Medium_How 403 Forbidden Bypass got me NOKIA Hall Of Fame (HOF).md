---
title: How 403 Forbidden Bypass got me NOKIA Hall Of Fame (HOF)
url: https://infosecwriteups.com/how-403-forbidden-bypass-got-me-nokia-hall-of-fame-hof-8acbd2c1c2c8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-03
fetch_date: 2025-10-03T21:38:31.201049
---

# How 403 Forbidden Bypass got me NOKIA Hall Of Fame (HOF)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8acbd2c1c2c8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-403-forbidden-bypass-got-me-nokia-hall-of-fame-hof-8acbd2c1c2c8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-403-forbidden-bypass-got-me-nokia-hall-of-fame-hof-8acbd2c1c2c8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8acbd2c1c2c8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8acbd2c1c2c8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How 403 Forbidden Bypass got me NOKIA Hall Of Fame (HOF)

[![Jaydeepsinh Thakor](https://miro.medium.com/v2/resize:fill:64:64/1*FUNe0rSNye4-PM3vI8UUHg.png)](https://medium.com/%40thakor_jd?source=post_page---byline--8acbd2c1c2c8---------------------------------------)

[Jaydeepsinh Thakor](https://medium.com/%40thakor_jd?source=post_page---byline--8acbd2c1c2c8---------------------------------------)

5 min read

·

Nov 2, 2022

--

8

Listen

Share

Hello, amazing people and bug bounty hunters, This is JD ( Jaydeepsinh Thakor ) I hope you all are fine ❤, In this write-up, I would like to share how I got my first HOF & how I was able to bypass 403 using simple method technique on Nokia Subdomain So let’s start,

Press enter or click to view image in full size

![]()

First, understand what 403 is. Basically, 403 is a status code when an unauthorized user tries to access some restricted pages and the server response gives an error with the 403 status code as forbidden. let’s understand in detail.

### **What is 403 forbidden?**

As normal users, we can’t have permission to access a particular web page/website/domain (only can access authorized users like admin, etc) so when we try to access that type of website it will give us an error 403 forbidden.

### **what is 403 forbidden bypass?**

Bypassing 403 Forbidden Error indicates that the client was able to communicate with the server, but the server won’t let the client access what was requested.

**After choosing my target (Nokia.com) which is wild scope, I started my recon process:**

> T**his is the simple methodology that I follow:**
> 1: sub-domains enumeration using different-different tools ( like amass, sub-finder,asset finder, etc)
> 2:Start assessing those websites manually & intercepting request and understanding how websites works
> 3:Checked different-different functionalities.

After analyzing I got some domain that gives me a 403 forbidden error so my mind blow up and I decide let’s try to bypass it :)

So I came on a subdomain which is something like [**https://subs.nokia.com.**](https://subs.nokia.com.)

Press enter or click to view image in full size

![]()

403 Forbidden page

Also, I tried simple Content Spoofing like iFrame injection/Text injection like these [**https://subs.nokia.com/!!Site-is-an-down-visit-evil.com**](https://subs.nokia.com/%21%21Site-is-an-down-visit-evil.com) [or **“/><p>INJECTION</p>**] but sadly it’s didn’t worked and without wasting my time I moved on 403 bypass method.

First I checked that does site contains hidden directories or not so I wrote [**https://subdomain.nokia.com/.htaccess**](https://subdomain.nokia.com/.htaccess)and it gives a 403 error instead of 404 “NOT FOUND” It means the .htaccess file exists in this subdomain.

> <https://subs.nokia.com> /.htaccess

Press enter or click to view image in full size

![]()

Error: You don’t have permission to access /.htaccess on this server.

### It’s Time to bypass this.

There are many different methods available for bypass 403 but first I used some basic and common ones like using the / (slash), /; etc…but NO LUCK :(

![]()

Also, you can automate that process, there are so many automation 403 bypass tools available on GitHub

Press enter or click to view image in full size

![]()

403 Bypass Tool

[## GitHub - iamj0ker/bypass-403: A simple script just made for self use for bypassing 403

### A simple script just made for self use for bypassing 403 - GitHub - iamj0ker/bypass-403: A simple script just made for…

github.com](https://github.com/iamj0ker/bypass-403?source=post_page-----8acbd2c1c2c8---------------------------------------)

[## GitHub - yunemse48/403bypasser

### 403bypasser, hedef sayfalardaki erişim kontrolü kısıtlamalarını aşmak için kullanılan teknikleri otomatikleştirir. Bu…

github.com](https://github.com/yunemse48/403bypasser?source=post_page-----8acbd2c1c2c8---------------------------------------)

> Then I move to the next method which is **the Change request method:**
>
> Change requested methods like **GET → POST, GET → TRACE**, etc.

So I fired up our Pro tool **Burp-Suite** and intercepted the request and sent it to the repeater [ we can do the same thing using curl also but I’m obsessed with Burp-Suit So..]

And I started playing with the repeater and changing the request method **GET → POST** but not worked it’s still showing 403. Then I again change it to **GET → TRACE** and

Here magic will happen, **BOOM** I got 200 OK responses

Press enter or click to view image in full size

![]()

![]()

Woooh

Then I click **“Show Response In Browser”** and paste it on the browser and guess what! the .htaccess / .htpasswd file pop-up and give me the download permission.

Press enter or click to view image in full size

![]()

But but … when I opened and saw those files that’s doesn’t contain any crucial information so I was a little bit sad

![]()

then I thought I found nothing but still, I bypassed their 403 mechanisms, so why shouldn’t report !!

**Cause let’s try a flip scenario:**

However I found nothing crucial information or passwords, okay but what if something important is used within the site and maintained in the same way, it may be possible to bypass an attacker and see/dump/access/ any sensitive file.

So after all this, I have sent a well written with a detailed explained report and POC-included mail to security-alert@nokia.com regarding this issue.

Then they validated the same from their end and notified me that it was a valid finding

Press enter or click to view image in full size

![]()

After some days they add me on their HALL OF FAME page as shown below

Press enter or click to view image in full size

![]()

Yeah, that’s it for today Thanks !! I hope you enjoyed reading it.

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all t...