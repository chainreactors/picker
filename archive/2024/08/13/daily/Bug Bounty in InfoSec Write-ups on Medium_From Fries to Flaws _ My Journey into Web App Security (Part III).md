---
title: From Fries to Flaws : My Journey into Web App Security (Part III)
url: https://infosecwriteups.com/from-fries-to-flaws-my-journey-into-web-app-security-part-iii-ce91eb384da7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-13
fetch_date: 2025-10-06T18:04:28.249070
---

# From Fries to Flaws : My Journey into Web App Security (Part III)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fce91eb384da7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-fries-to-flaws-my-journey-into-web-app-security-part-iii-ce91eb384da7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-fries-to-flaws-my-journey-into-web-app-security-part-iii-ce91eb384da7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ce91eb384da7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ce91eb384da7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# From Fries to Flaws : My Journey into Web App Security (Part III)

## Mastering Broken Access Control in FastFoodHackings Challenge and Excelling as a Bug Bounty Hunter

[![zerOiQ](https://miro.medium.com/v2/resize:fill:64:64/1*M6lvjH7YpCrR1SqB0tcYSg.png)](https://medium.com/%40zerOiQ?source=post_page---byline--ce91eb384da7---------------------------------------)

[zerOiQ](https://medium.com/%40zerOiQ?source=post_page---byline--ce91eb384da7---------------------------------------)

6 min read

·

Aug 6, 2024

--

1

Listen

Share

> [**bugbountytraining.com**](https://www.bugbountytraining.com/fastfoodhackings/)**/**[**FastFoodHackings**](https://www.bugbountytraining.com/fastfoodhackings/)

Press enter or click to view image in full size

![]()

> Welcome to the third part of our series on BugBountyTraining , In brief, [FastFoodHackings](https://www.bugbountytraining.com/fastfoodhackings/) is a training website created by
>
> [Sean (zseano)](https://medium.com/u/ca91e7064349?source=post_page---user_mention--ce91eb384da7---------------------------------------)
>
> . It helps people learn bug hunting through real-world scenarios. If you missed the first and second parts, be sure to check them out. Let’s continue our journey into uncovering bugs !
>
> [(Part I)](/from-fries-to-flaws-my-journey-into-web-app-security-part-i-958c67c20771) [(Part II)](https://medium.com/%40OiQ/from-fries-to-flaws-my-journey-into-web-app-security-part-ii-6127ecc7d93f)

In the previous part, we focused on the input boxes in the booking form. However, when I was sending the request, something caught my attention. I decided to understand and test it .

So , after forwarding the first request.

Press enter or click to view image in full size

![]()

The `Order_id` parameter grabbed my interest. It looks like it might be **Base64** encoded, so let's decode it and see what we uncover.

Press enter or click to view image in full size

![]()

Let’s use [**CyberChef**](https://cyberchef.org/) as our decoding tool, or we can simply right-click it and decode it in Burp Suite.

Press enter or click to view image in full size

![]()

It seems to be the same order number that appears on the screen after successfully submitting the order.

Press enter or click to view image in full size

![]()

Let’s send this request to Burp Suite **Repeater** and experiment with it. It might be vulnerable to some form of **Broken Access Control** based on my knowledge.

First, let’s send the same request and check if we get the same page.

Intuitively, we should.

Press enter or click to view image in full size

![]()

As we decoded the order value and discovered that it is `42069`, let’s experiment with this number to see if we can access orders belonging to other users.

For example, we can change it from `42069`to `42066`and observe what happens.

**But here’s the trick**: we need to encode the number in `Base64`before sending it. If we don’t , and send it as is, the request will be rejected.

As you can see, something interesting occurred .We gained access to another order submitted by someone else named`Raymundo Linney`with the email address `lavina81@heller.com`.

Press enter or click to view image in full size

![]()

This access was not supposed to be available, illustrating an example of [**Broken Access Control**](https://owasp.org/www-community/Broken_Access_Control) .

> And , we did it ! We uncovered a **BAC** vulnerability.

Next, let’s explore further. As we’ve already covered the login form and the booking feature, we have two more areas to test: the **Our Menu** feature and **Our Locations** page.

Starting with the **menu** page, it appears to be a standard page with the menu and no clickable elements or parameters to manipulate manually.

Press enter or click to view image in full size

![]()

So, let’s turn on **Burp Proxy** and see if we can uncover any hidden aspects.

After examining the initial requests, which included only CSS files, Google Fonts API, and other normal files, we found something interesting in the last request. This HTTP request is asking for the resource located at `/reviews.php` via the `loader.php` script on the server, with a parameter named `f` specifying the file name.

```
GET /fastfoodhackings/api/loader.php?f=/reviews.php HTTP/1.1
```

Press enter or click to view image in full size

![]()

Let’s send this request to **Repeater** and experiment with it to see what we uncover.

So, after rendering the request and seeing its content, it contains some client reviews.

Press enter or click to view image in full size

![]()

This led me to test for a [**Path Traversal Vulnerability**](https://owasp.org/www-community/attacks/Path_Traversal) or [**LFI (Local File Inclusion)**](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion) to see if it exists. Unfortunately, my intuition was wrong this time, and I didn’t find anything. The parameter is not vulnerable.

Let’s restart our thinking and approach this from a different angle. It’s time to think more outside the box.

What can we extract from this directory? I remember something we didn’t give importance to earlier: the **/admin** directory that redirects us to the home page. Let’s try to access it from here and see if it loads.

Interestingly, `admin.php` didn't give us anything, but `admin` did.

As you can see, we received a valid response that we didn’t get earlier. It displays a message telling us that we are not allowed to view this page. However, I believe we can find a way to bypass this restriction.

Press enter or click to view image in full size

![]()

Wait a minute 🤨 how does this page know that we are not allowed to see its content?🤔 Have you asked yourself this question before ?

Something must be telling the web app that we are strangers and not authorized to access ...