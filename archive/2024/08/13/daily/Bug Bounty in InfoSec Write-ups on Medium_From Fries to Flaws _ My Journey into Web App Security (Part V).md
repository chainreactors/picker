---
title: From Fries to Flaws : My Journey into Web App Security (Part V)
url: https://infosecwriteups.com/from-fries-to-flaws-my-journey-into-web-app-security-part-v-f0ea86e55845?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-13
fetch_date: 2025-10-06T18:04:16.256723
---

# From Fries to Flaws : My Journey into Web App Security (Part V)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff0ea86e55845&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-fries-to-flaws-my-journey-into-web-app-security-part-v-f0ea86e55845&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-fries-to-flaws-my-journey-into-web-app-security-part-v-f0ea86e55845&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f0ea86e55845---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f0ea86e55845---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# From Fries to Flaws : My Journey into Web App Security (Part V)

## Discovering Hidden EndPoints Using Different Techniques in FastFoodHackings Challenge

[![zerOiQ](https://miro.medium.com/v2/resize:fill:64:64/1*M6lvjH7YpCrR1SqB0tcYSg.png)](https://medium.com/%40zerOiQ?source=post_page---byline--f0ea86e55845---------------------------------------)

[zerOiQ](https://medium.com/%40zerOiQ?source=post_page---byline--f0ea86e55845---------------------------------------)

4 min read

·

Aug 12, 2024

--

1

Listen

Share

> [***bugbountytraining.com***](https://www.bugbountytraining.com/fastfoodhackings/)***/***[***FastFoodHackings***](https://www.bugbountytraining.com/fastfoodhackings/)

Press enter or click to view image in full size

![]()

> Welcome to the final part of our series on [BugBountyTraining](https://www.bugbountytraining.com/) , In brief, [FastFoodHackings](https://www.bugbountytraining.com/fastfoodhackings/) is a training website created by [Sean (zseano)](https://medium.com/u/ca91e7064349). It helps people learn bug hunting through real-world scenarios. If you missed the First , Second , Third or Fourth parts, be sure to check them out. Let’s continue our journey into uncovering bugs !
>
> [(Part I)](/from-fries-to-flaws-my-journey-into-web-app-security-part-i-958c67c20771) [(Part II)](https://medium.com/%40OiQ/from-fries-to-flaws-my-journey-into-web-app-security-part-ii-6127ecc7d93f) [(Part](https://medium.com/%40OiQ/from-fries-to-flaws-my-journey-into-web-app-security-part-iii-ce91eb384da7) III) ([Part](https://medium.com/%40OiQ/from-fries-to-flaws-my-journey-into-web-app-security-part-iv-956c3fcbec68) IV)

We did a great job in the previous parts by discovering many bugs and vulnerabilities, such as Broken Access control, Stored & Reflected XSS, Open Redirects .

I believe we’ve thoroughly checked every page, clicked on every clickable button, and tested every functionality. However, as we’ve mentioned before, checking the visible elements doesn’t guarantee we’ve covered everything. There are still hidden aspects waiting to be discovered .

To achieve this, we’re introducing a new tool OR actually its a browser extension that will help us uncover hidden elements on websites. This way, we can discover interesting things more easily, similar to how Burp Suite revealed hidden endpoints for us using Regex. Now, we’ll be able to unveil hidden elements without having to dig through the code line by line.

By installing the [**LazySec**](https://chromewebstore.google.com/detail/lazysec/llegephenamkbmnjbjpgkdakkfmgeggp) extension , Clicking on “ALL” checkbox and clicking the ‘Show Hidden Elements’ , you’ll be able to reveal all hidden elements in the Web App. This will assist in discovering new Features and Endpoints that might be vulnerable .

Press enter or click to view image in full size

![]()

Screenshot

We’ve found a hidden link that doesn’t redirect anywhere when clicked, which is curious given its hidden nature. Let’s investigate its source code further to gain a better understanding .

Press enter or click to view image in full size

![]()

Screenshot

Here, we have a link that appears to be invalid, but it includes an `id=` with a `redirectUrl` value. IDs are used in HTML to identify elements and are manipulated by JavaScript.

This could be a good hint to go back and investigate this ID further with Burp Suite .

Let’s use the **Filter** functionality, as we did earlier, to search through all files and uncover the parameters we need.

Press enter or click to view image in full size

![]()

Screenshot

We found it! Now, let’s try sending another link as a query in the `from` parameter to see if we can discover an Open Redirect or something interesting.

Press enter or click to view image in full size

![]()

Screenshot

> We successfully discovered an Open Redirect vulnerability.

This time, it’s straightforward: we’ve observed that whatever we enter in the URL gets injected into the `href=""`. Let’s inject some JavaScript code and see if we can achieve an XSS vulnerability.

Press enter or click to view image in full size

![]()

Screenshot

> We successfully discovered an XSS vulnerability .

We now have two more bugs added to our arsenal .

One last thing to check: below the `from` parameter, there's another one called `type`, and they seem identical. Let's examine the code further to understand its functionalities .

Press enter or click to view image in full size

![]()

Screenshot

Let’s break down the code for a better understanding. We’ll set the `from` parameter to any value and the `type` parameter to `1`, as mentioned in the code, to redirect us to our desired location. We'll concatenate the two parameters with `&`, followed by what’s written in the code. Additionally, we'll add a `#` before `redir`, because `redir` isn’t a parameter like `from` and `type`.

The `getHashValue` function is supposed to return a value based on the `redir` parameter. This function likely extracts a value from the URL’s hash portion (the part after `#` in a URL).

For example, if the URL is `http://OiQ.tn/#redir=someURL`, `getHashValue("redir"),`would extract and return the value `someURL`.

Intuitively, we’ll test this for Open Redirects, just like we did with the previous parameter. Then, we’ll try to escalate it to an XSS vulnerability, hoping for a successful result .

```
https://www.bugbountytraining.com/fastfoodhackings/?from=javascript:alert("XSS")&type=1#redir=https://google.com
```

Press enter or click to view image in full size

![]()

Screenshot

> And we did it , We successfully found another open redirect!

By replacing the Google URL and setting `redir` to `javascript:alert('XSS')`, we successfully achieved a new XSS vulnerability, confirming that both parameters are vulnerable .

```
https://www.bugbountytraining.com/fastfoodhackings/?from=OiQ&type=1#redir=javascript:alert("XSS")
```

Press enter or click ...