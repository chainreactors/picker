---
title: Common 403 Bypasses Part 2
url: https://infosecwriteups.com/common-403-bypasses-part-2-ae89060debec?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-31
fetch_date: 2025-10-06T17:42:16.442021
---

# Common 403 Bypasses Part 2

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fae89060debec&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcommon-403-bypasses-part-2-ae89060debec&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcommon-403-bypasses-part-2-ae89060debec&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ae89060debec---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ae89060debec---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Common 403 Bypasses Part 2

[![Ott3rly](https://miro.medium.com/v2/resize:fill:64:64/1*3wMPJmhJUNOpqobsPBkS8g.jpeg)](https://ott3rly.medium.com/?source=post_page---byline--ae89060debec---------------------------------------)

[Ott3rly](https://ott3rly.medium.com/?source=post_page---byline--ae89060debec---------------------------------------)

4 min read

·

Jul 15, 2024

--

Listen

Share

Back for more 403 bypasses? In this article, we will check various tools to help with the whole process. Get ready to level up your bypass skills. Let’s go!

We covered some fundamental 403 bypass techniques in our previous blog post. I usually use those techniques without overthinking, but sometimes I tend to use a couple of different tools for different scenarios.

## bypass-403.sh

The first tool is by iamj0ker, which is a simple bash script I use for quick checks. Using this tool is straightforward — you need to pass your targeted website and the endpoint like so:

```
./bypass-403.sh https://target.com endpoint
```

The endpoint could be “admin,” “secret,” “API,” a Swagger instance, or any other desired endpoint, but you must know that this endpoint exists beforehand. Let’s examine the script itself:

Press enter or click to view image in full size

![]()

The script is concise, containing only 60 lines of code, with roughly half dedicated to displaying information on the screen and various curl commands. It tries different paths and payloads, such as applying dots, slashes, dot-slash combinations, and various headers like the original URL and rewrite URL. The script also attempts to append extensions like .html and .php and applies some additional headers.

I usually use this tool when I have a large number of URLs gathered for a target and I’m working from the terminal. If I encounter a specific interesting URL that returns a 403 error, I start by using this tool to see if it can bypass the restriction.

## 4-ZERO-3

If you find a particularly interesting endpoint, such as one related to file uploads, imports, rendering, or potentially leaky information, I recommend using this [bash script](https://github.com/Dheerajmadhukar/4-ZERO-3). Although it was updated three years ago, most of its functionality still works. This script is more sophisticated than the previous one and will take longer to run since it performs many more checks. It does have a lot of lines of code, and it has a lot of different functions and different functions will run as different modules:

![]()

If you only want to try header bypasses, there is a function specifically for that. This function checks many more headers compared to the previous script, which only checked five or so. In addition, it will test for other techniques not previously mentioned, such as SQL injection, library injection bypasses, and more.

The script includes a function called “403 bypass,” which invokes various other functions. According to the script’s description, there is a bypass mode where you can select multiple types or just one. Even if you choose only one type, this script will take longer to run compared to the previous one due to its thoroughness:

Press enter or click to view image in full size

![]()

Use those two scripts in cases when you have a lot of results in your command line if you are hacking from the command line

## 403-bypasser

If you prefer manual hacking using Burp Suite, which I highly recommend, there are a few more tools available for that. Most of the hacking will be done manually, primarily using Burp Suite. I also recommend the tool “403-bypasser.” It can be found on the BApp Store:

Press enter or click to view image in full size

![]()

What does it do? The “403-bypasser” tool will perform basic endpoint fuzzing, similar to what I’ve shown earlier. While I usually do this manually, this tool automates the process for you. It will also try some header payloads and GET requests, covering the basics. Despite being developed a while ago, it still works effectively today. This tool has helped me find some interesting vulnerabilities.

## nowafpls

The last tool, presented by Shubs during Nahamcon, is called [nowafpls](https://github.com/assetnote/nowafpls). It simplifies certain bypasses for requests sent through Burp Suite using POST, PUT, and PATCH methods. Note that it won’t work with GET methods, but if you’re working with requests that contain body data, this tool can be very helpful. I highly recommend watching his [presentation](https://www.youtube.com/watch?v=0OMmWtU2Y_g) at Nahamcon for more insights.

Most WAFs have limitations on how much data they can process when a request body is sent. For HTTP requests containing a request body (such as POST, PUT, PATCH), the WAF typically processes up to a certain amount of data and analyzes it. The rest of the data, beyond the processing limit, passes through unchecked. The **nowafpls** plugin leverages this limitation by padding the request with junk data, making the WAF process only the initial part of the request while letting the remaining part go through uninspected.

## Summary

The purpose here was to understand what was happening under the hood while using different tools. The tool usage you could truly explore yourself. All in all, you shouldn’t rely too much on them but rather try to understand the techniques that they are providing. On the other hand, they do automate some microtasks. It was my pleasure sharing this knowledge, I wish you a nice hunt!

If you find this information useful, please share this article on your social media, I will greatly appreciate it! I am active on [Twitter](https://ott3rly.com/twitter), check out some content I post there daily! If you are interested in video content, check my [YouTube](https://ott3rly.com/youtube). Also, if you want to reach me personally, you can visit my [Discord](https://ott3rly.com/discord) server. Cheers!

*Originally published at* [*https://ott3rly.com*](https://ott3rly.com/common-403-bypasses-part-2/) *on July...