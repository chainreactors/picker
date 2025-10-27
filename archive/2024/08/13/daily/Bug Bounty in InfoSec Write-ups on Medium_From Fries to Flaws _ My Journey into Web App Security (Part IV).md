---
title: From Fries to Flaws : My Journey into Web App Security (Part IV)
url: https://infosecwriteups.com/from-fries-to-flaws-my-journey-into-web-app-security-part-iv-956c3fcbec68?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-13
fetch_date: 2025-10-06T18:04:23.286579
---

# From Fries to Flaws : My Journey into Web App Security (Part IV)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F956c3fcbec68&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-fries-to-flaws-my-journey-into-web-app-security-part-iv-956c3fcbec68&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-fries-to-flaws-my-journey-into-web-app-security-part-iv-956c3fcbec68&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-956c3fcbec68---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-956c3fcbec68---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# From Fries to Flaws : My Journey into Web App Security (Part IV)

## Mastering BAC And Discovering Hidden EndPoints Using Different Techniques in FastFoodHackings Challenge

[![zerOiQ](https://miro.medium.com/v2/resize:fill:64:64/1*M6lvjH7YpCrR1SqB0tcYSg.png)](https://medium.com/%40zerOiQ?source=post_page---byline--956c3fcbec68---------------------------------------)

[zerOiQ](https://medium.com/%40zerOiQ?source=post_page---byline--956c3fcbec68---------------------------------------)

7 min read

·

Aug 11, 2024

--

1

Listen

Share

> [***bugbountytraining.com***](https://www.bugbountytraining.com/fastfoodhackings/)***/***[***FastFoodHackings***](https://www.bugbountytraining.com/fastfoodhackings/)

Press enter or click to view image in full size

![]()

> Welcome to the fourth part of our series on BugBountyTraining , In brief, [FastFoodHackings](https://www.bugbountytraining.com/fastfoodhackings/) is a training website created by [Sean (zseano)](https://medium.com/u/ca91e7064349). It helps people learn bug hunting through real-world scenarios. If you missed the first , second or third parts, be sure to check them out. Let’s continue our journey into uncovering bugs !
>
> [(Part I)](/from-fries-to-flaws-my-journey-into-web-app-security-part-i-958c67c20771) [(Part II)](https://medium.com/%40OiQ/from-fries-to-flaws-my-journey-into-web-app-security-part-ii-6127ecc7d93f) [(Part III](https://medium.com/%40OiQ/from-fries-to-flaws-my-journey-into-web-app-security-part-iii-ce91eb384da7))

By examining this request further and checking for additional parameters to test, we might discover something interesting, just like we did in the previous part when we found the token that allowed us to log in as an admin, regardless of our existing authority.

Press enter or click to view image in full size

![]()

Screenshot

So, we’ll continue using Burp Suite to search through the code and files for the parameter `f=`, hoping to find something useful.

Press enter or click to view image in full size

![]()

Screenshot

Wow! This is the greatest discovery so far , we’ve finally found the credentials! I’m pretty sure these are the admin credentials.

Press enter or click to view image in full size

![]()

Screenshot

The credentials are as follows

Press enter or click to view image in full size

![]()

Screenshot

```
"username":"test-zseano" ,
"password":"SuP3RG0OdP@ssw0rd!"
```

And here you can see our admin panel. It might seem empty, but we’ve done a great job by examining this parameter and gaining access to the panel.

Press enter or click to view image in full size

![]()

Screenshot

It seems there’s nothing to do here , no clickable elements or inputs. But, just like we’ve done every time we’ve faced this issue, we’ll turn to our trusty friend, Burp Suite, to discover any hidden elements.

After reviewing the request, we only found some CSS and API font files as always . However, the last request includes an `id=` parameter that could be worth testing. Let's investigate it to see if it reveals any path traversal vulnerability .

Press enter or click to view image in full size

![]()

Screenshot

After testing various path traversal payloads, I didn’t find anything. However, I accidentally changed the `id` to 0, 1, and other small integers.

While 0 yielded no results, both 1 and 2 produced interesting findings.

Press enter or click to view image in full size

![]()

Screenshot

By assigning 1 to the `id=` parameter, it displays '**Test account for zseano**' .

Press enter or click to view image in full size

![]()

Screenshot

And , by assigning 2 , it displays '**Bio for account two. not much interesting here sorry**’ .

Press enter or click to view image in full size

![]()

Screenshot

And now we’ve confirmed our findings , we’re able to load data belonging to other users by accessing their accounts.

> We’ve discovered an IDOR (Insecure Direct Object Reference) vulnerability.

**So far, we’ve tested almost everything on the website, from the login form to the menu page, and we’ve clicked on nearly every visible button. As a result, we’ve discovered several bugs, including Open Redirects, XSS vulnerabilities, and Broken Access Control.**

Whether you’ve noticed or not, Our findings have come from hidden Endpoints and parameters. So, let’s continue with this methodology and approach, hoping to uncover more bugs just like before.

Press enter or click to view image in full size

![]()

We’ll be using an **Advanced Technique** called [**Regular Expressions**](https://en.wikipedia.org/wiki/Regular_expression), or in short [**Regex**](https://en.wikipedia.org/wiki/Regular_expression), to search for specific patterns in text. This powerful tool will help us identify hidden parameters, endpoints, or anomalies in the code that might otherwise go unnoticed. Our goal is to conduct an in-depth investigation within all the files we’ve intercepted through Burp , uncovering hidden information .

We want Burp Suite to search for any sequence of characters that matches this pattern: starting with a question mark `?`, followed by some text, and then followed by an equal sign `=`. The pattern would look like this: `?.*=`

In Regex, the `.` represents any character, and the `*` means any number of characters. However, there are some tricks we need to include.

First, we'll add a backslash `\` before the `?` to tell Burp that the `?` is part of the pattern, not a special character. Additionally, we'll add a `?` before the equal sign `=` to instruct Burp to stop matching once this pattern is satisfied, rather than continuing to the end of the line.

So, the final pattern will look like this:

```
\?.*?=
```

Press enter or click to view image in full size

![]()

Screenshot

A bit of investigation through the files revealed several pieces of code matching this pattern.

While most were uninteresting, except the`?promoCode=UKONLY`in the `book.php` file....