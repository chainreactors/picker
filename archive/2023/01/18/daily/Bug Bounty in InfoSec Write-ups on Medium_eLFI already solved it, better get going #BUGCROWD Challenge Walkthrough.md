---
title: eLFI already solved it, better get going #BUGCROWD Challenge Walkthrough
url: https://infosecwriteups.com/elfi-already-solved-it-better-get-going-bugcrowd-challenge-walkthrough-b83f6921056b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-18
fetch_date: 2025-10-04T04:08:10.010974
---

# eLFI already solved it, better get going #BUGCROWD Challenge Walkthrough

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb83f6921056b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Felfi-already-solved-it-better-get-going-bugcrowd-challenge-walkthrough-b83f6921056b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Felfi-already-solved-it-better-get-going-bugcrowd-challenge-walkthrough-b83f6921056b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b83f6921056b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b83f6921056b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# eLFI already solved it, better get going #BUGCROWD Challenge Walkthrough

[![Prasanth Bodepu](https://miro.medium.com/v2/resize:fill:64:64/1*sepNThSSaAqVwcGoL7G_GA.jpeg)](https://medium.com/%40prasanth.bodepu?source=post_page---byline--b83f6921056b---------------------------------------)

[Prasanth Bodepu](https://medium.com/%40prasanth.bodepu?source=post_page---byline--b83f6921056b---------------------------------------)

4 min read

·

Jan 17, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

In this Write-Up, I am going to walk you through the [bugcrowd’s open challenge](https://twitter.com/Bugcrowd/status/1606016814831570989?s=20&t=aam_TPp8kFfqYfJ67bR8KQ) to hackers.

* Note: In case you’re reading this Write-Up without trying out the [challenge](https://bugcrowd-advent-challenge.herokuapp.com/login.php). I request you to first give it a try and check this blog if you’re stuck.

1. Hint given**: “i am eLFI”**
2. So, I went to this link <https://bugcrowd-advent-challenge.herokuapp.com/login.php>

**3.** Tried **user1** and **Randompassword123** as credentials that was present on the login page itself and it gave me an internal server error as shown below.

Press enter or click to view image in full size

![]()

**4.** I tried to play around with the login.php but no luck.

**5.** I jumped right away to the view page source of the login.php application, went through the source code and few lines caught my attention which I highlighted below.

Press enter or click to view image in full size

![]()

**6.** Then I remembered the **Hint** and tried to sync that with the above lines of code.

**7.** That’s how I found a vulnerable endpoint which is **/style.php?css\_file=custom.css**

**8.** Here, when I tried to inject a random LFI payload, it showed **Hacker detected**, which confirmed that style.php is the vulnerable parameter.

[https://bugcrowd-advent-challenge.herokuapp.com/](https://bugcrowd-advent-challenge.herokuapp.com/login.php)style.php?css\_file=//..//..//..//etc/passwd

Press enter or click to view image in full size

![]()

**9.** Here I guessed it is filtering out **etc/passwd** so I tried URL, BASE64 encoding, and double encoding, but no luck.

**10.** Then, I played around with the application for a while. Finally, while fuzzing the application, I observed there’s another file as index.php

Press enter or click to view image in full size

![]()

**11.** But when I opened it, it redirected me to the login.php. But when you open the network tab you can see the index.php and the status code as 302.

Press enter or click to view image in full size

![]()

**12.** I felt a bit suspicious about this **index.php** and I wanted to see what is there in it. So, I googled about it.

Press enter or click to view image in full size

![]()

**13.** I came across this piece of code `php://filter/convert.base64-encode/resource=<filename>`

which helped me in bypassing the restriction and allowed me to view the source code of **index.php**

Press enter or click to view image in full size

![]()

**14.** Finally, **index.php** gave me some encoded string like this.

![]()

index.php

**15.** I decoded it using the below command. You can also use [**cyberchef**](https://gchq.github.io/CyberChef/)(You can also use burpsuite’s decoder)

echo “PD9waHAKCnNlc3Npb25fc3RhcnQoKTsKc2Vzc2lvbl9yZWdlbmVyYXRlX2lkKHRydWUpOwoKaWYgKGlzc2V0KCRfU0VTU0lPTlsidXNlciJdKSl7CiAgICBoZWFkZXIoIkxvY2F0aW9uOiBkYXNoYm9hcmQucGhwIik7CiAgICBleGl0KCk7Cn1lbHNlewogICAgaGVhZGVyKCJMb2NhdGlvbjogbG9naW4ucGhwIik7CiAgICBleGl0KCk7Cn0KCj8+” | base64 — decode

Press enter or click to view image in full size

![]()

index.php -> decoded

**16.** It showed me two Php files named **dashboard.php** and login.php

Now, I replaced the **index.php** with **dashboard.php and** it gave me the below encoded string.

Press enter or click to view image in full size

![]()

dashboard.php

**17.** This time I used cyberchef to decode, I found another file named sober.php in the source code.

Press enter or click to view image in full size

![]()

dashboard.php -> decoded

**18.** Now, I replaced the **dashboard.php** with **sober.php** and I found another encoded string

Press enter or click to view image in full size

![]()

**19.** After decoding the string I got the below below code. Here, I found another encoded string in the multi-line comments, but this time it is small compared to the earlier encoded strings.

Press enter or click to view image in full size

![]()

**20.** Finally, after decoding the string, I found this.

Press enter or click to view image in full size

![]()

flag

I don’t know why, but somehow I was attracted to this challenge and took off the first half of the day from work. Thanks to you [bugcrowd](https://twitter.com/Bugcrowd) : )

The challenge seems to be very simple after reading the walkthrough, but believe me, it took me a lot of brains to think and execute it.

I thank my friend [Paweł Wąsik](https://www.linkedin.com/in/pawe%C5%82-w%C4%85sik-b526bb1ba/) for his constant support.

**References:**

[## A Pentester's Guide to File Inclusion | Cobalt

### Read the Pentester's Guide to File Inclusion for key insights into this common vulnerability. See the expert's tips…

www.cobalt.io](https://www.cobalt.io/blog/a-pentesters-guide-to-file-inclusion?source=post_page-----b83f6921056b---------------------------------------)

[## Using PHP Wrappers within LFI to Obtain PHP Script Source Code

### You find a Local File Inclusion (LFI) running PHP, you're able to leverage a PHP wrapper to convert the file to Base64…

infinitelogins.com](https://infinitelogins.com/2020/04/25/lfi-php-wrappers-to-obtain-source-code/?source=post_page-----b83f6921056b---------------------------------------)

**Feel free to Connect with me at** **-**

* [LinkedIn](https://www.linkedin.com/in/prasanth-bodepu-411ba31a3/)
* [Twitter](https:...