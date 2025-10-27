---
title: From Fries to Flaws : My Journey into Web App Security (Part II)
url: https://infosecwriteups.com/from-fries-to-flaws-my-journey-into-web-app-security-part-ii-6127ecc7d93f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-13
fetch_date: 2025-10-06T18:04:43.073018
---

# From Fries to Flaws : My Journey into Web App Security (Part II)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6127ecc7d93f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-fries-to-flaws-my-journey-into-web-app-security-part-ii-6127ecc7d93f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-fries-to-flaws-my-journey-into-web-app-security-part-ii-6127ecc7d93f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6127ecc7d93f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6127ecc7d93f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# From Fries to Flaws : My Journey into Web App Security (Part II)

## Uncovering XSS in FastFoodHackings Challenge and Elevating Your Bug Bounty Skills

[![zerOiQ](https://miro.medium.com/v2/resize:fill:64:64/1*M6lvjH7YpCrR1SqB0tcYSg.png)](https://medium.com/%40zerOiQ?source=post_page---byline--6127ecc7d93f---------------------------------------)

[zerOiQ](https://medium.com/%40zerOiQ?source=post_page---byline--6127ecc7d93f---------------------------------------)

4 min read

·

Aug 3, 2024

--

1

Listen

Share

> [***bugbountytraining.com***](https://www.bugbountytraining.com/fastfoodhackings/)***/***[***FastFoodHackings***](https://www.bugbountytraining.com/fastfoodhackings/)

Press enter or click to view image in full size

![]()

> Welcome to the second part of our series on BugBountyTraining , In brief, [FastFoodHackings](https://www.bugbountytraining.com/fastfoodhackings/) is a training website created by
>
> [Sean (zseano)](https://medium.com/u/ca91e7064349?source=post_page---user_mention--6127ecc7d93f---------------------------------------)
>
> . It helps people learn bug hunting through real-world scenarios. If you missed the first part, be sure to check it out. Let’s continue our journey into uncovering bugs !
>
> [**(Part I)**](/from-fries-to-flaws-my-journey-into-web-app-security-part-i-958c67c20771)

Press enter or click to view image in full size

![]()

Screenshot

Last time , we found an **HTML Injection Vulnerability** . Let’s keep going and try to escalate it into **XSS** .

So, basically, we’ll replace the `h1`tag with a `<script>` tag and change the script content to `alert(something)` to see if we get an alert pop-up when it's executed successfully.

**Here's the trick**: we'll remove the last `>`, because the web app automatically appends the closing tag, as we saw in previous examples .

Press enter or click to view image in full size

![]()

Screenshot

So, we got our alert reflected here, but it doesn’t do anything because the web app uses some kind of filtering to prevent injecting JavaScript into the **HTML** .

However, we’ll try other methods and payloads to bypass this filter. One of my favorite XSS payload repositories is the[**XSS.js.org**](https://xss.js.org/#/xss01) website, which contains a large number of great payloads.

Let’s try some of them manually. If that doesn’t work, we’ll use Burp Suite Intruder.

After four failed attempts, the fifth one finally gave us the desired result: **XSS found!**

Press enter or click to view image in full size

![]()

Screenshot

```
https://www.bugbountytraining.com/fastfoodhackings/index.php?act=--%3E%3CIMG%20SRC=x%20onerror=%22alert(String.fromCharCode(88,83,83))%22
```

And here is the used payload

```
<IMG SRC=x onerror="alert(String.fromCharCode(88,83,83))"
```

Or we can simply

```
<IMG SRC=x onerror=alert("XSS")
```

Also , remember to omit the closing tag `>` from the payload as we did earlier .

And we did it , we achieved the desired XSS !

Now, let’s return to the home page and explore further. We’ll start by examining the booking form to see if it has any vulnerabilities.

Press enter or click to view image in full size

![]()

Screenshot

First, we’ll perform some manual testing. If we don’t find anything, we can use automated tools to dig deeper.

So, as a normal user, we’ll fill out the form inputs and observe how the web app behaves.

Press enter or click to view image in full size

![]()

Screenshot

After filling out the form, the web app displays: “**This order is pending confirmation.**” I also noticed that it redirects from `book.php` to `confirmed.php` , huum interesting .

After some manual attempts and testing, we didn’t find anything interesting. Let’s intercept the request through **Burp Suite** to see if we can find something .

Here’s the request :

Press enter or click to view image in full size

![]()

Screenshot

We didn’t find anything unusual except the data sent from the form.

After some investigation, I noticed something interesting, whenever we write into the form, the data gets **Reflected** in the source code within the `value` attribute. Here is an example:

Press enter or click to view image in full size

![]()

Screenshot

From this discovery, I think we can achieve a **Reflected XSS**.

Let’s intercept the request again and try injecting some XSS payloads from our repo [**XSS.js.org**](https://xss.js.org/#/xss03) , we hope we can successfully exploit it.

Press enter or click to view image in full size

![]()

Screenshot

So, as always, after many failed attempts trying to find the winning payload, we finally found it.

```
"><script>alert(233)</script>
```

Press enter or click to view image in full size

![]()

Screenshot

Out of curiosity, I wanted to determine which input field is vulnerable.

After retesting, I discovered that the `Date`input is the vulnerable field in this form.

Press enter or click to view image in full size

![]()

Screenshot

And I got the same result as above .

Here is the source code. As you can see, the script tag in the `Full Name`and `Email Address`fields is being placed within the input box, which means these inputs are not vulnerable.

However, in the `Date` field, we don’t see anything initially. When we inspect the code, we notice the selected `Date`followed by the closing tag `”>` we inserted, causing our script to be treated as part of the page’s code.

Press enter or click to view image in full size

![]()

Screenshot

**Good achievement for now**, but there’s still a long way to go. Let’s continue our journey in the next part and see what other vulnerabilities we can uncover.

### So far, we’ve uncovered 🐞🐞bugs, but there’s much more to explore. In the next part, we’ll dive deeper and find even more vulnerabilities. Hope you enjoyed this segment 🥳 see you soon!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----6127ecc7d93f-------------------------------...